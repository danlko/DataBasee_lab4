from app.my_project import db
from app.my_project.panel.domain.models import Panel
from app.my_project.video.domain.models import Video


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

    def get_videos_for_panel(self, panel_id):
        panel = self.get_by_id(panel_id)
        if panel:
            return panel.videos
        return None

    def add_video_to_panel(self, panel_id, video_id):
        panel = self.get_by_id(panel_id)
        video = db.session.query(Video).get(video_id)

        if panel and video:
            panel.videos.append(video)
            db.session.commit()
            return panel
        return None

    def remove_video_from_panel(self, panel_id, video_id):
        panel = self.get_by_id(panel_id)
        video = db.session.query(Video).get(video_id)

        if panel and video and video in panel.videos:
            panel.videos.remove(video)
            db.session.commit()
            return True
        return False