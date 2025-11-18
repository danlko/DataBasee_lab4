# app/my_project/panel/route/panel_route.py
from flask import Blueprint, jsonify, request, abort
from app.my_project.panel.service import panel_service

panel_bp = Blueprint('panel_bp', __name__, url_prefix='/panels')

# --- CRUD для Панелей ---
@panel_bp.route('/', methods=['GET'])
def get_all_panels():
    return jsonify(panel_service.get_all_panels()), 200

@panel_bp.route('/<int:panel_id>', methods=['GET'])
def get_panel(panel_id):
    panel = panel_service.get_panel_by_id(panel_id)
    if not panel:
        return abort(404, description="Panel not found")
    return jsonify(panel), 200

@panel_bp.route('/', methods=['POST'])
def create_panel():
    data = request.json
    if not data:
        return abort(400, description="Invalid input data.")
    return jsonify(panel_service.create_panel(data)), 201

@panel_bp.route('/<int:panel_id>', methods=['PUT'])
def update_panel(panel_id):
    data = request.json
    if not data:
        return abort(400, description="Invalid input data.")
    panel = panel_service.update_panel(panel_id, data)
    if not panel:
        return abort(404, description="Panel not found")
    return jsonify(panel), 200

@panel_bp.route('/<int:panel_id>', methods=['DELETE'])
def delete_panel(panel_id):
    if not panel_service.delete_panel(panel_id):
        return abort(404, description="Panel not found")
    return jsonify(message="Panel deleted successfully"), 200

# --- РОУТИ ДЛЯ M:M (Вимога Лабораторної) ---

@panel_bp.route('/<int:panel_id>/videos', methods=['GET'])
def get_videos_for_panel(panel_id):
    """
    GET /panels/<id>/videos
    Отримує всі відео, що транслюються на цій панелі.
    """
    videos = panel_service.get_videos_for_panel(panel_id)
    if videos is None:
        return abort(404, description="Panel not found")
    return jsonify(videos), 200

@panel_bp.route('/<int:panel_id>/videos/<int:video_id>', methods=['POST'])
def add_video_to_panel(panel_id, video_id):
    """
    POST /panels/<panel_id>/videos/<video_id>
    Створює зв'язок M:M між панеллю та відео.
    """
    panel = panel_service.add_video_to_panel(panel_id, video_id)
    if not panel:
        return abort(404, description="Panel or Video not found")
    return jsonify(panel), 201

@panel_bp.route('/<int:panel_id>/videos/<int:video_id>', methods=['DELETE'])
def remove_video_from_panel(panel_id, video_id):
    """
    DELETE /panels/<panel_id>/videos/<video_id>
    Видаляє зв'язок M:M.
    """
    if not panel_service.remove_video_from_panel(panel_id, video_id):
        return abort(404, description="Link not found or Panel/Video not found")
    return jsonify(message="Video removed from panel"), 200