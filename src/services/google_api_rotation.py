#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Google API Rotation System
Sistema de rotação de APIs para evitar rate limits
"""

import logging
import time
import json
import os
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class GoogleAPIRotation:
    """Sistema de rotação de APIs do Google Search"""

    def __init__(self):
        """Inicializa sistema de rotação"""
        self.api_keys = self._load_api_keys()
        self.current_key_index = 0
        self.key_usage = {}  # Tracking de uso por chave
        self.daily_reset_time = None
        self.max_requests_per_key = 100  # Limite diário por chave
        self.cooldown_period = 3600  # 1 hora de cooldown se limite atingido

        self._initialize_usage_tracking()

        logger.info(f"Google API Rotation inicializado com {len(self.api_keys)} chaves")

    def _load_api_keys(self) -> List[Dict[str, str]]:
        """Carrega chaves de API do Google"""
        api_keys = []

        # Carrega chaves do ambiente - usando nomes corretos das variáveis
        google_keys = [
            {
                'api_key': os.getenv('GOOGLE_SEARCH_KEY'),
                'cx': os.getenv('GOOGLE_CSE_ID'),
                'name': 'primary'
            },
            {
                'api_key': os.getenv('GOOGLE_SEARCH_API_KEY'),
                'cx': os.getenv('GOOGLE_SEARCH_CX'),
                'name': 'secondary'
            },
            {
                'api_key': os.getenv('GOOGLE_API_KEY'),
                'cx': os.getenv('GOOGLE_CX'),
                'name': 'tertiary'
            }
        ]

        # Filtra chaves válidas
        for key_config in google_keys:
            if key_config['api_key'] and key_config['cx']:
                api_keys.append(key_config)
                logger.info(f"✅ Chave Google configurada: {key_config['name']}")

        if not api_keys:
            logger.warning("⚠️ Nenhuma chave Google válida encontrada no ambiente")

        return api_keys

    def _initialize_usage_tracking(self):
        """Inicializa tracking de uso"""
        current_date = datetime.now().date()

        for i, key_config in enumerate(self.api_keys):
            key_name = key_config['name']
            self.key_usage[key_name] = {
                'requests_today': 0,
                'last_request_time': 0,
                'is_blocked': False,
                'block_until': None,
                'last_reset_date': current_date,
                'total_requests': 0,
                'success_rate': 1.0,
                'average_response_time': 0
            }

    def get_current_api_config(self) -> Optional[Dict[str, str]]:
        """Retorna configuração da API atual disponível"""

        if not self.api_keys:
            logger.error("❌ Nenhuma chave de API do Google configurada")
            return None

        # Reseta contadores diários se necessário
        self._reset_daily_counters_if_needed()

        # Procura chave disponível
        attempts = 0
        while attempts < len(self.api_keys):
            current_config = self.api_keys[self.current_key_index]
            key_name = current_config['name']
            usage = self.key_usage[key_name]

            # Verifica se a chave está disponível
            if self._is_key_available(key_name):
                logger.debug(f"✅ Usando chave Google: {key_name}")
                return current_config
            else:
                logger.debug(f"⚠️ Chave {key_name} não disponível, rotacionando...")
                self._rotate_to_next_key()
                attempts += 1

        # Se todas as chaves estão bloqueadas
        logger.error("❌ Todas as chaves do Google estão temporariamente bloqueadas")
        return self._get_least_used_key()

    def _is_key_available(self, key_name: str) -> bool:
        """Verifica se uma chave está disponível"""
        usage = self.key_usage[key_name]
        current_time = time.time()

        # Verifica se está bloqueada temporariamente
        if usage['is_blocked'] and usage['block_until']:
            if current_time < usage['block_until']:
                return False
            else:
                # Remove bloqueio expirado
                usage['is_blocked'] = False
                usage['block_until'] = None

        # Verifica limite diário
        if usage['requests_today'] >= self.max_requests_per_key:
            logger.warning(f"⚠️ Chave {key_name} atingiu limite diário")
            return False

        # Verifica rate limit (1 request por segundo)
        if current_time - usage['last_request_time'] < 1.0:
            return False

        return True

    def _rotate_to_next_key(self):
        """Rotaciona para próxima chave"""
        self.current_key_index = (self.current_key_index + 1) % len(self.api_keys)

    def _get_least_used_key(self) -> Optional[Dict[str, str]]:
        """Retorna a chave menos usada como último recurso"""

        if not self.api_keys:
            return None

        # Encontra chave com menor uso
        min_usage = float('inf')
        least_used_index = 0

        for i, key_config in enumerate(self.api_keys):
            key_name = key_config['name']
            usage = self.key_usage[key_name]['requests_today']

            if usage < min_usage:
                min_usage = usage
                least_used_index = i

        self.current_key_index = least_used_index
        return self.api_keys[least_used_index]

    def record_request(self, key_name: str, success: bool, response_time: float):
        """Registra uso de uma chave"""

        if key_name not in self.key_usage:
            return

        usage = self.key_usage[key_name]
        current_time = time.time()

        # Atualiza contadores
        usage['requests_today'] += 1
        usage['total_requests'] += 1
        usage['last_request_time'] = current_time

        # Atualiza taxa de sucesso
        if success:
            usage['success_rate'] = (usage['success_rate'] * 0.9) + (1.0 * 0.1)
        else:
            usage['success_rate'] = (usage['success_rate'] * 0.9) + (0.0 * 0.1)

        # Atualiza tempo médio de resposta
        usage['average_response_time'] = (usage['average_response_time'] * 0.9) + (response_time * 0.1)

        # Bloqueia temporariamente se muitas falhas
        if usage['success_rate'] < 0.3:
            usage['is_blocked'] = True
            usage['block_until'] = current_time + self.cooldown_period
            logger.warning(f"⚠️ Chave {key_name} bloqueada temporariamente devido a baixa taxa de sucesso")

    def record_rate_limit_hit(self, key_name: str):
        """Registra que uma chave atingiu rate limit"""

        if key_name not in self.key_usage:
            return

        usage = self.key_usage[key_name]
        current_time = time.time()

        # Bloqueia por período maior
        usage['is_blocked'] = True
        usage['block_until'] = current_time + (self.cooldown_period * 2)

        logger.warning(f"⚠️ Chave {key_name} atingiu rate limit - bloqueada por 2 horas")

        # Rotaciona imediatamente
        self._rotate_to_next_key()

    def _reset_daily_counters_if_needed(self):
        """Reseta contadores diários se necessário"""
        current_date = datetime.now().date()

        for key_name, usage in self.key_usage.items():
            if usage['last_reset_date'] < current_date:
                usage['requests_today'] = 0
                usage['last_reset_date'] = current_date
                usage['is_blocked'] = False
                usage['block_until'] = None
                logger.info(f"🔄 Contadores resetados para chave {key_name}")

    def get_usage_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas de uso"""
        stats = {
            'total_keys': len(self.api_keys),
            'current_key': self.api_keys[self.current_key_index]['name'] if self.api_keys else None,
            'keys_status': {}
        }

        for key_config in self.api_keys:
            key_name = key_config['name']
            usage = self.key_usage[key_name]

            stats['keys_status'][key_name] = {
                'requests_today': usage['requests_today'],
                'total_requests': usage['total_requests'],
                'success_rate': round(usage['success_rate'] * 100, 1),
                'average_response_time': round(usage['average_response_time'], 2),
                'is_blocked': usage['is_blocked'],
                'available': self._is_key_available(key_name)
            }

        return stats

    def force_rotate(self):
        """Força rotação para próxima chave"""
        self._rotate_to_next_key()
        logger.info(f"🔄 Rotação forçada para chave: {self.api_keys[self.current_key_index]['name']}")

    def unblock_all_keys(self):
        """Remove bloqueio de todas as chaves (para debug)"""
        for usage in self.key_usage.values():
            usage['is_blocked'] = False
            usage['block_until'] = None

        logger.info("🔓 Todas as chaves desbloqueadas")

    def get_next_api_key(self):
        """Obtém próxima chave da rotação"""
        if not self.api_keys:
            logger.warning("⚠️ Nenhuma chave Google disponível")
            return None, None

        key_data = self.api_keys[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.api_keys)

        return key_data.get('api_key'), key_data.get('search_engine_id')

    def get_next_api_keys(self):
        """Método compatível com código existente"""
        return self.get_next_api_key()
    
    def is_google_api_available(self) -> bool:
        """Verifica se há chaves do Google API disponíveis"""
        return len(self.api_keys) > 0

# Instância global
google_api_rotation = GoogleAPIRotation()