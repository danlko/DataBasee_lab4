from flask import Blueprint, jsonify, request, abort
from app.my_project.supermarket.service import retail_network_service

retail_network_bp = Blueprint('retail_network_bp', __name__, url_prefix='/networks')

@retail_network_bp.route('/', methods=['GET'])
def get_all_networks():
    networks = retail_network_service.get_all_networks()
    return jsonify(networks), 200  # 200 OK


@retail_network_bp.route('/<int:network_id>', methods=['GET'])
def get_network(network_id):
    network = retail_network_service.get_network_by_id(network_id)
    if not network:
        # 'abort' генерує HTTP-помилку
        return abort(404, description="RetailNetwork not found")
    return jsonify(network), 200  # 200 OK


@retail_network_bp.route('/', methods=['POST'])
def create_network():
    data = request.json
    if not data or 'name' not in data:
        return abort(400, description="Invalid input data. 'name' is required.")

    new_network = retail_network_service.create_network(data)
    return jsonify(new_network), 201


@retail_network_bp.route('/<int:network_id>', methods=['PUT'])
def update_network(network_id):
    data = request.json
    if not data:
        return abort(400, description="Invalid input data.")

    updated_network = retail_network_service.update_network(network_id, data)

    if not updated_network:
        return abort(404, description="RetailNetwork not found")

    return jsonify(updated_network), 200  # 200 OK


@retail_network_bp.route('/<int:network_id>', methods=['DELETE'])
def delete_network(network_id):
    success = retail_network_service.delete_network(network_id)
    if not success:
        return abort(404, description="RetailNetwork not found")

    return jsonify(message="RetailNetwork deleted successfully"), 200