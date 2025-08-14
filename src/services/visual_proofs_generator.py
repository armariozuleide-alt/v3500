#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Visual Proofs Generator
Gerador de Provas Visuais Instantâneas
"""

import time
import random
import logging
import json
import re
from typing import Dict, List, Any, Optional
from datetime import datetime
from services.ai_manager import ai_manager
from services.auto_save_manager import salvar_etapa, salvar_erro
from services.google_api_rotation import google_api_rotation

logger = logging.getLogger(__name__)

# Usa a instância global do rotador de chaves da API do Google
google_api_rotator = google_api_rotation

class VisualProofsGenerator:
    """Gerador de Provas Visuais Instantâneas"""

    def __init__(self):
        """Inicializa o gerador de provas visuais"""
        self.proof_types = self._load_proof_types()
        self.visual_elements = self._load_visual_elements()

        logger.info("Visual Proofs Generator inicializado")

    def _load_proof_types(self) -> Dict[str, Dict[str, Any]]:
        """Carrega tipos de provas visuais"""
        return {
            'antes_depois': {
                'nome': 'Transformação Antes/Depois',
                'objetivo': 'Mostrar transformação clara e mensurável',
                'impacto': 'Alto',
                'facilidade': 'Média'
            },
            'comparacao_competitiva': {
                'nome': 'Comparação vs Concorrência',
                'objetivo': 'Demonstrar superioridade clara',
                'impacto': 'Alto',
                'facilidade': 'Alta'
            },
            'timeline_resultados': {
                'nome': 'Timeline de Resultados',
                'objetivo': 'Mostrar progressão temporal',
                'impacto': 'Médio',
                'facilidade': 'Alta'
            },
            'social_proof_visual': {
                'nome': 'Prova Social Visual',
                'objetivo': 'Validação através de terceiros',
                'impacto': 'Alto',
                'facilidade': 'Média'
            },
            'demonstracao_processo': {
                'nome': 'Demonstração do Processo',
                'objetivo': 'Mostrar como funciona na prática',
                'impacto': 'Médio',
                'facilidade': 'Baixa'
            }
        }

    def _load_visual_elements(self) -> Dict[str, List[str]]:
        """Carrega elementos visuais disponíveis"""
        return {
            'graficos': ['Barras', 'Linhas', 'Pizza', 'Área', 'Dispersão'],
            'comparacoes': ['Lado a lado', 'Sobreposição', 'Timeline', 'Tabela'],
            'depoimentos': ['Vídeo', 'Texto', 'Áudio', 'Screenshot'],
            'demonstracoes': ['Screencast', 'Fotos', 'Infográfico', 'Animação'],
            'dados': ['Números', 'Percentuais', 'Valores', 'Métricas']
        }

    def generate_comprehensive_proofs(self, avatar_data: Dict[str, Any], context_data: Dict[str, Any] = None, drivers: List[Dict] = None, session_id: str = None) -> Dict[str, Any]:
        """Gera provas visuais abrangentes e detalhadas"""
        try:
            logger.info("🎭 Gerando provas visuais abrangentes...")

            if not context_data:
                context_data = {}

            segmento = context_data.get('segmento', 'mercado')
            produto = context_data.get('produto', 'produto')

            # Verifica se as chaves da API do Google estão configuradas
            if not google_api_rotator.is_google_api_available():
                logger.error("❌ Chaves Google API não configuradas. Não é possível gerar provas visuais.")
                return {
                    'success': False,
                    'error': 'Google API keys not configured.',
                    'message': 'Provedor google desabilitado temporariamente devido à falta de chaves API.'
                }

            # Conceitos para provas visuais
            conceitos_base = [
                f"Eficacia do {produto}",
                f"Transformacao no {segmento}",
                "Urgencia de acao",
                "Escassez temporal",
                "Prova social massiva",
                "Autoridade no mercado",
                "Simplicidade do metodo"
            ]

            provas_geradas = {}

            # Gera provas para cada conceito
            for i, conceito in enumerate(conceitos_base, 1):
                try:
                    # Tenta gerar com IA, se falhar, usa fallback
                    prova = self._generate_single_prova_with_ai(conceito, avatar_data, context_data)
                    if prova:
                        prova_key = f"prova_{i}_{conceito.lower().replace(' ', '_')}"
                        provas_geradas[prova_key] = prova
                        logger.info(f"✅ Prova visual {i} gerada: {conceito}")
                    else:
                        # Fallback para prova basica se IA falhar ou não retornar algo válido
                        logger.warning(f"⚠️ IA falhou para '{conceito}', usando prova básica.")
                        provas_geradas[f"prova_{i}_basica"] = self._create_basic_prova(conceito, segmento, produto)

                except Exception as e:
                    logger.error(f"❌ Erro ao processar geração para prova {i} ('{conceito}'): {e}")
                    # Fallback em caso de exceção geral durante a geração
                    provas_geradas[f"prova_{i}_fallback"] = self._create_basic_prova(conceito, segmento, produto)

            # Validação e melhoria das provas geradas
            provas_validadas = {}
            for key, prova in provas_geradas.items():
                # Verifica se a prova tem a estrutura esperada antes de validar a qualidade
                if isinstance(prova, dict) and self._validate_prova_quality(prova, context_data):
                    provas_validadas[key] = prova
                else:
                    logger.warning(f"Prova '{key}' falhou na validação de qualidade ou estrutura. Tentando criar prova básica como fallback.")
                    # Se a prova gerada (mesmo a básica) não passar na validação, cria uma nova prova básica.
                    provas_validadas[f"{key}_fallback_validacao"] = self._create_basic_prova(prova.get('conceito_alvo', 'conceito desconhecido'), segmento, produto)

            # Garante um mínimo de 5 provas, adicionando mais se necessário
            if len(provas_validadas) < 5:
                logger.info(f"Gerando provas adicionais para atingir o mínimo de 5. Atualmente: {len(provas_validadas)}")
                for i in range(len(provas_validadas), 5):
                    conceito_extra = f"Benefício adicional {i+1} para {produto}"
                    # Cria uma prova básica para os conceitos adicionais
                    provas_validadas[f"prova_extra_{i+1}"] = self._create_basic_prova(conceito_extra, segmento, produto)

            return {
                'success': True,
                'total_provas': len(provas_validadas),
                'provas_visuais': provas_validadas,
                'segmento': segmento,
                'produto': produto,
                'metadata': {
                    'generated_at': datetime.now().isoformat(),
                    'ai_generated': len([p for p in provas_validadas.values() if p.get('fonte') == 'ai_generated']),
                    'fallback_generated': len([p for p in provas_validadas.values() if p.get('fallback_mode')])
                }
            }

        except Exception as e:
            logger.error(f"❌ Erro critico ao gerar provas visuais abrangentes: {e}")
            # Cria provas de emergência se ocorrer um erro crítico geral
            return {
                'success': False,
                'error': str(e),
                'fallback_provas': self._create_emergency_provas(avatar_data, context_data)
            }

    def _create_emergency_provas(self, avatar_data: Dict[str, Any], context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria provas de emergência quando tudo falha"""
        segmento = context_data.get('segmento', 'mercado')
        produto = context_data.get('produto', 'produto')

        return {
            'prova_emergencia_1': self._create_basic_prova("Eficacia comprovada", segmento, produto),
            'prova_emergencia_2': self._create_basic_prova("Transformacao real", segmento, produto),
            'prova_emergencia_3': self._create_basic_prova("Resultados garantidos", segmento, produto)
        }

    def _validate_prova_quality(self, prova: Dict[str, Any], context_data: Dict[str, Any]) -> bool:
        """Valida a qualidade e relevância de uma prova visual"""
        if not isinstance(prova, dict):
            logger.warning(f"Tentativa de validar um objeto que não é um dicionário: {prova}")
            return False

        # Verifica se possui elementos essenciais
        required_keys = ['nome', 'conceito_alvo', 'tipo_prova', 'experimento', 'materiais', 'roteiro_completo', 'metricas_sucesso']
        if not all(key in prova for key in required_keys):
            logger.warning(f"Prova com chaves faltando: {prova.get('nome', 'Desconhecido')}")
            return False

        # Verifica se o conceito alvo está relacionado ao contexto
        segmento = context_data.get('segmento', '').lower()
        produto = context_data.get('produto', '').lower()
        conceito_alvo = prova.get('conceito_alvo', '').lower()

        if segmento and segmento not in conceito_alvo and \
           produto and produto not in conceito_alvo:
            logger.warning(f"Prova fora de contexto: {prova.get('nome', 'Desconhecido')}")
            return False

        # Verifica se há materiais e roteiro descritos
        if not prova.get('materiais') or not prova.get('roteiro_completo'):
            logger.warning(f"Prova sem materiais ou roteiro: {prova.get('nome', 'Desconhecido')}")
            return False

        # Verifica se 'materiais' é uma lista não vazia
        if not isinstance(prova.get('materiais'), list) or not prova.get('materiais'):
            logger.warning(f"Prova com 'materiais' inválido: {prova.get('nome', 'Desconhecido')}")
            return False

        # Verifica se 'roteiro_completo' é um dicionário com as chaves esperadas
        roteiro = prova.get('roteiro_completo')
        if not isinstance(roteiro, dict) or not all(k in roteiro for k in ['preparacao', 'execucao', 'impacto_esperado']):
            logger.warning(f"Prova com 'roteiro_completo' inválido: {prova.get('nome', 'Desconhecido')}")
            return False

        # Verifica se 'metricas_sucesso' é uma lista não vazia
        if not isinstance(prova.get('metricas_sucesso'), list) or not prova.get('metricas_sucesso'):
            logger.warning(f"Prova com 'metricas_sucesso' inválido: {prova.get('nome', 'Desconhecido')}")
            return False


        return True

    def _generate_single_prova_with_ai(self, conceito: str, avatar_data: Dict[str, Any], context_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Gera uma única prova visual usando IA"""
        try:
            segmento = context_data.get('segmento', 'negócios')
            produto = context_data.get('produto', 'produto')

            proof_type_info = self._select_best_proof_type(conceito, avatar_data)

            # Prompt para a IA
            prompt = f"""
Crie uma prova visual específica e convincente para o conceito: "{conceito}"

CONTEXTO:
- Segmento: {segmento}
- Produto: {produto}
- Avatar: Dores: {avatar_data.get('dores_viscerais', [])}, Desejos: {avatar_data.get('desejos_secretos', [])}

TIPO DE PROVA SUGERIDO: {proof_type_info['nome']}
OBJETIVO DA PROVA: {proof_type_info['objetivo']}
IMPACTO ESPERADO: {proof_type_info['impacto']}

FORMATO DE SAÍDA: JSON válido contendo as chaves:
- nome: Título da prova (Ex: "PROVI X: [Título Descritivo]")
- conceito_alvo: O conceito que a prova demonstra (igual ao input)
- tipo_prova: O tipo de prova selecionado (Ex: "{proof_type_info['nome']}")
- experimento: Descrição detalhada do que será demonstrado visualmente. Seja específico sobre os elementos visuais.
- materiais: Lista de materiais visuais necessários (Ex: ["Gráfico de barras comparativo", "Screenshot de dashboard", "Vídeo curto de depoimento"]). Seja específico.
- roteiro_completo: Dicionário com as chaves "preparacao", "execucao", "impacto_esperado". Descreva as etapas de forma clara e objetiva.
- metricas_sucesso: Lista de métricas para avaliar o sucesso da prova (Ex: ["Redução de objeções", "Aumento de engajamento"]).
- ai_generated: true (indica que foi gerado por IA)

AJUSTE O PROMPT PARA SER MAIS ESPECÍFICO E GERAR UM JSON MAIS DETALHADO E ACIONÁVEL.
Seja criativo e use os dados do avatar para personalizar a prova.
"""

            response = ai_manager.generate_analysis(prompt, max_tokens=1000)

            if response:
                proof_data = self._process_ai_response(response, conceito)
                if proof_data:
                    # Validação básica das chaves obrigatórias antes de retornar
                    if self._validate_prova_quality(proof_data, context_data):
                        proof_data['fonte'] = 'ai_generated' # Marca como gerado por IA
                        return proof_data
                    else:
                        logger.warning(f"Prova gerada por IA falhou na validação interna para o conceito '{conceito}'. Retornando None.")
                        return None
                else:
                    logger.warning(f"IA não retornou resposta válida ou JSON para o conceito '{conceito}'.")
                    # Se a IA falhar em retornar um JSON válido, tenta gerar uma prova de fallback
                    return self._create_fallback_visual_proof(conceito, context_data)
            else:
                logger.warning(f"IA não retornou resposta para o conceito '{conceito}'.")
                # Se a IA não retornar nada, também tenta gerar uma prova de fallback
                return self._create_fallback_visual_proof(conceito, context_data)

        except Exception as e:
            logger.error(f"Erro ao gerar prova visual com IA para o conceito '{conceito}': {e}")
            # Retorna uma prova de fallback em caso de qualquer exceção durante a geração com IA
            return self._create_fallback_visual_proof(conceito, context_data)

    def _process_ai_response(self, response: str, conceito: str) -> Optional[Dict[str, Any]]:
        """Processa resposta da IA para extrair prova visual"""

        try:
            # Valida tipo da resposta
            if not isinstance(response, str):
                logger.warning(f"⚠️ Resposta da IA não é string: {type(response)}")
                return None

            # Tenta extrair JSON usando regex mais robusto
            # Busca por ```json ... ``` ou apenas {...}
            json_match = re.search(r'```json\s*(\{.*?\})\s*```', response, re.DOTALL | re.IGNORECASE)
            if not json_match:
                json_match = re.search(r'\{.*\}', response, re.DOTALL) # Busca por qualquer JSON simples

            if json_match:
                json_str = json_match.group(1) if json_match.groups() else json_match.group(0)
                prova_data = json.loads(json_str)

                # Valida se é dicionário
                if not isinstance(prova_data, dict):
                    logger.warning(f"⚠️ JSON extraído não é um dicionário para o conceito '{conceito}': {type(prova_data)}")
                    return None

                # Valida estrutura mínima esperada
                required_fields = ['nome', 'conceito_alvo', 'tipo_prova', 'experimento']
                if all(field in prova_data for field in required_fields):
                    # Adiciona detalhes caso existam, ou cria um placeholder
                    prova_data['detalhes'] = self._extrair_detalhes_prova(response)
                    return prova_data
                else:
                    missing = [f for f in required_fields if f not in prova_data]
                    logger.warning(f"⚠️ Campos obrigatórios ausentes no JSON para '{conceito}': {missing}")
                    return None

            logger.warning(f"Nenhum bloco JSON encontrado na resposta da IA para o conceito '{conceito}'.")
            return None

        except json.JSONDecodeError as e:
            logger.error(f"Erro de decodificação JSON para o conceito '{conceito}': {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Erro ao processar resposta da IA para o conceito '{conceito}': {str(e)}")
            return None

    def _extrair_detalhes_prova(self, response_text: str) -> Dict[str, Any]:
        """Extrai detalhes adicionais da resposta da IA que não são estritamente o JSON principal."""
        detalhes = {}
        # Exemplo: Extrair informações de "impacto esperado" se presentes fora do JSON
        impacto_match = re.search(r"IMPACTO ESPERADO:\s*(.*?)(?:\n|$)", response_text, re.IGNORECASE)
        if impacto_match:
            detalhes['impacto_esperado'] = impacto_match.group(1).strip()
        return detalhes


    def _select_best_proof_type(self, concept: str, avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Seleciona melhor tipo de prova para o conceito"""

        concept_lower = concept.lower()

        # Mapeia conceitos para tipos de prova
        if any(word in concept_lower for word in ['resultado', 'crescimento', 'melhoria', 'eficacia', 'performance', 'ganho']):
            return self.proof_types['antes_depois']
        elif any(word in concept_lower for word in ['concorrente', 'melhor', 'superior', 'diferencial', 'vantagem']):
            return self.proof_types['comparacao_competitiva']
        elif any(word in concept_lower for word in ['tempo', 'rapidez', 'velocidade', 'progressao', 'jornada']):
            return self.proof_types['timeline_resultados']
        elif any(word in concept_lower for word in ['outros', 'clientes', 'pessoas', 'social', 'depoimento', 'confianca', 'feedback']):
            return self.proof_types['social_proof_visual']
        elif any(word in concept_lower for word in ['processo', 'metodo', 'como funciona', 'passo a passo', 'etapas']):
            return self.proof_types['demonstracao_processo']
        else: # Default caso nenhum seja encontrado
            logger.warning(f"Nenhum tipo de prova correspondente encontrado para o conceito: '{concept}'. Usando 'Demonstração do Processo' como padrão.")
            return self.proof_types['demonstracao_processo']

    def _create_basic_prova(self, concept: str, segmento: str, produto: str) -> Dict[str, Any]:
        """Cria uma prova visual básica como fallback"""
        # Tenta associar um tipo de prova baseada no conceito, se possível
        proof_type_info = self._select_best_proof_type(concept, {}) # Avatar data não é essencial aqui

        # Garante que proof_type_info é um dicionário e tem as chaves esperadas
        if not isinstance(proof_type_info, dict) or not all(k in proof_type_info for k in ['nome', 'objetivo', 'impacto', 'facilidade']):
            logger.error(f"Erro ao obter informações do tipo de prova para o conceito '{concept}'. Usando defaults.")
            proof_type_info = {
                'nome': 'Prova Genérica',
                'objetivo': 'Demonstrar valor',
                'impacto': 'Médio',
                'facilidade': 'Média'
            }

        return {
            'nome': f'PROVI: {proof_type_info["nome"]} para {produto}',
            'conceito_alvo': concept,
            'tipo_prova': proof_type_info['nome'],
            'experimento': f'Demonstração visual focada em "{concept}" para o {produto} no segmento de {segmento}.',
            'materiais': [
                f'Gráficos relevantes ({proof_type_info["nome"].lower()})',
                'Dados numéricos que suportam o conceito',
                'Screenshots de resultados ou interface',
                'Citações ou feedbacks curtos de clientes'
            ],
            'roteiro_completo': {
                'preparacao': f'Reunir dados e exemplos visuais que ilustrem o conceito "{concept}"',
                'execucao': f'Apresentar a prova de forma clara e concisa, conectando com os benefícios para o cliente',
                'impacto_esperado': 'Aumento da percepção de valor e confiança no produto'
            },
            'metricas_sucesso': [
                f'Redução de objeções relacionadas a "{concept}"',
                'Aumento de interesse e engajamento com a prova',
                f'Confirmação de que "{concept}" é um benefício chave percebido'
            ],
            'fallback_mode': True # Indica que é uma prova de fallback
        }

    def _get_default_visual_proofs(self, context_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Retorna provas visuais padrão como fallback geral"""

        segmento = context_data.get('segmento', 'negócios')
        produto = context_data.get('produto', 'produto')

        return [
            {
                'nome': f'PROVI 1: Resultados Comprovados em {segmento}',
                'conceito_alvo': f'Eficácia da metodologia em {segmento}',
                'tipo_prova': 'Antes/Depois',
                'experimento': f'Comparação visual de resultados antes e depois da aplicação da metodologia em {segmento}',
                'materiais': ['Gráficos de crescimento', 'Dados de performance', 'Screenshots de métricas'],
                'roteiro_completo': {
                    'preparacao': 'Organize dados de clientes que aplicaram a metodologia',
                    'execucao': 'Mostre transformação clara com números específicos',
                    'impacto_esperado': 'Convencimento através de evidência visual'
                },
                'metricas_sucesso': ['Redução de ceticismo', 'Aumento de interesse']
            },
            {
                'nome': f'PROVI 2: Comparação com Mercado em {segmento}',
                'conceito_alvo': f'Superioridade da abordagem em {segmento}',
                'tipo_prova': 'Comparação Competitiva',
                'experimento': f'Comparação visual entre abordagem tradicional e metodologia específica para {segmento}',
                'materiais': ['Tabelas comparativas', 'Gráficos de performance', 'Benchmarks do setor'],
                'roteiro_completo': {
                    'preparacao': 'Colete dados de mercado e benchmarks',
                    'execucao': 'Apresente comparação lado a lado',
                    'impacto_esperado': 'Demonstração clara de vantagem competitiva'
                },
                'metricas_sucesso': ['Compreensão do diferencial', 'Justificativa de preço premium']
            },
            {
                'nome': f'PROVI 3: Depoimentos Visuais {segmento}',
                'conceito_alvo': f'Validação social no {segmento}',
                'tipo_prova': 'Prova Social Visual',
                'experimento': f'Compilação visual de depoimentos de profissionais de {segmento}',
                'materiais': ['Vídeos de depoimento', 'Screenshots de resultados', 'Fotos de clientes'],
                'roteiro_completo': {
                    'preparacao': 'Selecione melhores depoimentos com resultados',
                    'execucao': 'Apresente sequência de validações sociais',
                    'impacto_esperado': 'Redução de risco percebido'
                },
                'metricas_sucesso': ['Aumento de confiança', 'Redução de objeções']
            }
        ]

    def _generate_fallback_visual_proof(self, conceito: str, contexto: Dict[str, Any]) -> Dict[str, Any]:
        """Gera prova visual de fallback quando IA falha ou não retorna dados úteis"""

        fallback_definitions = {
            'Eficacia do produto': {
                'tipo': 'Comparação Visual',
                'descricao': f'Demonstração prática da eficácia do {contexto.get("produto", "produto")}',
                'elementos': ['Antes vs Depois', 'Métricas de performance', 'Resultados mensuráveis'],
                'impacto_psicologico': 'Alto - prova tangível de resultados'
            },
            'Credibilidade da empresa': {
                'tipo': 'Prova Social',
                'descricao': 'Evidências da credibilidade e autoridade da empresa',
                'elementos': ['Certificações', 'Depoimentos', 'Cases de sucesso'],
                'impacto_psicologico': 'Alto - constrói confiança imediata'
            },
            'Qualidade superior': {
                'tipo': 'Demonstração Comparativa',
                'descricao': 'Comparação visual da qualidade superior',
                'elementos': ['Materiais premium', 'Processos diferenciados', 'Acabamento superior'],
                'impacto_psicologico': 'Médio-Alto - justifica valor premium'
            },
            'Urgencia de acao': {
                'tipo': 'Contagem Regressiva / Escassez',
                'descricao': 'Criação de senso de urgência para a ação',
                'elementos': ['Timer visual', 'Ofertas limitadas', 'Notificações de estoque baixo'],
                'impacto_psicologico': 'Alto - impulsiona decisão rápida'
            },
            'Escassez temporal': {
                'tipo': 'Oferta Limitada Visual',
                'descricao': 'Evidenciação de tempo ou quantidade limitada',
                'elementos': ['Datas de expiração claras', 'Indicadores de poucas unidades'],
                'impacto_psicologico': 'Alto - FOMO (Fear Of Missing Out)'
            },
            'Prova social massiva': {
                'tipo': 'Compilação de Depoimentos/Avaliações',
                'descricao': 'Apresentação de grande volume de feedback positivo',
                'elementos': ['Gráficos de satisfação', 'Múltiplos depoimentos curtos', 'Selos de aprovação'],
                'impacto_psicologico': 'Alto - validação em massa'
            },
            'Autoridade no mercado': {
                'tipo': 'Reconhecimento e Premiações',
                'descricao': 'Demonstração de posição de liderança e reconhecimento',
                'elementos': ['Logos de parceiros importantes', 'Prêmios recebidos', 'Menções na mídia'],
                'impacto_psicologico': 'Alto - estabelece confiança e credibilidade'
            },
            'Simplicidade do metodo': {
                'tipo': 'Infográfico Passo a Passo',
                'descricao': 'Simplificação visual do processo ou método',
                'elementos': ['Fluxogramas', 'Ícones explicativos', 'Listas numeradas'],
                'impacto_psicologico': 'Médio - facilita compreensão e adoção'
            }
        }

        # Busca a definição específica para o conceito
        definition = fallback_definitions.get(conceito)

        if definition:
            # Cria uma prova básica estruturada com base na definição encontrada
            return {
                'nome': f'PROVI: {definition["tipo"]} sobre {conceito}',
                'conceito_alvo': conceito,
                'tipo_prova': definition['tipo'],
                'experimento': definition['descricao'],
                'materiais': definition['elementos'],
                'roteiro_completo': {
                    'preparacao': f'Coletar materiais visuais que representem {conceito}',
                    'execucao': f'Apresentar {definition["tipo"]} de forma clara e direta',
                    'impacto_esperado': f'{definition.get("impacto_psicologico", "Médio")} - {definition["descricao"]}'
                },
                'metricas_sucesso': [f'Compreensão de {conceito}', 'Engajamento com a prova'],
                'is_fallback': True,
                'fallback_reason': 'IA falhou ou não retornou dados úteis'
            }
        else:
            # Caso genérico se o conceito não estiver mapeado
            logger.warning(f"Conceito de fallback não mapeado: '{conceito}'. Usando prova genérica.")
            return {
                'nome': f'PROVI: Prova Visual Genérica para {conceito}',
                'conceito_alvo': conceito,
                'tipo_prova': 'Demonstração Geral',
                'experimento': f'Apresentação de evidências visuais para suportar o conceito de "{conceito}"',
                'materiais': ['Evidência tangível', 'Comparação visual', 'Validação de terceiros'],
                'roteiro_completo': {
                    'preparacao': 'Reunir quaisquer dados visuais disponíveis',
                    'execucao': 'Mostrar visualmente o ponto principal do conceito',
                    'impacto_esperado': 'Suporte visual ao argumento principal'
                },
                'metricas_sucesso': ['Clareza da mensagem', 'Percepção de valor'],
                'is_fallback': True,
                'fallback_reason': 'Conceito não mapeado ou erro desconhecido'
            }

# Instância global
visual_proofs_generator = VisualProofsGenerator()