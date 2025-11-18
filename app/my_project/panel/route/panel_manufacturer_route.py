# app/my_project/panel/route/panel_manufacturer_route.py
from flask import Blueprint, jsonify, request, abort
from app.my_project.panel.service import panel_manufacturer_service

panel_manufacturer_bp = Blueprint('panel_manufacturer_bp', __name__, url_prefix='/panel-manufacturers')

@panel_manufacturer_bp.route('/', methods=['GET'])
def get_all_manufacturers():
    return jsonify(panel_manufacturer_service.get_all_manufacturers()), 200

@panel_manufacturer_bp.route('/<int:manufacturer_id>', methods=['GET'])
def get_manufacturer(manufacturer_id):
    manufacturer = panel_manufacturer_service.get_manufacturer_by_id(manufacturer_id)
    if not manufacturer:
        return abort(404, description="PanelManufacturer not found")
    return jsonify(manufacturer), 200

@panel_manufacturer_bp.route('/', methods=['POST'])
def create_manufacturer():
    data = request.json
    if not data or 'name' not in data:
        return abort(400, description="Invalid input data.")
    return jsonify(panel_manufacturer_service.create_manufacturer(data)), 201

@panel_manufacturer_bp.route('/<int:manufacturer_id>', methods=['PUT'])
def update_manufacturer(manufacturer_id):
    data = request.json
    if not data:
        return abort(400, description="Invalid input data.")
    manufacturer = panel_manufacturer_service.update_manufacturer(manufacturer_id, data)
    if not manufacturer:
        return abort(404, description="PanelManufacturer not found")
    return jsonify(manufacturer), 200

@panel_manufacturer_bp.route('/<int:manufacturer_id>', methods=['DELETE'])
def delete_manufacturer(manufacturer_id):
    if not panel_manufacturer_service.delete_manufacturer(manufacturer_id):
        return abort(404, description="PanelManufacturer not found")
    return jsonify(message="PanelManufacturer deleted successfully"), 200