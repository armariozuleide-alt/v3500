#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Production Content Extractor
Extrator de conteúdo robusto com Jina Reader Fallback System
"""

import logging
import requests
import trafilatura
import time
from typing import Optional, Dict, Any, List
from urllib.parse import urlparse, urljoin

logger = logging.getLogger(__name__)

class ProductionContentExtractor:
    """Extrator de conteúdo robusto com sistema de fallback Jina Reader"""

    def __init__(self):
        """Inicializa extrator de produção"""
        self.strategies = [
            'jina_reader',      # Novo: Jina Reader como primeira opção
            'trafilatura',
            'mercury_parser',   # Novo: Mercury Parser API
            'requests_html',
            'beautiful_soup',
            'simple_requests'
        ]
        self.timeout = 30
        self.jina_base_url = "https://r.jina.ai/"
        self.mercury_api_key = None  # Configurar se disponível
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        ]

        logger.info("Production Content Extractor inicializado com Jina Reader Fallback System")

    def extract_content(self, url: str, strategy_preference: Optional[str] = None) -> Optional[str]:
        """Extrai conteúdo usando múltiplas estratégias com fallback inteligente"""

        # Se uma estratégia específica foi solicitada, tenta ela primeiro
        if strategy_preference and strategy_preference in self.strategies:
            try:
                content = self._execute_strategy(strategy_preference, url)
                if content and len(content.strip()) > 100:  # Conteúdo válido
                    logger.info(f"✅ Estratégia preferida '{strategy_preference}' bem-sucedida")
                    return content
            except Exception as e:
                logger.warning(f"⚠️ Estratégia preferida '{strategy_preference}' falhou: {e}")

        # Executa todas as estratégias em ordem de prioridade
        for strategy in self.strategies:
            try:
                content = self._execute_strategy(strategy, url)
                if content and len(content.strip()) > 100:  # Validação básica
                    logger.info(f"✅ Estratégia '{strategy}' bem-sucedida para {url}")
                    return content

            except Exception as e:
                logger.warning(f"⚠️ Estratégia '{strategy}' falhou para {url}: {e}")
                continue

        logger.error(f"❌ TODAS as estratégias falharam para {url}")
        return None

    def _execute_strategy(self, strategy: str, url: str) -> Optional[str]:
        """Executa estratégia específica"""

        if strategy == 'jina_reader':
            return self._extract_with_jina_reader(url)
        elif strategy == 'trafilatura':
            return self._extract_with_trafilatura(url)
        elif strategy == 'mercury_parser':
            return self._extract_with_mercury_parser(url)
        elif strategy == 'requests_html':
            return self._extract_with_requests_html(url)
        elif strategy == 'beautiful_soup':
            return self._extract_with_bs4(url)
        elif strategy == 'simple_requests':
            return self._extract_with_simple_requests(url)
        else:
            logger.error(f"❌ Estratégia desconhecida: {strategy}")
            return None

    def _extract_with_jina_reader(self, url: str) -> Optional[str]:
        """Extrai usando Jina Reader API"""
        try:
            # Jina Reader API endpoint
            jina_url = f"{self.jina_base_url}{url}"

            headers = {
                'User-Agent': self._get_random_user_agent(),
                'Accept': 'text/plain, application/json',
                'X-Return-Format': 'text'  # Solicita texto limpo
            }

            response = requests.get(
                jina_url,
                headers=headers,
                timeout=self.timeout,
                allow_redirects=True
            )

            if response.status_code == 200:
                content = response.text.strip()
                if len(content) > 100:  # Validação básica
                    logger.debug(f"✅ Jina Reader extraiu {len(content)} caracteres")
                    return content
                else:
                    logger.warning("⚠️ Jina Reader retornou conteúdo muito curto")
                    return None
            else:
                logger.error(f"❌ Jina Reader erro: {response.status_code}")
                return None

        except Exception as e:
            logger.error(f"❌ Jina Reader falhou: {e}")
            return None

    def _extract_with_trafilatura(self, url: str) -> Optional[str]:
        """Extrai usando Trafilatura (fallback principal)"""
        try:
            # Configurações otimizadas para Trafilatura
            downloaded = trafilatura.fetch_url(
                url,
                no_ssl=False,
                include_comments=False,
                include_tables=True,
                include_formatting=False
            )

            if downloaded:
                extracted = trafilatura.extract(
                    downloaded,
                    include_comments=False,
                    include_tables=True,
                    include_formatting=False,
                    output_format='txt'
                )

                if extracted and len(extracted.strip()) > 100:
                    logger.debug(f"✅ Trafilatura extraiu {len(extracted)} caracteres")
                    return extracted

        except Exception as e:
            logger.error(f"❌ Trafilatura falhou: {e}")

        return None

    def _extract_with_mercury_parser(self, url: str) -> Optional[str]:
        """Extrai usando Mercury Parser API (se disponível)"""
        try:
            # Mercury Parser API (requer configuração)
            if not self.mercury_api_key:
                logger.debug("Mercury Parser API key não configurada")
                return None

            mercury_url = "https://mercury.postlight.com/parser"
            headers = {
                'X-API-KEY': self.mercury_api_key,
                'Content-Type': 'application/json'
            }

            params = {'url': url}

            response = requests.get(
                mercury_url,
                headers=headers,
                params=params,
                timeout=self.timeout
            )

            if response.status_code == 200:
                data = response.json()
                content = data.get('content', '')

                # Remove HTML tags básicos
                import re
                clean_content = re.sub(r'<[^>]+>', '', content)

                if len(clean_content.strip()) > 100:
                    logger.debug(f"✅ Mercury Parser extraiu {len(clean_content)} caracteres")
                    return clean_content

        except Exception as e:
            logger.error(f"❌ Mercury Parser falhou: {e}")

        return None

    def _extract_with_requests_html(self, url: str) -> Optional[str]:
        """Extrai usando requests com parsing HTML aprimorado"""
        try:
            headers = {
                'User-Agent': self._get_random_user_agent(),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }

            response = requests.get(
                url,
                headers=headers,
                timeout=self.timeout,
                allow_redirects=True
            )

            if response.status_code == 200:
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')

                # Remove scripts e styles
                for script in soup(["script", "style", "nav", "footer", "header"]):
                    script.decompose()

                # Busca conteúdo principal
                main_content = soup.find('main') or soup.find('article') or soup.find('div', class_=lambda x: x and 'content' in x.lower())

                if main_content:
                    text = main_content.get_text()
                else:
                    text = soup.get_text()

                # Limpa texto
                lines = (line.strip() for line in text.splitlines())
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                clean_text = ' '.join(chunk for chunk in chunks if chunk)

                if len(clean_text) > 100:
                    # Limita tamanho para evitar overflow
                    return clean_text[:15000]

        except Exception as e:
            logger.error(f"❌ Requests HTML falhou: {e}")

        return None

    def _extract_with_bs4(self, url: str) -> Optional[str]:
        """Extrai usando BeautifulSoup básico"""
        try:
            response = requests.get(
                url,
                timeout=self.timeout,
                headers={'User-Agent': self._get_random_user_agent()}
            )

            if response.status_code == 200:
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')
                text = soup.get_text()

                # Limpeza básica
                clean_text = ' '.join(text.split())

                if len(clean_text) > 100:
                    return clean_text[:10000]  # Limita tamanho

        except Exception as e:
            logger.error(f"❌ BeautifulSoup falhou: {e}")

        return None

    def _extract_with_simple_requests(self, url: str) -> Optional[str]:
        """Extrai usando requests simples (último recurso)"""
        try:
            response = requests.get(
                url,
                timeout=self.timeout,
                headers={'User-Agent': self._get_random_user_agent()}
            )

            if response.status_code == 200:
                # Retorna HTML bruto limitado
                content = response.text[:20000]

                if len(content) > 100:
                    return content

        except Exception as e:
            logger.error(f"❌ Simple requests falhou: {e}")

        return None

    def _get_random_user_agent(self) -> str:
        """Retorna user agent aleatório"""
        import random
        return random.choice(self.user_agents)

    def test_all_strategies(self, url: str) -> Dict[str, Any]:
        """Testa todas as estratégias para debugging"""

        results = {}

        for strategy in self.strategies:
            try:
                start_time = time.time()
                content = self._execute_strategy(strategy, url)
                execution_time = time.time() - start_time

                results[strategy] = {
                    'success': bool(content and len(content.strip()) > 100),
                    'content_length': len(content) if content else 0,
                    'execution_time': round(execution_time, 2),
                    'preview': content[:200] + '...' if content and len(content) > 200 else content
                }

            except Exception as e:
                results[strategy] = {
                    'success': False,
                    'error': str(e),
                    'execution_time': 0
                }

        return results

    def get_status(self) -> Dict[str, Any]:
        """Retorna status do extrator"""
        return {
            'strategies_available': self.strategies,
            'jina_reader_url': self.jina_base_url,
            'mercury_api_configured': bool(self.mercury_api_key),
            'timeout': self.timeout,
            'user_agents_count': len(self.user_agents)
        }

# Instância global
production_content_extractor = ProductionContentExtractor()