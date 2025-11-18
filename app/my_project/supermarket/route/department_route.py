# app/my_project/supermarket/route/department_route.py
from flask import Blueprint, jsonify, request, abort
from app.my_project.supermarket.service import department_service

department_bp = Blueprint('department_bp', __name__, url_prefix='/departments')

@department_bp.route('/', methods=['GET'])
def get_all_departments():
    departments = department_service.get_all_departments()
    return jsonify(departments), 200

@department_bp.route('/<int:department_id>', methods=['GET'])
def get_department(department_id):
    department = department_service.get_department_by_id(department_id)
    if not department:
        return abort(404, description="Department not found")
    return jsonify(department), 200

@department_bp.route('/', methods=['POST'])
def create_department():
    data = request.json
    if not data:
        return abort(400, description="Invalid input data.")
    new_department = department_service.create_department(data)
    return jsonify(new_department), 201

@department_bp.route('/<int:department_id>', methods=['PUT'])
def update_department(department_id):
    data = request.json
    if not data:
        return abort(400, description="Invalid input data.")
    updated_department = department_service.update_department(department_id, data)
    if not updated_department:
        return abort(404, description="Department not found")
    return jsonify(updated_department), 200

@department_bp.route('/<int:department_id>', methods=['DELETE'])
def delete_department(department_id):
    success = department_service.delete_department(department_id)
    if not success:
        return abort(404, description="Department not found")
    return jsonify(message="Department deleted successfully"), 200