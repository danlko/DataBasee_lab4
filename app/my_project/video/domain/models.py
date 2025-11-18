from app.my_project import db

class Brand(db.Model):
    __tablename__ = 'brand'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    videos = db.relationship('Video', back_populates='brand')

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


class VideoProducer(db.Model):
    __tablename__ = 'video_producer'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)

    # Зв'язок (One-to-Many до Video)
    videos = db.relationship('Video', back_populates='video_producer')

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'country': self.country}


class Video(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    format = db.Column(db.String(50), nullable=False)

    brand_id = db.Column(db.BigInteger, db.ForeignKey('brand.id'), nullable=False)
    producer_id = db.Column(db.BigInteger, db.ForeignKey('video_producer.id'), nullable=False)

    brand = db.relationship('Brand', back_populates='videos')
    video_producer = db.relationship('VideoProducer', back_populates='videos')

    panels = db.relationship('Panel', secondary='video_panel', back_populates='videos')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'duration': self.duration,
            'format': self.format,
            'brand_id': self.brand_id,
            'producer_id': self.producer_id,
            'brand_name': self.brand.name if self.brand else None,
            'producer_name': self.video_producer.name if self.video_producer else None
        }