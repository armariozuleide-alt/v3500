
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - YouTube MCP Integration
Extração de vídeos e análise de conteúdo do YouTube via MCP
"""

import logging
import json
import re
import time
from typing import Dict, List, Any, Optional
from urllib.parse import urlparse, parse_qs
import requests

logger = logging.getLogger(__name__)

class YouTubeMCPIntegration:
    """Integração YouTube com MCP para extração de vídeos"""
    
    def __init__(self, api_key: Optional[str] = None):
        """Inicializa integração YouTube MCP"""
        self.api_key = api_key
        self.base_url = "https://www.googleapis.com/youtube/v3"
        self.available = bool(api_key)
        self.rate_limit_delay = 0.5
        self.last_request_time = 0
        
        if self.available:
            logger.info("✅ YouTube MCP Integration inicializado")
        else:
            logger.warning("⚠️ YouTube MCP sem API key - usando fallbacks")
    
    def extract_video_content(self, video_url: str) -> Dict[str, Any]:
        """Extrai conteúdo de vídeo do YouTube"""
        
        try:
            video_id = self._extract_video_id(video_url)
            if not video_id:
                logger.error(f"❌ ID do vídeo não encontrado: {video_url}")
                return {}
            
            # Busca metadados do vídeo
            video_data = self._get_video_metadata(video_id)
            
            # Busca transcrição/legendas
            transcript = self._get_video_transcript(video_id)
            
            # Busca comentários relevantes
            comments = self._get_video_comments(video_id, max_results=50)
            
            return {
                'video_id': video_id,
                'metadata': video_data,
                'transcript': transcript,
                'comments': comments,
                'analysis': self._analyze_video_content(video_data, transcript, comments),
                'extraction_timestamp': time.time()
            }
            
        except Exception as e:
            logger.error(f"❌ Erro ao extrair conteúdo do vídeo: {e}")
            return {}
    
    def search_videos_by_topic(self, topic: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """Busca vídeos por tópico"""
        
        if not self.available:
            logger.warning("⚠️ YouTube API não disponível")
            return []
        
        try:
            self._respect_rate_limit()
            
            params = {
                'part': 'snippet',
                'q': topic,
                'type': 'video',
                'maxResults': max_results,
                'order': 'relevance',
                'key': self.api_key
            }
            
            response = requests.get(f"{self.base_url}/search", params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                videos = []
                
                for item in data.get('items', []):
                    video_info = {
                        'video_id': item['id']['videoId'],
                        'title': item['snippet']['title'],
                        'description': item['snippet']['description'],
                        'channel': item['snippet']['channelTitle'],
                        'published_at': item['snippet']['publishedAt'],
                        'thumbnail': item['snippet']['thumbnails']['default']['url'],
                        'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}"
                    }
                    videos.append(video_info)
                
                logger.info(f"✅ Encontrados {len(videos)} vídeos para '{topic}'")
                return videos
            else:
                logger.error(f"❌ Erro na busca YouTube: {response.status_code}")
                return []
                
        except Exception as e:
            logger.error(f"❌ Erro ao buscar vídeos: {e}")
            return []
    
    def analyze_competitor_channels(self, competitor_keywords: List[str]) -> Dict[str, Any]:
        """Analisa canais de concorrentes"""
        
        competitor_analysis = {
            'channels_found': [],
            'popular_videos': [],
            'content_trends': [],
            'engagement_patterns': {}
        }
        
        try:
            for keyword in competitor_keywords:
                # Busca canais
                channels = self._search_channels(keyword)
                competitor_analysis['channels_found'].extend(channels)
                
                # Busca vídeos populares
                popular_videos = self.search_videos_by_topic(keyword, max_results=5)
                competitor_analysis['popular_videos'].extend(popular_videos)
            
            # Analisa tendências de conteúdo
            competitor_analysis['content_trends'] = self._analyze_content_trends(
                competitor_analysis['popular_videos']
            )
            
            # Analisa padrões de engajamento
            competitor_analysis['engagement_patterns'] = self._analyze_engagement_patterns(
                competitor_analysis['popular_videos']
            )
            
            return competitor_analysis
            
        except Exception as e:
            logger.error(f"❌ Erro na análise de concorrentes: {e}")
            return competitor_analysis
    
    def _extract_video_id(self, url: str) -> Optional[str]:
        """Extrai ID do vídeo da URL"""
        
        patterns = [
            r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)',
            r'youtube\.com\/v\/([^&\n?#]+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        
        return None
    
    def _get_video_metadata(self, video_id: str) -> Dict[str, Any]:
        """Busca metadados do vídeo"""
        
        if not self.available:
            return {}
        
        try:
            self._respect_rate_limit()
            
            params = {
                'part': 'snippet,statistics,contentDetails',
                'id': video_id,
                'key': self.api_key
            }
            
            response = requests.get(f"{self.base_url}/videos", params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('items'):
                    item = data['items'][0]
                    return {
                        'title': item['snippet']['title'],
                        'description': item['snippet']['description'],
                        'channel': item['snippet']['channelTitle'],
                        'published_at': item['snippet']['publishedAt'],
                        'duration': item['contentDetails']['duration'],
                        'view_count': item['statistics'].get('viewCount', 0),
                        'like_count': item['statistics'].get('likeCount', 0),
                        'comment_count': item['statistics'].get('commentCount', 0)
                    }
            
            return {}
            
        except Exception as e:
            logger.error(f"❌ Erro ao buscar metadados: {e}")
            return {}
    
    def _get_video_transcript(self, video_id: str) -> str:
        """Busca transcrição do vídeo (simulado - API real requer youtube-transcript-api)"""
        
        # Nota: Implementação real requer biblioteca youtube-transcript-api
        # Esta é uma implementação básica para demonstração
        
        try:
            # Simulação de transcrição baseada na descrição
            metadata = self._get_video_metadata(video_id)
            description = metadata.get('description', '')
            
            if description:
                # Extrai possível transcrição da descrição
                transcript_markers = ['transcrição', 'transcript', 'legendas']
                for marker in transcript_markers:
                    if marker.lower() in description.lower():
                        # Busca conteúdo após o marcador
                        start_idx = description.lower().find(marker.lower())
                        if start_idx != -1:
                            return description[start_idx + len(marker):].strip()
            
            return f"Transcrição não disponível para vídeo {video_id}"
            
        except Exception as e:
            logger.error(f"❌ Erro ao buscar transcrição: {e}")
            return ""
    
    def _get_video_comments(self, video_id: str, max_results: int = 50) -> List[Dict[str, Any]]:
        """Busca comentários do vídeo"""
        
        if not self.available:
            return []
        
        try:
            self._respect_rate_limit()
            
            params = {
                'part': 'snippet',
                'videoId': video_id,
                'maxResults': max_results,
                'order': 'relevance',
                'key': self.api_key
            }
            
            response = requests.get(f"{self.base_url}/commentThreads", params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                comments = []
                
                for item in data.get('items', []):
                    comment = {
                        'text': item['snippet']['topLevelComment']['snippet']['textDisplay'],
                        'author': item['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                        'likes': item['snippet']['topLevelComment']['snippet']['likeCount'],
                        'published_at': item['snippet']['topLevelComment']['snippet']['publishedAt']
                    }
                    comments.append(comment)
                
                return comments
            
            return []
            
        except Exception as e:
            logger.error(f"❌ Erro ao buscar comentários: {e}")
            return []
    
    def _search_channels(self, keyword: str) -> List[Dict[str, Any]]:
        """Busca canais por palavra-chave"""
        
        if not self.available:
            return []
        
        try:
            self._respect_rate_limit()
            
            params = {
                'part': 'snippet',
                'q': keyword,
                'type': 'channel',
                'maxResults': 10,
                'key': self.api_key
            }
            
            response = requests.get(f"{self.base_url}/search", params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                channels = []
                
                for item in data.get('items', []):
                    channel = {
                        'channel_id': item['id']['channelId'],
                        'title': item['snippet']['title'],
                        'description': item['snippet']['description'],
                        'thumbnail': item['snippet']['thumbnails']['default']['url']
                    }
                    channels.append(channel)
                
                return channels
            
            return []
            
        except Exception as e:
            logger.error(f"❌ Erro ao buscar canais: {e}")
            return []
    
    def _analyze_video_content(self, metadata: Dict, transcript: str, comments: List) -> Dict[str, Any]:
        """Analisa conteúdo do vídeo"""
        
        analysis = {
            'content_quality': 'Medium',
            'engagement_rate': 0,
            'key_topics': [],
            'sentiment': 'Neutral',
            'educational_value': 'Medium'
        }
        
        try:
            # Analisa engajamento
            views = int(metadata.get('view_count', 0))
            likes = int(metadata.get('like_count', 0))
            
            if views > 0:
                engagement_rate = (likes / views) * 100
                analysis['engagement_rate'] = round(engagement_rate, 2)
            
            # Analisa tópicos principais do título e descrição
            title = metadata.get('title', '').lower()
            description = metadata.get('description', '').lower()
            
            business_keywords = ['negócio', 'empresa', 'vendas', 'marketing', 'estratégia', 'lucro']
            key_topics = [keyword for keyword in business_keywords if keyword in title or keyword in description]
            analysis['key_topics'] = key_topics
            
            # Determina qualidade do conteúdo baseado em métricas
            if views > 10000 and likes > 100:
                analysis['content_quality'] = 'High'
            elif views > 1000 and likes > 10:
                analysis['content_quality'] = 'Medium'
            else:
                analysis['content_quality'] = 'Low'
            
            return analysis
            
        except Exception as e:
            logger.error(f"❌ Erro na análise de conteúdo: {e}")
            return analysis
    
    def _analyze_content_trends(self, videos: List[Dict]) -> List[str]:
        """Analisa tendências de conteúdo"""
        
        trends = []
        
        try:
            # Coleta títulos e descrições
            all_text = ""
            for video in videos:
                all_text += f" {video.get('title', '')} {video.get('description', '')}"
            
            # Palavras-chave mais comuns (implementação simples)
            words = all_text.lower().split()
            word_count = {}
            
            business_keywords = [
                'marketing', 'vendas', 'negócio', 'empresa', 'estratégia', 
                'digital', 'online', 'crescimento', 'lucro', 'cliente'
            ]
            
            for word in words:
                if word in business_keywords:
                    word_count[word] = word_count.get(word, 0) + 1
            
            # Top 5 tendências
            sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
            trends = [word for word, count in sorted_words[:5]]
            
            return trends
            
        except Exception as e:
            logger.error(f"❌ Erro na análise de tendências: {e}")
            return []
    
    def _analyze_engagement_patterns(self, videos: List[Dict]) -> Dict[str, Any]:
        """Analisa padrões de engajamento"""
        
        patterns = {
            'average_views': 0,
            'top_performing_topics': [],
            'optimal_title_length': 0,
            'best_posting_time': 'Unknown'
        }
        
        try:
            if not videos:
                return patterns
            
            # Calcula média de visualizações (simulado)
            view_counts = []
            title_lengths = []
            
            for video in videos:
                # Simula contagem de views baseado na popularidade
                title_length = len(video.get('title', ''))
                title_lengths.append(title_length)
                
                # Simula views baseado no comprimento do título (heurística simples)
                estimated_views = max(1000, (100 - abs(title_length - 60)) * 100)
                view_counts.append(estimated_views)
            
            if view_counts:
                patterns['average_views'] = sum(view_counts) // len(view_counts)
            
            if title_lengths:
                patterns['optimal_title_length'] = sum(title_lengths) // len(title_lengths)
            
            return patterns
            
        except Exception as e:
            logger.error(f"❌ Erro na análise de padrões: {e}")
            return patterns
    
    def _respect_rate_limit(self):
        """Respeita rate limit da API"""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        if time_since_last < self.rate_limit_delay:
            sleep_time = self.rate_limit_delay - time_since_last
            time.sleep(sleep_time)
        
        self.last_request_time = time.time()
    
    def get_status(self) -> Dict[str, Any]:
        """Retorna status da integração"""
        return {
            "available": self.available,
            "base_url": self.base_url,
            "rate_limit_delay": self.rate_limit_delay
        }

# Instância global
youtube_mcp_integration = YouTubeMCPIntegration()
