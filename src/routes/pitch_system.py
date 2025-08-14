#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Pitch System Route
Rota para sistema completo de pitch devastador
"""

from flask import Blueprint, request, jsonify, render_template_string
import logging
from datetime import datetime
from services.pitch_master_architect import pitch_master_architect
from services.auto_save_manager import auto_save_manager
# Importar o novo serviço
from services.invisible_prepitch_architect import invisible_prepitch_architect

logger = logging.getLogger(__name__)

pitch_system_bp = Blueprint('pitch_system', __name__)

@pitch_system_bp.route('/pitch-system', methods=['GET'])
def pitch_system_interface():
    """Interface para sistema de pitch"""

    html_template = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sistema de Pitch Devastador - ARQV30</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                background: white;
                border-radius: 15px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                overflow: hidden;
            }
            .header {
                background: linear-gradient(135deg, #ff6b6b, #4ecdc4);
                color: white;
                padding: 30px;
                text-align: center;
            }
            .header h1 {
                font-size: 2.5em;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            .subtitle {
                font-size: 1.2em;
                opacity: 0.9;
            }
            .form-container {
                padding: 40px;
            }
            .form-group {
                margin-bottom: 25px;
            }
            label {
                display: block;
                margin-bottom: 8px;
                font-weight: 600;
                color: #333;
            }
            input, textarea, select {
                width: 100%;
                padding: 12px;
                border: 2px solid #e1e1e1;
                border-radius: 8px;
                font-size: 14px;
                transition: border-color 0.3s;
            }
            input:focus, textarea:focus, select:focus {
                outline: none;
                border-color: #667eea;
            }
            textarea {
                height: 120px;
                resize: vertical;
            }
            .btn-primary {
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                border: none;
                padding: 15px 30px;
                border-radius: 8px;
                font-size: 16px;
                font-weight: 600;
                cursor: pointer;
                transition: transform 0.3s;
                width: 100%;
            }
            .btn-primary:hover {
                transform: translateY(-2px);
            }
            .results {
                background: #f8f9fa;
                border: 1px solid #e9ecef;
                border-radius: 8px;
                padding: 20px;
                margin-top: 20px;
                display: none;
            }
            .loading {
                text-align: center;
                padding: 40px;
                display: none;
            }
            .spinner {
                border: 4px solid #f3f3f3;
                border-top: 4px solid #667eea;
                border-radius: 50%;
                width: 40px;
                height: 40px;
                animation: spin 1s linear infinite;
                margin: 0 auto 20px;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            .grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
            }
            @media (max-width: 768px) {
                .grid { grid-template-columns: 1fr; }
                .header h1 { font-size: 2em; }
                .form-container { padding: 20px; }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🎯 Sistema de Pitch Devastador</h1>
                <p class="subtitle">Crie pitches com conversão de 30-50% usando o protocolo AR completo</p>
            </div>

            <div class="form-container">
                <form id="pitchForm">
                    <div class="grid">
                        <div class="form-group">
                            <label for="segmento">Segmento/Nicho:</label>
                            <input type="text" id="segmento" name="segmento" required 
                                   placeholder="Ex: Produtos digitais, E-commerce, Consultoria">
                        </div>

                        <div class="form-group">
                            <label for="produto">Produto/Serviço:</label>
                            <input type="text" id="produto" name="produto" required 
                                   placeholder="Ex: Curso online, Mentoria, Sistema">
                        </div>
                    </div>

                    <div class="grid">
                        <div class="form-group">
                            <label for="preco">Preço (R$):</label>
                            <input type="number" id="preco" name="preco" required 
                                   placeholder="Ex: 1997">
                        </div>

                        <div class="form-group">
                            <label for="formato">Formato do Pitch:</label>
                            <select id="formato" name="formato" required>
                                <option value="">Selecione...</option>
                                <option value="webinar">Webinar</option>
                                <option value="presencial">Presencial</option>
                                <option value="live">Live</option>
                                <option value="gravado">Gravado</option>
                            </select>
                        </div>
                    </div>

                    <div class="grid">
                        <div class="form-group">
                            <label for="duracao">Duração Disponível:</label>
                            <select id="duracao" name="duracao" required>
                                <option value="">Selecione...</option>
                                <option value="45-60">45-60 minutos</option>
                                <option value="60-90">60-90 minutos</option>
                                <option value="90-120">90-120 minutos</option>
                            </select>
                        </div>

                        <div class="form-group">
                            <label for="temperatura">Temperatura da Audiência:</label>
                            <select id="temperatura" name="temperatura" required>
                                <option value="">Selecione...</option>
                                <option value="fria">Fria (não conhece você)</option>
                                <option value="morna">Morna (algum conhecimento)</option>
                                <option value="quente">Quente (já consome conteúdo)</option>
                                <option value="fervendo">Fervendo (super engajada)</option>
                            </select>
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="publico">Público-Alvo (Avatar):</label>
                        <textarea id="publico" name="publico" required 
                                  placeholder="Descreva seu avatar: idade, profissão, dores, desejos, objeções..."></textarea>
                    </div>

                    <div class="form-group">
                        <label for="dores">Principais Dores do Avatar:</label>
                        <textarea id="dores" name="dores" required 
                                  placeholder="Liste as principais dores, uma por linha..."></textarea>
                    </div>

                    <div class="form-group">
                        <label for="objecoes">Principais Objeções:</label>
                        <textarea id="objecoes" name="objecoes" required 
                                  placeholder="Liste as principais objeções, uma por linha..."></textarea>
                    </div>

                    <button type="submit" class="btn-primary">
                        🚀 Criar Sistema de Pitch Devastador
                    </button>
                </form>

                <div class="loading" id="loading">
                    <div class="spinner"></div>
                    <p>Criando seu sistema de pitch devastador...</p>
                </div>

                <div class="results" id="results"></div>
            </div>
        </div>

        <script>
        document.getElementById('pitchForm').addEventListener('submit', async function(e) {
            e.preventDefault();

            const loading = document.getElementById('loading');
            const results = document.getElementById('results');
            const form = e.target;

            loading.style.display = 'block';
            results.style.display = 'none';

            const formData = new FormData(form);
            const data = Object.fromEntries(formData);

            // Converter dores e objeções em arrays
            data.dores = data.dores.split('\\n').filter(d => d.trim());
            data.objecoes = data.objecoes.split('\\n').filter(o => o.trim());

            try {
                const response = await fetch('/pitch-system/create', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data)
                });

                const result = await response.json();

                loading.style.display = 'none';
                results.style.display = 'block';
                results.innerHTML = formatPitchResults(result);

            } catch (error) {
                loading.style.display = 'none';
                results.style.display = 'block';
                results.innerHTML = '<div style="color: red;">Erro ao criar sistema de pitch: ' + error.message + '</div>';
            }
        });

        function formatPitchResults(data) {
            return `
                <h3>🎯 Sistema de Pitch Criado com Sucesso!</h3>
                <p><strong>Conversão Esperada:</strong> ${data.conversao_esperada || '30-50%'}</p>
                <p><strong>Estrutura Escolhida:</strong> ${data.etapa_1_arquitetura?.estrutura_escolhida?.nome || 'Estrutura Otimizada'}</p>
                <p><strong>Drives Selecionados:</strong> ${data.etapa_2_pre_pitch?.drives_selecionados?.length || 12} drives customizados</p>
                <p><strong>Script Completo:</strong> Disponível com timing detalhado</p>
                <div style="margin-top: 20px; padding: 15px; background: #e8f5e8; border-radius: 8px;">
                    <strong>✅ Seu sistema está pronto!</strong><br>
                    Arquivo salvo automaticamente para download e implementação.
                </div>
            `;
        }
        </script>
    </body>
    </html>
    """

    return render_template_string(html_template)

@pitch_system_bp.route('/pitch-system/create', methods=['POST'])
def create_pitch_system():
    """Cria sistema completo de pitch"""

    try:
        data = request.get_json()

        # Processa dados do formulário
        context_data = {
            'segmento': data.get('segmento', ''),
            'produto': data.get('produto', ''),
            'preco': data.get('preco', 0),
            'publico': data.get('publico', ''),
            'formato': data.get('formato', ''),
            'duracao': data.get('duracao', ''),
            'temperatura': data.get('temperatura', '')
        }

        # Cria avatar_data a partir das informações
        avatar_data = {
            'dores_reais': data.get('dores', []),
            'objecoes_reais': data.get('objecoes', []),
            'desejos_profundos': [
                f"Ter sucesso em {context_data['segmento']}",
                "Superar limitações atuais",
                "Alcançar reconhecimento"
            ],
            'medos_secretos': [
                "Não conseguir os resultados",
                "Desperdiçar dinheiro",
                "Ficar para trás"
            ]
        }

        # Cria drivers_data básico
        drivers_data = {
            'drivers_customizados': [
                {'nome': 'ambicao_expandida', 'relevancia': 0.9},
                {'nome': 'coragem_prioritaria', 'relevancia': 0.8},
                {'nome': 'decisao_vs_condicao', 'relevancia': 0.85}
            ]
        }

        # Cria sistema completo de pitch
        pitch_system = pitch_master_architect.create_complete_pitch_system(
            context_data, avatar_data, drivers_data
        )

        # Salva automaticamente
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"pitch_system_{context_data['segmento']}_{timestamp}"

        auto_save_manager.save_analysis(
            filename,
            pitch_system,
            "pitch_system"
        )

        logger.info(f"✅ Sistema de pitch criado: {filename}")

        return jsonify({
            'success': True,
            'filename': filename,
            **pitch_system
        })

    except Exception as e:
        logger.error(f"❌ Erro ao criar sistema de pitch: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@pitch_system_bp.route('/pitch-system/templates', methods=['GET'])
def get_pitch_templates():
    """Retorna templates de pitch prontos"""

    templates = {
        "produtos_digitais": {
            "nome": "Template Produtos Digitais",
            "estrutura": "epico_imersivo",
            "drives_recomendados": [
                "ambicao_expandida",
                "oportunidade_oculta", 
                "diagnostico_brutal",
                "coragem_prioritaria"
            ],
            "conversao_esperada": "40-60%"
        },
        "consultoria": {
            "nome": "Template Consultoria",
            "estrutura": "classico_expandido",
            "drives_recomendados": [
                "mentor_extrator",
                "metodo_vs_sorte",
                "prova_viva",
                "exclusividade_tribal"
            ],
            "conversao_esperada": "35-50%"
        },
        "cursos_online": {
            "nome": "Template Cursos Online",
            "estrutura": "comprimido_urgente",
            "drives_recomendados": [
                "deadline_mental",
                "ambiente_propulsor",
                "antecipacao_massiva",
                "comprometimento_publico"
            ],
            "conversao_esperada": "30-45%"
        }
    }

    return jsonify(templates)

@pitch_system_bp.route('/generate-invisible-prepitch', methods=['POST'])
def generate_invisible_prepitch():
    """Gera pré-pitch invisível completo"""
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'Dados não fornecidos'}), 400

        # Extrai dados do avatar
        avatar_data = data.get('avatar_data', {})
        pitch_structure = data.get('pitch_structure', 'classica')
        target_emotion = data.get('target_emotion', 'transformacao')

        logger.info(f"🎯 Gerando pré-pitch invisível - estrutura: {pitch_structure}")

        # Gera pré-pitch invisível completo
        prepitch_result = invisible_prepitch_architect.generate_complete_prepitch(
            avatar_data=avatar_data,
            pitch_structure=pitch_structure,
            target_emotion=target_emotion
        )

        # Adiciona metadados
        prepitch_result['metadata'] = {
            'generated_at': datetime.now().isoformat(),
            'structure_type': pitch_structure,
            'target_emotion': target_emotion,
            'generator': 'Invisible Pre-Pitch Architect v2.0'
        }

        logger.info("✅ Pré-pitch invisível gerado com sucesso")

        return jsonify({
            'success': True,
            'prepitch': prepitch_result
        })

    except Exception as e:
        logger.error(f"❌ Erro ao gerar pré-pitch invisível: {e}")
        return jsonify({'error': str(e)}), 500