from flask import Blueprint, jsonify, request, abort
from app.my_project.video.service import video_producer_service

video_producer_bp = Blueprint('video_producer_bp', __name__, url_prefix='/video-producers')

@video_producer_bp.route('/', methods=['GET'])
def get_all_producers():
    return jsonify(video_producer_service.get_all_producers()), 200

@video_producer_bp.route('/<int:producer_id>', methods=['GET'])
def get_producer(producer_id):
    producer = video_producer_service.get_producer_by_id(producer_id)
    if not producer:
        return abort(404, description="VideoProducer not found")
    return jsonify(producer), 200

@video_producer_bp.route('/', methods=['POST'])
def create_producer():
    data = request.json
    if not data or 'name' not in data:
        return abort(400, description="Invalid input data.")
    return jsonify(video_producer_service.create_producer(data)), 201

@video_producer_bp.route('/<int:producer_id>', methods=['PUT'])
def update_producer(producer_id):
    data = request.json
    if not data:
        return abort(400, description="Invalid input data.")
    producer = video_producer_service.update_producer(producer_id, data)
    if not producer:
        return abort(404, description="VideoProducer not found")
    return jsonify(producer), 200

@video_producer_bp.route('/<int:producer_id>', methods=['DELETE'])
def delete_producer(producer_id):
    if not video_producer_service.delete_producer(producer_id):
        return abort(404, description="VideoProducer not found")
    return jsonify(message="VideoProducer deleted successfully"), 200