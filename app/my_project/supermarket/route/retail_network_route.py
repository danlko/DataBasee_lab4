# app/my_project/supermarket/route/retail_network_route.py

from flask import Blueprint, jsonify, request, abort
# Імпортуємо наш готовий сервіс
from app.my_project.supermarket.service import retail_network_service

# Створюємо "Креслення" (Blueprint) для наших роутів
# 'retail_network_bp' - унікальне ім'я для реєстрації
retail_network_bp = Blueprint('retail_network_bp', __name__, url_prefix='/networks')


# --- РОУТИ ДЛЯ CRUD-ОПЕРАЦІЙ ---

@retail_network_bp.route('/', methods=['GET'])
def get_all_networks():
    """
    GET /networks
    Отримує список всіх роздрібних мереж.
    """
    networks = retail_network_service.get_all_networks()
    return jsonify(networks), 200  # 200 OK


@retail_network_bp.route('/<int:network_id>', methods=['GET'])
def get_network(network_id):
    """
    GET /networks/<id>
    Отримує одну мережу за ID.
    """
    network = retail_network_service.get_network_by_id(network_id)
    if not network:
        # 'abort' генерує HTTP-помилку
        return abort(404, description="RetailNetwork not found")
    return jsonify(network), 200  # 200 OK


@retail_network_bp.route('/', methods=['POST'])
def create_network():
    """
    POST /networks
    Створює нову мережу.
    Очікує JSON в тілі запиту, наприклад: {"name": "Нова Мережа"}
    """
    # request.json отримує дані, надіслані в Postman
    data = request.json
    if not data or 'name' not in data:
        return abort(400, description="Invalid input data. 'name' is required.")

    new_network = retail_network_service.create_network(data)
    # Повертаємо створений об'єкт і статус 201 Created
    return jsonify(new_network), 201


@retail_network_bp.route('/<int:network_id>', methods=['PUT'])
def update_network(network_id):
    """
    PUT /networks/<id>
    Оновлює існуючу мережу.
    Очікує JSON в тілі запиту, наприклад: {"name": "Оновлена Назва"}
    """
    data = request.json
    if not data:
        return abort(400, description="Invalid input data.")

    updated_network = retail_network_service.update_network(network_id, data)

    if not updated_network:
        return abort(404, description="RetailNetwork not found")

    return jsonify(updated_network), 200  # 200 OK


@retail_network_bp.route('/<int:network_id>', methods=['DELETE'])
def delete_network(network_id):
    """
    DELETE /networks/<id>
    Видаляє мережу за ID.
    """
    success = retail_network_service.delete_network(network_id)
    if not success:
        return abort(404, description="RetailNetwork not found")

    # Повертаємо порожню відповідь і статус 204 No Content
    return jsonify(message="RetailNetwork deleted successfully"), 200