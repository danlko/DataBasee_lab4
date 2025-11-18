# app/my_project/video/service/video_service.py
from app.my_project.video.dao import video_dao

class VideoService:
    def get_all_videos(self):
        videos = video_dao.get_all()
        return [v.to_dict() for v in videos]

    def get_video_by_id(self, video_id):
        video = video_dao.get_by_id(video_id)
        return video.to_dict() if video else None

    def create_video(self, data):
        return video_dao.create(data).to_dict()

    def update_video(self, video_id, data):
        updated_video = video_dao.update(video_id, data)
        return updated_video.to_dict() if updated_video else None

    def delete_video(self, video_id):
        return video_dao.delete(video_id)