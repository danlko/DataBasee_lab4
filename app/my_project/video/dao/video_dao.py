from app.my_project import db
from app.my_project.video.domain.models import Video

class VideoDAO:
    def get_all(self):
        return db.session.query(Video).all()

    def get_by_id(self, video_id):
        return db.session.query(Video).get(video_id)

    def create(self, data):
        new_video = Video(**data)
        db.session.add(new_video)
        db.session.commit()
        return new_video

    def update(self, video_id, data):
        video = self.get_by_id(video_id)
        if video:
            for key, value in data.items():
                setattr(video, key, value)
            db.session.commit()
            return video
        return None

    def delete(self, video_id):
        video = self.get_by_id(video_id)
        if video:
            db.session.delete(video)
            db.session.commit()
            return True
        return False