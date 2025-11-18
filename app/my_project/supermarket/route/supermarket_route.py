# app/my_project/supermarket/route/supermarket_route.py
from flask import Blueprint, jsonify, request, abort
from app.my_project.supermarket.service import supermarket_service

supermarket_bp = Blueprint('supermarket_bp', __name__, url_prefix='/supermarkets')


@supermarket_bp.route('/', methods=['GET'])
def get_all_supermarkets():
    supermarkets = supermarket_service.get_all_supermarkets()
    return jsonify(supermarkets), 200


@supermarket_bp.route('/<int:supermarket_id>', methods=['GET'])
def get_supermarket(supermarket_id):
    supermarket = supermarket_service.get_supermarket_by_id(supermarket_id)
    if not supermarket:
        return abort(404, description="Supermarket not found")
    return jsonify(supermarket), 200


@supermarket_bp.route('/', methods=['POST'])
def create_supermarket():
    data = request.json
    if not data:
        return abort(400, description="Invalid input data.")
    new_supermarket = supermarket_service.create_supermarket(data)
    return jsonify(new_supermarket), 201


@supermarket_bp.route('/<int:supermarket_id>', methods=['PUT'])
def update_supermarket(supermarket_id):
    data = request.json
    if not data:
        return abort(400, description="Invalid input data.")
    updated_supermarket = supermarket_service.update_supermarket(supermarket_id, data)
    if not updated_supermarket:
        return abort(404, description="Supermarket not found")
    return jsonify(updated_supermarket), 200


@supermarket_bp.route('/<int:supermarket_id>', methods=['DELETE'])
def delete_supermarket(supermarket_id):
    success = supermarket_service.delete_supermarket(supermarket_id)
    if not success:
        return abort(404, description="Supermarket not found")
    return jsonify(message="Supermarket deleted successfully"), 200


# --- РОУТ ДЛЯ M:1 (Вимога Лабораторної) ---
@supermarket_bp.route('/<int:supermarket_id>/departments', methods=['GET'])
def get_departments_for_supermarket(supermarket_id):
    """
    GET /supermarkets/<id>/departments
    Отримує всі відділи для конкретного супермаркету.
    """
    departments = supermarket_service.get_departments_for_supermarket(supermarket_id)
    if departments is None:
        # Це означає, що сам супермаркет не знайдено
        return abort(404, description="Supermarket not found")

    # Повертаємо список відділів (може бути порожнім)
    return jsonify(departments), 200