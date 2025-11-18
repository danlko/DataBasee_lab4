# app/my_project/panel/service/panel_manufacturer_service.py
from app.my_project.panel.dao import panel_manufacturer_dao

class PanelManufacturerService:
    def get_all_manufacturers(self):
        manufacturers = panel_manufacturer_dao.get_all()
        return [m.to_dict() for m in manufacturers]

    def get_manufacturer_by_id(self, manufacturer_id):
        manufacturer = panel_manufacturer_dao.get_by_id(manufacturer_id)
        return manufacturer.to_dict() if manufacturer else None

    def create_manufacturer(self, data):
        return panel_manufacturer_dao.create(data).to_dict()

    def update_manufacturer(self, manufacturer_id, data):
        updated = panel_manufacturer_dao.update(manufacturer_id, data)
        return updated.to_dict() if updated else None

    def delete_manufacturer(self, manufacturer_id):
        return panel_manufacturer_dao.delete(manufacturer_id)