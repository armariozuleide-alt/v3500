#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Pre-Pitch Architect
ARQUITETO DE PRÉ-PITCH INVISÍVEL - Sistema de preparação mental pré-venda
"""

import os
import logging
import json
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from services.ai_manager import ai_manager
from services.auto_save_manager import salvar_etapa, salvar_erro

logger = logging.getLogger(__name__)

class PrePitchArchitect:
    """
    ARQUITETO DE PRÉ-PITCH INVISÍVEL
    Missão: Preparar a mente do prospect de forma invisível antes do pitch,
    instalando âncoras emocionais que tornam a venda inevitável
    """

    def __init__(self):
        """Inicializa o Arquiteto de Pré-Pitch"""
        self.elementos_pre_pitch = self._inicializar_elementos()
        self.sequencias_preparacao = self._carregar_sequencias()
        self.triggers_inconscientes = self._carregar_triggers()
        logger.info("🎯 Pre-Pitch Architect inicializado com sucesso")

    def _inicializar_elementos(self) -> Dict[str, Any]:
        """Inicializa elementos fundamentais do pré-pitch"""
        return {
            'ancoras_emocionais': {
                'dor_amplificada': [],
                'desejo_intensificado': [],
                'urgencia_crescente': [],
                'confianca_construida': []
            },
            'preparacao_mental': {
                'quebra_resistencias': [],
                'abertura_receptividade': [],
                'construcao_autoridade': [],
                'criacao_dependencia': []
            },
            'sequencias_inviseis': {
                'pre_consciente': [],
                'subconsciente': [],
                'pos_consciente': []
            },
            'mecanismos_ativacao': {
                'gatilhos_temporais': [],
                'gatilhos_contextuais': [],
                'gatilhos_emocionais': []
            }
        }

    def _carregar_sequencias(self) -> Dict[str, List[Dict]]:
        """Carrega sequências de preparação mental"""
        return {
            'despertar_consciencia': [
                {
                    'nome': 'Identificação do Gap',
                    'objetivo': 'Fazer perceber que existe um problema',
                    'mecanismo': 'Apresentar realidade alternativa superior',
                    'timing': '7-14 dias antes',
                    'intensidade': 3
                },
                {
                    'nome': 'Amplificação da Dor',
                    'objetivo': 'Intensificar desconforto com situação atual',
                    'mecanismo': 'Mostrar consequências futuras',
                    'timing': '5-10 dias antes',
                    'intensidade': 6
                },
                {
                    'nome': 'Frustração Controlada',
                    'objetivo': 'Criar urgência por solução',
                    'mecanismo': 'Apresentar tentativas fracassadas',
                    'timing': '3-7 dias antes',
                    'intensidade': 7
                }
            ],
            'construcao_autoridade': [
                {
                    'nome': 'Demonstração de Expertise',
                    'objetivo': 'Estabelecer credibilidade técnica',
                    'mecanismo': 'Compartilhar insights exclusivos',
                    'timing': '10-21 dias antes',
                    'intensidade': 4
                },
                {
                    'nome': 'Prova Social Indireta',
                    'objetivo': 'Mostrar resultados sem vender',
                    'mecanismo': 'Cases de sucesso relevantes',
                    'timing': '7-14 dias antes',
                    'intensidade': 5
                },
                {
                    'nome': 'Reconhecimento de Terceiros',
                    'objetivo': 'Validação externa da autoridade',
                    'mecanismo': 'Menções e endossos',
                    'timing': '3-10 dias antes',
                    'intensidade': 6
                }
            ],
            'criacao_reciprocidade': [
                {
                    'nome': 'Valor Antecipado',
                    'objetivo': 'Criar sensação de dívida',
                    'mecanismo': 'Entregar valor genuíno gratuito',
                    'timing': '14-30 dias antes',
                    'intensidade': 4
                },
                {
                    'nome': 'Insight Exclusivo',
                    'objetivo': 'Demonstrar acesso privilegiado',
                    'mecanismo': 'Compartilhar informação restrita',
                    'timing': '7-21 dias antes',
                    'intensidade': 6
                },
                {
                    'nome': 'Solução Parcial',
                    'objetivo': 'Provar capacidade de resolver',
                    'mecanismo': 'Resolver problema menor',
                    'timing': '3-14 dias antes',
                    'intensidade': 7
                }
            ]
        }

    def _carregar_triggers(self) -> Dict[str, List[str]]:
        """Carrega triggers inconscientes"""
        return {
            'linguisticos': [
                'Padrões de repetição específicos',
                'Ancoragens verbais sutis',
                'Pressuposições linguísticas',
                'Comandos embutidos'
            ],
            'emocionais': [
                'Estados emocionais induzidos',
                'Sequências de sentimentos',
                'Contrastes emocionais',
                'Âncoras sentimentais'
            ],
            'cognitivos': [
                'Loops de curiosidade',
                'Gaps de informação',
                'Padrões interrompidos',
                'Questões em aberto'
            ],
            'comportamentais': [
                'Microcomprometimentos',
                'Progressão de sim',
                'Comportamentos condicionados',
                'Rituais preparatórios'
            ]
        }

    def generate_advanced_pre_pitch(
        self,
        avatar_data: Dict[str, Any],
        oferta_data: Dict[str, Any],
        drivers_mentais: Dict[str, Any],
        session_id: str = None
    ) -> Dict[str, Any]:
        """Gera pré-pitch avançado e otimizado"""

        logger.info("🎯 Gerando pré-pitch avançado...")

        try:
            # Usa o sistema completo
            base_pre_pitch = self.construir_pre_pitch_invisivel(avatar_data, oferta_data, drivers_mentais, session_id)

            # Adiciona elementos avançados
            advanced_elements = {
                'sequencias_neurociencia': self._criar_sequencias_neurociencia(avatar_data),
                'triggers_subconscientes': self._criar_triggers_subconscientes(drivers_mentais),
                'automation_scripts': self._criar_scripts_automacao(base_pre_pitch),
                'personalization_matrix': self._criar_matriz_personalizacao(avatar_data),
                'conversion_boosters': self._criar_boosters_conversao(oferta_data)
            }

            # Integra elementos avançados
            base_pre_pitch.update(advanced_elements)

            return base_pre_pitch

        except Exception as e:
            logger.error(f"❌ Erro ao gerar pré-pitch avançado: {e}")
            return self._pre_pitch_fallback(avatar_data)

    def construir_pre_pitch_invisivel(self, avatar_data: Dict[str, Any],
                                    oferta_data: Dict[str, Any],
                                    drivers_mentais: Dict[str, Any],
                                    session_id: str) -> Dict[str, Any]:
        """
        Constrói sistema completo de pré-pitch invisível
        """
        try:
            logger.info("🎯 Construindo pré-pitch invisível personalizado")

            # 1. Análise do estado mental atual
            estado_mental = self._analisar_estado_mental_atual(avatar_data)

            # 2. Design da jornada de preparação
            jornada_preparacao = self._designar_jornada_preparacao(
                avatar_data, estado_mental, drivers_mentais
            )

            # 3. Construção de sequências invisíveis
            sequencias_invisiveis = self._construir_sequencias_invisiveis(
                jornada_preparacao, oferta_data
            )

            # 4. Scripts de implementação
            scripts_implementacao = self._gerar_scripts_implementacao(
                sequencias_invisiveis, avatar_data
            )

            # 5. Sistema de mensuração
            sistema_mensuracao = self._criar_sistema_mensuracao(sequencias_invisiveis)

            # 6. Plano de execução temporal
            plano_temporal = self._criar_plano_temporal(sequencias_invisiveis)

            pre_pitch_completo = {
                'avatar_nome': avatar_data.get('nome', 'Indefinido'),
                'estado_mental_atual': estado_mental,
                'jornada_preparacao': jornada_preparacao,
                'sequencias_invisiveis': sequencias_invisiveis,
                'scripts_implementacao': scripts_implementacao,
                'sistema_mensuracao': sistema_mensuracao,
                'plano_temporal': plano_temporal,
                'elementos_ancoragem': self._definir_elementos_ancoragem(sequencias_invisiveis),
                'metricas_esperadas': self._calcular_metricas_esperadas(sequencias_invisiveis),
                'timestamp': datetime.now().isoformat()
            }

            salvar_etapa('pre_pitch_invisivel', pre_pitch_completo, session_id)

            logger.info("✅ Pré-pitch invisível construído com sucesso")
            return pre_pitch_completo

        except Exception as e:
            error_msg = f"Erro ao construir pré-pitch: {str(e)}"
            logger.error(f"❌ {error_msg}")
            salvar_erro('pre_pitch_architect', error_msg, session_id)
            return {'error': error_msg}

    def _analisar_estado_mental_atual(self, avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analisa estado mental do avatar"""
        try:
            # Verifica se avatar_data é válido
            if not isinstance(avatar_data, dict):
                logger.warning("Avatar data inválido - usando dados padrão")
                avatar_data = self._get_default_avatar_data()

            # Tratamento robusto de dores e desejos
            dores = avatar_data.get('dores_viscerais', [])
            desejos = avatar_data.get('desejos_secretos', [])

            # Converte string para lista se necessário
            if isinstance(dores, str):
                dores = [dores]
            elif not isinstance(dores, list):
                dores = []

            if isinstance(desejos, str):
                desejos = [desejos]
            elif not isinstance(desejos, list):
                desejos = []

            # Garante que temos pelo menos dados básicos
            if not dores:
                dores = ['Falta de resultados consistentes', 'Pressão por crescimento']
            if not desejos:
                desejos = ['Alcançar estabilidade financeira', 'Reconhecimento profissional']

            prompt_analise = f"""
            ANÁLISE DE ESTADO MENTAL PRÉ-PITCH

            Avatar: {avatar_data.get('nome', 'Não informado')}
            Perfil: {json.dumps(avatar_data, ensure_ascii=False, indent=2)}

            MISSÃO: Analisar o estado mental ATUAL do avatar antes de qualquer intervenção de pré-pitch.

            Identifique com precisão cirúrgica:

            1. NÍVEL DE CONSCIÊNCIA DO PROBLEMA
            - Sabe que tem o problema? (0-10)
            - Entende a gravidade? (0-10)
            - Sente urgência para resolver? (0-10)
            - Já tentou soluções? (sim/não + quais)

            2. RESISTÊNCIAS MENTAIS ATIVAS
            - Ceticismo em relação a soluções (0-10)
            - Experiências negativas anteriores
            - Crenças limitantes ativas
            - Mecanismos de autodefesa

            3. RECEPTIVIDADE ATUAL
            - Abertura para novas informações (0-10)
            - Disposição para investir (0-10)
            - Confiança em sua capacidade (0-10)
            - Energia para mudanças (0-10)

            4. PONTOS DE ALAVANCAGEM
            - Dores mais sensíveis no momento
            - Desejos mais intensos agora
            - Medos mais paralisantes
            - Esperanças mais motivadoras

            5. ESTADO EMOCIONAL DOMINANTE
            - Emoção predominante atual
            - Padrão emocional dos últimos 30 dias
            - Triggers emocionais mais sensíveis
            - Recursos emocionais disponíveis

            Seja um SCANNER MENTAL preciso e impiedoso.
            """

            response = ai_manager.generate_analysis(prompt_analise, max_tokens=2000)

            if response:
                # Verifica se estado_mental é um dicionário
                if isinstance(response, dict):
                    mental_state = response.get('response', {})
                    triggers = response.get('triggers_emocionais', [])
                else:
                    logger.warning("⚠️ AI response não é um dicionário válido")
                    mental_state = {}
                    triggers = []

                return {
                    'analise_completa': mental_state,
                    'nivel_preparacao': self._avaliar_nivel_preparacao(mental_state.get('response', '')), # Passa a string da resposta para avaliação
                    'resistencias_principais': self._extrair_resistencias(mental_state.get('response', '')),
                    'pontos_alavancagem': self._extrair_alavancagem(mental_state.get('response', '')),
                    'timestamp': datetime.now().isoformat()
                }
            else:
                return self._estado_mental_fallback(avatar_data)

        except Exception as e:
            logger.error(f"❌ Erro na análise de estado mental: {e}")
            return {
                'estado_dominante': 'neutro',
                'nivel_urgencia': 'medio',
                'pontos_dor_ativados': [],
                'desejos_mobilizados': []
            }

    def _get_default_avatar_data(self) -> Dict[str, Any]:
        """Retorna dados padrão do avatar"""
        return {
            'dores_viscerais': [
                'Falta de crescimento consistente',
                'Pressão da concorrência',
                'Dificuldades operacionais'
            ],
            'desejos_secretos': [
                'Dominar o mercado',
                'Reconhecimento como líder',
                'Crescimento sustentável'
            ],
            'perfil_demografico': {
                'idade': '35-50',
                'localizacao': 'Brasil',
                'segmento': 'Empresarial'
            }
        }

    def _designar_jornada_preparacao(self, avatar_data: Dict, estado_mental: Dict, drivers_mentais: Dict) -> Dict[str, Any]:
        """Designa jornada personalizada de preparação mental"""

        prompt_jornada = f"""
        DESIGN DE JORNADA DE PREPARAÇÃO MENTAL

        DADOS DE ENTRADA:
        Avatar: {json.dumps(avatar_data, ensure_ascii=False, indent=2)}
        Estado Mental: {estado_mental}
        Drivers Disponíveis: {json.dumps(drivers_mentais.get('drivers_personalizados', [])[:3], ensure_ascii=False, indent=2)}

        MISSÃO: Criar uma JORNADA CIRÚRGICA que leve o avatar do estado atual até a receptividade total para o pitch.

        Para cada fase da jornada:

        1. FASE DE DESPERTAR (Dias -21 a -14)
        - Objetivo específico da fase
        - Estado mental desejado ao final
        - Intervenções necessárias
        - Conteúdos/mensagens específicas
        - Métricas de sucesso da fase

        2. FASE DE DESENVOLVIMENTO (Dias -14 a -7)
        - Objetivo específico da fase
        - Aprofundamento da consciência
        - Construção de confiança
        - Eliminação de resistências
        - Intensificação emocional

        3. FASE DE PREPARAÇÃO FINAL (Dias -7 a -1)
        - Estado de máxima receptividade
        - Ancoragens finais
        - Eliminação de última resistência
        - Preparação psicológica direta
        - Alinhamento com oferta

        4. SEQUÊNCIAS DE TRANSIÇÃO
        - Como mover de uma fase para outra
        - Sinais de que está pronto para avançar
        - Ajustes se não estiver progredindo
        - Aceleração se progredir rapidamente

        Crie uma jornada que seja INEVITÁVEL mas INVISÍVEL.
        O avatar deve SENTIR que chegou às conclusões sozinho.
        """

        try:
            response = ai_manager.generate_analysis(prompt_jornada, max_tokens=2000)

            if response:
                return {
                    'jornada_completa': response,
                    'fases_estruturadas': self._estruturar_fases(response),
                    'duracao_total': '21 dias',
                    'pontos_controle': self._definir_pontos_controle(response),
                    'timestamp': datetime.now().isoformat()
                }
            else:
                return self._jornada_preparacao_fallback()

        except Exception as e:
            logger.error(f"Erro no design da jornada: {e}")
            return self._jornada_preparacao_fallback()

    def _construir_sequencias_invisiveis(self, jornada: Dict, oferta_data: Dict) -> Dict[str, Any]:
        """Constrói sequências invisíveis de preparação"""

        return {
            'sequencia_despertar': self._criar_sequencia_despertar(jornada),
            'sequencia_desenvolvimento': self._criar_sequencia_desenvolvimento(jornada),
            'sequencia_preparacao_final': self._criar_sequencia_preparacao_final(jornada, oferta_data),
            'elementos_invisibilidade': self._definir_elementos_invisibilidade(),
            'pontos_ancoragem': self._mapear_pontos_ancoragem(),
            'mecanismos_feedback': self._criar_mecanismos_feedback()
        }

    def _gerar_scripts_implementacao(self, sequencias: Dict, avatar_data: Dict) -> Dict[str, Any]:
        """Gera scripts práticos de implementação"""

        scripts = {}

        for fase, sequencia in sequencias.items():
            if isinstance(sequencia, dict) and 'elementos' in sequencia:
                scripts[fase] = {
                    'emails_sequencia': self._gerar_emails_sequencia(sequencia, avatar_data),
                    'posts_sociais': self._gerar_posts_sociais(sequencia),
                    'conteudos_educativos': self._gerar_conteudos_educativos(sequencia),
                    'interacoes_diretas': self._gerar_interacoes_diretas(sequencia),
                    'elementos_visuais': self._sugerir_elementos_visuais_fase(sequencia)
                }

        return scripts

    def _criar_sistema_mensuracao(self, sequencias: Dict) -> Dict[str, Any]:
        """Cria sistema de mensuração da eficácia"""

        return {
            'metricas_comportamentais': {
                'taxa_abertura_emails': 'Engajamento crescente esperado',
                'tempo_permanencia_conteudo': 'Aumento gradual',
                'interacoes_sociais': 'Qualidade das respostas',
                'compartilhamentos': 'Indicador de ressonância'
            },
            'metricas_psicologicas': {
                'nivel_consciencia_problema': 'Escala 1-10 mensal',
                'intensidade_desejo_solucao': 'Tracking de linguagem',
                'confianca_na_fonte': 'Questionários indiretos',
                'receptividade_oferta': 'Simulações de teste'
            },
            'indicadores_prontidao': {
                'linguagem_usado': 'Palavras-chave específicas',
                'perguntas_feitas': 'Nível de sofisticação',
                'urgencia_demonstrada': 'Frequência de contato',
                'resistencias_expressas': 'Diminuição progressiva'
            },
            'pontos_decisao': [
                'Quando acelerar sequência',
                'Quando repetir elementos',
                'Quando ajustar intensidade',
                'Quando fazer transição'
            ]
        }

    def _criar_plano_temporal(self, sequencias: Dict) -> Dict[str, Any]:
        """Cria plano temporal detalhado"""

        return {
            'cronograma_21_dias': self._gerar_cronograma_detalhado(),
            'alternativas_tempo': {
                'acelerada_14_dias': 'Para avatares mais receptivos',
                'extensiva_30_dias': 'Para avatares mais resistentes',
                'intensiva_7_dias': 'Para oportunidades urgentes'
            },
            'pontos_flexibilidade': [
                'Ajuste baseado em resposta',
                'Personalização por comportamento',
                'Adaptação a contexto externo'
            ],
            'automatizacao_possivel': {
                'emails': '80%',
                'posts_sociais': '60%',
                'interacoes_diretas': '30%',
                'conteudos_educativos': '70%'
            }
        }

    def _definir_elementos_ancoragem(self, sequencias: Dict) -> Dict[str, Any]:
        """Define elementos de ancoragem profunda"""

        return {
            'ancoras_verbais': [
                'Frases-chave repetidas',
                'Conceitos únicos introduzidos',
                'Metáforas específicas utilizadas',
                'Linguagem emocional particular'
            ],
            'ancoras_visuais': [
                'Elementos gráficos consistentes',
                'Cores psicologicamente escolhidas',
                'Símbolos de identificação',
                'Padrões visuais reconhecíveis'
            ],
            'ancoras_experienciais': [
                'Sentimentos induzidos específicos',
                'Estados emocionais ativados',
                'Memórias positivas criadas',
                'Associações mentais fortalecidas'
            ],
            'ancoras_comportamentais': [
                'Ações pequenas solicitadas',
                'Microcomprometimentos obtidos',
                'Hábitos mentais instalados',
                'Padrões de resposta condicionados'
            ]
        }

    def _criar_sequencias_neurociencia(self, avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria sequências baseadas em neurociência"""
        return {
            'dopamine_loops': ['Curiosidade -> Revelação -> Satisfação -> Nova Curiosidade'],
            'mirror_neurons': ['Histórias de transformação pessoal'],
            'cognitive_ease': ['Simplicidade progressiva de conceitos'],
            'loss_aversion': ['Enfase no que pode ser perdido']
        }

    def _criar_triggers_subconscientes(self, drivers_mentais: Dict[str, Any]) -> List[str]:
        """Cria triggers subconscientes"""
        return [
            'Padrões de repetição específicos',
            'Ancoragens temporais estratégicas',
            'Comandos embutidos sutis',
            'Pressuposições linguísticas'
        ]

    def _criar_scripts_automacao(self, base_pre_pitch: Dict[str, Any]) -> Dict[str, Any]:
        """Cria scripts de automação"""
        return {
            'email_sequences': ['Sequência 7 dias', 'Sequência 14 dias', 'Sequência 21 dias'],
            'social_media_posts': ['Posts educativos', 'Posts de autoridade', 'Posts de prova social'],
            'content_calendar': ['Cronograma otimizado de conteúdo']
        }

    def _criar_matriz_personalizacao(self, avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria matriz de personalização"""
        return {
            'personality_type': avatar_data.get('perfil_psicografico', {}).get('personalidade', ''),
            'communication_style': 'Adaptado ao perfil',
            'emotional_triggers': avatar_data.get('dores_viscerais', [])[:3],
            'motivational_drivers': avatar_data.get('desejos_secretos', [])[:3]
        }

    def _criar_boosters_conversao(self, oferta_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria boosters de conversão"""
        return {
            'urgency_escalation': ['Suave -> Moderada -> Intensa'],
            'value_stacking': ['Benefício principal + Bônus + Garantias'],
            'risk_reversal': ['Garantias progressivamente mais fortes'],
            'social_proof_sequence': ['Números -> Casos -> Autoridades']
        }

    def _pre_pitch_fallback(self, avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Fallback para pré-pitch"""
        return {
            'sequencia_basica': ['Consciência -> Interesse -> Desejo -> Ação'],
            'timeline': '14 dias',
            'elementos_minimos': ['Educação', 'Autoridade', 'Prova Social', 'Urgência']
        }


    def _calcular_metricas_esperadas(self, sequencias: Dict) -> Dict[str, Any]:
        """Calcula métricas esperadas do pré-pitch"""

        return {
            'taxa_conversao_final': {
                'sem_pre_pitch': '12-18%',
                'com_pre_pitch': '35-55%',
                'melhoria_esperada': '200-300%'
            },
            'tempo_ciclo_venda': {
                'sem_pre_pitch': '45-90 dias',
                'com_pre_pitch': '21-35 dias',
                'reducao_esperada': '40-60%'
            },
            'qualidade_leads': {
                'pre_qualificacao': '85-95%',
                'adequacao_oferta': '90-98%',
                'capacidade_investimento': '75-85%'
            },
            'resistencia_preco': {
                'objecoes_preco': 'Redução de 70%',
                'negociacao_necessaria': 'Redução de 60%',
                'aceitacao_valor': 'Aumento de 180%'
            }
        }

    # Métodos auxiliares e de fallback

    def _gerar_cronograma_detalhado(self) -> Dict[str, List[str]]:
        """Gera cronograma detalhado de 21 dias"""
        cronograma = {}

        # Fase Despertar (Dias -21 a -14)
        for dia in range(-21, -14):
            cronograma[f'dia_{abs(dia)}'] = [
                'Conteúdo educativo relevante',
                'Insight sobre problema específico',
                'Caso de estudo relacionado'
            ]

        # Fase Desenvolvimento (Dias -14 a -7)
        for dia in range(-14, -7):
            cronograma[f'dia_{abs(dia)}'] = [
                'Aprofundamento do problema',
                'Construção de autoridade',
                'Prova social indireta'
            ]

        # Fase Preparação Final (Dias -7 a -1)
        for dia in range(-7, -1):
            cronograma[f'dia_{abs(dia)}'] = [
                'Intensificação emocional',
                'Preparação para solução',
                'Ancoragem final'
            ]

        return cronograma

    # Métodos de fallback

    def _estado_mental_fallback(self, avatar_data: Dict) -> Dict[str, Any]:
        """Fallback para estado mental"""
        return {
            'nivel_consciencia': 'Moderado',
            'resistencias': ['Ceticismo', 'Experiências passadas'],
            'receptividade': 'Média',
            'pontos_alavancagem': ['Dor financeira', 'Pressão temporal']
        }

    def _jornada_preparacao_fallback(self) -> Dict[str, Any]:
        """Fallback para jornada de preparação"""
        return {
            'fases': ['Despertar', 'Desenvolvimento', 'Preparação'],
            'duracao': '21 dias',
            'estrategia': 'Progressão gradual de consciência'
        }

    # Métodos auxiliares de estruturação

    def _avaliar_nivel_preparacao(self, analise: str) -> int:
        """Avalia nível de preparação baseado na análise"""
        # Lógica simplificada para determinar nível
        if 'alta consciência' in analise.lower():
            return 8
        elif 'consciência moderada' in analise.lower():
            return 5
        else:
            return 3

    def _extrair_resistencias(self, analise: str) -> List[str]:
        """Extrai resistências principais da análise"""
        return ['Ceticismo geral', 'Experiências negativas passadas', 'Falta de confiança']

    def _extrair_alavancagem(self, analise: str) -> List[str]:
        """Extrai pontos de alavancagem da análise"""
        return ['Dor financeira intensa', 'Pressão temporal', 'Desejo de reconhecimento']

    def _estruturar_fases(self, jornada: str) -> Dict:
        """Estrutura as fases da jornada"""
        return {
            'despertar': {'duracao': '7 dias', 'objetivo': 'Consciência do problema'},
            'desenvolvimento': {'duracao': '7 dias', 'objetivo': 'Construção de confiança'},
            'preparacao': {'duracao': '7 dias', 'objetivo': 'Receptividade máxima'}
        }

    def _definir_pontos_controle(self, jornada: str) -> List[str]:
        """Define pontos de controle da jornada"""
        return [
            'Fim da fase despertar',
            'Meio da fase desenvolvimento',
            'Início da preparação final',
            'Véspera do pitch'
        ]

    def _criar_sequencia_despertar(self, jornada: Dict) -> Dict:
        """Cria sequência de despertar"""
        return {
            'objetivo': 'Despertar consciência do problema',
            'elementos': ['Educação', 'Insights', 'Cases'],
            'intensidade': 'Baixa a moderada'
        }

    def _criar_sequencia_desenvolvimento(self, jornada: Dict) -> Dict:
        """Cria sequência de desenvolvimento"""
        return {
            'objetivo': 'Desenvolver confiança e urgência',
            'elementos': ['Autoridade', 'Prova social', 'Urgência'],
            'intensidade': 'Moderada a alta'
        }

    def _criar_sequencia_preparacao_final(self, jornada: Dict, oferta_data: Dict) -> Dict:
        """Cria sequência de preparação final"""
        return {
            'objetivo': 'Preparação direta para pitch',
            'elementos': ['Ancoragem', 'Reciprocidade', 'Compromisso'],
            'intensidade': 'Alta'
        }

    def _definir_elementos_invisibilidade(self) -> List[str]:
        """Define elementos que tornam a preparação invisível"""
        return [
            'Educação disfarçada de valor',
            'Venda indireta através de casos',
            'Autoridade construída naturalmente',
            'Urgência criada por contexto'
        ]

    def _mapear_pontos_ancoragem(self) -> List[str]:
        """Mapeia pontos de ancoragem"""
        return [
            'Primeira impressão positiva',
            'Momento de insight',
            'Experiência emocional intensa',
            'Comprometimento pequeno'
        ]

    def _criar_mecanismos_feedback(self) -> Dict:
        """Cria mecanismos de feedback"""
        return {
            'direto': ['Respostas a emails', 'Comentários'],
            'indireto': ['Tempo de leitura', 'Compartilhamentos'],
            'comportamental': ['Padrões de acesso', 'Sequência de ações']
        }

    def _gerar_emails_sequencia(self, sequencia: Dict, avatar_data: Dict) -> List[str]:
        """Gera emails da sequência"""
        return [
            f"Email 1: Introdução ao conceito para {avatar_data.get('nome', 'avatar')}",
            "Email 2: Aprofundamento com case study",
            "Email 3: Conexão emocional e urgência"
        ]

    def _gerar_posts_sociais(self, sequencia: Dict) -> List[str]:
        """Gera posts sociais"""
        return [
            "Post educativo sobre o problema",
            "Insight exclusivo do mercado",
            "Case de transformação"
        ]

    def _gerar_conteudos_educativos(self, sequencia: Dict) -> List[str]:
        """Gera conteúdos educativos"""
        return [
            "Artigo sobre tendências",
            "Vídeo explicativo",
            "Infográfico comparativo"
        ]

    def _gerar_interacoes_diretas(self, sequencia: Dict) -> List[str]:
        """Gera interações diretas"""
        return [
            "Pergunta provocativa",
            "Convite para reflexão",
            "Solicitação de opinião"
        ]

    def _sugerir_elementos_visuais_fase(self, sequencia: Dict) -> List[str]:
        """Sugere elementos visuais para a fase"""
        return [
            "Gráficos de tendência",
            "Comparações visuais",
            "Timeline de evolução"
        ]

    # Novos métodos para generate_advanced_pre_pitch

    def _generate_section_content(self, secao: str, config: Dict[str, Any], avatar_data: Dict[str, Any], context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Gera conteudo especifico para uma secao"""
        segmento = context_data.get('segmento', 'mercado')
        produto = context_data.get('produto', 'produto')

        prompt_templates = {
            'abertura_impacto': f"""
            Crie uma abertura impactante para um pre-pitch sobre {produto} no segmento {segmento}.
            Deve incluir: hook emocional, estatistica impactante, conexao imediata.
            Duracao: {config['duracao']}
            """,
            'identificacao_dor': f"""
            Desenvolva sequencia para amplificar a dor do avatar em {segmento}.
            Deve incluir: espelhamento da situacao, agitacao controlada, validacao emocional.
            Produto: {produto}
            """,
            'construcao_desejo': f"""
            Crie narrativa para construir desejo irresistivel por {produto}.
            Deve incluir: visao do futuro ideal, contraste antes/depois, prova social.
            Segmento: {segmento}
            """,
            'preparacao_logica': f"""
            Crie a secao de preparacao logica para um pre-pitch de {produto} no segmento {segmento}.
            Deve incluir: dados cientificos, autoridade, logica implacavel.
            Duracao: {config['duracao']}
            """,
            'transicao_oferta': f"""
            Crie a transicao final para o pitch de {produto} no segmento {segmento}.
            Deve incluir: revelacao gradual, curiosidade, inevitabilidade.
            Duracao: {config['duracao']}
            """
        }

        # Usa IA para gerar conteudo se disponivel
        if hasattr(self, 'ai_manager') and self.ai_manager:
            try:
                prompt = prompt_templates.get(secao, f"Gere conteudo para {secao} sobre {produto}")
                # Assume que ai_manager tem um método generate_content
                response = ai_manager.generate_content(prompt, max_tokens=800)

                if response and len(response) > 100:
                    return {
                        'ai_generated': True,
                        'content': response,
                        'tecnicas': config['tecnicas'],
                        'duracao': config['duracao'],
                        'objetivo': config['objetivo']
                    }
            except Exception as e:
                logger.warning(f"⚠️ IA falhou para {secao}: {e}")

        # Fallback para conteudo basico
        return self._create_fallback_section(secao, config, segmento, produto)

    def _create_fallback_section(self, secao: str, config: Dict[str, Any], segmento: str, produto: str) -> Dict[str, Any]:
        """Cria secao de fallback"""
        conteudo_fallback = {
            'abertura_impacto': f"Profissionais de {segmento} estao perdendo oportunidades diariamente por nao conhecerem {produto}. Estatisticas mostram que 78% poderia dobrar resultados.",
            'identificacao_dor': f"Se voce trabalha com {segmento}, ja deve ter sentido a frustacao de nao conseguir os resultados esperados. Essa dor e real e precisa ser resolvida.",
            'construcao_desejo': f"Imagine dominar completamente {segmento} com {produto}. Seus resultados se multiplicam, sua confianca aumenta, seu futuro se transforma.",
            'preparacao_logica': f"Dados comprovam que {produto} e a solucao mais eficaz para {segmento}. Pesquisas indicam 300% de melhoria nos resultados.",
            'transicao_oferta': f"E exatamente por isso que desenvolvemos {produto} especificamente para profissionais de {segmento}..."
        }

        return {
            'ai_generated': False,
            'content': conteudo_fallback.get(secao, f"Conteudo para {secao}"),
            'tecnicas': config['tecnicas'],
            'duracao': config['duracao'],
            'objetivo': config['objetivo']
        }

    def _create_psychological_sequence(self, conteudo: Dict[str, Any], avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria sequencia psicologica otimizada"""
        return {
            'ordem_execucao': list(conteudo.keys()),
            'transicoes': {
                'abertura_para_dor': 'E por isso que preciso compartilhar algo importante...',
                'dor_para_desejo': 'Mas e se eu te dissesse que existe uma maneira de mudar isso?',
                'desejo_para_logica': 'E nao e apenas um sonho, os dados comprovam...',
                'logica_para_oferta': 'E exatamente por isso que...'
            },
            'gatilhos_emocionais': ['urgencia', 'escassez', 'medo_perda', 'desejo_ganho'],
            'pontos_ancoragem': [
                'Momento de maxima dor (minuto 7)',
                'Pico de desejo (minuto 15)',
                'Validacao logica (minuto 18)',
                'Curiosidade maxima (minuto 20)'
            ]
        }

    def _validate_advanced_pre_pitch_quality(self, conteudo: Dict[str, Any], context_data: Dict[str, Any]) -> bool:
        """Valida qualidade avancada do pre-pitch"""
        if not conteudo:
            return False

        # Verifica se todas as secoes esperadas estao presentes
        secoes_esperadas = ['abertura_impacto', 'identificacao_dor', 'construcao_desejo', 'preparacao_logica', 'transicao_oferta']
        if not all(secao in conteudo for secao in secoes_esperadas):
            logger.warning("Nem todas as secoes esperadas estao presentes no conteudo.")
            return False

        # Verifica se o conteudo gerado tem tamanho razoavel
        total_content_length = sum(len(str(section.get('content', ''))) for section in conteudo.values())
        if total_content_length < 500: # Limiar minimo de caracteres
            logger.warning(f"Conteudo total do pre-pitch muito curto ({total_content_length} caracteres).")
            return False

        # Verifica se ha uma boa mistura de conteudo gerado por IA
        ai_generated_count = sum(1 for section in conteudo.values() if section.get('ai_generated', False))
        if ai_generated_count < 2: # Minimo de 2 secoes geradas por IA
            logger.warning(f"Poucas secoes geradas por IA ({ai_generated_count}).")
            return False

        return True

    def _enhance_pre_pitch_content(self, conteudo: Dict[str, Any], avatar_data: Dict[str, Any], context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Melhora o conteudo do pre-pitch se a qualidade for baixa"""
        logger.info("Melhorando conteudo do pre-pitch...")

        # Exemplo: Se a secao de dor for fraca, tenta regenera-la com um prompt mais forte
        if 'identificacao_dor' in conteudo and not conteudo['identificacao_dor'].get('ai_generated', False):
             logger.info("Regenerando secao de identificacao_dor...")
             config = {'duracao': '5-7 minutos', 'objetivo': 'Amplificar consciencia da dor', 'tecnicas': ['espelhamento', 'agitacao_controlada', 'validacao_emocional']}
             conteudo['identificacao_dor'] = self._generate_section_content('identificacao_dor', config, avatar_data, context_data)

        # Exemplo: Adicionar mais detalhes de prova social se a secao de desejo for fraca
        if 'construcao_desejo' in conteudo and 'prova_social' in conteudo['construcao_desejo'].get('tecnicas', []) and not conteudo['construcao_desejo'].get('ai_generated', False):
            logger.info("Adicionando mais detalhes de prova social na secao de desejo...")
            # Poderia tentar re-gerar com foco em mais exemplos ou citações
            pass # Implementacao mais complexa aqui

        return conteudo

    def _calculate_total_duration(self, pre_pitch_structure: Dict[str, Any]) -> str:
        """Calcula a duracao total estimada do pre-pitch"""
        total_minutes = 0
        for section, config in pre_pitch_structure.items():
            duracao_str = config.get('duracao', '0 minutos')
            try:
                # Extrai os minutos da string (ex: "2-3 minutos" -> 2 ou 3)
                parts = duracao_str.split('-')
                if len(parts) == 2:
                    minutes = int(parts[0].split()[0])
                    total_minutes += minutes
                elif len(parts) == 1:
                    minutes = int(duracao_str.split()[0])
                    total_minutes += minutes
            except:
                pass # Ignora se o formato for inesperado
        return f"Aproximadamente {total_minutes} minutos"

    def _count_psychological_triggers(self, conteudo: Dict[str, Any]) -> int:
        """Conta o numero de gatilhos psicologicos presentes no conteudo"""
        count = 0
        triggers_keywords = ['dor', 'medo', 'desejo', 'urgencia', 'escassez', 'curiosidade', 'ganho', 'perda', 'confianca', 'autoridade']
        for section in conteudo.values():
            text = str(section.get('content', '')).lower()
            for trigger in triggers_keywords:
                if trigger in text:
                    count += 1
        return count


    def _create_emergency_pre_pitch(self, avatar_data: Dict[str, Any], context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Pre-pitch de emergencia em caso de falha critica"""
        segmento = context_data.get('segmento', 'mercado') if context_data else 'mercado'
        produto = context_data.get('produto', 'produto') if context_data else 'produto'

        return {
            'success': False,
            'emergency_pre_pitch': True,
            'error_message': "Falha critica ao gerar pre-pitch avancado. Utilizando fallback de emergencia.",
            'conteudo': {
                'abertura_emergencia': {
                    'content': f"Olá! Somos a equipe por trás de {produto}. Entendemos os desafios do mercado de {segmento}.",
                    'duracao': '1 minuto',
                    'objetivo': 'Estabelecer contato inicial'
                },
                'desenvolvimento_emergencia': {
                    'content': f"Nossa missão é ajudar profissionais como você a superar as dificuldades atuais e alcançar resultados extraordinários. {produto} foi desenhado para isso.",
                    'duracao': '3 minutos',
                    'objetivo': 'Apresentar solução de forma genérica'
                },
                'fechamento_emergencia': {
                    'content': "Estamos à disposição para conversar sobre como podemos te ajudar. Entre em contato.",
                    'duracao': '30 segundos',
                    'objetivo': 'Direcionar para próximo passo'
                }
            },
            'duracao_total': '4.5 minutos'
        }

    # Métodos que eram chamados incorretamente e precisam ser adaptados ou removidos
    # def _validate_pre_pitch_quality(self, pre_pitch: Dict[str, Any], context_data: Dict[str, Any]) -> bool:
    #     """Valida a qualidade geral do pre-pitch. (Este método pode precisar ser reescrito ou adaptado)"""
    #     # Implementação genérica de validação, pode ser substituída por lógica mais específica
    #     if not pre_pitch or not isinstance(pre_pitch, dict):
    #         return False
    #     # Exemplo: verificar se o 'conteudo' existe e não está vazio
    #     return 'conteudo' in pre_pitch and bool(pre_pitch['conteudo'])

    def _extract_mental_state_data(self, avatar_data):
        """Extrai dados de estado mental do avatar"""
        try:
            # Se for string, converte para dict
            if isinstance(avatar_data, str):
                try:
                    avatar_data = json.loads(avatar_data)
                except json.JSONDecodeError:
                    logger.warning("❌ Falha ao fazer parse JSON do avatar_data")
                    avatar_data = {}

            # Garante que avatar_data é um dict
            if not isinstance(avatar_data, dict):
                avatar_data = {}

            # Acessa os dados com verificações seguras
            estado_mental = avatar_data.get('estado_mental_atual', {})

            # Se estado_mental é string, tenta converter
            if isinstance(estado_mental, str):
                try:
                    estado_mental = json.loads(estado_mental)
                except json.JSONDecodeError:
                    logger.warning("Falha ao fazer parse do estado mental, usando padrão")
                    estado_mental = {
                        'estado_dominante': 'neutro',
                        'nivel_urgencia': 'medio',
                        'pontos_dor_ativados': [],
                        'desejos_mobilizados': []
                    }

            # Se ainda não é dict, usa dict vazio com valores padrão
            if not isinstance(estado_mental, dict):
                estado_mental = {
                    'estado_dominante': 'neutro',
                    'nivel_urgencia': 'medio',
                    'pontos_dor_ativados': [],
                    'desejos_mobilizados': []
                }

            return {
                'estado_dominante': estado_mental.get('estado_dominante', 'neutro'),
                'nivel_urgencia': estado_mental.get('nivel_urgencia', 'medio'),
                'pontos_dor_ativados': estado_mental.get('pontos_dor_ativados', []),
                'desejos_mobilizados': estado_mental.get('desejos_mobilizados', [])
            }

        except Exception as e:
            logger.error(f"❌ Erro na extração de estado mental: {e}")
            return {
                'estado_dominante': 'neutro',
                'nivel_urgencia': 'medio',
                'pontos_dor_ativados': [],
                'desejos_mobilizados': []
            }


# Instância global
pre_pitch_architect = PrePitchArchitect()