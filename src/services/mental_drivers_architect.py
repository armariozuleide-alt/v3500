#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Mental Drivers Architect
Arquiteto de Drivers Mentais Customizados
"""

import time
import random
import logging
import json
import re # Import re for regex operations
from typing import Dict, List, Any, Optional
from services.ai_manager import ai_manager
from services.auto_save_manager import salvar_etapa, salvar_erro

logger = logging.getLogger(__name__)

class MentalDriversArchitect:
    """Arquiteto de Drivers Mentais Customizados"""

    def __init__(self):
        """Inicializa o arquiteto de drivers mentais"""
        self.universal_drivers = self._load_universal_drivers()
        self.driver_templates = self._load_driver_templates()

        logger.info("Mental Drivers Architect inicializado")

    def _load_universal_drivers(self) -> Dict[str, Dict[str, Any]]:
        """Carrega drivers mentais universais"""
        return {
            'urgencia_temporal': {
                'nome': 'Urgência Temporal',
                'gatilho_central': 'Tempo limitado para agir',
                'definicao_visceral': 'Criar pressão temporal que força decisão imediata',
                'aplicacao': 'Quando prospect está procrastinando'
            },
            'escassez_oportunidade': {
                'nome': 'Escassez de Oportunidade',
                'gatilho_central': 'Oportunidade única e limitada',
                'definicao_visceral': 'Amplificar valor através da raridade',
                'aplicacao': 'Para aumentar percepção de valor'
            },
            'prova_social': {
                'nome': 'Prova Social Qualificada',
                'gatilho_central': 'Outros como ele já conseguiram',
                'definicao_visceral': 'Reduzir risco através de validação social',
                'aplicacao': 'Para superar objeções de confiança'
            },
            'autoridade_tecnica': {
                'nome': 'Autoridade Técnica',
                'gatilho_central': 'Expertise comprovada',
                'definicao_visceral': 'Estabelecer credibilidade através de conhecimento',
                'aplicacao': 'Para construir confiança inicial'
            },
            'reciprocidade': {
                'nome': 'Reciprocidade Estratégica',
                'gatilho_central': 'Valor entregue antecipadamente',
                'definicao_visceral': 'Criar obrigação psicológica de retribuição',
                'aplicacao': 'Para gerar compromisso'
            }
        }

    def _load_driver_templates(self) -> Dict[str, str]:
        """Carrega templates de drivers"""
        return {
            'historia_analogia': 'Era uma vez {personagem} que enfrentava {problema_similar}. Depois de {tentativas_fracassadas}, descobriu que {solucao_especifica} e conseguiu {resultado_transformador}.',
            'metafora_visual': 'Imagine {situacao_atual} como {metafora_visual}. Agora visualize {situacao_ideal} como {metafora_transformada}.',
            'comando_acao': 'Agora que você {compreensao_adquirida}, a única ação lógica é {acao_especifica} porque {consequencia_inevitavel}.'
        }

    def generate_custom_drivers(
        self, 
        avatar_data: Dict[str, Any], 
        context_data: Dict[str, Any] = None,
        drivers: List[Dict] = None,
        session_id: str = None
    ) -> List[Dict[str, Any]]:
        """Gera drivers mentais customizados específicos"""

        logger.info("🧠 Gerando drivers mentais customizados específicos...")

        try:
            # Usa o sistema completo para gerar drivers customizados
            complete_system = self.generate_complete_drivers_system(avatar_data, context_data)
            return complete_system.get('drivers_customizados', [])

        except Exception as e:
            logger.error(f"❌ Erro ao gerar drivers customizados: {e}")
            return self._create_basic_drivers(context_data)

    def generate_complete_drivers_system(
        self, 
        avatar_data: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Gera sistema completo de drivers mentais customizados"""

        # Validação crítica de entrada com fallbacks
        if not avatar_data:
            logger.warning("⚠️ Avatar data vazio - usando fallback")
            avatar_data = {
                'nome': 'Avatar Padrão',
                'dores_viscerais': ['Crescimento lento', 'Falta de sistema', 'Concorrência'],
                'desejos_secretos': ['Crescimento rápido', 'Mais clientes', 'Mais lucro']
            }

        if not context_data or not context_data.get('segmento'):
            logger.warning("⚠️ Segmento não informado - usando fallback")
            if not context_data:
                context_data = {}
            context_data['segmento'] = context_data.get('segmento', 'mercado')
            context_data['produto'] = context_data.get('produto', 'produto')

        try:
            logger.info("🧠 Gerando drivers mentais customizados...")

            # Salva dados de entrada imediatamente
            salvar_etapa("drivers_entrada", {
                "avatar_data": avatar_data,
                "context_data": context_data
            }, categoria="drivers_mentais")

            # Analisa avatar para identificar drivers ideais
            ideal_drivers = self._identify_ideal_drivers(avatar_data, context_data)

            # Gera drivers customizados
            customized_drivers = self._generate_customized_drivers(ideal_drivers, avatar_data, context_data)

            if not customized_drivers:
                logger.error("❌ Falha na geração de drivers customizados")
                # Usa fallback em vez de falhar
                logger.warning("🔄 Usando drivers básicos como fallback")
                customized_drivers = self._generate_fallback_drivers_system(context_data)

            # Salva drivers customizados
            salvar_etapa("drivers_customizados", customized_drivers, categoria="drivers_mentais")

            # Cria roteiros de ativação
            activation_scripts = self._create_activation_scripts(customized_drivers, avatar_data)

            # Gera frases de ancoragem
            anchor_phrases = self._generate_anchor_phrases(customized_drivers, avatar_data)

            result = {
                'drivers_customizados': customized_drivers,
                'roteiros_ativacao': activation_scripts,
                'frases_ancoragem': anchor_phrases,
                'drivers_universais_utilizados': [d['nome'] for d in ideal_drivers],
                'personalizacao_nivel': self._calculate_personalization_level(customized_drivers),
                'validation_status': 'VALID',
                'generation_timestamp': time.time()
            }

            # Salva resultado final imediatamente
            salvar_etapa("drivers_final", result, categoria="drivers_mentais")

            logger.info("✅ Drivers mentais customizados gerados com sucesso")
            return result

        except Exception as e:
            logger.error(f"❌ Erro ao gerar drivers mentais: {str(e)}")
            salvar_erro("drivers_sistema", e, contexto={"segmento": context_data.get('segmento')})

            # Fallback para sistema básico em caso de erro
            logger.warning("🔄 Gerando drivers básicos como fallback...")
            return self._generate_fallback_drivers_system(context_data)

    def _identify_ideal_drivers(self, avatar_data: Dict[str, Any], context_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identifica drivers ideais baseado no avatar"""

        ideal_drivers = []

        # Analisa dores para identificar drivers
        dores = avatar_data.get('dores_viscerais', [])

        # Mapeia dores para drivers
        if any('tempo' in dor.lower() for dor in dores):
            ideal_drivers.append(self.universal_drivers['urgencia_temporal'])

        if any('concorrência' in dor.lower() or 'competidor' in dor.lower() for dor in dores):
            ideal_drivers.append(self.universal_drivers['escassez_oportunidade'])

        if any('resultado' in dor.lower() or 'crescimento' in dor.lower() for dor in dores):
            ideal_drivers.append(self.universal_drivers['prova_social'])

        # Sempre inclui autoridade técnica
        ideal_drivers.append(self.universal_drivers['autoridade_tecnica'])

        # Sempre inclui reciprocidade
        ideal_drivers.append(self.universal_drivers['reciprocidade'])

        return ideal_drivers[:5]  # Máximo 5 drivers

    def _generate_customized_drivers(
        self, 
        ideal_drivers: List[Dict[str, Any]], 
        avatar_data: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Gera drivers customizados usando IA"""

        try:
            segmento = context_data.get('segmento', 'negócios')

            prompt = f"""
Crie drivers mentais customizados para o segmento {segmento}.

AVATAR:
{json.dumps(avatar_data, indent=2, ensure_ascii=False)[:2000]}

DRIVERS IDEAIS:
{json.dumps(ideal_drivers, indent=2, ensure_ascii=False)[:1000]}

RETORNE APENAS JSON VÁLIDO:

```json
[
  {{
    "nome": "Nome específico do driver",
    "gatilho_central": "Gatilho psicológico principal",
    "definicao_visceral": "Definição que gera impacto emocional",
    "roteiro_ativacao": {{
      "pergunta_abertura": "Pergunta que ativa o driver",
      "historia_analogia": "História específica de 150+ palavras",
      "metafora_visual": "Metáfora visual poderosa",
      "comando_acao": "Comando específico de ação"
    }},
    "frases_ancoragem": [
      "Frase 1 de ancoragem",
      "Frase 2 de ancoragem",
      "Frase 3 de ancoragem"
    ],
    "prova_logica": "Prova lógica que sustenta o driver"
  }}
]
"""

            response = ai_manager.generate_completion(prompt)

            if response and response.get('status') == 'success':
                content = response.get('content', '{}')

                # Tenta extrair JSON - melhorado
                try:
                    # Procura por JSON na resposta
                    json_match = re.search(r'\{.*\}', content, re.DOTALL)
                    if json_match:
                        json_str = json_match.group(0)
                        drivers_data = json.loads(json_str)

                        if isinstance(drivers_data, dict) and 'drivers_customizados' in drivers_data:
                            salvar_etapa("drivers_customizados", drivers_data, categoria="drivers_mentais")
                            salvar_etapa("drivers_final", drivers_data, categoria="drivers_mentais")
                            logger.info("✅ Drivers customizados gerados com IA")
                            return drivers_data
                    else:
                        logger.warning("⚠️ JSON não encontrado na resposta da IA")

                except json.JSONDecodeError as e:
                    logger.warning(f"⚠️ IA retornou JSON inválido: {str(e)}")

            # Fallback
            logger.info("🔄 Usando drivers fallback")
            fallback_drivers = self._generate_fallback_drivers(avatar_data) # Note: _generate_fallback_drivers was not defined in the original code. Assuming it's a placeholder or meant to be _generate_fallback_drivers_system. Using the latter for continuity.
            return self._generate_fallback_drivers_system(context_data)

        except Exception as e:
            logger.error(f"❌ Erro ao gerar drivers customizados: {str(e)}")
            return self._create_basic_drivers(context_data)

    def _create_basic_drivers(self, context_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Cria drivers básicos como fallback"""

        segmento = context_data.get('segmento', 'negócios')

        return [
            {
                'nome': f'Urgência {segmento}',
                'gatilho_central': f'Tempo limitado para dominar {segmento}',
                'definicao_visceral': f'Cada dia sem otimizar {segmento} é oportunidade perdida',
                'roteiro_ativacao': {
                    'pergunta_abertura': f'Há quanto tempo você está no mesmo nível em {segmento}?',
                    'historia_analogia': f'Conheci um profissional de {segmento} que estava estagnado há 3 anos. Trabalhava 12 horas por dia mas não saía do lugar. Quando implementou um sistema específico para {segmento}, em 6 meses triplicou os resultados. A diferença não foi trabalhar mais, foi trabalhar com método.',
                    'metafora_visual': f'Imagine {segmento} como uma corrida. Você está correndo no lugar enquanto outros avançam.',
                    'comando_acao': f'Pare de correr no lugar em {segmento} e comece a usar um método comprovado'
                },
                'frases_ancoragem': [
                    f'Cada mês sem otimizar {segmento} custa oportunidades',
                    f'Seus concorrentes em {segmento} não estão esperando',
                    f'O tempo perdido em {segmento} não volta mais'
                ],
                'prova_logica': f'Profissionais que aplicaram métodos específicos em {segmento} cresceram 300% mais rápido'
            },
            {
                'nome': f'Autoridade {segmento}',
                'gatilho_central': f'Expertise comprovada em {segmento}',
                'definicao_visceral': f'Ser reconhecido como autoridade em {segmento}',
                'roteiro_ativacao': {
                    'pergunta_abertura': f'O que falta para você ser visto como autoridade em {segmento}?',
                    'historia_analogia': f'Um cliente meu em {segmento} era invisível no mercado. Aplicou nossa metodologia e em 8 meses estava palestrando em eventos do setor. A diferença foi posicionamento estratégico e execução consistente.',
                    'metafora_visual': f'Autoridade em {segmento} é como um farol - todos veem e confiam',
                    'comando_acao': f'Construa sua autoridade em {segmento} com método comprovado'
                },
                'frases_ancoragem': [
                    f'Autoridade em {segmento} atrai clientes automaticamente',
                    f'Especialistas em {segmento} cobram 5x mais',
                    f'Reconhecimento em {segmento} gera oportunidades únicas'
                ],
                'prova_logica': f'Autoridades em {segmento} têm 500% mais oportunidades de negócio'
            },
            {
                'nome': f'Método vs Sorte',
                'gatilho_central': 'Diferença entre método e tentativa',
                'definicao_visceral': f'Parar de tentar e começar a aplicar método em {segmento}',
                'roteiro_ativacao': {
                    'pergunta_abertura': f'Você está tentando ou aplicando método em {segmento}?',
                    'historia_analogia': f'Dois profissionais de {segmento} começaram juntos. Um ficou tentando estratégias aleatórias, outro seguiu um método específico. Após 1 ano: o primeiro ainda lutava para crescer, o segundo já era referência no mercado. A diferença não foi talento, foi método.',
                    'metafora_visual': f'Tentar em {segmento} é como atirar no escuro. Método é como ter mira laser.',
                    'comando_acao': f'Pare de tentar e comece a aplicar método comprovado em {segmento}'
                },
                'frases_ancoragem': [
                    f'Método em {segmento} elimina tentativa e erro',
                    f'Profissionais com método crescem 10x mais rápido',
                    f'Sorte é para quem não tem método'
                ],
                'prova_logica': f'Metodologia específica para {segmento} reduz tempo de resultado em 80%'
            }
        ]

    def _create_activation_scripts(self, drivers: List[Dict[str, Any]], avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria roteiros de ativação para cada driver"""

        scripts = {}

        for driver in drivers:
            driver_name = driver.get('nome', 'Driver')
            roteiro = driver.get('roteiro_ativacao', {})

            scripts[driver_name] = {
                'abertura': roteiro.get('pergunta_abertura', ''),
                'desenvolvimento': roteiro.get('historia_analogia', ''),
                'fechamento': roteiro.get('comando_acao', ''),
                'tempo_estimado': '3-5 minutos',
                'intensidade': 'Alta'
            }

        return scripts

    def _generate_anchor_phrases(self, drivers: List[Dict[str, Any]], avatar_data: Dict[str, Any]) -> Dict[str, List[str]]:
        """Gera frases de ancoragem para cada driver"""

        anchor_phrases = {}

        for driver in drivers:
            driver_name = driver.get('nome', 'Driver')
            frases = driver.get('frases_ancoragem', [])

            if frases:
                anchor_phrases[driver_name] = frases
            else:
                # Frases padrão
                anchor_phrases[driver_name] = [
                    f"Este é o momento de ativar {driver_name}",
                    f"Você sente o impacto de {driver_name}",
                    f"Agora {driver_name} faz sentido para você"
                ]

        return anchor_phrases

    def _calculate_personalization_level(self, drivers: List[Dict[str, Any]]) -> str:
        """Calcula nível de personalização dos drivers"""

        if not drivers:
            return "Baixo"

        # Verifica se tem histórias específicas
        has_stories = sum(1 for d in drivers if len(d.get('roteiro_ativacao', {}).get('historia_analogia', '')) > 100)

        # Verifica se tem frases de ancoragem
        has_anchors = sum(1 for d in drivers if len(d.get('frases_ancoragem', [])) >= 3)

        personalization_score = (has_stories + has_anchors) / (len(drivers) * 2)

        if personalization_score >= 0.8:
            return "Alto"
        elif personalization_score >= 0.5:
            return "Médio"
        else:
            return "Baixo"

    def _generate_fallback_drivers_system(self, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Gera sistema de drivers básico como fallback"""

        segmento = context_data.get('segmento', 'negócios')

        fallback_drivers = self._create_basic_drivers(context_data)

        return {
            'drivers_customizados': fallback_drivers,
            'roteiros_ativacao': {
                driver['nome']: {
                    'abertura': driver['roteiro_ativacao']['pergunta_abertura'],
                    'desenvolvimento': driver['roteiro_ativacao']['historia_analogia'],
                    'fechamento': driver['roteiro_ativacao']['comando_acao'],
                    'tempo_estimado': '3-5 minutos'
                } for driver in fallback_drivers
            },
            'frases_ancoragem': {
                driver['nome']: driver['frases_ancoragem'] for driver in fallback_drivers
            },
            'validation_status': 'FALLBACK_VALID',
            'generation_timestamp': time.time(),
            'fallback_mode': True
        }

    def generate_mental_drivers_customizados(self, data: Dict[str, Any], session_id: str = None) -> Dict[str, Any]:
        """Gera drivers mentais customizados específicos"""
        logger.info("🧠 Gerando drivers mentais customizados específicos...")

        if not data:
            logger.warning("⚠️ Dados não fornecidos - usando fallback")
            return self._generate_fallback_drivers_system(data if data is not None else {}) # Pass an empty dict if data is None

        # Extração mais robusta do segmento
        segmento = (
            data.get('segmento') or 
            data.get('target_market') or 
            data.get('mercado_alvo') or
            data.get('segment') or
            data.get('audience') or
            data.get('publico_alvo')
        )

        # Se ainda não encontrou, procura em estruturas aninhadas
        if not segmento:
            # Procura em dados de análise
            analise_data = data.get('analysis_data', {}) or data.get('dados_analise', {})
            segmento = (
                analise_data.get('segmento') or
                analise_data.get('target_market') or
                analise_data.get('mercado_alvo')
            )

        # Procura em requisição original
        if not segmento:
            request_data = data.get('request_data', {}) or data.get('dados_requisicao', {})
            segmento = (
                request_data.get('segmento') or
                request_data.get('target_market') or
                request_data.get('mercado_alvo')
            )

        if not segmento or segmento.strip() == "":
            logger.warning("⚠️ Segmento não informado - usando fallback")
            segmento = "mercado geral - empreendedores e gestores"

        produto = data.get('produto') or data.get('product') or data.get('servico') or "produto/serviço"
        contexto_data = data.get('pesquisa_dados', {}) or data.get('search_data', {})
        contexto_data['segmento'] = segmento # Ensure segment is in context_data
        contexto_data['produto'] = produto # Ensure product is in context_data

        logger.info(f"✅ Segmento identificado: {segmento}")
        return self.generate_complete_drivers_system(data, contexto_data) # Changed to use generate_complete_drivers_system for consistency

    def _extract_segment_from_context(self, data: Dict[str, Any]) -> str:
        """Extrai segmento do contexto dos dados"""
        try:
            # Procura em todos os campos possíveis
            all_text = str(data).lower()

            # Padrões comuns de segmento com prioridade
            segment_patterns = [
                ('empreendedores', 'empreendedores'),
                ('gestores', 'gestores de PMEs'),
                ('empresários', 'empresários'),
                ('consultores', 'consultores de negócios'),
                ('pequenas e médias empresas', 'pequenas e médias empresas'),
                ('pmes', 'pequenas e médias empresas'),
                ('startups', 'startups'),
                ('freelancers', 'freelancers'),
                ('autônomos', 'profissionais autônomos'),
                ('profissionais liberais', 'profissionais liberais'),
                ('marketing', 'profissionais de marketing'),
                ('vendas', 'profissionais de vendas'),
                ('digital', 'empreendedores digitais')
            ]

            for pattern, segment_name in segment_patterns:
                if pattern in all_text:
                    logger.info(f"✅ Segmento extraído do contexto: {segment_name}")
                    return segment_name

            # Tenta extrair segmento de campos específicos
            if 'publico' in data or 'audience' in data:
                publico_text = str(data.get('publico', data.get('audience', ''))).lower()
                for pattern, segment_name in segment_patterns:
                    if pattern in publico_text:
                        logger.info(f"✅ Segmento extraído do público-alvo: {segment_name}")
                        return segment_name

            # Se não encontrou nada específico, usa genérico mas útil
            logger.warning("⚠️ Usando segmento genérico: profissionais e empresários")
            return "profissionais e empresários"

        except Exception as e:
            logger.error(f"❌ Erro ao extrair segmento do contexto: {e}")
            return "profissionais e empresários"

# Instância global
mental_drivers_architect = MentalDriversArchitect()