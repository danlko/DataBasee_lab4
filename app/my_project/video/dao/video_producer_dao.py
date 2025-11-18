# app/my_project/video/dao/video_producer_dao.py
from app.my_project import db
from app.my_project.video.domain.models import VideoProducer

class VideoProducerDAO:
    def get_all(self):
        return db.session.query(VideoProducer).all()

    def get_by_id(self, producer_id):
        return db.session.query(VideoProducer).get(producer_id)

    def create(self, data):
        new_producer = VideoProducer(**data)
        db.session.add(new_producer)
        db.session.commit()
        return new_producer

    def update(self, producer_id, data):
        producer = self.get_by_id(producer_id)
        if producer:
            for key, value in data.items():
                setattr(producer, key, value)
            db.session.commit()
            return producer
        return None

    def delete(self, producer_id):
        producer = self.get_by_id(producer_id)
        if producer:
            db.session.delete(producer)
            db.session.commit()
            return True
        return False