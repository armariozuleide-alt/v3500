
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Pitch Master Architect
Sistema completo de pitch devastador com conversão 30-50%
Baseado no protocolo AR completo do anexo
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
import json
import re

logger = logging.getLogger(__name__)

class PitchMasterArchitect:
    """Arquiteto Master de Pitch - Sistema Completo de Alta Conversão"""
    
    def __init__(self):
        """Inicializa o arquiteto de pitch"""
        self.drives_mentais = self._load_drives_mentais()
        self.estruturas_pitch = self._load_estruturas_pitch()
        self.scripts_devastadores = self._load_scripts_devastadores()
        logger.info("🎯 Pitch Master Architect inicializado")
    
    def _load_drives_mentais(self) -> Dict[str, Any]:
        """Carrega os 17 drives mentais disponíveis"""
        return {
            "oportunidade_oculta": {
                "instalacao": "Existe algo acontecendo que 97% não perceberam...",
                "ativacao": "Lembra quando falei sobre [oportunidade]? É AGORA ou NUNCA.",
                "quando_usar": "Avatar não percebe mudança no mercado",
                "intensidade": 8.5
            },
            "ambicao_expandida": {
                "instalacao": "Você está pensando muito pequeno...",
                "ativacao": "Quem aqui ainda está se contentando com migalhas?",
                "quando_usar": "Avatar tem metas medíocres",
                "intensidade": 9.0
            },
            "diagnostico_brutal": {
                "instalacao": "A verdade dói, mas liberta...",
                "ativacao": "Vamos encarar: você está onde está por falta de [recurso]",
                "quando_usar": "Avatar em negação sobre situação",
                "intensidade": 9.5
            },
            "indignacao_produtiva": {
                "instalacao": "Isso deveria te revoltar...",
                "ativacao": "Você vai aceitar isso? SÉRIO MESMO?",
                "quando_usar": "Avatar conformado com mediocridade",
                "intensidade": 8.8
            },
            "ambiente_propulsor": {
                "instalacao": "Você é a média das 5 pessoas...",
                "ativacao": "Onde estão suas águias?",
                "quando_usar": "Avatar cercado de negatividade",
                "intensidade": 7.5
            },
            "metodo_vs_sorte": {
                "instalacao": "Tentar sem método é como...",
                "ativacao": "Quer continuar no mato ou pegar a estrada?",
                "quando_usar": "Avatar tentando sozinho sem sistema",
                "intensidade": 8.0
            },
            "mentor_extrator": {
                "instalacao": "Todo campeão teve um treinador...",
                "ativacao": "Quem está extraindo seu melhor?",
                "quando_usar": "Avatar orgulhoso/independente demais",
                "intensidade": 8.7
            },
            "coragem_prioritaria": {
                "instalacao": "Dinheiro não é problema, é prioridade...",
                "ativacao": "Você tem medo de quê?",
                "quando_usar": "Objeção principal é dinheiro",
                "intensidade": 9.2
            },
            "decisao_vs_condicao": {
                "instalacao": "Existem dois tipos de pessoas...",
                "ativacao": "Você vive de decisão ou desculpa?",
                "quando_usar": "Avatar cheio de desculpas",
                "intensidade": 8.9
            },
            "antecipacao_massiva": {
                "instalacao": "Tem algo especial vindo...",
                "ativacao": "Lembram do grupo seleto?",
                "quando_usar": "Criar curiosidade sobre oferta",
                "intensidade": 7.8
            },
            "trofeu_intimo": {
                "instalacao": "No fundo, o que você quer é...",
                "ativacao": "Imagine o rosto do seu filho quando...",
                "quando_usar": "Conectar com desejo emocional",
                "intensidade": 9.8
            },
            "comprometimento_publico": {
                "instalacao": "Quem está comprometido...",
                "ativacao": "Digite EU VOU se está pronto",
                "quando_usar": "Aumentar taxa de conversão",
                "intensidade": 8.3
            },
            "vilao_comum": {
                "instalacao": "Existe um inimigo comum...",
                "ativacao": "Sabe quem não quer seu sucesso?",
                "quando_usar": "Unir audiência contra algo",
                "intensidade": 8.6
            },
            "prova_viva": {
                "instalacao": "Pessoas como você conseguiram...",
                "ativacao": "[Nome], levante e conte",
                "quando_usar": "Quebrar ceticismo",
                "intensidade": 9.3
            },
            "deadline_mental": {
                "instalacao": "O tempo não espera...",
                "ativacao": "Daqui 1 ano você estará onde?",
                "quando_usar": "Avatar procrastinador",
                "intensidade": 8.4
            },
            "exclusividade_tribal": {
                "instalacao": "Nem todos estão prontos...",
                "ativacao": "Isso não é para a massa",
                "quando_usar": "Criar senso de elite",
                "intensidade": 8.1
            },
            "catarse_emocional": {
                "instalacao": "Existe um momento...",
                "ativacao": "[Vídeo/História emocionante]",
                "quando_usar": "Quebrar resistência lógica",
                "intensidade": 9.9
            }
        }
    
    def _load_estruturas_pitch(self) -> Dict[str, Any]:
        """Carrega as estruturas de pitch disponíveis"""
        return {
            "classico_expandido": {
                "nome": "Pitch Clássico Expandido",
                "duracao": "60-90 min",
                "conversao_esperada": "35-50%",
                "fases": {
                    "pre_pitch": {"duracao": "20-30 min", "objetivo": "Preparação psicológica"},
                    "transicao": {"duracao": "5 min", "objetivo": "Ponte emocional"},
                    "pitch_core": {"duracao": "30-40 min", "objetivo": "Apresentação da oferta"},
                    "close_multiplo": {"duracao": "10-15 min", "objetivo": "Pressão de fechamento"},
                    "qa_estrategico": {"duracao": "10-15 min", "objetivo": "Destruição final de objeções"}
                },
                "melhor_para": "Audiência morna/quente, produto complexo, ticket alto"
            },
            "comprimido_urgente": {
                "nome": "Pitch Comprimido Urgente",
                "duracao": "45-60 min",
                "conversao_esperada": "30-45%",
                "fases": {
                    "pre_pitch_integrado": {"duracao": "15 min", "objetivo": "Drives + Urgência"},
                    "pitch_direto": {"duracao": "20-25 min", "objetivo": "Oferta sem enrolação"},
                    "close_agressivo": {"duracao": "10-15 min", "objetivo": "Decisão imediata"},
                    "bonus_drop": {"duracao": "5 min", "objetivo": "Última cartada"}
                },
                "melhor_para": "Audiência quente, tempo limitado, decisão rápida"
            },
            "epico_imersivo": {
                "nome": "Pitch Épico Imersivo",
                "duracao": "90-120 min",
                "conversao_esperada": "40-60%",
                "fases": {
                    "pre_pitch_cinematografico": {"duracao": "30-40 min", "objetivo": "Experiência total"},
                    "pitch_demonstrativo": {"duracao": "40-50 min", "objetivo": "Prova absoluta"},
                    "close_consultivo": {"duracao": "15-20 min", "objetivo": "Personalização"},
                    "ultima_chance": {"duracao": "5-10 min", "objetivo": "Escassez real"}
                },
                "melhor_para": "Evento premium, audiência fria/morna, transformação profunda"
            }
        }
    
    def _load_scripts_devastadores(self) -> Dict[str, Any]:
        """Carrega scripts matadores para momentos-chave"""
        return {
            "quebra_objecao_dinheiro": """
'Não tenho dinheiro' é a desculpa mais COVARDE que existe.
Você tem dinheiro para [item 1], para [item 2], para [item 3].
Mas não tem para VOCÊ?
Não é falta de dinheiro. É falta de AMOR PRÓPRIO.
Quanto vale sua transformação? R$ 100? R$ 1.000?
Se não vale [investimento], você não vale nada para você mesmo.
            """,
            "quebra_objecao_tempo": """
24 horas. Todo mundo tem.
- 8 dormindo
- 8 trabalhando  
- 8 sobrando
Onde vão suas 8 horas?
2h Netflix + 2h Instagram + 2h reclamando = 6h DESPERDIÇADAS.
Não é falta de tempo. É falta de PRIORIDADE.
            """,
            "urgencia_mental": """
Calculadora. Agora. Sua idade x 365 = dias vividos.
27.375 (75 anos) - seus dias = dias restantes.
Cada dia procrastinando = dia roubado do futuro.
Quanto mais você vai deixar roubarem?
            """,
            "trofeu_intimo_ativacao": """
Fecha os olhos. É manhã de Natal.
Seu filho abre o presente. O que queria.
'Obrigado! Você é o melhor pai/mãe do mundo!'
Agora imagine o contrário.
'Por que Papai Noel não trouxe?'
Qual cena você escolhe viver?
            """,
            "momento_mentor_catarse": """
[LUZES BAIXAS - MÚSICA EMOCIONAL]
Um menino. Disseram que não conseguiria.
Fraco demais. Pobre demais.
Um homem viu o que outros não viam.
'Chora hoje. Vence amanhã.'
Esse menino era eu.
Esse homem, agora, sou eu para vocês.
Mas só ajudo quem QUER ser ajudado.
            """
        }
    
    def create_complete_pitch_system(
        self, 
        context_data: Dict[str, Any],
        avatar_data: Dict[str, Any],
        drivers_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Cria sistema completo de pitch personalizado"""
        
        logger.info("🎯 Criando sistema completo de pitch devastador...")
        
        try:
            # ETAPA 1: Arquitetura e estratégia
            arquitetura = self._create_pitch_architecture(context_data, avatar_data)
            
            # ETAPA 2: Pré-pitch invisível completo
            pre_pitch = self._create_pre_pitch_system(context_data, avatar_data, drivers_data)
            
            # ETAPA 3: Pitch de vendas masterclass
            pitch_vendas = self._create_sales_pitch(context_data, avatar_data, arquitetura)
            
            # Integração completa
            sistema_completo = {
                "tipo_sistema": "PITCH_DEVASTADOR_COMPLETO",
                "conversao_esperada": arquitetura.get("conversao_esperada", "35-50%"),
                "etapa_1_arquitetura": arquitetura,
                "etapa_2_pre_pitch": pre_pitch,
                "etapa_3_pitch_vendas": pitch_vendas,
                "cronograma_execucao": self._create_execution_timeline(arquitetura),
                "checklist_preparacao": self._create_preparation_checklist(),
                "metricas_monitoramento": self._create_monitoring_metrics(),
                "planos_contingencia": self._create_contingency_plans()
            }
            
            return sistema_completo
            
        except Exception as e:
            logger.error(f"❌ Erro ao criar sistema de pitch: {e}")
            return self._create_fallback_pitch_system(context_data)
    
    def _create_pitch_architecture(
        self, 
        context_data: Dict[str, Any], 
        avatar_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """ETAPA 1: Cria arquitetura estratégica do pitch"""
        
        segmento = context_data.get('segmento', 'Não especificado')
        produto = context_data.get('produto', 'Não especificado')
        publico = context_data.get('publico', 'Não especificado')
        
        # Análise estratégica do contexto
        avatar_analysis = self._analyze_avatar_depth(avatar_data)
        product_analysis = self._analyze_product_complexity(context_data)
        moment_analysis = self._analyze_pitch_moment(context_data)
        
        # Seleção da estrutura ideal
        estrutura_ideal = self._select_optimal_structure(avatar_analysis, product_analysis, moment_analysis)
        
        # Definição de elementos críticos
        stack_valor = self._design_value_stack(context_data)
        garantias = self._design_guarantees(context_data)
        precificacao = self._design_pricing_model(context_data)
        
        # Mapeamento psicológico
        jornada_emocional = self._map_emotional_journey(estrutura_ideal)
        pontos_nao_retorno = self._identify_no_return_points()
        
        return {
            "analise_contexto": {
                "avatar_profundo": avatar_analysis,
                "produto_oferta": product_analysis,
                "momento_pitch": moment_analysis
            },
            "estrutura_escolhida": estrutura_ideal,
            "elementos_criticos": {
                "stack_valor": stack_valor,
                "garantias": garantias,
                "modelo_precificacao": precificacao
            },
            "mapeamento_psicologico": {
                "jornada_emocional": jornada_emocional,
                "pontos_nao_retorno": pontos_nao_retorno
            },
            "recursos_producao": self._define_production_resources(estrutura_ideal),
            "justificativa_escolhas": self._justify_architecture_choices(
                estrutura_ideal, avatar_analysis, product_analysis
            )
        }
    
    def _create_pre_pitch_system(
        self, 
        context_data: Dict[str, Any],
        avatar_data: Dict[str, Any], 
        drivers_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """ETAPA 2: Cria pré-pitch invisível completo"""
        
        # Análise inteligente dos drives
        drives_analysis = self._analyze_intelligent_drives(avatar_data, context_data)
        
        # Seleção dos 12 drives mais devastadores
        selected_drives = self._select_12_lethal_drives(drives_analysis, avatar_data)
        
        # Desenvolvimento do pré-pitch baseado na estrutura
        pre_pitch_script = self._develop_pre_pitch_script(selected_drives, context_data)
        
        # Scripts matadores para momentos-chave
        killer_scripts = self._create_killer_moment_scripts(avatar_data, context_data)
        
        return {
            "analise_drives": drives_analysis,
            "drives_selecionados": selected_drives,
            "script_completo": pre_pitch_script,
            "scripts_matadores": killer_scripts,
            "timing_detalhado": self._create_detailed_timing(pre_pitch_script),
            "elementos_visuais": self._define_visual_elements(pre_pitch_script),
            "elementos_sonoros": self._define_audio_elements(pre_pitch_script),
            "pontos_interacao": self._define_interaction_points(pre_pitch_script)
        }
    
    def _create_sales_pitch(
        self, 
        context_data: Dict[str, Any],
        avatar_data: Dict[str, Any], 
        arquitetura: Dict[str, Any]
    ) -> Dict[str, Any]:
        """ETAPA 3: Cria pitch de vendas masterclass"""
        
        estrutura = arquitetura.get("estrutura_escolhida", {})
        
        # Abertura pós pré-pitch
        abertura = self._create_post_pre_pitch_opening()
        
        # Apresentação da solução
        apresentacao_solucao = self._create_solution_presentation(context_data)
        
        # Stack de valor progressivo
        stack_progressivo = self._create_progressive_value_stack(context_data)
        
        # Precificação e ancoragem
        precificacao = self._create_pricing_anchoring(context_data)
        
        # Garantias múltiplas
        garantias = self._create_multiple_guarantees(context_data)
        
        # Escassez e urgência real
        escassez_urgencia = self._create_real_scarcity_urgency()
        
        # Close múltiplo progressivo
        close_multiplo = self._create_progressive_multiple_close()
        
        # Q&A estratégico + última cartada
        qa_ultima_cartada = self._create_strategic_qa_final_card()
        
        return {
            "abertura_pos_pre_pitch": abertura,
            "apresentacao_solucao": apresentacao_solucao,
            "stack_valor_progressivo": stack_progressivo,
            "precificacao_ancoragem": precificacao,
            "garantias_multiplas": garantias,
            "escassez_urgencia": escassez_urgencia,
            "close_multiplo_progressivo": close_multiplo,
            "qa_estrategico_ultima_cartada": qa_ultima_cartada,
            "elementos_finais": self._create_final_elements(),
            "script_palavra_por_palavra": self._create_word_by_word_script()
        }
    
    def _analyze_avatar_depth(self, avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analisa avatar em profundidade"""
        
        dores = avatar_data.get('dores_reais', [])
        medos = avatar_data.get('medos_secretos', [])
        desejos = avatar_data.get('desejos_profundos', [])
        objecoes = avatar_data.get('objecoes_reais', [])
        
        return {
            "nivel_consciencia": self._calculate_consciousness_level(dores, medos),
            "temperatura_emocional": self._calculate_emotional_temperature(avatar_data),
            "sofisticacao_problema": self._calculate_problem_sophistication(dores),
            "capacidade_investimento": self._calculate_investment_capacity(avatar_data),
            "resistencias_principais": self._identify_main_resistances(objecoes),
            "drivers_ativacao": self._identify_activation_drivers(desejos, medos)
        }
    
    def _analyze_product_complexity(self, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analisa complexidade do produto/oferta"""
        
        produto = context_data.get('produto', '')
        segmento = context_data.get('segmento', '')
        
        return {
            "complexidade_solucao": self._calculate_solution_complexity(produto),
            "ticket_medio_vs_mercado": self._analyze_ticket_vs_market(context_data),
            "diferencial_competitivo": self._identify_competitive_differential(produto),
            "velocidade_resultado": self._calculate_result_speed(produto),
            "nivel_suporte_necessario": self._calculate_support_level(produto)
        }
    
    def _analyze_pitch_moment(self, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analisa momento do pitch"""
        
        return {
            "horas_conteudo_anterior": context_data.get('horas_conteudo', 0),
            "estado_mental_esperado": self._predict_mental_state(context_data),
            "drives_ja_instalados": self._identify_pre_installed_drives(context_data),
            "energia_audiencia": self._predict_audience_energy(context_data),
            "nivel_trust_buildup": self._calculate_trust_level(context_data)
        }
    
    def _select_optimal_structure(
        self, 
        avatar_analysis: Dict[str, Any],
        product_analysis: Dict[str, Any], 
        moment_analysis: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Seleciona estrutura ótima baseada nas análises"""
        
        # Scoring para cada estrutura
        classico_score = 0
        comprimido_score = 0
        epico_score = 0
        
        # Fatores de decisão
        if avatar_analysis.get("temperatura_emocional", 0) < 5:
            epico_score += 3
            classico_score += 2
        elif avatar_analysis.get("temperatura_emocional", 0) > 7:
            comprimido_score += 3
            classico_score += 1
        
        if product_analysis.get("complexidade_solucao", 0) > 7:
            epico_score += 2
            classico_score += 3
        
        # Seleciona estrutura com maior score
        scores = {
            "classico_expandido": classico_score,
            "comprimido_urgente": comprimido_score,
            "epico_imersivo": epico_score
        }
        
        estrutura_escolhida = max(scores, key=scores.get)
        
        return {
            **self.estruturas_pitch[estrutura_escolhida],
            "score_analysis": scores,
            "fatores_decisao": self._explain_decision_factors(scores, avatar_analysis, product_analysis)
        }
    
    def _analyze_intelligent_drives(
        self, 
        avatar_data: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Análise inteligente dos drives baseada no avatar"""
        
        dores = avatar_data.get('dores_reais', [])
        medos = avatar_data.get('medos_secretos', [])
        desejos = avatar_data.get('desejos_profundos', [])
        objecoes = avatar_data.get('objecoes_reais', [])
        
        drives_analysis = {}
        
        for drive_name, drive_data in self.drives_mentais.items():
            relevancia = self._calculate_drive_relevance(
                drive_data, dores, medos, desejos, objecoes
            )
            
            drives_analysis[drive_name] = {
                **drive_data,
                "relevancia_avatar": relevancia,
                "justificativa": self._justify_drive_relevance(drive_data, avatar_data),
                "customizacao": self._customize_drive_for_avatar(drive_data, avatar_data)
            }
        
        return drives_analysis
    
    def _select_12_lethal_drives(
        self, 
        drives_analysis: Dict[str, Any], 
        avatar_data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Seleciona os 12 drives mais letais"""
        
        # Ordena drives por relevância e intensidade
        sorted_drives = sorted(
            drives_analysis.items(),
            key=lambda x: (x[1]['relevancia_avatar'] * x[1]['intensidade']),
            reverse=True
        )
        
        # Seleciona top 12
        selected_drives = []
        for i, (drive_name, drive_data) in enumerate(sorted_drives[:12]):
            selected_drives.append({
                "nome": drive_name,
                "posicao": i + 1,
                **drive_data,
                "script_customizado": self._create_custom_script(drive_data, avatar_data)
            })
        
        return selected_drives
    
    def _develop_pre_pitch_script(
        self, 
        selected_drives: List[Dict[str, Any]], 
        context_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Desenvolve script completo do pré-pitch"""
        
        segmento = context_data.get('segmento', '')
        
        # Script por fases
        script_fases = {
            "fase_emocional": self._create_emotional_phase_script(selected_drives, segmento),
            "fase_logica": self._create_logical_phase_script(context_data),
            "transicao_pitch": self._create_transition_script(selected_drives)
        }
        
        return {
            "duracao_total": "20-30 minutos",
            "script_por_fases": script_fases,
            "timing_detalhado": self._create_phase_timing(script_fases),
            "indicacoes_energia": self._create_energy_indicators(script_fases),
            "pontos_checklist": self._create_script_checkpoints(script_fases)
        }
    
    def _create_fallback_pitch_system(self, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Sistema de pitch básico como fallback"""
        
        return {
            "tipo_sistema": "PITCH_BASICO_FALLBACK",
            "conversao_esperada": "20-30%",
            "estrutura_simples": "Apresentação → Benefícios → Preço → Close",
            "drives_basicos": ["ambicao_expandida", "coragem_prioritaria", "decisao_vs_condicao"],
            "script_simples": f"Pitch básico para {context_data.get('segmento', 'produto')}",
            "melhorias_sugeridas": [
                "Implementar análise completa de avatar",
                "Desenvolver drives mentais customizados",
                "Criar sistema de garantias múltiplas",
                "Implementar escassez real"
            ]
        }
    
    # Métodos auxiliares simplificados para não estender demais
    def _calculate_consciousness_level(self, dores: List[str], medos: List[str]) -> int:
        """Calcula nível de consciência (1-10)"""
        if len(dores) > 5 and len(medos) > 3:
            return 8
        elif len(dores) > 3:
            return 6
        return 4
    
    def _calculate_emotional_temperature(self, avatar_data: Dict[str, Any]) -> int:
        """Calcula temperatura emocional (1-10)"""
        urgencia = len(avatar_data.get('medos_secretos', []))
        return min(10, max(1, urgencia + 3))
    
    def _calculate_solution_complexity(self, produto: str) -> int:
        """Calcula complexidade da solução (1-10)"""
        if "sistema" in produto.lower() or "método" in produto.lower():
            return 8
        elif "curso" in produto.lower():
            return 6
        return 4
    
    def _calculate_drive_relevance(
        self, 
        drive_data: Dict[str, Any], 
        dores: List[str], 
        medos: List[str], 
        desejos: List[str], 
        objecoes: List[str]
    ) -> float:
        """Calcula relevância do drive para o avatar"""
        
        base_relevance = 0.5
        
        # Aumenta relevância baseado em correspondências
        quando_usar = drive_data.get('quando_usar', '').lower()
        
        if 'dinheiro' in quando_usar and any('dinheiro' in obj.lower() for obj in objecoes):
            base_relevance += 0.3
        
        if 'tempo' in quando_usar and any('tempo' in obj.lower() for obj in objecoes):
            base_relevance += 0.3
            
        if 'medo' in quando_usar and len(medos) > 2:
            base_relevance += 0.2
        
        return min(1.0, base_relevance)
    
    def _justify_drive_relevance(self, drive_data: Dict[str, Any], avatar_data: Dict[str, Any]) -> str:
        """Justifica relevância do drive"""
        return f"Drive relevante pois avatar apresenta {drive_data.get('quando_usar', 'características compatíveis')}"
    
    def _customize_drive_for_avatar(self, drive_data: Dict[str, Any], avatar_data: Dict[str, Any]) -> str:
        """Customiza drive para o avatar específico"""
        return drive_data.get('instalacao', '').replace('[recurso]', 'sistema').replace('[oportunidade]', 'momento')
    
    def _create_custom_script(self, drive_data: Dict[str, Any], avatar_data: Dict[str, Any]) -> str:
        """Cria script customizado para o drive"""
        return f"{drive_data.get('instalacao', '')} → {drive_data.get('ativacao', '')}"

# Instância global
pitch_master_architect = PitchMasterArchitect()
