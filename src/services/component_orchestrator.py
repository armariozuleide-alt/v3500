#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Component Orchestrator com tratamento robusto de erros
"""

import logging
import threading
from datetime import datetime
from typing import Dict, Any, Callable

logger = logging.getLogger(__name__)
"""
ARQV30 Enhanced v2.0 - Component Orchestrator
Orquestrador seguro de componentes com validação rigorosa
"""

import logging
import time
import json
from typing import Dict, List, Any, Optional, Callable
from datetime import datetime
from services.auto_save_manager import salvar_etapa, salvar_erro

# Supondo que 'mental_drivers_architect' e 'services.auto_save_manager' estejam disponíveis
# Se não, elas precisarão ser importadas ou definidas.
# Exemplo de importação (ajuste o caminho conforme necessário):
# import mental_drivers_architect 

# Mock para fins de exemplo se os imports não existirem
class MockMentalDriversArchitect:
    def generate_custom_drivers(self, avatar_data, context_data, session_id=None):
        logger.info("Mock: Gerando drivers mentais...")
        # Simula um retorno com a estrutura esperada
        return {
            'drivers_customizados': [
                {'nome': 'Mock Driver 1', 'gatilho_central': 'Mock Trigger 1', 'definicao_visceral': 'Mock Visceral 1'},
                {'nome': 'Mock Driver 2', 'gatilho_central': 'Mock Trigger 2', 'definicao_visceral': 'Mock Visceral 2'}
            ],
            'total_drivers': 2
        }

class MockAutoSaveManager:
    def salvar_etapa(self, etapa_nome, dados, categoria="analise_completa"):
        logger.info(f"Mock: Salvando etapa '{etapa_nome}' na categoria '{categoria}'.")
        # Em um cenário real, isso salvaria os dados.
        pass
    def salvar_erro(self, etapa_nome, erro_detalhado, categoria="analise_completa"):
        logger.error(f"Mock: Salvando erro na etapa '{etapa_nome}'. Erro: {erro_detalhado}")
        pass

# Substitua as classes reais pelas mocks se elas não estiverem disponíveis no ambiente de execução
try:
    import mental_drivers_architect
except ImportError:
    logger.warning("Mocking 'mental_drivers_architect' porque não foi encontrado.")
    mental_drivers_architect = MockMentalDriversArchitect()

try:
    from services.auto_save_manager import salvar_etapa, salvar_erro
except ImportError:
    logger.warning("Mocking 'services.auto_save_manager' porque não foi encontrado.")
    salvar_etapa = MockAutoSaveManager().salvar_etapa
    salvar_erro = MockAutoSaveManager().salvar_erro


logger = logging.getLogger(__name__)

class ComponentValidationError(Exception):
    """Exceção para erros de validação de componentes"""
    pass

class ComponentOrchestrator:
    """Component Orchestrator com tratamento robusto de erros"""

    def __init__(self):
        """Inicializa o orquestrador"""
        self.component_registry = {}
        self.execution_order = []
        self.validation_rules = {}
        self.component_results = {}
        self.execution_stats = {}
        self.components = {} # Adicionado para compatibilidade com a segunda parte do código

        logger.info("Component Orchestrator inicializado")

    def register_component(
        self,
        name: str,
        executor: Callable,
        dependencies: List[str] = None,
        validation_rules: Dict[str, Any] = None,
        required: bool = True
    ):
        """Registra um componente no orquestrador"""

        self.component_registry[name] = {
            'executor': executor,
            'dependencies': dependencies or [],
            'validation_rules': validation_rules or {},
            'required': required,
            'status': 'pending'
        }
        # Compatibilidade com a versão antiga que usava self.components
        self.components[name] = executor

        if name not in self.execution_order:
            self.execution_order.append(name)

        logger.info(f"📝 Componente registrado: {name}")

    def execute_components(
        self,
        data: Dict[str, Any],
        progress_callback: Optional[Callable] = None
    ) -> Dict[str, Any]:
        """Executa todos os componentes de forma orquestrada"""

        results = {}
        components_executed = 0

        logger.info(f"🚀 Iniciando execução de {len(self.components)} componentes")

        # Prepara dados básicos se não existirem
        base_data = self._prepare_base_data(data)

        for component_name, component_func in self.components.items():
            try:
                logger.info(f"🔄 Executando componente: {component_name}")

                if progress_callback:
                    progress_callback(components_executed + 1, f"Executando {component_name}...")

                # Prepara dados específicos para o componente
                component_data = self._prepare_component_data(base_data, component_name)

                # Executa o componente
                result = component_func(component_data)

                # Normaliza resultado se necessário
                result = self._normalize_component_result(component_name, result)

                # Valida o resultado
                if self._validate_component_result(component_name, result):
                    results[component_name] = result
                    logger.info(f"✅ {component_name}: Sucesso")

                    # Salva resultado intermediário
                    salvar_etapa(f"componente_{component_name}", result, categoria="analise_completa")
                else:
                    logger.error(f"❌ Componente {component_name} falhou na validação")
                    results[component_name] = {'error': f'Falha na validação de {component_name}', 'component': component_name}

                components_executed += 1

            except Exception as e:
                logger.error(f"❌ Erro ao executar {component_name}: {e}")
                results[component_name] = {'error': str(e), 'component': component_name}
                components_executed += 1

        # Relatório final
        successful_components = sum(1 for result in results.values() if not result.get('error'))
        total_components = len(results)

        report = {
            'components_executed': total_components,
            'successful_components': successful_components,
            'success_rate': (successful_components / total_components * 100) if total_components > 0 else 0,
            'results': results,
            'execution_summary': {
                'total_time': time.time(),
                'components_status': {name: 'success' if not result.get('error') else 'failed'
                                   for name, result in results.items()}
            }
        }

        # Salva relatório
        salvar_etapa("component_orchestrator_report", report, categoria="analise_completa")

        return report

    def _prepare_base_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Prepara dados básicos com fallbacks"""
        base_data = data.copy()

        # Garante segmento e produto
        base_data['segmento'] = base_data.get('segmento') or base_data.get('context_data', {}).get('segmento', 'mercado')
        base_data['produto'] = base_data.get('produto') or base_data.get('context_data', {}).get('produto', 'produto')


        # Garante context_data
        if 'context_data' not in base_data:
            base_data['context_data'] = {}

        base_data['context_data'].update({
            'segmento': base_data['segmento'],
            'produto': base_data['produto']
        })

        # Garante avatar_data básico
        if 'avatar_data' not in base_data or not base_data['avatar_data']:
            base_data['avatar_data'] = {
                'nome': f'Avatar {base_data["segmento"]}',
                'dores_viscerais': [
                    f'Dificuldades em {base_data["segmento"]}',
                    'Falta de crescimento',
                    'Concorrência intensa'
                ],
                'desejos_secretos': [
                    f'Dominar {base_data["segmento"]}',
                    'Crescimento acelerado',
                    'Liderança de mercado'
                ]
            }

        return base_data

    def _prepare_component_data(self, base_data: Dict[str, Any], component_name: str) -> Dict[str, Any]:
        """Prepara dados específicos para cada componente"""
        component_data = base_data.copy()

        # Dados específicos por componente
        if component_name == 'mental_drivers':
            # Mental drivers precisa de estrutura específica com 'data' contendo avatar e context
            component_data['data'] = {
                'avatar_data': component_data.get('avatar_data', {}),
                'context_data': component_data.get('context_data', {}),
                'session_id': component_data.get('session_id')
            }
        elif component_name in ['visual_proofs', 'anti_objection', 'pre_pitch', 'future_predictions']:
            # Estes componentes usam avatar_data e context_data diretamente,
            # mas o orquestrador já os preparou em base_data.
            # Se precisarem de uma chave específica, seria aqui.
            pass # Mantém a estrutura de base_data

        return component_data

    def _normalize_component_result(self, component_name: str, result: Any) -> Dict[str, Any]:
        """Normaliza resultado do componente para dict"""
        if isinstance(result, list):
            logger.info(f"🔄 Convertendo lista para dict em {component_name}")
            return {
                'success': True,
                'data': result,
                'total_items': len(result),
                'component': component_name
            }

        if not isinstance(result, dict):
            logger.warning(f"⚠️ Convertendo {type(result)} para dict em {component_name}")
            return {
                'success': False,
                'data': str(result),
                'component': component_name,
                'converted': True
            }

        return result

    def _validate_component_result(self, component_name: str, result: Any, expected_type: type = dict) -> bool:
        """Valida resultado do componente"""
        if not isinstance(result, expected_type):
            logger.warning(f"⚠️ {component_name}: Tipo inválido - esperado {expected_type}, recebido {type(result)}")
            # Se for lista mas esperávamos dict, tentamos converter
            if isinstance(result, list) and expected_type == dict:
                logger.info(f"🔄 Tentando converter lista para dict em {component_name}")
                # Uma conversão simples de lista para dict pode ser um mapeamento ou uma estrutura padrão
                # Aqui, retornamos True assumindo que a normalização já tratou isso ou que a estrutura da lista é aceitável.
                # Se uma conversão específica for necessária, ela deve ser feita aqui ou em _normalize_component_result
                return True
            return False

        # Verifica se há um erro explícito no resultado do componente, exceto se for um fallback
        if isinstance(result, dict) and result.get('error') and not result.get('fallback_used'):
            logger.warning(f"⚠️ {component_name}: Erro reportado pelo componente - {result.get('error')}")
            return False

        return True

    def _execute_mental_drivers(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Executa geração de drivers mentais"""
        try:
            # Garante que o segmento esteja presente
            segmento = data.get('segmento') or data.get('context_data', {}).get('segmento', 'mercado')
            produto = data.get('produto') or data.get('context_data', {}).get('produto', 'produto')

            # Monta context_data corretamente
            context_data = {
                'segmento': segmento,
                'produto': produto,
                **data.get('context_data', {})
            }

            # Monta avatar_data básico se não existir
            avatar_data = data.get('avatar_data', {})
            if not avatar_data:
                avatar_data = {
                    'nome': f'Avatar {segmento}',
                    'dores_viscerais': [
                        f'Dificuldades em {segmento}',
                        'Falta de resultados',
                        'Concorrência alta'
                    ],
                    'desejos_secretos': [
                        f'Dominar {segmento}',
                        'Crescer rapidamente',
                        'Ser referência'
                    ]
                }

            # Chama a função real ou mockada
            result = mental_drivers_architect.generate_custom_drivers(
                avatar_data,
                context_data,
                session_id=data.get('session_id')
            )

            # Garante que retorna um dict
            if isinstance(result, list):
                return {
                    'success': True,
                    'drivers_customizados': result,
                    'total_drivers': len(result)
                }

            return result if isinstance(result, dict) else {'error': 'Formato inválido retornado pelo driver generator'}

        except Exception as e:
            logger.error(f"❌ Erro na geração de drivers mentais: {e}")
            # Retorna um fallback com estrutura de erro clara
            return {
                'error': str(e),
                'fallback_used': True,
                'drivers_basicos': [
                    {
                        'nome': f'Urgência {data.get("segmento", "Mercado")}',
                        'gatilho_central': 'Tempo limitado para agir',
                        'definicao_visceral': 'Cada dia perdido é oportunidade que não volta'
                    }
                ]
            }


    # Métodos legados da primeira versão que podem não ser mais usados diretamente,
    # mas mantidos para referência ou compatibilidade caso a arquitetura mude.
    def execute_component_safely(self, component_name: str, component_func, *args, **kwargs):
        """Executa componente com tratamento seguro de erros"""
        try:
            logger.info(f"🚀 Executando componente: {component_name}")
            result = component_func(*args, **kwargs)

            # O status aqui é mais simples, sem a complexidade do orchestrator principal
            # Se for usado, precisa ser adaptado ou removido.
            # self.components_status[component_name] = { ... }

            return result

        except Exception as e:
            logger.error(f"❌ Erro no componente {component_name}: {e}")
            return self._create_component_fallback(component_name, str(e))

    def _create_component_fallback(self, component_name: str, error_msg: str) -> Dict[str, Any]:
        """Cria resultado de fallback para componente com falha"""
        return {
            'status': 'fallback',
            'component': component_name,
            'error': error_msg,
            'fallback_used': True,
            'timestamp': datetime.now().isoformat(),
            'message': f'Componente {component_name} executado com fallback devido a erro'
        }

    def get_components_status(self) -> Dict[str, Any]:
        """Retorna status de todos os componentes"""
        # Este método parece ser de uma versão mais antiga e pode não refletir o estado atual
        # do `component_registry` da nova implementação. Se necessário, deve ser reescrito.
        status_dict = {}
        if hasattr(self, 'component_registry'):
            status_dict = {
                'total_components': len(self.component_registry),
                'successful_components': len([c for c in self.component_registry.values() if c['status'] == 'success']),
                'failed_components': len([c for c in self.component_registry.values() if c['status'] == 'failed']),
                'components_detail': self.component_registry
            }
        return status_dict

    def get_component_status(self, component_name: str) -> str:
        """Retorna status de um componente"""
        # Retorna o status do registro de componentes
        return self.component_registry.get(component_name, {}).get('status', 'not_found')

    def get_execution_summary(self) -> Dict[str, Any]:
        """Retorna resumo da execução"""
        # Este método pode precisar ser adaptado para usar os resultados mais recentes do execute_components
        status_counts = {}
        if hasattr(self, 'component_registry'):
            for component_name, component_info in self.component_registry.items():
                status = component_info.get('status', 'unknown')
                status_counts[status] = status_counts.get(status, 0) + 1

        return {
            'total_components': len(self.component_registry),
            'status_breakdown': status_counts,
            'success_rate': status_counts.get('success', 0) / len(self.component_registry) * 100 if self.component_registry else 0
        }

# Instância global
component_orchestrator = ComponentOrchestrator()