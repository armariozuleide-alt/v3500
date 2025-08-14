#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Progress Routes ULTRA-ROBUSTAS
Rotas para controle de progresso e sessões com fallbacks
"""

import os
import logging
import json
import shutil
from flask import Blueprint, request, jsonify
from datetime import datetime
import services.auto_save_manager as auto_save_manager # Changed import to allow calling helper functions

logger = logging.getLogger(__name__)

progress_bp = Blueprint("progress", __name__)

# Dictionary to hold progress trackers for each session
_progress_trackers = {}

class EnhancedProgressTracker:
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.current_step = 0
        self.message = "Iniciando..."
        self.details = ""
        self.completed = False

    def update(self, step: int, message: str, details: str = None):
        self.current_step = step
        self.message = message
        self.details = details if details else ""
        logger.info(f"Progress {self.session_id}: Step {self.current_step} - {self.message}")
        # In a real scenario, this would save the data to a file or database.
        # For now, we'll just log it.

    def complete(self):
        self.completed = True
        self.message = "Concluído!"
        logger.info(f"Progress {self.session_id}: Concluído.")

def get_progress_tracker(session_id: str) -> EnhancedProgressTracker:
    if session_id not in _progress_trackers:
        _progress_trackers[session_id] = EnhancedProgressTracker(session_id)
    return _progress_trackers[session_id]

def update_analysis_progress(session_id: str, step: int, message: str, details: str = None):
    tracker = get_progress_tracker(session_id)
    tracker.update(step, message, details)

# Add the helper functions to the blueprint's scope
def obter_sessoes():
    """Obtém lista de sessões salvas"""
    try:
        # Call the function from the imported module
        return auto_save_manager.listar_sessoes()
    except Exception as e:
        logger.error(f"Erro ao obter sessões: {e}")
        return []

def obter_progresso_sessao(session_id: str):
    """Obtém progresso de uma sessão específica"""
    try:
        # Call the function from the imported module
        return auto_save_manager.obter_info_sessao(session_id)
    except Exception as e:
        logger.error(f"Erro ao obter progresso da sessão {session_id}: {e}")
        return None


@progress_bp.route("/api/sessions", methods=["GET"])
def get_sessions():
    """Obtém todas as sessões salvas"""
    try:
        sessions = obter_sessoes()
        return jsonify({
            "success": True,
            "sessions": sessions,
            "total": len(sessions)
        })
    except Exception as e:
        logger.error(f"❌ Erro ao obter sessões: {e}")
        return jsonify({
            "success": False,
            "error": str(e),
            "sessions": [],
            "total": 0
        }), 500

@progress_bp.route("/api/sessions/<session_id>/progress", methods=["GET"])
def get_session_progress(session_id):
    """Obtém progresso de uma sessão específica"""
    try:
        # Retrieve the progress tracker for the session
        tracker = _progress_trackers.get(session_id)
        if tracker is None:
            # If not in memory, try to load from auto_save_manager if it stores progress
            progress_data = obter_progresso_sessao(session_id)
            if progress_data:
                # Reconstruct tracker from saved data if necessary
                # This part might need more sophisticated logic depending on how progress is saved
                return jsonify({
                    "success": True,
                    "session_id": session_id,
                    "progress": progress_data
                })
            else:
                return jsonify({
                    "success": False,
                    "error": f"Progresso para a sessão {session_id} não encontrado.",
                    "session_id": session_id,
                    "progress": {}
                }), 404

        return jsonify({
            "success": True,
            "session_id": session_id,
            "progress": {
                "current_step": tracker.current_step,
                "message": tracker.message,
                "details": tracker.details,
                "completed": tracker.completed
            }
        })
    except Exception as e:
        logger.error(f"❌ Erro ao obter progresso da sessão {session_id}: {e}")
        return jsonify({
            "success": False,
            "error": str(e),
            "session_id": session_id,
            "progress": {}
        }), 500

@progress_bp.route("/api/sessions/<session_id>/results", methods=["GET"])
def get_session_results(session_id):
    """Obtém resultados de uma sessão específica"""
    try:
        # Busca dados da sessão
        # AUTO_SAVE_DIR is assumed to be defined in auto_save_manager or a config file
        # If AUTO_SAVE_DIR is not defined, it will cause an ImportError or NameError
        # For now, assuming it's available or will be handled by the auto_save_manager import
        session_dir = os.path.join(auto_save_manager.AUTO_SAVE_DIR, "analise_completa", session_id)


        if not os.path.exists(session_dir):
            return jsonify({
                "success": False,
                "error": "Sessão não encontrada",
                "session_id": session_id,
                "results": {}
            }), 404

        results = {}

        # Coleta todos os arquivos da sessão
        for filename in os.listdir(session_dir):
            if filename.endswith(".json"):
                filepath = os.path.join(session_dir, filename)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        component_name = filename.replace(".json", "").replace(f"_{session_id}", "")
                        results[component_name] = data
                except Exception as e:
                    logger.warning(f"⚠️ Erro ao carregar {filename}: {e}")
                    continue

        if not results:
            return jsonify({
                "success": False,
                "error": "Nenhum resultado encontrado para esta sessão",
                "session_id": session_id,
                "results": {}
            }), 404

        return jsonify({
            "success": True,
            "session_id": session_id,
            "results": results,
            "components_count": len(results)
        })

    except NameError:
        logger.error("❌ AUTO_SAVE_DIR não está definido. Verifique a configuração de auto_save_manager.")
        return jsonify({
            "success": False,
            "error": "Configuração de diretório de salvamento automático ausente.",
            "session_id": session_id,
            "results": {}
        }), 500
    except Exception as e:
        logger.error(f"❌ Erro ao obter resultados da sessão {session_id}: {e}")
        return jsonify({
            "success": False,
            "error": str(e),
            "session_id": session_id,
            "results": {}
        }), 500

@progress_bp.route("/api/sessions/clear", methods=["POST"])
def clear_sessions():
    """Limpa todas as sessões salvas"""
    try:
        data = request.get_json() or {}
        confirm = data.get("confirm", False)

        if not confirm:
            return jsonify({
                "success": False,
                "error": "Confirmação necessária para limpar sessões",
                "cleared_count": 0
            }), 400

        # Conta sessões antes de limpar
        sessions_before = obter_sessoes()
        count_before = len(sessions_before)

        # Remove diretórios de análise
        dirs_to_clear = [
            os.path.join(auto_save_manager.AUTO_SAVE_DIR, "analise_completa"),
            os.path.join(auto_save_manager.AUTO_SAVE_DIR, "drivers_mentais"),
            os.path.join(auto_save_manager.AUTO_SAVE_DIR, "pesquisa_web"),
            os.path.join(auto_save_manager.AUTO_SAVE_DIR, "logs")
        ]

        cleared_count = 0
        for dir_path in dirs_to_clear:
            if os.path.exists(dir_path):
                try:
                    shutil.rmtree(dir_path)
                    os.makedirs(dir_path, exist_ok=True)
                    cleared_count += 1
                    logger.info(f"🧹 Diretório {dir_path} limpo")
                except Exception as e:
                    logger.warning(f"⚠️ Erro ao limpar {dir_path}: {e}")

        # Limpa também diretório de relatórios intermediários
        relatorios_dir = os.path.join(auto_save_manager.AUTO_SAVE_DIR, "relatorios_intermediarios")
        if os.path.exists(relatorios_dir):
            try:
                shutil.rmtree(relatorios_dir)
                os.makedirs(relatorios_dir, exist_ok=True)
                logger.info("🧹 Relatórios intermediários limpos")
            except Exception as e:
                logger.warning(f"⚠️ Erro ao limpar relatórios: {e}")

        return jsonify({
            "success": True,
            "message": f"Sessões limpas com sucesso",
            "cleared_count": count_before,
            "directories_cleared": cleared_count
        })

    except NameError:
        logger.error("❌ AUTO_SAVE_DIR não está definido. Verifique a configuração de auto_save_manager.")
        return jsonify({
            "success": False,
            "error": "Configuração de diretório de salvamento automático ausente.",
            "cleared_count": 0
        }), 500
    except Exception as e:
        logger.error(f"❌ Erro ao limpar sessões: {e}")
        return jsonify({
            "success": False,
            "error": str(e),
            "cleared_count": 0
        }), 500

@progress_bp.route("/api/sessions/<session_id>", methods=["DELETE"])
def delete_session(session_id):
    """Remove uma sessão específica"""
    try:
        # Remove da análise completa
        session_dir = os.path.join(auto_save_manager.AUTO_SAVE_DIR, "analise_completa", session_id)
        removed_files = 0

        if os.path.exists(session_dir):
            shutil.rmtree(session_dir)
            removed_files += 1

        # Remove dos drivers mentais
        drivers_dir = os.path.join(auto_save_manager.AUTO_SAVE_DIR, "drivers_mentais", session_id)
        if os.path.exists(drivers_dir):
            shutil.rmtree(drivers_dir)
            removed_files += 1

        # Remove dos logs
        logs_dir = os.path.join(auto_save_manager.AUTO_SAVE_DIR, "logs", session_id)
        if os.path.exists(logs_dir):
            shutil.rmtree(logs_dir)
            removed_files += 1

        # Remove da pesquisa web
        web_dir = os.path.join(auto_save_manager.AUTO_SAVE_DIR, "pesquisa_web", session_id)
        if os.path.exists(web_dir):
            shutil.rmtree(web_dir)
            removed_files += 1

        # Remove dos relatórios intermediários
        relatorio_dir = os.path.join(auto_save_manager.AUTO_SAVE_DIR, "relatorios_intermediarios", session_id)
        if os.path.exists(relatorio_dir):
            shutil.rmtree(relatorio_dir)
            removed_files += 1

        if removed_files == 0:
            return jsonify({
                "success": False,
                "error": "Sessão não encontrada",
                "session_id": session_id
            }), 404

        return jsonify({
            "success": True,
            "message": f"Sessão {session_id} removida com sucesso",
            "session_id": session_id,
            "removed_files": removed_files
        })

    except NameError:
        logger.error("❌ AUTO_SAVE_DIR não está definido. Verifique a configuração de auto_save_manager.")
        return jsonify({
            "success": False,
            "error": "Configuração de diretório de salvamento automático ausente.",
            "session_id": session_id
        }), 500
    except Exception as e:
        logger.error(f"❌ Erro ao remover sessão {session_id}: {e}")
        return jsonify({
            "success": False,
            "error": str(e),
            "session_id": session_id
        }), 500

@progress_bp.route("/api/system/status", methods=["GET"])
def get_system_status():
    """Obtém status do sistema"""
    try:
        # Verifica APIs configuradas
        apis_status = {
            "gemini": bool(os.getenv("GEMINI_API_KEY")),
            "groq": bool(os.getenv("GROQ_API_KEY")),
            "openai": bool(os.getenv("OPENAI_API_KEY")),
            "google_search": bool(os.getenv("GOOGLE_SEARCH_KEY") and os.getenv("GOOGLE_CSE_ID")),
            "serper": bool(os.getenv("SERPER_API_KEY")),
            "exa": bool(os.getenv("EXA_API_KEY"))
        }

        # Conta sessões
        sessions = obter_sessoes()

        # Calcula uso de disco
        total_size = 0
        for root, dirs, files in os.walk(auto_save_manager.AUTO_SAVE_DIR):
            for file in files:
                filepath = os.path.join(root, file)
                try:
                    total_size += os.path.getsize(filepath)
                except:
                    pass

        return jsonify({
            "success": True,
            "apis": apis_status,
            "sessions": {
                "count": len(sessions),
                "disk_usage_mb": round(total_size / 1024 / 1024, 2)
            },
            "timestamp": datetime.now().isoformat()
        })

    except NameError:
        logger.error("❌ AUTO_SAVE_DIR não está definido. Verifique a configuração de auto_save_manager.")
        return jsonify({
            "success": False,
            "error": "Configuração de diretório de salvamento automático ausente."
        }), 500
    except Exception as e:
        logger.error(f"❌ Erro ao obter status do sistema: {e}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


