
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Strategic Keywords Analyzer
Analisador de palavras-chave estratégicas
"""

import logging
import time
from datetime import datetime
from typing import Dict, List, Optional, Any

logger = logging.getLogger(__name__)

class StrategicKeywordsAnalyzer:
    """Analisador de Palavras-Chave Estratégicas"""

    def __init__(self):
        """Inicializa o analisador de keywords"""
        logger.info("🔤 Strategic Keywords Analyzer inicializado")

    def analyze_keywords(self, avatar_data: Dict[str, Any], research_data: Dict[str, Any], data: Dict[str, Any]) -> Dict[str, Any]:
        """Analisa palavras-chave estratégicas"""
        try:
            segmento = data.get('segmento', '')
            produto = data.get('produto', '')
            
            # Extrai palavras do conteúdo pesquisado
            content_keywords = self._extract_keywords_from_content(research_data)
            
            keywords_analysis = {
                "palavras_chave_primarias": [
                    {
                        "keyword": f"{produto}",
                        "volume_estimado": 5000,
                        "competicao": "Alta",
                        "intencao": "Comercial",
                        "prioridade": "Alta"
                    },
                    {
                        "keyword": f"{segmento}",
                        "volume_estimado": 8000,
                        "competicao": "Média",
                        "intencao": "Informacional",
                        "prioridade": "Alta"
                    }
                ],
                "palavras_chave_secundarias": [
                    {
                        "keyword": f"como {produto}",
                        "volume_estimado": 2000,
                        "competicao": "Baixa",
                        "intencao": "Informacional",
                        "prioridade": "Média"
                    },
                    {
                        "keyword": f"melhor {produto}",
                        "volume_estimado": 1500,
                        "competicao": "Média",
                        "intencao": "Comercial",
                        "prioridade": "Média"
                    }
                ],
                "palavras_chave_long_tail": [
                    {
                        "keyword": f"como escolher {produto} para {segmento}",
                        "volume_estimado": 500,
                        "competicao": "Baixa",
                        "intencao": "Informacional",
                        "prioridade": "Baixa"
                    }
                ],
                "oportunidades_seo": [
                    f"Criar conteúdo sobre '{produto} para {segmento}'",
                    f"Otimizar para 'como implementar {produto}'",
                    f"Focar em 'benefícios do {produto}'"
                ],
                "estrategia_conteudo": {
                    "blog_posts": [
                        f"Guia completo de {produto}",
                        f"10 dicas para {segmento}",
                        f"Como escolher o melhor {produto}"
                    ],
                    "videos": [
                        f"Tutorial: {produto} passo a passo",
                        f"Depoimentos de clientes {segmento}"
                    ],
                    "infograficos": [
                        f"Estatísticas do mercado {segmento}",
                        f"Comparativo de {produto}"
                    ]
                },
                "keywords_extraidas": content_keywords,
                "metadata": {
                    "generated_at": datetime.utcnow().isoformat(),
                    "fallback_mode": False,
                    "total_keywords": len(content_keywords)
                }
            }

            return keywords_analysis

        except Exception as e:
            logger.error(f"❌ Erro na análise de keywords: {e}")
            return {
                "error": f"Falha na análise de keywords: {str(e)}",
                "palavras_chave_primarias": [],
                "metadata": {
                    "generated_at": datetime.utcnow().isoformat(),
                    "fallback_mode": True
                }
            }

    def _extract_keywords_from_content(self, research_data: Dict[str, Any]) -> List[str]:
        """Extrai palavras-chave do conteúdo pesquisado"""
        try:
            keywords = []
            
            if isinstance(research_data, dict) and 'extracted_content' in research_data:
                extracted_content = research_data['extracted_content']
                if isinstance(extracted_content, list):
                    for content_item in extracted_content[:5]:  # Primeiros 5 itens
                        if isinstance(content_item, dict):
                            content = content_item.get('content', '')
                            title = content_item.get('title', '')
                            
                            # Extrai palavras importantes
                            text = f"{title} {content}".lower()
                            words = text.split()
                            
                            # Filtra palavras relevantes (mais de 3 caracteres)
                            relevant_words = [w for w in words if len(w) > 3 and w.isalpha()]
                            keywords.extend(relevant_words[:10])  # Top 10 por item
            
            # Remove duplicatas e retorna top 20
            unique_keywords = list(set(keywords))
            return unique_keywords[:20]
            
        except Exception as e:
            logger.warning(f"⚠️ Erro ao extrair keywords: {e}")
            return ["marketing", "vendas", "negócio", "estratégia", "crescimento"]

# Instância global
strategic_keywords_analyzer = StrategicKeywordsAnalyzer()
