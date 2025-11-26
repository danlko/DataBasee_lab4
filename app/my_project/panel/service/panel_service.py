from app.my_project.panel.dao import panel_dao


class PanelService:
    def get_all_panels(self):
        """
        Стандартний вивід панелей для /api/panels/
        """
        panels = panel_dao.get_all()
        return [p.to_dict() for p in panels]

    def get_all_connections(self):
        """
        ОСЬ ЦЕ ДЛЯ URL: /api/panels/videos
        Повертає плоский список зв'язків Panel-Video.
        """
        panels = panel_dao.get_all()
        result = []

        for panel in panels:
            # Якщо у панелі немає відео, цей цикл просто не спрацює
            for video in panel.videos:
                brand_name = video.brand.name if video.brand else "No Brand"

                # Формуємо плоский об'єкт, як ви просили
                item = {
                    "panel_id": panel.id,
                    "video_brand_name": brand_name,
                    "video_id": video.id,
                    "video_title": video.title
                }
                result.append(item)

        return result

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

    def get_videos_for_panel(self, panel_id):
        """
        Для URL: /api/panels/<id>/videos
        """
        panel = panel_dao.get_by_id(panel_id)
        if not panel:
            return None

        custom_response = []
        for video in panel.videos:
            brand_name = video.brand.name if video.brand else "No Brand"
            item = {
                "video_brand_name": brand_name,
                "panel_serial_number": panel.serial_number,
                "panel_id": panel.id,
                "video_id": video.id,
                "video_title": video.title
            }
            custom_response.append(item)
        return custom_response

    def add_video_to_panel(self, panel_id, video_id):
        panel = panel_dao.add_video_to_panel(panel_id, video_id)
        return panel.to_dict() if panel else None

    def remove_video_from_panel(self, panel_id, video_id):
        return panel_dao.remove_video_from_panel(panel_id, video_id)