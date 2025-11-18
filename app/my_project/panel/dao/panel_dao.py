# app/my_project/panel/dao/panel_dao.py
from app.my_project import db
from app.my_project.panel.domain.models import Panel
from app.my_project.video.domain.models import Video  # Потрібно для M:M


class PanelDAO:
    def get_all(self):
        return db.session.query(Panel).all()

    def get_by_id(self, panel_id):
        return db.session.query(Panel).get(panel_id)

    def create(self, data):
        new_panel = Panel(**data)
        db.session.add(new_panel)
        db.session.commit()
        return new_panel

    def update(self, panel_id, data):
        panel = self.get_by_id(panel_id)
        if panel:
            for key, value in data.items():
                setattr(panel, key, value)
            db.session.commit()
            return panel
        return None

    def delete(self, panel_id):
        panel = self.get_by_id(panel_id)
        if panel:
            db.session.delete(panel)
            db.session.commit()
            return True
        return False

    # --- Специфічні запити для M:M (Вимога Лабораторної) ---
    def get_videos_for_panel(self, panel_id):
        """
        Отримує всі відео, пов'язані з конкретною панеллю.
        """
        panel = self.get_by_id(panel_id)
        if panel:
            # SQLAlchemy магія: просто звертаємось до .videos
            return panel.videos
        return None

    def add_video_to_panel(self, panel_id, video_id):
        """
        Додає існуюче відео до існуючої панелі (створює M:M зв'язок).
        """
        panel = self.get_by_id(panel_id)
        video = db.session.query(Video).get(video_id)

        if panel and video:
            # Просто додаємо об'єкт video до списку .videos панелі
            panel.videos.append(video)
            db.session.commit()
            return panel
        return None

    def remove_video_from_panel(self, panel_id, video_id):
        """
        Видаляє зв'язок M:M між панеллю та відео.
        """
        panel = self.get_by_id(panel_id)
        video = db.session.query(Video).get(video_id)

        if panel and video and video in panel.videos:
            # Видаляємо об'єкт video зі списку
            panel.videos.remove(video)
            db.session.commit()
            return True
        return False