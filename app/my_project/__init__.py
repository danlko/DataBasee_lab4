from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .supermarket.domain import models
from .video.domain import models
from .panel.domain import models