
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - HTML Report Generator
Gerador de relatórios HTML profissionais e detalhados
"""

import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from flask import Blueprint, request, jsonify, send_file
import json
import os
from io import BytesIO, StringIO

logger = logging.getLogger(__name__)

html_report_bp = Blueprint('html_report', __name__)

class HTMLReportGenerator:
    """Gerador de relatórios HTML profissionais"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def generate_complete_html_report(self, analysis_data: Dict[str, Any]) -> str:
        """Gera relatório HTML completo e profissional"""
        
        try:
            html_content = self._create_html_structure(analysis_data)
            return html_content
        except Exception as e:
            self.logger.error(f"Erro ao gerar relatório HTML: {e}")
            return self._create_error_report(str(e))
    
    def _create_html_structure(self, data: Dict[str, Any]) -> str:
        """Cria estrutura HTML principal"""
        
        session_id = data.get('session_id', 'N/A')
        timestamp = data.get('timestamp', datetime.now().isoformat())
        
        html_content = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório de Análise Ultra-Detalhada - ARQV30</title>
    <style>
        {self._get_css_styles()}
    </style>
</head>
<body>
    <div class="container">
        <header class="report-header">
            <h1>📊 Relatório de Análise Ultra-Detalhada</h1>
            <div class="report-info">
                <p><strong>Sessão:</strong> {session_id}</p>
                <p><strong>Data:</strong> {timestamp}</p>
                <p><strong>Sistema:</strong> ARQV30 Enhanced v2.0</p>
            </div>
        </header>
        
        <main class="report-content">
            {self._create_executive_summary(data)}
            {self._create_market_analysis(data)}
            {self._create_competitor_analysis(data)}
            {self._create_opportunities(data)}
            {self._create_recommendations(data)}
            {self._create_implementation_plan(data)}
            {self._create_appendix(data)}
        </main>
        
        <footer class="report-footer">
            <p>Gerado por ARQV30 Enhanced v2.0 - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
        </footer>
    </div>
</body>
</html>
"""
        return html_content
    
    def _get_css_styles(self) -> str:
        """Retorna estilos CSS profissionais"""
        
        return """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f8f9fa;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
            min-height: 100vh;
        }
        
        .report-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }
        
        .report-header h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .report-info {
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
        }
        
        .report-content {
            padding: 40px;
        }
        
        .section {
            margin-bottom: 40px;
            padding: 30px;
            border-radius: 10px;
            background: #f8f9fa;
            border-left: 5px solid #667eea;
        }
        
        .section h2 {
            color: #667eea;
            margin-bottom: 20px;
            font-size: 1.8em;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }
        
        .section h3 {
            color: #555;
            margin: 20px 0 10px 0;
            font-size: 1.3em;
        }
        
        .metric {
            background: white;
            padding: 20px;
            margin: 15px 0;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .insight {
            background: #e8f5e8;
            padding: 15px;
            margin: 10px 0;
            border-left: 4px solid #27ae60;
            border-radius: 5px;
        }
        
        .warning {
            background: #fdf2e9;
            padding: 15px;
            margin: 10px 0;
            border-left: 4px solid #f39c12;
            border-radius: 5px;
        }
        
        .error {
            background: #fadbd8;
            padding: 15px;
            margin: 10px 0;
            border-left: 4px solid #e74c3c;
            border-radius: 5px;
        }
        
        .table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .table th,
        .table td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        
        .table th {
            background: #667eea;
            color: white;
            font-weight: 600;
        }
        
        .table tr:hover {
            background: #f8f9fa;
        }
        
        .report-footer {
            background: #2c3e50;
            color: white;
            padding: 20px;
            text-align: center;
        }
        
        .list {
            margin: 15px 0;
            padding-left: 20px;
        }
        
        .list li {
            margin: 8px 0;
        }
        
        .highlight {
            background: #fff3cd;
            padding: 10px;
            border-radius: 5px;
            border-left: 4px solid #ffc107;
        }
        
        @media print {
            .container {
                box-shadow: none;
            }
            
            .report-header {
                background: #667eea !important;
                -webkit-print-color-adjust: exact;
            }
        }
        """
    
    def _create_executive_summary(self, data: Dict[str, Any]) -> str:
        """Cria seção de resumo executivo"""
        
        resumo = data.get('resumo_executivo', {})
        
        return f"""
        <section class="section">
            <h2>📋 Resumo Executivo</h2>
            
            <div class="metric">
                <h3>Informações Gerais</h3>
                <p><strong>Segmento Analisado:</strong> {resumo.get('segmento_analisado', 'N/A')}</p>
                <p><strong>Produto/Serviço:</strong> {resumo.get('produto_servico', 'N/A')}</p>
                <p><strong>Qualidade da Análise:</strong> {resumo.get('qualidade_analise', 0):.1f}%</p>
                <p><strong>Componentes Gerados:</strong> {resumo.get('componentes_gerados', 0)}</p>
            </div>
            
            <div class="highlight">
                <h3>Principais Conclusões</h3>
                <p>{resumo.get('principais_conclusoes', 'Análise em andamento...')}</p>
            </div>
        </section>
        """
    
    def _create_market_analysis(self, data: Dict[str, Any]) -> str:
        """Cria seção de análise de mercado"""
        
        mercado = data.get('analise_mercado', {})
        
        return f"""
        <section class="section">
            <h2>📈 Análise de Mercado</h2>
            
            <div class="metric">
                <h3>Tamanho do Mercado</h3>
                <p><strong>Valor Estimado:</strong> {mercado.get('tamanho_mercado', 'N/A')}</p>
                <p><strong>Taxa de Crescimento:</strong> {mercado.get('taxa_crescimento', 'N/A')}</p>
                <p><strong>Tendências Principais:</strong> {mercado.get('tendencias', 'N/A')}</p>
            </div>
            
            <div class="metric">
                <h3>Oportunidades Identificadas</h3>
                <ul class="list">
                    {self._render_list_items(mercado.get('oportunidades', []))}
                </ul>
            </div>
            
            <div class="metric">
                <h3>Desafios do Mercado</h3>
                <ul class="list">
                    {self._render_list_items(mercado.get('desafios', []))}
                </ul>
            </div>
        </section>
        """
    
    def _create_competitor_analysis(self, data: Dict[str, Any]) -> str:
        """Cria seção de análise de concorrentes"""
        
        concorrentes = data.get('analise_concorrentes', {})
        
        return f"""
        <section class="section">
            <h2>🥊 Análise da Concorrência</h2>
            
            <div class="metric">
                <h3>Principais Concorrentes</h3>
                {self._render_competitor_table(concorrentes.get('principais', []))}
            </div>
            
            <div class="metric">
                <h3>Análise SWOT da Concorrência</h3>
                <div class="insight">
                    <h4>Forças dos Concorrentes:</h4>
                    <ul class="list">
                        {self._render_list_items(concorrentes.get('forcas', []))}
                    </ul>
                </div>
                
                <div class="warning">
                    <h4>Fraquezas dos Concorrentes:</h4>
                    <ul class="list">
                        {self._render_list_items(concorrentes.get('fraquezas', []))}
                    </ul>
                </div>
            </div>
        </section>
        """
    
    def _create_opportunities(self, data: Dict[str, Any]) -> str:
        """Cria seção de oportunidades"""
        
        oportunidades = data.get('oportunidades', {})
        
        return f"""
        <section class="section">
            <h2>💡 Oportunidades de Negócio</h2>
            
            <div class="metric">
                <h3>Oportunidades Prioritárias</h3>
                {self._render_opportunities_list(oportunidades.get('prioritarias', []))}
            </div>
            
            <div class="metric">
                <h3>Nichos Não Explorados</h3>
                <ul class="list">
                    {self._render_list_items(oportunidades.get('nichos', []))}
                </ul>
            </div>
            
            <div class="highlight">
                <h3>Recomendação Principal</h3>
                <p>{oportunidades.get('recomendacao_principal', 'Análise em andamento...')}</p>
            </div>
        </section>
        """
    
    def _create_recommendations(self, data: Dict[str, Any]) -> str:
        """Cria seção de recomendações"""
        
        recomendacoes = data.get('recomendacoes', {})
        
        return f"""
        <section class="section">
            <h2>🎯 Recomendações Estratégicas</h2>
            
            <div class="metric">
                <h3>Ações Imediatas (30 dias)</h3>
                <ul class="list">
                    {self._render_list_items(recomendacoes.get('imediatas', []))}
                </ul>
            </div>
            
            <div class="metric">
                <h3>Ações de Médio Prazo (90 dias)</h3>
                <ul class="list">
                    {self._render_list_items(recomendacoes.get('medio_prazo', []))}
                </ul>
            </div>
            
            <div class="metric">
                <h3>Ações de Longo Prazo (180+ dias)</h3>
                <ul class="list">
                    {self._render_list_items(recomendacoes.get('longo_prazo', []))}
                </ul>
            </div>
        </section>
        """
    
    def _create_implementation_plan(self, data: Dict[str, Any]) -> str:
        """Cria seção de plano de implementação"""
        
        implementacao = data.get('plano_implementacao', {})
        
        return f"""
        <section class="section">
            <h2>⚡ Plano de Implementação</h2>
            
            <div class="metric">
                <h3>Recursos Necessários</h3>
                <p><strong>Orçamento Estimado:</strong> {implementacao.get('orcamento', 'N/A')}</p>
                <p><strong>Tempo de Implementação:</strong> {implementacao.get('tempo', 'N/A')}</p>
                <p><strong>Equipe Necessária:</strong> {implementacao.get('equipe', 'N/A')}</p>
            </div>
            
            <div class="metric">
                <h3>Cronograma de Execução</h3>
                {self._render_timeline(implementacao.get('cronograma', {}))}
            </div>
            
            <div class="warning">
                <h3>Riscos e Mitigações</h3>
                <ul class="list">
                    {self._render_list_items(implementacao.get('riscos', []))}
                </ul>
            </div>
        </section>
        """
    
    def _create_appendix(self, data: Dict[str, Any]) -> str:
        """Cria seção de apêndice"""
        
        return f"""
        <section class="section">
            <h2>📎 Apêndice</h2>
            
            <div class="metric">
                <h3>Fontes de Dados</h3>
                <p>Esta análise foi baseada em:</p>
                <ul class="list">
                    <li>Dados de pesquisa de mercado atualizados</li>
                    <li>Análise de concorrentes diretos e indiretos</li>
                    <li>Tendências identificadas por IA avançada</li>
                    <li>Fontes públicas e bases de dados especializadas</li>
                </ul>
            </div>
            
            <div class="metric">
                <h3>Metodologia</h3>
                <p>A análise foi conduzida utilizando o sistema ARQV30 Enhanced v2.0, que combina:</p>
                <ul class="list">
                    <li>Inteligência Artificial Gemini 2.5 Pro</li>
                    <li>Múltiplos motores de busca especializados</li>
                    <li>Análise de dados em tempo real</li>
                    <li>Validação cruzada de informações</li>
                </ul>
            </div>
            
            <div class="highlight">
                <h3>Limitações</h3>
                <p>Esta análise é baseada em dados disponíveis publicamente e pode não refletir informações confidenciais ou estratégicas dos concorrentes. Recomenda-se validação adicional para decisões críticas de negócio.</p>
            </div>
        </section>
        """
    
    def _render_list_items(self, items: List[str]) -> str:
        """Renderiza itens de lista"""
        
        if not items:
            return "<li>Nenhum item identificado</li>"
        
        return "".join([f"<li>{item}</li>" for item in items])
    
    def _render_competitor_table(self, competitors: List[Dict]) -> str:
        """Renderiza tabela de concorrentes"""
        
        if not competitors:
            return "<p>Nenhum concorrente identificado</p>"
        
        table_html = """
        <table class="table">
            <thead>
                <tr>
                    <th>Concorrente</th>
                    <th>Posição</th>
                    <th>Principais Forças</th>
                    <th>Principais Fraquezas</th>
                </tr>
            </thead>
            <tbody>
        """
        
        for comp in competitors:
            table_html += f"""
                <tr>
                    <td>{comp.get('nome', 'N/A')}</td>
                    <td>{comp.get('posicao', 'N/A')}</td>
                    <td>{comp.get('forcas', 'N/A')}</td>
                    <td>{comp.get('fraquezas', 'N/A')}</td>
                </tr>
            """
        
        table_html += """
            </tbody>
        </table>
        """
        
        return table_html
    
    def _render_opportunities_list(self, opportunities: List[Dict]) -> str:
        """Renderiza lista de oportunidades"""
        
        if not opportunities:
            return "<p>Nenhuma oportunidade identificada</p>"
        
        html = ""
        for i, opp in enumerate(opportunities, 1):
            html += f"""
            <div class="insight">
                <h4>Oportunidade {i}: {opp.get('titulo', 'N/A')}</h4>
                <p><strong>Descrição:</strong> {opp.get('descricao', 'N/A')}</p>
                <p><strong>Potencial:</strong> {opp.get('potencial', 'N/A')}</p>
                <p><strong>Complexidade:</strong> {opp.get('complexidade', 'N/A')}</p>
            </div>
            """
        
        return html
    
    def _render_timeline(self, timeline: Dict[str, Any]) -> str:
        """Renderiza timeline"""
        
        if not timeline:
            return "<p>Timeline não disponível</p>"
        
        html = ""
        for phase, details in timeline.items():
            html += f"""
            <div class="metric">
                <h4>{phase.replace('_', ' ').title()}</h4>
                <p>{details}</p>
            </div>
            """
        
        return html
    
    def _create_error_report(self, error_message: str) -> str:
        """Cria relatório de erro"""
        
        return f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Erro na Geração do Relatório</title>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; }}
        .error {{ background: #fadbd8; padding: 20px; border-left: 4px solid #e74c3c; }}
    </style>
</head>
<body>
    <div class="error">
        <h1>❌ Erro na Geração do Relatório</h1>
        <p><strong>Mensagem:</strong> {error_message}</p>
        <p><strong>Timestamp:</strong> {datetime.now().isoformat()}</p>
        <p>Por favor, tente novamente ou entre em contato com o suporte.</p>
    </div>
</body>
</html>
        """

# Instância global
html_report_generator = HTMLReportGenerator()

@html_report_bp.route('/generate_html_report', methods=['POST'])
def generate_html_report():
    """Endpoint para gerar relatório HTML"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'error': 'Dados são obrigatórios'
            }), 400
        
        # Gera relatório HTML
        html_content = html_report_generator.generate_complete_html_report(data)
        
        return jsonify({
            'status': 'success',
            'html_content': html_content,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Erro ao gerar relatório HTML: {e}")
        return jsonify({
            'error': f'Erro interno: {str(e)}'
        }), 500

@html_report_bp.route('/download_html_report', methods=['POST'])
def download_html_report():
    """Endpoint para download do relatório HTML"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'error': 'Dados são obrigatórios'
            }), 400
        
        # Gera relatório HTML
        html_content = html_report_generator.generate_complete_html_report(data)
        
        # Cria arquivo em memória
        buffer = BytesIO()
        buffer.write(html_content.encode('utf-8'))
        buffer.seek(0)
        
        filename = f"relatorio_analise_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        
        return send_file(
            buffer,
            as_attachment=True,
            download_name=filename,
            mimetype='text/html'
        )
        
    except Exception as e:
        logger.error(f"Erro ao fazer download do relatório HTML: {e}")
        return jsonify({
            'error': f'Erro interno: {str(e)}'
        }), 500
