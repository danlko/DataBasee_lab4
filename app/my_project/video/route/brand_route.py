from flask import Blueprint, jsonify, request, abort
from app.my_project.video.service import brand_service

brand_bp = Blueprint('brand_bp', __name__, url_prefix='/brands')

@brand_bp.route('/', methods=['GET'])
def get_all_brands():
    return jsonify(brand_service.get_all_brands()), 200

@brand_bp.route('/<int:brand_id>', methods=['GET'])
def get_brand(brand_id):
    brand = brand_service.get_brand_by_id(brand_id)
    if not brand:
        return abort(404, description="Brand not found")
    return jsonify(brand), 200

@brand_bp.route('/', methods=['POST'])
def create_brand():
    data = request.json
    if not data or 'name' not in data:
        return abort(400, description="Invalid input data.")
    return jsonify(brand_service.create_brand(data)), 201

@brand_bp.route('/<int:brand_id>', methods=['PUT'])
def update_brand(brand_id):
    data = request.json
    if not data:
        return abort(400, description="Invalid input data.")
    brand = brand_service.update_brand(brand_id, data)
    if not brand:
        return abort(404, description="Brand not found")
    return jsonify(brand), 200

@brand_bp.route('/<int:brand_id>', methods=['DELETE'])
def delete_brand(brand_id):
    if not brand_service.delete_brand(brand_id):
        return abort(404, description="Brand not found")
    return jsonify(message="Brand deleted successfully"), 200