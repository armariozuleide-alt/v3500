#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - DeepSeek AI Client
Cliente para API DeepSeek AI com modelo deepseek-chat-v3-0324:free
"""

import logging
import requests
import json
import time
from typing import Dict, Any, Optional
import os

logger = logging.getLogger(__name__)

class DeepSeekClient:
    """Cliente para API DeepSeek AI com modelo v3"""

    def __init__(self, api_key: Optional[str] = None):
        """Inicializa cliente DeepSeek"""
        self.api_key = api_key or os.getenv('DEEPSEEK_API_KEY')
        self.base_url = "https://api.deepseek.com/v1"
        self.model = "deepseek-chat-v3-0324:free"  # Modelo específico configurado
        self.available = bool(self.api_key)
        self.rate_limit_delay = 1.0  # Delay entre requests
        self.last_request_time = 0

        if self.available:
            logger.info(f"✅ DeepSeek AI Client inicializado com modelo {self.model}")
            self._test_connection()
        else:
            logger.warning("⚠️ DeepSeek AI Client sem API key - desabilitado")

    def _test_connection(self) -> bool:
        """Testa conexão com a API"""
        try:
            test_response = self.generate_analysis("Teste de conexão", max_tokens=10)
            if test_response:
                logger.info("✅ DeepSeek AI conexão validada")
                return True
            else:
                logger.warning("⚠️ DeepSeek AI teste de conexão falhou")
                return False
        except Exception as e:
            logger.error(f"❌ DeepSeek AI teste de conexão erro: {e}")
            return False

    def _respect_rate_limit(self):
        """Respeita rate limit da API"""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time

        if time_since_last < self.rate_limit_delay:
            sleep_time = self.rate_limit_delay - time_since_last
            time.sleep(sleep_time)

        self.last_request_time = time.time()

    def generate_analysis(self, prompt: str, max_tokens: int = 1000) -> Optional[str]:
        """Gera análise usando DeepSeek v3"""

        if not self.available:
            logger.warning("DeepSeek não disponível - sem API key")
            return None

        self._respect_rate_limit()

        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "User-Agent": "ARQV30-Enhanced-v2.0"
            }

            data = {
                "model": self.model,
                "messages": [
                    {
                        "role": "system", 
                        "content": "Você é um especialista em análise de mercado e persuasão. Forneça respostas detalhadas e actionáveis."
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                "max_tokens": max_tokens,
                "temperature": 0.7,
                "top_p": 0.9,
                "frequency_penalty": 0.1,
                "presence_penalty": 0.1
            }

            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=data,
                timeout=60  # Timeout aumentado
            )

            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content']
                logger.debug(f"✅ DeepSeek resposta: {len(content)} caracteres")
                return content
            elif response.status_code == 429:
                logger.warning("⚠️ DeepSeek rate limit atingido, aguardando...")
                time.sleep(5)
                return self.generate_analysis(prompt, max_tokens)  # Retry
            else:
                logger.error(f"❌ DeepSeek API erro: {response.status_code} - {response.text}")
                return None

        except requests.exceptions.Timeout:
            logger.error("❌ DeepSeek timeout - requisição demorou mais que 60s")
            return None
        except Exception as e:
            logger.error(f"❌ Erro ao conectar com DeepSeek: {e}")
            return None

    def generate_structured_analysis(self, prompt: str, format_type: str = "json") -> Optional[Dict[str, Any]]:
        """Gera análise estruturada"""

        structured_prompt = f"""
{prompt}

IMPORTANTE: Responda APENAS no formato {format_type.upper()} válido, sem texto adicional antes ou depois.
"""

        response = self.generate_analysis(structured_prompt, max_tokens=2000)

        if response and format_type.lower() == "json":
            try:
                # Limpa resposta para extrair JSON
                clean_response = response.strip()
                if "```json" in clean_response:
                    start = clean_response.find("```json") + 7
                    end = clean_response.rfind("```")
                    clean_response = clean_response[start:end].strip()

                return json.loads(clean_response)
            except json.JSONDecodeError:
                logger.error("❌ DeepSeek retornou JSON inválido")
                return None

        return {"content": response} if response else None

    def get_status(self) -> Dict[str, Any]:
        """Retorna status do cliente"""
        return {
            "available": self.available,
            "model": self.model,
            "base_url": self.base_url,
            "rate_limit_delay": self.rate_limit_delay
        }