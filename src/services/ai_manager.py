#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - AI Manager com Sistema de Fallback
Gerenciador inteligente de múltiplas IAs com sistema de fallback automático
"""

import os
import logging
import time
import json
from typing import Dict, List, Optional, Any
import requests
from datetime import datetime, timedelta

# Imports condicionais para os clientes de IA
try:
    import google.generativeai as genai
    HAS_GEMINI = True
except ImportError:
    HAS_GEMINI = False

try:
    import openai
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

try:
    from services.groq_client import groq_client
    HAS_GROQ_CLIENT = True
except ImportError:
    HAS_GROQ_CLIENT = False

logger = logging.getLogger(__name__)

class AIManager:
    """Gerenciador de IAs com sistema de fallback automático"""

    def __init__(self):
        """Inicializa o gerenciador de IAs"""
        self.providers = {
            'gemini': {
                'client': None,
                'available': False,
                'priority': 1,  # GEMINI PRO CONFIRMADO COMO PRIORIDADE MÁXIMA
                'error_count': 0,
                'model': 'gemini-2.0-flash-exp',  # Gemini 2.5 Pro
                'max_errors': 2,
                'last_success': None,
                'consecutive_failures': 0
            },
            'groq': {
                'client': None,
                'available': False,
                'priority': 2,  # FALLBACK AUTOMÁTICO
                'error_count': 0,
                'model': 'llama3-70b-8192',
                'max_errors': 2,
                'last_success': None,
                'consecutive_failures': 0
            },
            'openai': {
                'client': None,
                'available': False,
                'priority': 3,
                'error_count': 0,
                'model': 'gpt-3.5-turbo',
                'max_errors': 2,
                'last_success': None,
                'consecutive_failures': 0
            },
            'huggingface': {
                'client': None,
                'available': False,
                'priority': 4,
                'error_count': 0,
                'models': ["HuggingFaceH4/zephyr-7b-beta", "google/flan-t5-base"],
                'current_model_index': 0,
                'max_errors': 3,
                'last_success': None,
                'consecutive_failures': 0
            }
        }

        # Inicializa status e controle de falhas
        self.provider_failures = {name: 0 for name in self.providers}
        self.last_error = {name: None for name in self.providers}
        self.provider_enabled = {name: True for name in self.providers}
        self.last_failure_time = {name: None for name in self.providers}
        self.max_failures = 3 # Limite geral de falhas consecutivas antes de desativar
        self.rate_limits = {} # Dicionário para rastrear rate limits

        self.initialize_providers()
        available_count = len([p for p in self.providers.values() if p['available']])
        logger.info(f"🤖 AI Manager inicializado com {available_count} provedores disponíveis.")

    def initialize_providers(self):
        """Inicializa todos os provedores de IA com base nas chaves de API disponíveis."""

        # Inicializa Gemini
        if HAS_GEMINI:
            try:
                gemini_key = os.getenv('GEMINI_API_KEY')
                if gemini_key:
                    genai.configure(api_key=gemini_key)
                    # Tenta inicializar com um modelo mais estável primeiro
                    try:
                        self.providers['gemini']['client'] = genai.GenerativeModel("gemini-1.5-pro-latest")
                        self.providers['gemini']['available'] = True
                        logger.info("✅ Gemini 1.5 Pro (gemini-1.5-pro-latest) inicializado como MODELO PRIMÁRIO")
                    except Exception as gemini_init_error:
                        logger.warning(f"⚠️ Falha ao inicializar Gemini 1.5 Pro, tentando Gemini 2.5 Pro (gemini-2.0-flash-exp): {str(gemini_init_error)}")
                        try:
                            self.providers['gemini']['client'] = genai.GenerativeModel("gemini-2.0-flash-exp")
                            self.providers['gemini']['available'] = True
                            logger.info("✅ Gemini 2.5 Pro (gemini-2.0-flash-exp) inicializado como MODELO PRIMÁRIO")
                        except Exception as gemini_flash_error:
                            logger.error(f"❌ Falha ao inicializar Gemini com ambos os modelos: {str(gemini_flash_error)}")
                            self.providers['gemini']['available'] = False

            except Exception as e:
                logger.warning(f"⚠️ Falha ao configurar Gemini API: {str(e)}")
                self.providers['gemini']['available'] = False
        else:
            logger.warning("⚠️ Biblioteca 'google-generativeai' não instalada.")

        # Inicializa OpenAI
        if HAS_OPENAI:
            try:
                openai_key = os.getenv('OPENAI_API_KEY')
                if openai_key:
                    self.providers["openai"]["client"] = openai.OpenAI(api_key=openai_key)
                    self.providers["openai"]["available"] = True
                    logger.info("✅ OpenAI (gpt-3.5-turbo) inicializado com sucesso")
            except Exception as e:
                logger.info(f"ℹ️ OpenAI não disponível: {str(e)}")
                self.providers["openai"]["available"] = False
        else:
            logger.info("ℹ️ Biblioteca 'openai' não instalada.")

        # Inicializa Groq
        try:
            if HAS_GROQ_CLIENT and groq_client and groq_client.is_enabled():
                self.providers['groq']['client'] = groq_client
                self.providers['groq']['available'] = True
                logger.info("✅ Groq (llama3-70b-8192) inicializado com sucesso")
            else:
                logger.info("ℹ️ Groq client não configurado")
                self.providers['groq']['available'] = False
        except Exception as e:
            logger.info(f"ℹ️ Groq não disponível: {str(e)}")
            self.providers['groq']['available'] = False

        # Inicializa HuggingFace
        try:
            hf_key = os.getenv('HUGGINGFACE_API_KEY')
            if hf_key:
                self.providers['huggingface']['client'] = {
                    'api_key': hf_key,
                    'base_url': 'https://api-inference.huggingface.co/models/'
                }
                self.providers['huggingface']['available'] = True
                logger.info("✅ HuggingFace inicializado com sucesso")
        except Exception as e:
            logger.info(f"ℹ️ HuggingFace não disponível: {str(e)}")
            self.providers['huggingface']['available'] = False

    def get_best_provider(self) -> Optional[str]:
        """Retorna o melhor provedor disponível com base na prioridade e contagem de erros."""
        current_time = time.time()

        # Tenta reabilitar provedores desabilitados após um cooldown
        for name, provider in self.providers.items():
            # Verifica se o provedor está desabilitado e se o cooldown para reabilitação expirou
            cooldown_duration = 600 # 10 minutos
            if not provider['available'] and provider.get('last_failure_time') and current_time - provider['last_failure_time'] > cooldown_duration:
                logger.info(f"🔄 Tentando reabilitar provedor {name} após cooldown de {cooldown_duration}s")
                provider['available'] = True # Marca como disponível para tentativa
                self.provider_enabled[name] = True # Garante que está habilitado
                self.provider_failures[name] = 0 # Reseta falhas para reavaliar
                self.last_error[name] = None
                self.last_failure_time[name] = None
                # Se foi desabilitado por rate limit, pode ter sido resolvido
                if name == 'gemini' and HAS_GEMINI:
                    provider['available'] = True
                elif name == 'groq' and HAS_GROQ_CLIENT:
                    provider['available'] = True
                elif name == 'openai' and HAS_OPENAI:
                    provider['available'] = True
                elif name == 'huggingface':
                    provider['available'] = True
            # Se o provedor está habilitado, mas foi desativado, verifica cooldown também
            elif not self.provider_enabled[name] and provider.get('last_failure_time') and current_time - provider['last_failure_time'] > cooldown_duration:
                logger.info(f"🔄 Reativando provedor {name} que estava desabilitado por falhas excessivas.")
                self.provider_enabled[name] = True
                self.last_failure_time[name] = None # Limpa o tempo de falha para não reativar imediatamente

        # Filtra provedores que estão marcados como desabilitados ou excederam falhas consecutivas
        available_providers = [
            (name, provider) for name, provider in self.providers.items()
            if provider['available'] and self.provider_enabled[name] and self.provider_failures[name] < self.max_failures
        ]

        if not available_providers:
            logger.warning("🔄 Nenhum provedor saudável disponível. Resetando contadores de falha para reavaliar.")
            # Reseta falhas para todos os provedores que não estão temporariamente desabilitados
            for name, provider in self.providers.items():
                if not provider['available']: # Mantém desabilitados se ainda em cooldown
                    continue
                if self.provider_failures[name] > 0: # Reseta apenas se houve falhas
                    # Não resetar error_count (histórico), apenas falhas consecutivas
                    self.provider_failures[name] = 0
                    self.last_error[name] = None
                    self.last_failure_time[name] = None
                    self.provider_enabled[name] = True # Reabilita explicitamente

            # Reavalia a disponibilidade após o reset
            available_providers = [(name, p) for name, p in self.providers.items() if p['available'] and self.provider_enabled[name]]

        if available_providers:
            # Ordena por prioridade e número de falhas consecutivas (como um fator secundário)
            available_providers.sort(key=lambda x: (x[1]['priority'], self.provider_failures[x[0]]))
            return available_providers[0][0]

        logger.critical("❌ TODOS OS PROVEDORES ESTÃO INDISPONÍVEIS OU DESABILITADOS.")
        return None

    def generate_analysis(self, prompt: str, max_tokens: int = 1000, temperature: float = 0.7) -> Optional[str]:
        """Gera análise usando o melhor provedor disponível"""
        return self._try_providers('generate', prompt, max_tokens=max_tokens, temperature=temperature)

    def generate_completion(self, prompt: str, max_tokens: int = 4000, temperature: float = 0.7) -> str:
        """Método de compatibilidade - mesmo que generate_analysis"""
        return self.generate_analysis(prompt, max_tokens, temperature)

    def generate_content(self, prompt: str, max_tokens: int = 4000, temperature: float = 0.7) -> Optional[str]:
        """Gera conteúdo usando o melhor provedor disponível - método compatibilidade"""

        try:
            result = self.generate_analysis(prompt, max_tokens, temperature)
            if result and result.get('response'):
                return result['response']
            return None

        except Exception as e:
            logger.error(f"❌ Erro na geração de conteúdo: {e}")
            return None

    def generate_parallel_analysis(self, prompts: List[Dict[str, Any]], max_tokens: int = 8192) -> Dict[str, Any]:
        """Gera múltiplas análises em paralelo usando diferentes provedores"""

        from concurrent.futures import ThreadPoolExecutor, as_completed

        results = {}

        with ThreadPoolExecutor(max_workers=len(prompts)) as executor:
            future_to_prompt = {}

            for prompt_data in prompts:
                prompt_id = prompt_data['id']
                prompt_text = prompt_data['prompt']
                preferred_provider = prompt_data.get('provider')

                future = executor.submit(
                    self.generate_analysis,
                    prompt_text,
                    max_tokens,
                    preferred_provider
                )
                future_to_prompt[future] = prompt_id

            # Coleta resultados
            for future in as_completed(future_to_prompt, timeout=600):
                prompt_id = future_to_prompt[future]
                try:
                    result = future.result()
                    results[prompt_id] = {
                        'success': bool(result),
                        'content': result,
                        'error': None
                    }
                except Exception as e:
                    results[prompt_id] = {
                        'success': False,
                        'content': None,
                        'error': str(e)
                    }

        return results

    def _record_success(self, provider_name: str):
        """Registra sucesso do provedor"""
        if provider_name in self.providers:
            # Reseta falhas consecutivas e o contador de erros total
            self.providers[provider_name]['consecutive_failures'] = 0
            self.provider_failures[provider_name] = 0
            self.last_error[provider_name] = None
            self.last_failure_time[provider_name] = None
            self.provider_enabled[provider_name] = True # Garante que está habilitado após sucesso
            self.providers[provider_name]['last_success'] = time.time()
            logger.info(f"✅ Sucesso registrado para {provider_name}")

    def _record_failure(self, provider_name: str, error_msg: str):
        """Registra falha do provedor e atualiza estado."""
        if provider_name not in self.providers:
            return

        self.provider_failures[provider_name] += 1
        self.last_error[provider_name] = error_msg
        self.providers[provider_name]['error_count'] += 1 # Mantém o contador histórico
        self.last_failure_time[provider_name] = time.time() # Registra tempo da última falha

        if self.provider_failures[provider_name] >= self.max_failures:
            self.provider_enabled[provider_name] = False
            logger.warning(f"⚠️ Desabilitando {provider_name} temporariamente após {self.provider_failures[provider_name]} falhas consecutivas.")

        logger.error(f"❌ Falha registrada para {provider_name}: {error_msg}")

    def _handle_provider_failure(self, provider_name: Optional[str], error: Exception):
        """Trata falhas de provedor com fallback e controle aprimorado."""
        error_str = str(error)

        # Se provider_name é None (por exemplo, get_best_provider retornou None), não registramos falha específica.
        if provider_name:
            # Verifica se é rate limit e aplica tratamento específico
            if any(keyword in error_str.lower() for keyword in ['429', 'rate limit', 'quota', 'exceeded', 'too many']):
                # Rate limit mais agressivo para Gemini
                if provider_name == 'gemini':
                    self._handle_rate_limit(provider_name, error_str, extended_timeout=600)  # 10 minutos
                else:
                    self._handle_rate_limit(provider_name, error_str)
            else:
                self._record_failure(provider_name, error_str) # Registra falha comum

        # Tenta obter o próximo provedor disponível com fallback
        # Passa o prompt e max_tokens para que o fallback possa tentar gerar conteúdo
        return self._get_next_available_provider([provider_name] if provider_name else [])

    def _call_provider(self, provider_name: str, prompt: str, max_tokens: int) -> Optional[str]:
        """Chama a função de geração do provedor especificado."""
        if provider_name == 'gemini':
            return self._generate_with_gemini(prompt, max_tokens)
        elif provider_name == 'groq':
            return self._generate_with_groq(prompt, max_tokens)
        elif provider_name == 'openai':
            return self._generate_with_openai(prompt, max_tokens)
        elif provider_name == 'huggingface':
            return self._generate_with_huggingface(prompt, max_tokens)
        return None

    def _generate_with_gemini(self, prompt: str, max_tokens: int) -> Optional[str]:
        """Gera conteúdo usando Gemini."""
        client = self.providers['gemini']['client']
        if not client:
            raise Exception("Cliente Gemini não inicializado.")

        config = {
            "temperature": 0.8,  # Criatividade controlada
            "max_output_tokens": min(max_tokens, 8192),
            "top_p": 0.95,
            "top_k": 64
        }
        safety = [
            {"category": c, "threshold": "BLOCK_NONE"}
            for c in ["HARM_CATEGORY_HARASSMENT", "HARM_CATEGORY_HATE_SPEECH", "HARM_CATEGORY_SEXUALLY_EXPLICIT", "HARM_CATEGORY_DANGEROUS_CONTENT"]
        ]
        try:
            response = client.generate_content(prompt, generation_config=config, safety_settings=safety)
            if response.text:
                logger.info(f"✅ Gemini gerou {len(response.text)} caracteres")
                return response.text
            else:
                # Tenta obter a razão se não houver texto
                if response.prompt_feedback:
                    logger.warning(f"⚠️ Gemini retornou feedback de prompt: {response.prompt_feedback}")
                if response.candidates and response.candidates[0].finish_reason:
                    logger.warning(f"⚠️ Gemini finalizado com razão: {response.candidates[0].finish_reason}")
                raise Exception("Resposta vazia do Gemini")
        except Exception as e:
            error_msg = str(e)
            # Verifica se é rate limit para aplicar tratamento específico
            if any(keyword in error_msg.lower() for keyword in ['429', 'rate limit', 'quota', 'exceeded', 'too many']):
                self._handle_rate_limit(self.providers['gemini']['model'], error_msg, extended_timeout=600)
            else:
                self._record_failure('gemini', error_msg)
            raise e

    def _generate_with_groq(self, prompt: str, max_tokens: int) -> Optional[str]:
        """Gera conteúdo usando Groq."""
        client = self.providers['groq']['client']
        if not client:
            raise Exception("Cliente Groq não inicializado.")

        try:
            content = client.generate(prompt, max_tokens=min(max_tokens, 8192))
            if content:
                logger.info(f"✅ Groq gerou {len(content)} caracteres")
                return content
            else:
                raise Exception("Resposta vazia do Groq")
        except Exception as e:
            error_msg = str(e)
            if any(keyword in error_msg.lower() for keyword in ['429', 'rate limit', 'quota', 'exceeded', 'too many']):
                self._handle_rate_limit('groq', error_msg)
            else:
                self._record_failure('groq', error_msg)
            raise e

    def _generate_with_openai(self, prompt: str, max_tokens: int) -> Optional[str]:
        """Gera conteúdo usando OpenAI."""
        client = self.providers['openai']['client']
        if not client:
            raise Exception("Cliente OpenAI não inicializado.")

        try:
            response = client.chat.completions.create(
                model=self.providers['openai']['model'],
                messages=[
                    {"role": "system", "content": "Você é um especialista em análise de mercado ultra-detalhada."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=min(max_tokens, 4096),
                temperature=0.7
            )
            content = response.choices[0].message.content
            if content:
                logger.info(f"✅ OpenAI gerou {len(content)} caracteres")
                return content
            else:
                raise Exception("Resposta vazia do OpenAI")
        except Exception as e:
            error_msg = str(e)
            if any(keyword in error_msg.lower() for keyword in ['429', 'rate limit', 'quota', 'exceeded', 'too many']):
                self._handle_rate_limit('openai', error_msg)
            else:
                self._record_failure('openai', error_msg)
            raise e

    def _generate_with_huggingface(self, prompt: str, max_tokens: int) -> Optional[str]:
        """Gera conteúdo usando HuggingFace com rotação de modelos."""
        config = self.providers['huggingface']
        if not config['client']:
            raise Exception("Cliente HuggingFace não inicializado.")

        for _ in range(len(config['models'])):
            model_index = config['current_model_index']
            model = config['models'][model_index]
            config['current_model_index'] = (model_index + 1) % len(config['models']) # Rotaciona para a próxima vez

            try:
                url = f"{config['client']['base_url']}{model}"
                headers = {"Authorization": f"Bearer {config['client']['api_key']}"}
                payload = {"inputs": prompt, "parameters": {"max_new_tokens": min(max_tokens, 1024)}}
                response = requests.post(url, headers=headers, json=payload, timeout=60)

                if response.status_code == 200:
                    res_json = response.json()
                    content = res_json[0].get("generated_text", "")
                    if content:
                        logger.info(f"✅ HuggingFace ({model}) gerou {len(content)} caracteres")
                        return content
                elif response.status_code == 503:
                    logger.warning(f"⚠️ Modelo HuggingFace {model} está carregando (503), tentando próximo...")
                    continue
                else:
                    error_msg = f"Erro {response.status_code}: {response.text}"
                    logger.warning(f"⚠️ Erro no modelo {model}: {error_msg}")
                    # Trata rate limit específico do HuggingFace se aplicável
                    if response.status_code == 429:
                         self._handle_rate_limit('huggingface', error_msg)
                    else:
                        self._record_failure('huggingface', error_msg)
                    continue # Tenta o próximo modelo
            except Exception as e:
                error_msg = str(e)
                logger.warning(f"⚠️ Erro no modelo {model}: {error_msg}")
                self._record_failure('huggingface', error_msg)
                continue # Tenta o próximo modelo

        raise Exception("Todos os modelos HuggingFace falharam")

    def reset_provider_errors(self, provider_name: str = None):
        """Reset contadores de erro dos provedores"""
        if provider_name:
            if provider_name in self.providers:
                self.providers[provider_name]['error_count'] = 0
                self.providers[provider_name]['consecutive_failures'] = 0
                self.provider_failures[provider_name] = 0
                self.last_error[provider_name] = None
                self.last_failure_time[provider_name] = None
                self.provider_enabled[provider_name] = True
                # Tenta reabilitar o provedor se ele tinha um cliente configurado
                if self.providers[provider_name]['client'] or (provider_name == 'gemini' and HAS_GEMINI) or \
                   (provider_name == 'groq' and HAS_GROQ_CLIENT) or \
                   (provider_name == 'openai' and HAS_OPENAI):
                    self.providers[provider_name]['available'] = True
                logger.info(f"🔄 Reset erros do provedor: {provider_name}")
        else:
            for name, provider in self.providers.items():
                provider['error_count'] = 0
                provider['consecutive_failures'] = 0
                self.provider_failures[name] = 0
                self.last_error[name] = None
                self.last_failure_time[name] = None
                self.provider_enabled[name] = True
                # Só reabilita se tem cliente configurado ou se a biblioteca existe
                if provider.get('client') or \
                   (name == 'gemini' and HAS_GEMINI) or \
                   (name == 'groq' and HAS_GROQ_CLIENT) or \
                   (name == 'openai' and HAS_OPENAI):
                    provider['available'] = True
            logger.info("🔄 Reset erros de todos os provedores")

    def _get_next_available_provider(self, exclude: List[str]) -> Optional[str]:
        """Busca e retorna o nome do próximo provedor disponível, excluindo os listados."""
        current_time = time.time()

        # Tenta reabilitar provedores desabilitados após um cooldown
        for name, provider in self.providers.items():
            cooldown_duration = 600 # 10 minutos
            # Se o provedor está indisponível ou desabilitado, verifica se o cooldown expirou
            if (not provider['available'] or not self.provider_enabled.get(name, True)) and \
               provider.get('last_failure_time') and current_time - provider['last_failure_time'] > cooldown_duration:
                logger.info(f"🔄 Tentando reabilitar provedor {name} para fallback")
                provider['available'] = True
                self.provider_enabled[name] = True
                self.provider_failures[name] = 0 # Reseta falhas para reavaliar
                self.last_error[name] = None
                self.last_failure_time[name] = None

        # Filtra provedores que estão marcados como desabilitados ou excederam falhas consecutivas
        available_providers = [
            (name, provider) for name, provider in self.providers.items()
            if name not in exclude and provider['available'] and self.provider_enabled.get(name, True) and self.provider_failures.get(name, 0) < self.max_failures
        ]

        if not available_providers:
            logger.critical("❌ Todos os provedores de fallback falharam ou estão indisponíveis.")
            return None

        # Ordena por prioridade
        available_providers.sort(key=lambda x: (x[1]['priority'], self.provider_failures[x[0]]))
        return available_providers[0][0]

    def _handle_rate_limit(self, provider_name: str, error_msg: str, extended_timeout: int = None):
        """Lida com rate limits, desabilitando o provedor temporariamente."""

        # Calcula tempo de reset baseado no erro ou timeout estendido
        reset_minutes = extended_timeout // 60 if extended_timeout else 4  # Default 4 minutos

        if not extended_timeout:
            if 'day' in error_msg.lower():
                reset_minutes = 1440  # 24 horas
            elif 'hour' in error_msg.lower():
                reset_minutes = 60  # 1 hora
            elif 'minute' in error_msg.lower():
                reset_minutes = 10  # 10 minutos

        reset_time = datetime.now() + timedelta(minutes=reset_minutes)

        # Atualiza o registro de rate limit
        self.rate_limits[provider_name] = {
            'reset_time': reset_time,
            'attempts': self.rate_limits.get(provider_name, {}).get('attempts', 0) + 1
        }

        logger.warning(f"⚠️ Rate limit atingido para {provider_name}")
        logger.warning(f"🔄 Desabilitado por {reset_minutes}m (tentativa {self.rate_limits[provider_name]['attempts']})")

        # Registra a falha e desabilita o provedor
        self._record_failure(provider_name, error_msg)
        self.provider_enabled[provider_name] = False # Marca explicitamente como desabilitado
        self.last_failure_time[provider_name] = time.time() # Atualiza o tempo da última falha para o cooldown

    def get_provider_status(self) -> Dict[str, Any]:
        """Retorna status detalhado dos provedores"""
        status = {}

        for name, provider in self.providers.items():
            status[name] = {
                'available': provider['available'] and self.provider_enabled.get(name, True),
                'priority': provider['priority'],
                'error_count': provider['error_count'],
                'consecutive_failures': self.provider_failures.get(name, 0),
                'last_success': provider.get('last_success'),
                'last_failure_time': self.last_failure_time.get(name),
                'enabled': self.provider_enabled.get(name, True),
                'max_errors': provider['max_errors'],
                'model': provider.get('model', 'N/A')
            }

        return status

    def _try_providers(self, method: str, prompt: str, **kwargs) -> Optional[Dict[str, Any]]:
        """Tenta executar o método especificado nos provedores disponíveis em ordem de prioridade."""
        provider_name = self.get_best_provider()

        if not provider_name:
            logger.error("❌ Nenhum provedor de IA disponível para tentar.")
            return None

        try:
            response_data = None
            if method == 'generate':
                response = self._call_provider(provider_name, prompt, kwargs.get('max_tokens', 1000))
                if response:
                    self._record_success(provider_name)
                    response_data = {
                        'response': response,
                        'provider': provider_name,
                        'tokens': len(response.split()) * 1.3,  # Estimativa aproximada
                        'success': True
                    }
                else:
                    self._record_failure(provider_name, "Resposta vazia do provedor.")
            # Adicione outros métodos conforme necessário aqui

            if response_data:
                return response_data
            else:
                # Se a resposta foi vazia ou falhou, tenta o próximo provedor
                return self._handle_provider_failure(provider_name, Exception("Falha na primeira tentativa de gerar resposta."))

        except Exception as e:
            logger.error(f"❌ Erro ao tentar provedor {provider_name} para o método {method}: {e}")
            return self._handle_provider_failure(provider_name, e)

# Instância global
ai_manager = AIManager()