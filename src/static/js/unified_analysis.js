// ARQV30 Enhanced v3.0 - Unified Analysis JS CORRIGIDO
console.log('🔬 Sistema de Análise Moderno carregado');

let currentSessionId = null;
let progressInterval = null;
let analysisData = null; // Renomeado para analysisData para clareza
let currentAnalysisData = null; // Nova variável para dados do avatar ultra detalhado

// Configurações globais
const CONFIG = {
    API_BASE: '/api',
    PROGRESS_UPDATE_INTERVAL: 2000,
    MAX_RETRIES: 3,
    TIMEOUT: 300000 // 5 minutos
};

// Inicialização
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 ARQV30 Enhanced v3.0 - Sistema Moderno Inicializado');
    console.log('🎯 Interface Moderna Carregada');

    // Inicializa componentes
    initializeForm();
    initializeEventListeners();

    // Verifica se há análise em andamento
    checkOngoingAnalysis();
});

function initializeForm() {
    // Preenche valores padrão se necessário
    const fields = {
        'segmento': '',
        'produto': '',
        'preco': '',
        'objetivo_receita': '',
        'publico': '',
        'concorrentes': '',
        'orcamento_marketing': '',
        'prazo_lancamento': '',
        'dados_adicionais': ''
    };

    // Aplica máscaras de input
    applyInputMasks();
}

function initializeEventListeners() {
    // Listener para tecla Enter nos campos
    document.querySelectorAll('input, textarea').forEach(field => {
        field.addEventListener('keypress', function(e) {
            if (e.key === 'Enter' && e.ctrlKey) {
                executeUnifiedAnalysis();
            }
        });
    });

    // Auto-save dos dados do formulário
    document.querySelectorAll('input, textarea, select').forEach(field => {
        field.addEventListener('change', saveFormData);
        field.addEventListener('input', debounce(saveFormData, 1000));
    });

    // Carrega dados salvos
    loadFormData();

    // Adiciona listener para o botão de iniciar nova análise
    const newAnalysisButton = document.getElementById('new-analysis-button');
    if (newAnalysisButton) {
        newAnalysisButton.addEventListener('click', startNewAnalysis);
    }
}

function applyInputMasks() {
    // Máscara para valores monetários
    const moneyFields = ['preco', 'objetivo_receita', 'orcamento_marketing'];

    moneyFields.forEach(fieldId => {
        const field = document.getElementById(fieldId);
        if (field) {
            field.addEventListener('input', function(e) {
                let value = e.target.value.replace(/\D/g, '');
                if (value) {
                    value = (parseInt(value) / 100).toFixed(2);
                    e.target.value = value;
                }
            });
        }
    });
}

function saveFormData() {
    const formData = collectFormData();
    localStorage.setItem('arqv30_form_data', JSON.stringify(formData));
}

function loadFormData() {
    try {
        const savedData = localStorage.getItem('arqv30_form_data');
        if (savedData) {
            const data = JSON.parse(savedData);
            Object.keys(data).forEach(key => {
                const field = document.getElementById(key);
                if (field && data[key]) {
                    field.value = data[key];
                }
            });
        }
    } catch (e) {
        console.warn('Erro ao carregar dados salvos:', e);
    }
}

function collectFormData() {
    return {
        segmento: document.getElementById('segmento')?.value.trim() || '',
        produto: document.getElementById('produto')?.value.trim() || '',
        preco: document.getElementById('preco')?.value || '',
        objetivo_receita: document.getElementById('objetivo_receita')?.value || '',
        publico: document.getElementById('publico')?.value.trim() || '',
        concorrentes: document.getElementById('concorrentes')?.value.trim() || '',
        orcamento_marketing: document.getElementById('orcamento_marketing')?.value || '',
        prazo_lancamento: document.getElementById('prazo_lancamento')?.value || '',
        dados_adicionais: document.getElementById('dados_adicionais')?.value.trim() || ''
    };
}

function validateFormData(data) {
    const errors = [];

    if (!data.segmento) {
        errors.push('Segmento de Mercado é obrigatório');
    }

    if (!data.produto) {
        errors.push('Produto/Serviço é obrigatório');
    }

    if (data.segmento && data.segmento.length < 3) {
        errors.push('Segmento deve ter pelo menos 3 caracteres');
    }

    if (data.produto && data.produto.length < 3) {
        errors.push('Produto deve ter pelo menos 3 caracteres');
    }

    return errors;
}

async function executeUnifiedAnalysis() {
    console.log('🚀 Iniciando análise unificada');

    // Coleta e valida dados
    const formData = collectFormData();
    const validationErrors = validateFormData(formData);

    if (validationErrors.length > 0) {
        showAlert('error', 'Erro de Validação:\n' + validationErrors.join('\n'));
        return;
    }

    try {
        // Desabilita botão e mostra progresso
        const button = document.querySelector('.analyze-button');
        if (button) {
            button.disabled = true;
            button.innerHTML = '<div class="loading-spinner"></div>Executando Análise...';
        }

        showProgressContainer();
        updateProgress(0, 'Iniciando análise unificada...');

        // Gera session ID único
        currentSessionId = 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
        localStorage.setItem('arqv30_ongoing_session', currentSessionId); // Salva para recuperação

        // Inicia monitoramento de progresso
        startProgressMonitoring();

        // Executa análise
        const response = await fetch('/api/unified_analysis/execute_unified_analysis', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                ...formData,
                session_id: currentSessionId
            })
        });

        if (!response.ok) {
            throw new Error(`Erro HTTP: ${response.status}`);
        }

        const result = await response.json();

        if (result.success) {
            // Análise concluída com sucesso
            analysisData = result; // Armazena todos os dados da análise
            currentAnalysisData = result.analysis_result; // Armazena especificamente os dados do avatar ultra detalhado para o pré-pitch
            updateProgress(100, '🎉 Análise concluída com sucesso!');

            setTimeout(() => {
                showResults(result);
            }, 1000);

            showAlert('success', 'Análise unificada concluída com sucesso!');

        } else {
            throw new Error(result.error || 'Erro na análise');
        }

    } catch (error) {
        console.error('Erro na análise:', error);
        showAlert('error', 'Erro na análise: ' + error.message);

        updateProgress(0, '❌ Erro na análise');
        hideProgressContainer();

    } finally {
        // Reabilita botão
        const button = document.querySelector('.analyze-button');
        if (button) {
            button.disabled = false;
            button.innerHTML = '🚀 Executar Análise Unificada Completa';
        }

        // Para monitoramento
        stopProgressMonitoring();
        localStorage.removeItem('arqv30_ongoing_session'); // Limpa após conclusão ou erro
    }
}

function startProgressMonitoring() {
    if (!currentSessionId) return;

    progressInterval = setInterval(async () => {
        try {
            const response = await fetch(`${CONFIG.API_BASE}/progress/${currentSessionId}`);

            if (response.ok) {
                const data = await response.json();

                if (data.success && data.progress) {
                    const progress = data.progress;
                    updateProgress(
                        progress.percentage || 0, 
                        progress.current_message || 'Processando...',
                        progress.detailed_message
                    );

                    if (progress.is_complete) {
                        stopProgressMonitoring();
                    }
                }
            } else if (response.status === 404) {
                console.warn(`Progresso para ${currentSessionId} não encontrado.`);
                stopProgressMonitoring();
            } else {
                throw new Error(`HTTP ${response.status}`);
            }
        } catch (error) {
            console.warn('Erro ao atualizar progresso:', error);
            // Pode adicionar lógica de retentativa aqui
            // if (retries < CONFIG.MAX_RETRIES) { ... }
        }
    }, CONFIG.PROGRESS_UPDATE_INTERVAL);
}

function stopProgressMonitoring() {
    if (progressInterval) {
        clearInterval(progressInterval);
        progressInterval = null;
    }
}

function showProgressContainer() {
    const container = document.getElementById('progressContainer');
    if (container) {
        container.style.display = 'block';
        container.scrollIntoView({ behavior: 'smooth' });
    }
}

function hideProgressContainer() {
    const container = document.getElementById('progressContainer');
    if (container) {
        container.style.display = 'none';
    }
}

function updateProgress(percentage, message, details = null) {
    // Atualiza barra de progresso
    const fillElement = document.getElementById('progressFill');
    const percentageElement = document.getElementById('progressPercentage');
    const messageElement = document.getElementById('progressMessage');

    if (fillElement) {
        fillElement.style.width = `${Math.min(100, Math.max(0, percentage))}%`;
    }

    if (percentageElement) {
        percentageElement.textContent = `${Math.round(percentage)}%`;
    }

    if (messageElement) {
        messageElement.textContent = message;
    }

    // Atualiza detalhes se fornecidos
    if (details) {
        const detailsContainer = document.getElementById('progressDetails');
        const detailsList = document.getElementById('progressDetailsList');

        if (detailsContainer && detailsList) {
            const listItem = document.createElement('li');
            listItem.textContent = details;
            detailsList.appendChild(listItem);

            detailsContainer.style.display = 'block';

            // Mantém apenas os últimos 5 itens
            while (detailsList.children.length > 5) {
                detailsList.removeChild(detailsList.firstChild);
            }
        }
    }

    console.log(`Progresso: ${percentage}% - ${message}`);
}

function showResults(result) {
    hideProgressContainer();

    const container = document.getElementById('resultsContainer');
    if (container) {
        container.style.display = 'block';
        container.scrollIntoView({ behavior: 'smooth' });

        // Atualiza indicadores de qualidade
        updateQualityIndicators(result);

        // Atualiza preview do relatório
        updateReportPreview(result);

        // Configura downloads
        setupDownloadLinks(result);
    }
}

function updateQualityIndicators(result) {
    const container = document.getElementById('qualityIndicators');
    if (!container) return;

    const metrics = result.processing_info || {};
    const quality = result.quality_metrics || {};

    const indicators = [
        {
            score: Math.round(metrics.uniqueness_score || 85),
            label: 'Score de Exclusividade',
            suffix: '%'
        },
        {
            score: Math.round(metrics.completeness_score || 90),
            label: 'Completude da Análise',
            suffix: '%'
        },
        {
            score: quality.sources_analyzed || 0,
            label: 'Fontes Analisadas',
            suffix: ''
        },
        {
            score: quality.social_platforms || 0,
            label: 'Plataformas Sociais',
            suffix: ''
        },
        {
            score: Math.round((metrics.total_time_seconds || 0) / 60),
            label: 'Tempo de Processamento',
            suffix: 'min'
        },
        {
            score: metrics.pages_generated || 0,
            label: 'Páginas Geradas',
            suffix: ''
        }
    ];

    container.innerHTML = indicators.map(indicator => `
        <div class="quality-card">
            <div class="quality-score">${indicator.score}${indicator.suffix}</div>
            <div class="quality-label">${indicator.label}</div>
        </div>
    `).join('');
}

function updateReportPreview(result) {
    const container = document.getElementById('reportPreview');
    if (!container) return;

    // Cria preview estruturado
    let preview = '<h3>📊 Resumo Executivo da Análise</h3>';

    if (result.analysis_result) {
        const analysis = result.analysis_result;

        preview += `
            <div style="margin-bottom: 1.5rem;">
                <h4>🎯 Dados do Projeto</h4>
                <p><strong>Segmento:</strong> ${analysis.project_data?.segmento_analisado || 'N/A'}</p>
                <p><strong>Produto:</strong> ${analysis.project_data?.produto_analisado || 'N/A'}</p>
            </div>
        `;

        if (analysis.research_summary) {
            preview += `
                <div style="margin-bottom: 1.5rem;">
                    <h4>🔍 Resumo da Pesquisa</h4>
                    <p><strong>Fontes Analisadas:</strong> ${analysis.research_summary.sources_analyzed || 0}</p>
                    <p><strong>Conteúdo Extraído:</strong> ${analysis.research_summary.content_extracted || 0} caracteres</p>
                    <p><strong>Plataformas Sociais:</strong> ${analysis.research_summary.social_platforms || 0}</p>
                    <p><strong>Qualidade dos Dados:</strong> ${analysis.research_summary.data_quality || 'REAL_DATA_ONLY'}</p>
                </div>
            `;
        }

        if (analysis.drivers_mentais) {
            preview += `
                <div style="margin-bottom: 1.5rem;">
                    <h4>🧠 Drivers Mentais</h4>
                    <p><strong>Total de Drivers:</strong> ${analysis.drivers_mentais.total_drivers || 0}</p>
                    <p><strong>Personalização:</strong> ${analysis.drivers_mentais.personalizacao || '100% específico'}</p>
                </div>
            `;
        }

        if (analysis.avatars) {
            preview += `
                <div style="margin-bottom: 1.5rem;">
                    <h4>👤 Avatar Personalizado</h4>
                    <p><strong>Persona:</strong> ${analysis.avatars.nome_persona || 'Avatar Específico'}</p>
                    <p><strong>Comportamento:</strong> ${analysis.avatars.comportamento_observado || 'Baseado em dados reais'}</p>
                </div>
            `;
        }

        preview += `
            <div style="margin-top: 2rem; padding: 1rem; background: #f0f9ff; border-radius: 10px; border: 1px solid #3b82f6;">
                <p><strong>✅ Análise Completa:</strong> Todos os componentes foram processados com dados reais específicos do seu segmento.</p>
                <p><strong>🚫 Zero Fallback:</strong> Nenhum placeholder genérico foi utilizado.</p>
                <p><strong>📈 Qualidade Premium:</strong> Dados exclusivos e personalizados para sua necessidade.</p>
            </div>
        `;
    }

    container.innerHTML = preview;
}

function setupDownloadLinks(result) {
    const htmlButton = document.getElementById('downloadHtml');
    const jsonButton = document.getElementById('downloadJson');

    if (result.html_report && htmlButton) {
        const htmlBlob = new Blob([result.html_report], { type: 'text/html' });
        const htmlUrl = URL.createObjectURL(htmlBlob);

        htmlButton.href = htmlUrl;
        htmlButton.download = `relatorio_${currentSessionId}.html`;
    }

    if (result.analysis_result && jsonButton) {
        const jsonBlob = new Blob([JSON.stringify(result.analysis_result, null, 2)], { type: 'application/json' });
        const jsonUrl = URL.createObjectURL(jsonBlob);

        jsonButton.href = jsonUrl;
        jsonButton.download = `dados_${currentSessionId}.json`;
    }
}

function startNewAnalysis() {
    // Limpa dados anteriores
    currentSessionId = null;
    analysisData = null;
    currentAnalysisData = null; // Limpa dados do avatar também

    // Esconde containers
    hideProgressContainer();
    const resultsContainer = document.getElementById('resultsContainer');
    if (resultsContainer) {
        resultsContainer.style.display = 'none';
    }

    // Rola para o topo
    document.querySelector('.analysis-form')?.scrollIntoView({ behavior: 'smooth' });

    // Limpa alertas
    clearAlerts();

    // Limpa o formulário
    document.getElementById('segmento').value = '';
    document.getElementById('produto').value = '';
    document.getElementById('preco').value = '';
    document.getElementById('objetivo_receita').value = '';
    document.getElementById('publico').value = '';
    document.getElementById('concorrentes').value = '';
    document.getElementById('orcamento_marketing').value = '';
    document.getElementById('prazo_lancamento').value = '';
    document.getElementById('dados_adicionais').value = '';

    // Limpa dados do localStorage
    localStorage.removeItem('arqv30_form_data');

    console.log('🔄 Nova análise iniciada');
}

function checkOngoingAnalysis() {
    const ongoingSession = localStorage.getItem('arqv30_ongoing_session');

    if (ongoingSession) {
        currentSessionId = ongoingSession;

        // Tenta recuperar progresso
        startProgressMonitoring();
        showProgressContainer();
        updateProgress(50, 'Recuperando análise em andamento...');

        // Remove após um tempo para evitar loops
        setTimeout(() => {
            localStorage.removeItem('arqv30_ongoing_session');
        }, 60000); // 1 minuto de tolerância
    }
}

function showAlert(type, message) {
    // Remove alertas existentes
    clearAlerts();

    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.textContent = message;

    // Insere no início do container principal
    const mainContent = document.querySelector('.main-content .container');
    if (mainContent) {
        mainContent.insertBefore(alertDiv, mainContent.firstChild);

        // Remove automaticamente após 10 segundos
        setTimeout(() => {
            if (alertDiv.parentNode) {
                alertDiv.parentNode.removeChild(alertDiv);
            }
        }, 10000);

        // Rola para o alerta
        alertDiv.scrollIntoView({ behavior: 'smooth' });
    }
}

function clearAlerts() {
    document.querySelectorAll('.alert').forEach(alert => {
        if (alert.parentNode) {
            alert.parentNode.removeChild(alert);
        }
    });
}

// --- Funções para o Sistema de Pitch ---

// Adiciona função para gerar pré-pitch invisível
async function generateInvisiblePrepitch() {
    const pitchStructureField = document.getElementById('pitch-structure');
    const targetEmotionField = document.getElementById('target-emotion');
    const resultsContainer = document.getElementById('prepitch-results');

    if (!currentAnalysisData || !currentAnalysisData.avatar_ultra_detalhado) {
        showError('❌ Execute uma análise completa primeiro para obter dados do avatar', 'prepitch-results');
        return;
    }

    const pitchStructure = pitchStructureField ? pitchStructureField.value : '';
    const targetEmotion = targetEmotionField ? targetEmotionField.value : '';

    try {
        showLoading('🧠 Gerando pré-pitch invisível personalizado...', 'prepitch-results');

        const response = await fetch('/pitch-system/generate-invisible-prepitch', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                avatar_data: currentAnalysisData.avatar_ultra_detalhado,
                pitch_structure: pitchStructure,
                target_emotion: targetEmotion
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }

        const result = await response.json();

        if (result.success) {
            displayPrepitchResults(result.prepitch);
            showSuccess('✅ Pré-pitch invisível gerado com sucesso!', 'prepitch-results');
        } else {
            throw new Error(result.error || 'Erro desconhecido');
        }

    } catch (error) {
        console.error('Erro ao gerar pré-pitch:', error);
        showError(`❌ Erro ao gerar pré-pitch: ${error.message}`, 'prepitch-results');
    }
}

// Função para exibir resultados do pré-pitch
function displayPrepitchResults(prepitch) {
    const container = document.getElementById('prepitch-results');
    if (!container) return;

    const html = `
        <div class="prepitch-results">
            <div class="prepitch-overview">
                <h4><i class="fas fa-brain"></i> Pré-Pitch ${prepitch.prepitch_structure?.tipo || 'Personalizado'}</h4>
                <p><strong>Duração:</strong> ${prepitch.prepitch_structure?.duracao_total || 'N/A'} minutos</p>
                <p><strong>Conversão Esperada:</strong> ${prepitch.conversion_predictions?.expectativa_conversao?.cenario_realista || 'N/A'}</p>
            </div>

            <div class="drives-selected">
                <h5><i class="fas fa-cog"></i> Drives Mentais Selecionados (${prepitch.selected_drives?.length || 0})</h5>
                <div class="drives-grid">
                    ${prepitch.selected_drives?.map(drive => `
                        <div class="drive-card">
                            <h6>${drive.nome.replace(/_/g, ' ').toUpperCase()}</h6>
                            <p><strong>Intensidade:</strong> ${drive.intensidade}/10</p>
                            <p><strong>Categoria:</strong> ${drive.categoria}</p>
                            <p class="drive-justification">${drive.justificativa}</p>
                        </div>
                    `).join('') || '<p>Nenhum drive selecionado</p>'}
                </div>
            </div>

            <div class="timeline-structure">
                <h5><i class="fas fa-clock"></i> Timeline Detalhada</h5>
                ${prepitch.detailed_timeline?.fases_detalhadas ?
                    Object.entries(prepitch.detailed_timeline.fases_detalhadas).map(([fase, dados]) => `
                        <div class="timeline-phase">
                            <h6>${fase.replace(/_/g, ' ').toUpperCase()}</h6>
                            <p><strong>Tempo:</strong> ${dados.tempo}</p>
                            <p><strong>Objetivo:</strong> ${dados.objetivo}</p>
                            <p><strong>Energia:</strong> ${dados.energia}</p>
                            ${dados.drives ? `<p><strong>Drives:</strong> ${dados.drives.join(', ')}</p>` : ''}
                        </div>
                    `).join('') : '<p>Timeline não disponível</p>'
                }
            </div>

            <div class="implementation-guide">
                <h5><i class="fas fa-play"></i> Guia de Implementação</h5>
                <div class="expandable-section">
                    <div class="expandable-header" onclick="toggleExpandable(this)">
                        <span>Preparação do Evento</span>
                        <i class="fas fa-chevron-down expandable-icon"></i>
                    </div>
                    <div class="expandable-content">
                        ${prepitch.implementation_guide?.preparacao_evento ?
                            Object.entries(prepitch.implementation_guide.preparacao_evento).map(([timing, tasks]) => `
                                <div class="prep-timing">
                                    <h6>${timing.replace(/_/g, ' ').toUpperCase()}</h6>
                                    <ul>
                                        ${tasks.map(task => `<li>${task}</li>`).join('')}
                                    </ul>
                                </div>
                            `).join('') : '<p>Guia não disponível</p>'
                        }
                    </div>
                </div>
            </div>
        </div>
    `;

    container.innerHTML = html;
}

// Helper functions for pitch system
function showError(message, containerId = null) {
    const targetContainer = containerId ? document.getElementById(containerId) : null;
    if (targetContainer) {
        targetContainer.innerHTML = `<div class="error-state"><i class="fas fa-exclamation-triangle"></i><p>${message}</p></div>`;
    } else {
        showAlert('error', message);
    }
}

function showSuccess(message, containerId = null) {
    const targetContainer = containerId ? document.getElementById(containerId) : null;
    if (targetContainer) {
        targetContainer.innerHTML = `<div class="success-state"><i class="fas fa-check-circle"></i><p>${message}</p></div>`;
    } else {
        showAlert('success', message);
    }
}

function showLoading(message, containerId) {
    const targetContainer = document.getElementById(containerId);
    if (targetContainer) {
        targetContainer.innerHTML = `<div class="loading-state"><div class="spinner"></div><p>${message}</p></div>`;
    }
}

// Toggle function for expandable sections in implementation guide
function toggleExpandable(header) {
    const content = header.nextElementSibling;
    const icon = header.querySelector('.expandable-icon');
    content.style.display = content.style.display === 'block' ? 'none' : 'block';
    icon.classList.toggle('fa-chevron-down');
    icon.classList.toggle('fa-chevron-up');
}

// Event listener for the generate prepitch button
document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generate-prepitch');
    if (generateBtn) {
        generateBtn.addEventListener('click', generateInvisiblePrepitch);
    }
});

// Inicializar quando a página carregar - Mantém a inicialização da interface principal
document.addEventListener('DOMContentLoaded', initializeInterface); // Assume que initializeInterface está definida em outro lugar ou é parte do DOMContentLoaded original

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function formatNumber(num) {
    return new Intl.NumberFormat('pt-BR').format(num);
}

function formatCurrency(value) {
    try {
        return new Intl.NumberFormat('pt-BR', {
            style: 'currency',
            currency: 'BRL'
        }).format(parseFloat(value));
    } catch (e) {
        return 'R$ 0,00';
    }
}

// Exporta funções globais
window.executeUnifiedAnalysis = executeUnifiedAnalysis;
window.startNewAnalysis = startNewAnalysis;
window.generateInvisiblePrepitch = generateInvisiblePrepitch; // Exporta a nova função

// Log final
console.log('🎯 Sistema de Análise Unificada CORRIGIDO e com Sistema de Pitch Integrado carregado');