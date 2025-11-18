from flask import Blueprint, jsonify, request, abort
from app.my_project.video.service import video_service

video_bp = Blueprint('video_bp', __name__, url_prefix='/videos')

@video_bp.route('/', methods=['GET'])
def get_all_videos():
    return jsonify(video_service.get_all_videos()), 200

@video_bp.route('/<int:video_id>', methods=['GET'])
def get_video(video_id):
    video = video_service.get_video_by_id(video_id)
    if not video:
        return abort(404, description="Video not found")
    return jsonify(video), 200

@video_bp.route('/', methods=['POST'])
def create_video():
    data = request.json
    if not data:
        return abort(400, description="Invalid input data.")
    return jsonify(video_service.create_video(data)), 201

@video_bp.route('/<int:video_id>', methods=['PUT'])
def update_video(video_id):
    data = request.json
    if not data:
        return abort(400, description="Invalid input data.")
    video = video_service.update_video(video_id, data)
    if not video:
        return abort(404, description="Video not found")
    return jsonify(video), 200

@video_bp.route('/<int:video_id>', methods=['DELETE'])
def delete_video(video_id):
    if not video_service.delete_video(video_id):
        return abort(404, description="Video not found")
    return jsonify(message="Video deleted successfully"), 200