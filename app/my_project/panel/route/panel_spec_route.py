from flask import Blueprint, jsonify, request, abort
from app.my_project.panel.service import panel_spec_service

panel_spec_bp = Blueprint('panel_spec_bp', __name__, url_prefix='/panel-specs')

@panel_spec_bp.route('/', methods=['GET'])
def get_all_specs():
    return jsonify(panel_spec_service.get_all_specs()), 200

@panel_spec_bp.route('/<int:spec_id>', methods=['GET'])
def get_spec(spec_id):
    spec = panel_spec_service.get_spec_by_id(spec_id)
    if not spec:
        return abort(404, description="PanelSpec not found")
    return jsonify(spec), 200

@panel_spec_bp.route('/', methods=['POST'])
def create_spec():
    data = request.json
    if not data:
        return abort(400, description="Invalid input data.")
    return jsonify(panel_spec_service.create_spec(data)), 201

@panel_spec_bp.route('/<int:spec_id>', methods=['PUT'])
def update_spec(spec_id):
    data = request.json
    if not data:
        return abort(400, description="Invalid input data.")
    spec = panel_spec_service.update_spec(spec_id, data)
    if not spec:
        return abort(404, description="PanelSpec not found")
    return jsonify(spec), 200

@panel_spec_bp.route('/<int:spec_id>', methods=['DELETE'])
def delete_spec(spec_id):
    if not panel_spec_service.delete_spec(spec_id):
        return abort(404, description="PanelSpec not found")
    return jsonify(message="PanelSpec deleted successfully"), 200