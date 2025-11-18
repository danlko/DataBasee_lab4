# app/my_project/__init__.py

from flask_sqlalchemy import SQLAlchemy

# 1. СТВОРЮЄМО 'db' ТУТ,
#    а не в main.py
db = SQLAlchemy()

# 2. Також імпортуємо всі моделі,
#    щоб SQLAlchemy їх "побачив" при ініціалізації.
from .supermarket.domain import models
from .video.domain import models
from .panel.domain import models