# app/my_project/panel/service/panel_service.py
from app.my_project.panel.dao import panel_dao

class PanelService:
    def get_all_panels(self):
        panels = panel_dao.get_all()
        return [p.to_dict() for p in panels]

    def get_panel_by_id(self, panel_id):
        panel = panel_dao.get_by_id(panel_id)
        return panel.to_dict() if panel else None

    def create_panel(self, data):
        return panel_dao.create(data).to_dict()

    def update_panel(self, panel_id, data):
        updated = panel_dao.update(panel_id, data)
        return updated.to_dict() if updated else None

    def delete_panel(self, panel_id):
        return panel_dao.delete(panel_id)

    # --- Специфічні запити для M:M (Вимога Лабораторної) ---
    def get_videos_for_panel(self, panel_id):
        videos = panel_dao.get_videos_for_panel(panel_id)
        if videos is not None:
            return [v.to_dict() for v in videos]
        return None # Якщо панель не знайдено

    def add_video_to_panel(self, panel_id, video_id):
        panel = panel_dao.add_video_to_panel(panel_id, video_id)
        return panel.to_dict() if panel else None

    def remove_video_from_panel(self, panel_id, video_id):
        return panel_dao.remove_video_from_panel(panel_id, video_id)