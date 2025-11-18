# app/my_project/video/dao/__init__.py
from .brand_dao import BrandDAO
from .video_producer_dao import VideoProducerDAO
from .video_dao import VideoDAO

brand_dao = BrandDAO()
video_producer_dao = VideoProducerDAO()
video_dao = VideoDAO()