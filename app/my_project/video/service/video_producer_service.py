from app.my_project.video.dao import video_producer_dao

class VideoProducerService:
    def get_all_producers(self):
        producers = video_producer_dao.get_all()
        return [p.to_dict() for p in producers]

    def get_producer_by_id(self, producer_id):
        producer = video_producer_dao.get_by_id(producer_id)
        return producer.to_dict() if producer else None

    def create_producer(self, data):
        return video_producer_dao.create(data).to_dict()

    def update_producer(self, producer_id, data):
        updated_producer = video_producer_dao.update(producer_id, data)
        return updated_producer.to_dict() if updated_producer else None

    def delete_producer(self, producer_id):
        return video_producer_dao.delete(producer_id)