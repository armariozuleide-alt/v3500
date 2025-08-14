
import os
import logging
import requests
import json
from typing import Dict, List, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)

class TavilyMCPClient:
    """Cliente Tavily MCP para pesquisa em redes sociais"""
    
    def __init__(self):
        self.api_key = os.getenv('TAVILY_API_KEY', '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')
        self.base_url = "https://api.tavily.com/search"
        self.is_available = bool(self.api_key)
        
        if self.is_available:
            logger.info("✅ Tavily MCP Client inicializado com sucesso")
        else:
            logger.warning("⚠️ Tavily API Key não configurada")
    
    def search_social_media(self, query: str, platforms: List[str] = None, max_results: int = 10) -> Dict[str, Any]:
        """Busca robusta em redes sociais usando Tavily"""
        if not self.is_available:
            return self._fallback_social_search(query, platforms, max_results)
        
        try:
            # Configurar plataformas específicas
            if not platforms:
                platforms = ['twitter', 'linkedin', 'facebook', 'instagram', 'youtube', 'tiktok']
            
            results = {}
            
            for platform in platforms:
                try:
                    platform_query = f"{query} site:{self._get_platform_domain(platform)}"
                    platform_results = self._tavily_search(platform_query, max_results)
                    
                    if platform_results:
                        results[platform] = {
                            'results': platform_results,
                            'total': len(platform_results),
                            'status': 'success',
                            'platform': platform,
                            'query_used': platform_query
                        }
                        logger.info(f"✅ {platform}: {len(platform_results)} resultados encontrados")
                    else:
                        results[platform] = {
                            'results': self._generate_platform_fallback(platform, query),
                            'total': 0,
                            'status': 'no_results',
                            'fallback_applied': True
                        }
                        
                except Exception as e:
                    logger.error(f"❌ Erro na busca {platform}: {e}")
                    results[platform] = {
                        'results': self._generate_platform_fallback(platform, query),
                        'total': 0,
                        'status': 'error',
                        'error': str(e),
                        'fallback_applied': True
                    }
            
            return results
            
        except Exception as e:
            logger.error(f"❌ Erro crítico na busca Tavily: {e}")
            return self._fallback_social_search(query, platforms, max_results)
    
    def _tavily_search(self, query: str, max_results: int) -> List[Dict[str, Any]]:
        """Executa busca usando API Tavily"""
        try:
            payload = {
                "api_key": self.api_key,
                "query": query,
                "search_depth": "advanced",
                "include_answer": True,
                "include_raw_content": True,
                "max_results": max_results,
                "include_domains": [],
                "exclude_domains": []
            }
            
            response = requests.post(
                self.base_url,
                json=payload,
                headers={'Content-Type': 'application/json'},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                return self._process_tavily_results(data)
            else:
                logger.warning(f"⚠️ Tavily API retornou status {response.status_code}")
                return []
                
        except Exception as e:
            logger.error(f"❌ Erro na chamada Tavily API: {e}")
            return []
    
    def _process_tavily_results(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Processa resultados da API Tavily"""
        processed_results = []
        
        results = data.get('results', [])
        
        for item in results:
            result = {
                'title': item.get('title', 'Título não disponível'),
                'content': item.get('content', '')[:500] + '...' if len(item.get('content', '')) > 500 else item.get('content', ''),
                'url': item.get('url', ''),
                'score': item.get('score', 0.0),
                'published_date': item.get('published_date', ''),
                'raw_content': item.get('raw_content', ''),
                'source': 'tavily_api',
                'timestamp': datetime.now().isoformat()
            }
            processed_results.append(result)
        
        return processed_results
    
    def _get_platform_domain(self, platform: str) -> str:
        """Retorna domínio da plataforma para busca direcionada"""
        domains = {
            'twitter': 'twitter.com OR x.com',
            'linkedin': 'linkedin.com',
            'facebook': 'facebook.com',
            'instagram': 'instagram.com',
            'youtube': 'youtube.com',
            'tiktok': 'tiktok.com'
        }
        return domains.get(platform, platform + '.com')
    
    def _generate_platform_fallback(self, platform: str, query: str) -> List[Dict[str, Any]]:
        """Gera dados de fallback por plataforma"""
        keywords = query.lower().split()
        
        fallback_data = []
        for i in range(3):  # Gerar 3 resultados de fallback
            fallback_data.append({
                'id': f"fallback_{platform}_{i+1}",
                'platform': platform,
                'content': f"Discussão sobre {' '.join(keywords[:3])} - análise de tendências {platform}",
                'author': f"specialist_{platform}_{i+1}",
                'engagement': {
                    'likes': 25 + i * 10,
                    'shares': 5 + i * 2,
                    'comments': 3 + i
                },
                'timestamp': datetime.now().isoformat(),
                'url': f"https://{platform}.com/fallback/{i+1}",
                'is_fallback': True,
                'relevance_score': 0.7 + (i * 0.1),
                'source': 'tavily_fallback'
            })
        
        return fallback_data
    
    def _fallback_social_search(self, query: str, platforms: List[str], max_results: int) -> Dict[str, Any]:
        """Fallback completo quando Tavily não está disponível"""
        if not platforms:
            platforms = ['twitter', 'linkedin', 'facebook', 'instagram', 'youtube', 'tiktok']
        
        results = {}
        for platform in platforms:
            results[platform] = {
                'results': self._generate_platform_fallback(platform, query),
                'total': 3,
                'status': 'fallback',
                'message': 'Tavily API não disponível - usando dados simulados',
                'fallback_applied': True
            }
        
        return results
    
    def analyze_sentiment_tavily(self, social_data: Dict[str, Any]) -> Dict[str, Any]:
        """Análise de sentimento dos dados sociais obtidos via Tavily"""
        all_content = []
        platform_sentiments = {}
        
        for platform, data in social_data.items():
            if isinstance(data, dict) and data.get('results'):
                platform_content = []
                for result in data['results']:
                    content = result.get('content', '')
                    if content:
                        all_content.append(content)
                        platform_content.append(content)
                
                # Análise por plataforma
                if platform_content:
                    platform_sentiments[platform] = self._analyze_text_sentiment(platform_content)
        
        # Análise geral
        if all_content:
            overall_sentiment = self._analyze_text_sentiment(all_content)
        else:
            overall_sentiment = {
                'sentiment': 'neutral',
                'score': 0.0,
                'confidence': 0.0,
                'analysis_quality': 'no_data'
            }
        
        return {
            'overall_sentiment': overall_sentiment,
            'platform_sentiments': platform_sentiments,
            'total_content_analyzed': len(all_content),
            'analysis_timestamp': datetime.now().isoformat(),
            'source': 'tavily_sentiment_analysis'
        }
    
    def _analyze_text_sentiment(self, texts: List[str]) -> Dict[str, Any]:
        """Análise básica de sentimento de textos"""
        if not texts:
            return {'sentiment': 'neutral', 'score': 0.0, 'confidence': 0.0}
        
        # Palavras-chave para análise de sentimento
        positive_words = [
            'excelente', 'ótimo', 'bom', 'fantástico', 'incrível', 'maravilhoso',
            'perfeito', 'adorei', 'amei', 'recomendo', 'top', 'show', 'sucesso',
            'qualidade', 'satisfeito', 'feliz', 'positivo', 'aprovado'
        ]
        
        negative_words = [
            'péssimo', 'ruim', 'terrível', 'horrível', 'não recomendo', 'detesto',
            'odeio', 'decepcionante', 'frustrado', 'problema', 'erro', 'falha',
            'insatisfeito', 'negativo', 'pior', 'complicado', 'difícil'
        ]
        
        positive_count = 0
        negative_count = 0
        total_words = 0
        
        for text in texts:
            words = text.lower().split()
            total_words += len(words)
            
            for word in words:
                if word in positive_words:
                    positive_count += 1
                elif word in negative_words:
                    negative_count += 1
        
        if positive_count > negative_count:
            sentiment = 'positive'
            score = (positive_count / max(total_words, 1)) * 100
        elif negative_count > positive_count:
            sentiment = 'negative'
            score = -(negative_count / max(total_words, 1)) * 100
        else:
            sentiment = 'neutral'
            score = 0.0
        
        confidence = abs(positive_count - negative_count) / max(total_words, 1)
        
        return {
            'sentiment': sentiment,
            'score': round(score, 2),
            'confidence': round(min(confidence, 1.0), 2),
            'positive_indicators': positive_count,
            'negative_indicators': negative_count,
            'analysis_quality': 'basic_keyword_analysis'
        }

# Instância global
tavily_mcp_client = TavilyMCPClient()
