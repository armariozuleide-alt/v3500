
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Arquiteto do Pré-Pitch Invisível
Sistema baseado no anexo para criação de instalação psicológica profunda
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
import json

logger = logging.getLogger(__name__)

class InvisiblePrePitchArchitect:
    """Arquiteto do Pré-Pitch Invisível - Instalação Psicológica Profunda"""

    def __init__(self):
        """Inicializa o arquiteto do pré-pitch"""
        self.mental_drives = self._load_mental_drives_library()
        self.pitch_structures = self._load_pitch_structures()
        self.killer_scripts = self._load_killer_scripts()
        logger.info("🎯 Invisible Pre-Pitch Architect inicializado")

    def _load_mental_drives_library(self) -> Dict[str, Any]:
        """Carrega biblioteca completa dos 17 drives mentais"""
        return {
            "oportunidade_oculta": {
                "instalacao": "Existe algo acontecendo que 97% não perceberam...",
                "ativacao": "Lembra quando falei sobre [oportunidade]? É AGORA ou NUNCA.",
                "quando_usar": "Avatar não percebe mudança no mercado",
                "intensidade": 8,
                "categoria": "urgencia"
            },
            "ambicao_expandida": {
                "instalacao": "Você está pensando muito pequeno...",
                "ativacao": "Quem aqui ainda está se contentando com migalhas?",
                "quando_usar": "Avatar tem metas medíocres",
                "intensidade": 9,
                "categoria": "desejo"
            },
            "diagnostico_brutal": {
                "instalacao": "A verdade dói, mas liberta...",
                "ativacao": "Vamos encarar: você está onde está por falta de [recurso]",
                "quando_usar": "Avatar em negação sobre situação",
                "intensidade": 10,
                "categoria": "confronto"
            },
            "indignacao_produtiva": {
                "instalacao": "Isso deveria te revoltar...",
                "ativacao": "Você vai aceitar isso? SÉRIO MESMO?",
                "quando_usar": "Avatar conformado com mediocridade",
                "intensidade": 9,
                "categoria": "confronto"
            },
            "ambiente_propulsor": {
                "instalacao": "Você é a média das 5 pessoas...",
                "ativacao": "Onde estão suas águias?",
                "quando_usar": "Avatar cercado de negatividade",
                "intensidade": 7,
                "categoria": "social"
            },
            "metodo_vs_sorte": {
                "instalacao": "Tentar sem método é como...",
                "ativacao": "Quer continuar no mato ou pegar a estrada?",
                "quando_usar": "Avatar tentando sozinho sem sistema",
                "intensidade": 8,
                "categoria": "logica"
            },
            "mentor_extrator": {
                "instalacao": "Todo campeão teve um treinador...",
                "ativacao": "Quem está extraindo seu melhor?",
                "quando_usar": "Avatar orgulhoso/independente demais",
                "intensidade": 8,
                "categoria": "autoridade"
            },
            "coragem_prioritaria": {
                "instalacao": "Dinheiro não é problema, é prioridade...",
                "ativacao": "Você tem medo de quê?",
                "quando_usar": "Objeção principal é dinheiro",
                "intensidade": 9,
                "categoria": "objecoes"
            },
            "decisao_vs_condicao": {
                "instalacao": "Existem dois tipos de pessoas...",
                "ativacao": "Você vive de decisão ou desculpa?",
                "quando_usar": "Avatar cheio de desculpas",
                "intensidade": 8,
                "categoria": "acao"
            },
            "antecipacao_massiva": {
                "instalacao": "Tem algo especial vindo...",
                "ativacao": "Lembram do grupo seleto?",
                "quando_usar": "Criar curiosidade sobre oferta",
                "intensidade": 7,
                "categoria": "curiosidade"
            },
            "trofeu_intimo": {
                "instalacao": "No fundo, o que você quer é...",
                "ativacao": "Imagine o rosto do seu filho quando...",
                "quando_usar": "Conectar com desejo emocional",
                "intensidade": 10,
                "categoria": "emocional"
            },
            "comprometimento_publico": {
                "instalacao": "Quem está comprometido...",
                "ativacao": "Digite EU VOU se está pronto",
                "quando_usar": "Aumentar taxa de conversão",
                "intensidade": 8,
                "categoria": "compromisso"
            },
            "vilao_comum": {
                "instalacao": "Existe um inimigo comum...",
                "ativacao": "Sabe quem não quer seu sucesso?",
                "quando_usar": "Unir audiência contra algo",
                "intensidade": 9,
                "categoria": "tribal"
            },
            "prova_viva": {
                "instalacao": "Pessoas como você conseguiram...",
                "ativacao": "[Nome], levante e conte",
                "quando_usar": "Quebrar ceticismo",
                "intensidade": 9,
                "categoria": "credibilidade"
            },
            "deadline_mental": {
                "instalacao": "O tempo não espera...",
                "ativacao": "Daqui 1 ano você estará onde?",
                "quando_usar": "Avatar procrastinador",
                "intensidade": 8,
                "categoria": "urgencia"
            },
            "exclusividade_tribal": {
                "instalacao": "Nem todos estão prontos...",
                "ativacao": "Isso não é para a massa",
                "quando_usar": "Criar senso de elite",
                "intensidade": 8,
                "categoria": "exclusividade"
            },
            "catarse_emocional": {
                "instalacao": "Existe um momento...",
                "ativacao": "[Vídeo/História emocionante]",
                "quando_usar": "Quebrar resistência lógica",
                "intensidade": 10,
                "categoria": "emocional"
            }
        }

    def _load_pitch_structures(self) -> Dict[str, Any]:
        """Carrega estruturas de pitch disponíveis"""
        return {
            "classica": {
                "nome": "Pitch Clássico Expandido",
                "duracao": "60-90 min",
                "pre_pitch": "20-30 min",
                "transicao": "5 min",
                "pitch_core": "30-40 min",
                "close_multiplo": "10-15 min",
                "qa_estrategico": "10-15 min",
                "melhor_para": "Audiência morna/quente, alta complexidade"
            },
            "comprimida": {
                "nome": "Pitch Comprimido Urgente",
                "duracao": "45-60 min",
                "pre_pitch": "15 min",
                "pitch_direto": "20-25 min",
                "close_agressivo": "10-15 min",
                "bonus_drop": "5 min",
                "melhor_para": "Audiência quente, baixa complexidade"
            },
            "epica": {
                "nome": "Pitch Épico Imersivo",
                "duracao": "90-120 min",
                "pre_pitch": "30-40 min",
                "pitch_demonstrativo": "40-50 min",
                "close_consultivo": "15-20 min",
                "ultima_chance": "5-10 min",
                "melhor_para": "Audiência fria, alta conversão necessária"
            }
        }

    def _load_killer_scripts(self) -> Dict[str, Any]:
        """Carrega scripts matadores para momentos-chave"""
        return {
            "quebra_objecao_dinheiro": {
                "script": "'Não tenho dinheiro' é a desculpa mais COVARDE que existe.\nVocê tem dinheiro para [item 1], para [item 2], para [item 3].\nMas não tem para VOCÊ?\nNão é falta de dinheiro. É falta de AMOR PRÓPRIO.\nQuanto vale sua transformação? R$ 100? R$ 1.000?\nSe não vale [investimento], você não vale nada para você mesmo.",
                "momento": "Objeção de preço",
                "intensidade": 10
            },
            "quebra_objecao_tempo": {
                "script": "24 horas. Todo mundo tem.\n- 8 dormindo\n- 8 trabalhando\n- 8 sobrando\nOnde vão suas 8 horas?\n2h Netflix + 2h Instagram + 2h reclamando = 6h DESPERDIÇADAS.\nNão é falta de tempo. É falta de PRIORIDADE.",
                "momento": "Objeção de tempo",
                "intensidade": 9
            },
            "criacao_urgencia_mental": {
                "script": "Calculadora. Agora. Sua idade x 365 = dias vividos.\n27.375 (75 anos) - seus dias = dias restantes.\nCada dia procrastinando = dia roubado do futuro.\nQuanto mais você vai deixar roubarem?",
                "momento": "Criar urgência",
                "intensidade": 9
            },
            "ativacao_trofeu_intimo": {
                "script": "Fecha os olhos. É manhã de Natal.\nSeu filho abre o presente. O que queria.\n'Obrigado! Você é o melhor pai/mãe do mundo!'\nAgora imagine o contrário.\n'Por que Papai Noel não trouxe?'\nQual cena você escolhe viver?",
                "momento": "Conectar com desejo profundo",
                "intensidade": 10
            },
            "momento_mentor_catarse": {
                "script": "[LUZES BAIXAS - MÚSICA EMOCIONAL]\n'Um menino. Disseram que não conseguiria.\nFraco demais. Pobre demais.\nUm homem viu o que outros não viam.\n'Chora hoje. Vence amanhã.'\nEsse menino era eu.\nEsse homem, agora, sou eu para vocês.\nMas só ajudo quem QUER ser ajudado.'",
                "momento": "Estabelecer autoridade emocional",
                "intensidade": 10
            }
        }

    def generate_complete_prepitch(
        self,
        avatar_data: Dict[str, Any],
        pitch_structure: str = "classica",
        target_emotion: str = "transformacao"
    ) -> Dict[str, Any]:
        """Gera pré-pitch invisível completo baseado no avatar"""

        logger.info(f"🎯 Gerando pré-pitch invisível para estrutura {pitch_structure}")

        try:
            # 1. Análise inteligente do avatar
            avatar_analysis = self._analyze_avatar_for_drives(avatar_data)

            # 2. Seleção personalizada dos 12 drives
            selected_drives = self._select_optimal_drives(avatar_analysis)

            # 3. Estrutura do pré-pitch baseada no formato
            prepitch_structure = self._create_prepitch_structure(pitch_structure, selected_drives)

            # 4. Scripts personalizados
            personalized_scripts = self._generate_personalized_scripts(avatar_data, selected_drives)

            # 5. Timeline detalhada
            detailed_timeline = self._create_detailed_timeline(prepitch_structure, personalized_scripts)

            # 6. Elementos visuais e musicais
            audiovisual_elements = self._design_audiovisual_elements(selected_drives)

            # 7. Métricas de engajamento
            engagement_metrics = self._define_engagement_metrics(selected_drives)

            return {
                "avatar_analysis": avatar_analysis,
                "selected_drives": selected_drives,
                "prepitch_structure": prepitch_structure,
                "personalized_scripts": personalized_scripts,
                "detailed_timeline": detailed_timeline,
                "audiovisual_elements": audiovisual_elements,
                "engagement_metrics": engagement_metrics,
                "implementation_guide": self._create_implementation_guide(detailed_timeline),
                "backup_scenarios": self._create_backup_scenarios(selected_drives),
                "conversion_predictions": self._predict_conversion_rates(avatar_analysis, selected_drives)
            }

        except Exception as e:
            logger.error(f"❌ Erro ao gerar pré-pitch: {e}")
            return self._fallback_prepitch(avatar_data)

    def _analyze_avatar_for_drives(self, avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analisa avatar para mapear drives ideais"""

        # Extrai características do avatar
        dores = avatar_data.get('dores_principais', [])
        medos = avatar_data.get('medos_secretos', [])
        desejos = avatar_data.get('desejos_secretos', [])
        objecoes = avatar_data.get('muralhas_desconfianca_objecoes', [])
        temperatura = avatar_data.get('temperatura_emocional', 'morna')

        analysis = {
            "perfil_psicologico": {
                "dominante_dor": self._identify_dominant_pain(dores),
                "medo_principal": self._identify_main_fear(medos),
                "desejo_primario": self._identify_primary_desire(desejos),
                "objecao_critica": self._identify_critical_objection(objecoes),
                "temperatura_atual": temperatura
            },
            "drives_recomendados": {
                "para_dores": self._map_drives_for_pains(dores),
                "para_medos": self._map_drives_for_fears(medos),
                "para_desejos": self._map_drives_for_desires(desejos),
                "para_objecoes": self._map_drives_for_objections(objecoes),
                "para_temperatura": self._map_drives_for_temperature(temperatura)
            },
            "estrategia_emocional": {
                "intensidade_recomendada": self._calculate_recommended_intensity(avatar_data),
                "sequencia_otima": self._determine_optimal_sequence(avatar_data),
                "pontos_resistencia": self._identify_resistance_points(avatar_data)
            }
        }

        return analysis

    def _select_optimal_drives(self, avatar_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Seleciona os 12 drives mais devastadores para o avatar"""

        # Coleta todos os drives recomendados
        recommended_drives = []
        for category, drives in avatar_analysis["drives_recomendados"].items():
            for drive in drives:
                if drive not in [d["nome"] for d in recommended_drives]:
                    drive_data = self.mental_drives[drive].copy()
                    drive_data["nome"] = drive
                    drive_data["categoria_origem"] = category
                    drive_data["score"] = self._calculate_drive_score(drive, avatar_analysis)
                    recommended_drives.append(drive_data)

        # Ordena por score e seleciona os 12 melhores
        recommended_drives.sort(key=lambda x: x["score"], reverse=True)
        selected_drives = recommended_drives[:12]

        # Adiciona justificativa para cada drive
        for drive in selected_drives:
            drive["justificativa"] = self._generate_drive_justification(drive, avatar_analysis)
            drive["timing_otimo"] = self._calculate_optimal_timing(drive, avatar_analysis)

        return selected_drives

    def _create_prepitch_structure(
        self,
        structure_type: str,
        selected_drives: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Cria estrutura do pré-pitch baseada no tipo escolhido"""

        base_structure = self.pitch_structures[structure_type]
        prepitch_duration = int(base_structure["pre_pitch"].split()[0])

        if structure_type == "classica":
            return self._create_classic_structure(prepitch_duration, selected_drives)
        elif structure_type == "comprimida":
            return self._create_compressed_structure(prepitch_duration, selected_drives)
        elif structure_type == "epica":
            return self._create_epic_structure(prepitch_duration, selected_drives)

    def _create_classic_structure(self, duration: int, drives: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Cria estrutura clássica de 25 minutos"""

        return {
            "tipo": "Clássica",
            "duracao_total": 25,
            "fases": {
                "abertura_impactante": {
                    "tempo": "00:00-03:00",
                    "duracao": 3,
                    "drives": [drives[0]["nome"], drives[1]["nome"]],
                    "objetivo": "Destruir ilusão e criar tensão",
                    "energia": "Calma crescendo para tensão",
                    "elementos": ["Dado chocante", "Estatística impactante"]
                },
                "expansao_desejo": {
                    "tempo": "03:00-06:00",
                    "duracao": 3,
                    "drives": [drives[2]["nome"], drives[3]["nome"]],
                    "objetivo": "Expandir visão e conectar com sonhos",
                    "energia": "Inspiracional crescente",
                    "elementos": ["Visualização", "Música inspiracional"]
                },
                "confronto_realidade": {
                    "tempo": "06:00-10:00",
                    "duracao": 4,
                    "drives": [drives[4]["nome"], drives[5]["nome"], drives[6]["nome"]],
                    "objetivo": "Confrontar situação atual",
                    "energia": "Confrontadora mas empática",
                    "elementos": ["Calendário/relógio", "Espelho da realidade"]
                },
                "inimigo_revelado": {
                    "tempo": "10:00-13:00",
                    "duracao": 3,
                    "drives": [drives[7]["nome"], drives[8]["nome"]],
                    "objetivo": "Revelar vilão comum",
                    "energia": "Tensão/conspiração",
                    "elementos": ["Exposição do esquema", "Música tensa"]
                },
                "possibilidade_real": {
                    "tempo": "13:00-16:00",
                    "duracao": 3,
                    "drives": [drives[9]["nome"], drives[10]["nome"]],
                    "objetivo": "Mostrar possibilidade real",
                    "energia": "Esperançosa crescente",
                    "elementos": ["Case ao vivo", "Prova social"]
                },
                "momento_verdade": {
                    "tempo": "16:00-18:00",
                    "duracao": 2,
                    "drives": [drives[11]["nome"]],
                    "objetivo": "Forçar decisão interna",
                    "energia": "Épica de batalha",
                    "elementos": ["Compromisso público", "Música épica"]
                },
                "plano_matematico": {
                    "tempo": "18:00-21:00",
                    "duracao": 3,
                    "drives": ["metodo_vs_sorte"],
                    "objetivo": "Provar viabilidade matemática",
                    "energia": "Lógica convincente",
                    "elementos": ["Quadro", "Calculadora ao vivo"]
                },
                "evidencias_irrefutaveis": {
                    "tempo": "21:00-23:00",
                    "duracao": 2,
                    "drives": ["prova_viva"],
                    "objetivo": "Apresentar evidências finais",
                    "energia": "Convicção absoluta",
                    "elementos": ["Gráficos", "Estatísticas"]
                },
                "ponte_perfeita": {
                    "tempo": "23:00-25:00",
                    "duracao": 2,
                    "drives": ["antecipacao_massiva"],
                    "objetivo": "Transição para oferta",
                    "energia": "Urgência máxima",
                    "elementos": ["Ponte para pitch", "Anticipação"]
                }
            }
        }

    def _create_compressed_structure(self, duration: int, drives: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Cria estrutura comprimida de 15 minutos"""

        return {
            "tipo": "Comprimida",
            "duracao_total": 15,
            "fases": {
                "quebra_realidade": {
                    "tempo": "00:00-02:00",
                    "duracao": 2,
                    "drives": [drives[0]["nome"], drives[1]["nome"], drives[2]["nome"]],
                    "objetivo": "Quebrar realidade imediatamente",
                    "energia": "Impacto máximo",
                    "script_exemplo": "Você tem 15 minutos para mudar sua vida. Literalmente."
                },
                "prova_relampago": {
                    "tempo": "02:00-05:00",
                    "duracao": 3,
                    "drives": [drives[3]["nome"], drives[4]["nome"]],
                    "objetivo": "Provas rápidas e contundentes",
                    "energia": "Evidência bombardeada",
                    "elementos": ["3 cases de 30s cada"]
                },
                "expansao_urgente": {
                    "tempo": "05:00-08:00",
                    "duracao": 3,
                    "drives": [drives[5]["nome"], drives[6]["nome"], drives[7]["nome"]],
                    "objetivo": "Expandir urgência e desejo",
                    "energia": "Pressão crescente",
                    "elementos": ["Comparação temporal"]
                },
                "decisao_forcada": {
                    "tempo": "08:00-11:00",
                    "duracao": 3,
                    "drives": [drives[8]["nome"], drives[9]["nome"]],
                    "objetivo": "Forçar decisão binária",
                    "energia": "Confronto direto",
                    "elementos": ["Separação tribal"]
                },
                "evidencia_rapida": {
                    "tempo": "11:00-13:00",
                    "duracao": 2,
                    "drives": [drives[10]["nome"]],
                    "objetivo": "Evidência lógica rápida",
                    "energia": "Lógica irrefutável",
                    "elementos": ["3 dados rápidos"]
                },
                "transicao_explosiva": {
                    "tempo": "13:00-15:00",
                    "duracao": 2,
                    "drives": [drives[11]["nome"]],
                    "objetivo": "Transição explosiva para oferta",
                    "energia": "Anticipação máxima",
                    "elementos": ["Abertura das portas"]
                }
            }
        }

    def _create_epic_structure(self, duration: int, drives: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Cria estrutura épica de 35 minutos"""

        return {
            "tipo": "Épica",
            "duracao_total": 35,
            "fases": {
                "abertura_hollywoodiana": {
                    "tempo": "00:00-05:00",
                    "duracao": 5,
                    "drives": ["catarse_emocional"],
                    "objetivo": "Experiência cinematográfica",
                    "energia": "Emocional máxima",
                    "elementos": ["Vídeo 2-3 min", "História épica"]
                },
                "jornada_heroi": {
                    "tempo": "05:00-12:00",
                    "duracao": 7,
                    "drives": [drives[0]["nome"], drives[1]["nome"], drives[2]["nome"]],
                    "objetivo": "Jornada do herói completa",
                    "energia": "Narrativa envolvente",
                    "elementos": ["Mundo comum", "Chamado", "Mentor"]
                },
                "demonstracao_poder": {
                    "tempo": "12:00-20:00",
                    "duracao": 8,
                    "drives": [drives[3]["nome"], drives[4]["nome"], drives[5]["nome"]],
                    "objetivo": "Demonstração do método",
                    "energia": "Prova absoluta",
                    "elementos": ["Demo ao vivo", "Múltiplos cases"]
                },
                "construcao_elite": {
                    "tempo": "20:00-27:00",
                    "duracao": 7,
                    "drives": [drives[6]["nome"], drives[7]["nome"], drives[8]["nome"]],
                    "objetivo": "Criar senso de elite",
                    "energia": "Tribal intensa",
                    "elementos": ["Separação", "Nova identidade"]
                },
                "preparacao_logica": {
                    "tempo": "27:00-32:00",
                    "duracao": 5,
                    "drives": [drives[9]["nome"], drives[10]["nome"]],
                    "objetivo": "Preparação lógica final",
                    "energia": "Convicção racional",
                    "elementos": ["Matemática", "ROI"]
                },
                "chamado_final": {
                    "tempo": "32:00-35:00",
                    "duracao": 3,
                    "drives": [drives[11]["nome"]],
                    "objetivo": "Chamado final épico",
                    "energia": "Climax emocional",
                    "elementos": ["Abertura das portas"]
                }
            }
        }

    def _generate_personalized_scripts(
        self,
        avatar_data: Dict[str, Any],
        selected_drives: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Gera scripts personalizados baseados no avatar"""

        segmento = avatar_data.get('segmento', 'empreendedor')
        principal_dor = avatar_data.get('dores_principais', ['crescimento lento'])[0]
        principal_desejo = avatar_data.get('desejos_secretos', ['sucesso'])[0]

        personalized_scripts = {}

        for drive in selected_drives:
            drive_name = drive["nome"]
            base_drive = self.mental_drives[drive_name]

            # Personaliza script de instalação
            instalacao = base_drive["instalacao"].replace("[segmento]", segmento)
            instalacao = instalacao.replace("[dor]", principal_dor)
            instalacao = instalacao.replace("[desejo]", principal_desejo)

            # Personaliza script de ativação
            ativacao = base_drive["ativacao"].replace("[segmento]", segmento)
            ativacao = ativacao.replace("[dor]", principal_dor)
            ativacao = ativacao.replace("[desejo]", principal_desejo)

            personalized_scripts[drive_name] = {
                "instalacao_personalizada": instalacao,
                "ativacao_personalizada": ativacao,
                "contexto_avatar": f"Para {segmento} com dor '{principal_dor}' e desejo '{principal_desejo}'",
                "momento_ideal": drive["timing_otimo"],
                "intensidade_recomendada": drive["intensidade"]
            }

        # Adiciona scripts matadores personalizados
        for script_name, script_data in self.killer_scripts.items():
            script_personalizado = script_data["script"]
            script_personalizado = script_personalizado.replace("[segmento]", segmento)
            script_personalizado = script_personalizado.replace("[dor]", principal_dor)

            personalized_scripts[f"killer_{script_name}"] = {
                "script_completo": script_personalizado,
                "momento": script_data["momento"],
                "intensidade": script_data["intensidade"]
            }

        return personalized_scripts

    def _create_detailed_timeline(
        self,
        structure: Dict[str, Any],
        scripts: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Cria timeline detalhada com scripts específicos"""

        detailed_timeline = {
            "estrutura": structure["tipo"],
            "duracao_total": f"{structure['duracao_total']} minutos",
            "fases_detalhadas": {}
        }

        for fase_name, fase_data in structure["fases"].items():
            detailed_timeline["fases_detalhadas"][fase_name] = {
                **fase_data,
                "scripts_especificos": [],
                "transicoes": [],
                "elementos_visuais": [],
                "elementos_sonoros": []
            }

            # Adiciona scripts específicos para cada drive da fase
            for drive in fase_data.get("drives", []):
                if drive in scripts:
                    detailed_timeline["fases_detalhadas"][fase_name]["scripts_especificos"].append({
                        "drive": drive,
                        "instalacao": scripts[drive]["instalacao_personalizada"],
                        "ativacao": scripts[drive]["ativacao_personalizada"],
                        "timing": scripts[drive]["momento_ideal"]
                    })

            # Adiciona transições suaves
            detailed_timeline["fases_detalhadas"][fase_name]["transicoes"] = self._create_phase_transitions(fase_name, fase_data)

        return detailed_timeline

    def _design_audiovisual_elements(self, selected_drives: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Projeta elementos audiovisuais para maximizar impacto"""

        return {
            "elementos_visuais": {
                "slides_impacto": [
                    "Estatísticas chocantes com números grandes",
                    "Comparações visuais antes/depois",
                    "Gráficos de crescimento exponencial",
                    "Fotos emocionais (família, sonhos)",
                    "Calendário com dias riscados"
                ],
                "demonstracoes_ao_vivo": [
                    "Calculadora de oportunidade perdida",
                    "Simulador de resultados",
                    "Comparação de cenários"
                ],
                "elementos_cenicos": [
                    "Lighting dramático para momentos-chave",
                    "Props físicos (relógio, calendário)",
                    "Quadro/flipchart para matemática ao vivo"
                ]
            },
            "elementos_sonoros": {
                "trilha_sonora": {
                    "abertura": "Épica/Misteriosa",
                    "confronto": "Tensa/Dramática",
                    "inspiracao": "Elevada/Motivacional",
                    "urgencia": "Intensa/Rápida",
                    "climax": "Épica/Transformadora"
                },
                "efeitos_sonoros": [
                    "Tique-taque de relógio para urgência",
                    "Som de notificação para alertas",
                    "Silêncio dramático antes de revelações"
                ]
            },
            "interatividade": {
                "momentos_participacao": [
                    "Escrever novo objetivo 10x maior",
                    "Calcular dias de vida restantes",
                    "Levantar mão para compromissos",
                    "Chat com 'EU VOU' ou similar"
                ],
                "elementos_urgencia": [
                    "Timer visível contando",
                    "Contador de pessoas conectadas",
                    "Vagas disponíveis diminuindo"
                ]
            }
        }

    def _define_engagement_metrics(self, selected_drives: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Define métricas para medir engajamento durante o pré-pitch"""

        return {
            "metricas_emociais": {
                "reacoes_chat": ["🔥", "💯", "😱", "💪", "👏"],
                "palavras_chave_positivas": ["SIM", "QUERO", "EU VOU", "PRECISO"],
                "indicadores_urgencia": ["AGORA", "HOJE", "JÁ"],
                "sinais_resistencia": ["MAS", "PORÉM", "CARO", "DIFÍCIL"]
            },
            "metricas_comportamentais": {
                "tempo_tela": "Mínimo 90% do tempo",
                "interacoes": "Pelo menos 3 participações",
                "permanencia": "Até o final do pré-pitch",
                "engajamento_picos": "Momentos de maior atividade"
            },
            "indicadores_conversao": {
                "nivel_1_interesse": "Participação ativa",
                "nivel_2_engajamento": "Múltiplas interações",
                "nivel_3_urgencia": "Demonstra pressa/urgência",
                "nivel_4_pronto": "Pede informações sobre oferta"
            }
        }

    def _create_implementation_guide(self, timeline: Dict[str, Any]) -> Dict[str, Any]:
        """Cria guia de implementação prático"""

        return {
            "preparacao_evento": {
                "24h_antes": [
                    "Testar todos os equipamentos audiovisuais",
                    "Preparar props físicos (relógio, calculadora)",
                    "Ensaiar transições entre fases",
                    "Configurar sistema de chat/interação"
                ],
                "2h_antes": [
                    "Verificar internet e backup",
                    "Testar slides e vídeos",
                    "Aquecer voz e energia",
                    "Revisar scripts principais"
                ],
                "30min_antes": [
                    "Entrar no estado emocional correto",
                    "Verificar chat e engagement tools",
                    "Preparar primeira frase impactante"
                ]
            },
            "execucao_live": {
                "energy_management": "Começar 7/10, subir para 10/10 nos momentos-chave",
                "timing_control": "Usar cronômetro visível, respeitar tempos",
                "audience_reading": "Observar chat e ajustar intensidade",
                "backup_plans": "Scripts alternativos para baixo engajamento"
            },
            "pos_evento": {
                "imediato": [
                    "Capturar dados de engajamento",
                    "Identificar leads quentes",
                    "Salvar gravação para análise"
                ],
                "24h_depois": [
                    "Analisar métricas de conversão",
                    "Ajustar scripts baseado no feedback",
                    "Preparar follow-up para interessados"
                ]
            }
        }

    def _create_backup_scenarios(self, selected_drives: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Cria cenários de backup para situações imprevistas"""

        return {
            "baixo_engajamento": {
                "sinais": "Chat quieto, poucas reações",
                "acao": "Intensificar confronto, usar drives mais agressivos",
                "scripts_emergencia": [
                    "Vou parar aqui. Quem realmente quer mudar de vida?",
                    "Se vocês não estão engajados, eu também não vou estar",
                    "Última chance: quem quer resultados diferentes?"
                ]
            },
            "resistencia_alta": {
                "sinais": "Comentários negativos, objeções no chat",
                "acao": "Usar drives de prova social e autoridade",
                "estrategia": "Mostrar mais cases, intensificar credibilidade"
            },
            "problemas_tecnicos": {
                "sem_slides": "Continuar apenas com fala, usar quadro físico",
                "sem_audio": "Usar chat intensivamente, slides mais visuais",
                "sem_internet": "Modo offline preparado com conteúdo local"
            },
            "interrupcoes": {
                "perguntas_fora_hora": "Anotar para responder depois",
                "trolls_chat": "Ignorar ou banir rapidamente",
                "tempo_estourando": "Comprimir fases menos críticas"
            }
        }

    def _predict_conversion_rates(
        self,
        avatar_analysis: Dict[str, Any],
        selected_drives: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Prediz taxas de conversão baseadas no setup"""

        # Calcula score baseado em múltiplos fatores
        avatar_score = self._calculate_avatar_alignment_score(avatar_analysis)
        drives_score = self._calculate_drives_effectiveness_score(selected_drives)
        structure_score = 0.8  # Assumindo estrutura bem executada

        overall_score = (avatar_score * 0.4 + drives_score * 0.4 + structure_score * 0.2)

        return {
            "expectativa_conversao": {
                "cenario_conservador": f"{max(overall_score * 20, 5):.1f}%",
                "cenario_realista": f"{overall_score * 35:.1f}%",
                "cenario_otimista": f"{min(overall_score * 50, 65):.1f}%"
            },
            "fatores_impacto": {
                "alinhamento_avatar": f"{avatar_score * 100:.1f}%",
                "efetividade_drives": f"{drives_score * 100:.1f}%",
                "qualidade_execucao": f"{structure_score * 100:.1f}%"
            },
            "melhorias_sugeridas": self._suggest_conversion_improvements(overall_score),
            "benchmarks": {
                "pre_pitch_medio": "15-25%",
                "pre_pitch_bom": "25-40%",
                "pre_pitch_excepcional": "40-60%",
                "seu_potencial": f"{overall_score * 35:.1f}%"
            }
        }

    # Métodos auxiliares para cálculos
    def _identify_dominant_pain(self, dores: List[str]) -> str:
        """Identifica dor dominante"""
        return dores[0] if dores else "crescimento lento"

    def _identify_main_fear(self, medos: List[str]) -> str:
        """Identifica medo principal"""
        return medos[0] if medos else "fracasso"

    def _identify_primary_desire(self, desejos: List[str]) -> str:
        """Identifica desejo primário"""
        return desejos[0] if desejos else "sucesso"

    def _identify_critical_objection(self, objecoes: List[str]) -> str:
        """Identifica objeção crítica"""
        return objecoes[0] if objecoes else "preço"

    def _map_drives_for_pains(self, dores: List[str]) -> List[str]:
        """Mapeia drives para dores específicas"""
        drive_mapping = {
            "crescimento lento": ["diagnostico_brutal", "indignacao_produtiva", "deadline_mental"],
            "falta de clientes": ["vilao_comum", "metodo_vs_sorte", "prova_viva"],
            "baixa receita": ["ambicao_expandida", "trofeu_intimo", "coragem_prioritaria"],
            "falta de sistema": ["mentor_extrator", "metodo_vs_sorte", "ambiente_propulsor"]
        }
        
        mapped_drives = []
        for dor in dores:
            for key, drives in drive_mapping.items():
                if key.lower() in dor.lower():
                    mapped_drives.extend(drives)
        
        return list(set(mapped_drives)) if mapped_drives else ["diagnostico_brutal", "metodo_vs_sorte"]

    def _map_drives_for_fears(self, medos: List[str]) -> List[str]:
        """Mapeia drives para medos específicos"""
        fear_mapping = {
            "fracasso": ["prova_viva", "mentor_extrator", "decisao_vs_condicao"],
            "investimento": ["coragem_prioritaria", "trofeu_intimo", "deadline_mental"],
            "tempo": ["deadline_mental", "oportunidade_oculta", "decisao_vs_condicao"],
            "julgamento": ["exclusividade_tribal", "ambiente_propulsor", "vilao_comum"]
        }
        
        mapped_drives = []
        for medo in medos:
            for key, drives in fear_mapping.items():
                if key.lower() in medo.lower():
                    mapped_drives.extend(drives)
        
        return list(set(mapped_drives)) if mapped_drives else ["coragem_prioritaria", "decisao_vs_condicao"]

    def _map_drives_for_desires(self, desejos: List[str]) -> List[str]:
        """Mapeia drives para desejos específicos"""
        desire_mapping = {
            "liberdade": ["trofeu_intimo", "ambicao_expandida", "exclusividade_tribal"],
            "reconhecimento": ["prova_viva", "exclusividade_tribal", "ambiente_propulsor"],
            "crescimento": ["ambicao_expandida", "oportunidade_oculta", "metodo_vs_sorte"],
            "segurança": ["prova_viva", "mentor_extrator", "coragem_prioritaria"]
        }
        
        mapped_drives = []
        for desejo in desejos:
            for key, drives in desire_mapping.items():
                if key.lower() in desejo.lower():
                    mapped_drives.extend(drives)
        
        return list(set(mapped_drives)) if mapped_drives else ["ambicao_expandida", "trofeu_intimo"]

    def _map_drives_for_objections(self, objecoes: List[str]) -> List[str]:
        """Mapeia drives para objeções específicas"""
        objection_mapping = {
            "preço": ["coragem_prioritaria", "trofeu_intimo", "deadline_mental"],
            "tempo": ["deadline_mental", "decisao_vs_condicao", "oportunidade_oculta"],
            "ceticismo": ["prova_viva", "mentor_extrator", "metodo_vs_sorte"],
            "complexidade": ["metodo_vs_sorte", "mentor_extrator", "prova_viva"]
        }
        
        mapped_drives = []
        for objecao in objecoes:
            for key, drives in objection_mapping.items():
                if key.lower() in objecao.lower():
                    mapped_drives.extend(drives)
        
        return list(set(mapped_drives)) if mapped_drives else ["coragem_prioritaria", "prova_viva"]

    def _map_drives_for_temperature(self, temperatura: str) -> List[str]:
        """Mapeia drives para temperatura da audiência"""
        temperature_mapping = {
            "fria": ["catarse_emocional", "prova_viva", "oportunidade_oculta"],
            "morna": ["diagnostico_brutal", "ambicao_expandida", "trofeu_intimo"],
            "quente": ["decisao_vs_condicao", "comprometimento_publico", "antecipacao_massiva"]
        }
        
        return temperature_mapping.get(temperatura, ["diagnostico_brutal", "prova_viva"])

    def _calculate_recommended_intensity(self, avatar_data: Dict[str, Any]) -> int:
        """Calcula intensidade recomendada (1-10)"""
        temperatura = avatar_data.get('temperatura_emocional', 'morna')
        resistencia = len(avatar_data.get('muralhas_desconfianca_objecoes', []))
        
        base_intensity = {
            'fria': 6,
            'morna': 8,
            'quente': 9
        }.get(temperatura, 7)
        
        # Ajusta baseado na resistência
        intensity = base_intensity + min(resistencia, 2)
        
        return min(intensity, 10)

    def _determine_optimal_sequence(self, avatar_data: Dict[str, Any]) -> List[str]:
        """Determina sequência ótima de drives"""
        temperatura = avatar_data.get('temperatura_emocional', 'morna')
        
        if temperatura == 'fria':
            return ['emocional', 'credibilidade', 'logica', 'acao']
        elif temperatura == 'morna':
            return ['confronto', 'emocional', 'credibilidade', 'acao']
        else:  # quente
            return ['confronto', 'acao', 'urgencia', 'exclusividade']

    def _identify_resistance_points(self, avatar_data: Dict[str, Any]) -> List[str]:
        """Identifica pontos de resistência"""
        objecoes = avatar_data.get('muralhas_desconfianca_objecoes', [])
        medos = avatar_data.get('medos_secretos', [])
        
        resistance_points = []
        
        # Mapeia objeções para pontos de resistência
        for objecao in objecoes:
            if 'preço' in objecao.lower() or 'caro' in objecao.lower():
                resistance_points.append('investimento_financeiro')
            elif 'tempo' in objecao.lower():
                resistance_points.append('disponibilidade_tempo')
            elif 'funciona' in objecao.lower() or 'resultado' in objecao.lower():
                resistance_points.append('ceticismo_metodologia')
        
        return resistance_points

    def _calculate_drive_score(self, drive_name: str, avatar_analysis: Dict[str, Any]) -> float:
        """Calcula score de relevância do drive para o avatar"""
        drive_data = self.mental_drives[drive_name]
        
        # Score base da intensidade do drive
        base_score = drive_data["intensidade"] / 10
        
        # Bonus se o drive aparece em múltiplas categorias recomendadas
        recommendations = avatar_analysis["drives_recomendados"]
        appearance_count = sum(1 for drives in recommendations.values() if drive_name in drives)
        appearance_bonus = appearance_count * 0.2
        
        # Bonus baseado na categoria do drive vs necessidades do avatar
        category_bonus = self._calculate_category_alignment(drive_data["categoria"], avatar_analysis)
        
        total_score = base_score + appearance_bonus + category_bonus
        return min(total_score, 1.0)

    def _calculate_category_alignment(self, drive_category: str, avatar_analysis: Dict[str, Any]) -> float:
        """Calcula alinhamento da categoria do drive com necessidades do avatar"""
        temperatura = avatar_analysis["perfil_psicologico"]["temperatura_atual"]
        
        category_alignment = {
            'fria': {
                'emocional': 0.3,
                'credibilidade': 0.2,
                'logica': 0.1,
                'confronto': 0.0
            },
            'morna': {
                'confronto': 0.3,
                'emocional': 0.2,
                'credibilidade': 0.1,
                'urgencia': 0.1
            },
            'quente': {
                'acao': 0.3,
                'urgencia': 0.2,
                'exclusividade': 0.1,
                'compromisso': 0.1
            }
        }
        
        return category_alignment.get(temperatura, {}).get(drive_category, 0.05)

    def _generate_drive_justification(self, drive: Dict[str, Any], avatar_analysis: Dict[str, Any]) -> str:
        """Gera justificativa para seleção do drive"""
        perfil = avatar_analysis["perfil_psicologico"]
        
        justification_templates = {
            'confronto': f"Necessário para quebrar negação sobre '{perfil['dominante_dor']}'",
            'emocional': f"Conecta com desejo profundo por '{perfil['desejo_primario']}'",
            'credibilidade': f"Reduz ceticismo e medo de '{perfil['medo_principal']}'",
            'urgencia': f"Combate procrastinação típica de audiência '{perfil['temperatura_atual']}'",
            'acao': f"Força decisão para superar objeção '{perfil['objecao_critica']}'",
            'exclusividade': f"Cria senso de elite para audiência '{perfil['temperatura_atual']}'"
        }
        
        return justification_templates.get(drive["categoria"], f"Drive complementar para perfil {perfil['temperatura_atual']}")

    def _calculate_optimal_timing(self, drive: Dict[str, Any], avatar_analysis: Dict[str, Any]) -> str:
        """Calcula timing ótimo para o drive"""
        categoria = drive["categoria"]
        temperatura = avatar_analysis["perfil_psicologico"]["temperatura_atual"]
        
        timing_map = {
            'fria': {
                'emocional': 'início',
                'credibilidade': 'meio',
                'logica': 'final',
                'confronto': 'evitar'
            },
            'morna': {
                'confronto': 'início',
                'emocional': 'meio',
                'credibilidade': 'meio',
                'acao': 'final'
            },
            'quente': {
                'confronto': 'início',
                'acao': 'meio',
                'urgencia': 'final',
                'exclusividade': 'final'
            }
        }
        
        return timing_map.get(temperatura, {}).get(categoria, 'meio')

    def _create_phase_transitions(self, fase_name: str, fase_data: Dict[str, Any]) -> List[str]:
        """Cria transições suaves entre fases"""
        transitions = {
            'abertura_impactante': [
                "Agora que você viu a realidade nua e crua...",
                "Mas calma, não vim aqui só para te deixar mal..."
            ],
            'expansao_desejo': [
                "Agora que você expandiu sua visão...",
                "Mas existe um problema..."
            ],
            'confronto_realidade': [
                "E por que você não conseguiu ainda?",
                "Deixa eu te mostrar o verdadeiro culpado..."
            ],
            'inimigo_revelado': [
                "Mas nem tudo está perdido...",
                "Existe uma saída, e vou te mostrar..."
            ],
            'possibilidade_real': [
                "A pergunta agora é simples...",
                "Você está pronto para a verdade?"
            ]
        }
        
        return transitions.get(fase_name, ["Agora...", "Então..."])

    def _calculate_avatar_alignment_score(self, avatar_analysis: Dict[str, Any]) -> float:
        """Calcula score de alinhamento com avatar"""
        # Fatores que contribuem para o alinhamento
        temperatura_score = {
            'fria': 0.6,
            'morna': 0.8,
            'quente': 0.9
        }.get(avatar_analysis["perfil_psicologico"]["temperatura_atual"], 0.7)
        
        drives_match = len(avatar_analysis["drives_recomendados"]["para_dores"]) / 5  # Normaliza para 0-1
        
        return (temperatura_score + drives_match) / 2

    def _calculate_drives_effectiveness_score(self, selected_drives: List[Dict[str, Any]]) -> float:
        """Calcula score de efetividade dos drives selecionados"""
        intensidade_media = sum(drive["intensidade"] for drive in selected_drives) / len(selected_drives) / 10
        
        # Bonus para diversidade de categorias
        categorias = set(drive["categoria"] for drive in selected_drives)
        diversidade_bonus = len(categorias) / 6  # 6 categorias principais
        
        return (intensidade_media + diversidade_bonus) / 2

    def _suggest_conversion_improvements(self, overall_score: float) -> List[str]:
        """Sugere melhorias para aumentar conversão"""
        if overall_score < 0.5:
            return [
                "Intensificar drives emocionais",
                "Adicionar mais provas sociais",
                "Melhorar alinhamento com avatar",
                "Aumentar urgência e escassez"
            ]
        elif overall_score < 0.7:
            return [
                "Refinar timing dos drives",
                "Personalizar scripts ainda mais",
                "Adicionar elementos visuais impactantes"
            ]
        else:
            return [
                "Otimizar transições entre fases",
                "Testar variações de intensidade",
                "Adicionar elementos de gamificação"
            ]

    def _fallback_prepitch(self, avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Pré-pitch básico como fallback"""
        return {
            "tipo": "Pré-pitch Básico",
            "drives_selecionados": ["diagnostico_brutal", "prova_viva", "trofeu_intimo"],
            "estrutura": "Simples de 15 minutos",
            "expectativa_conversao": "15-25%"
        }

# Instância global
invisible_prepitch_architect = InvisiblePrePitchArchitect()
