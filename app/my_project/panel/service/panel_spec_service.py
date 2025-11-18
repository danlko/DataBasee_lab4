# app/my_project/panel/service/panel_spec_service.py
from app.my_project.panel.dao import panel_spec_dao

class PanelSpecService:
    def get_all_specs(self):
        specs = panel_spec_dao.get_all()
        return [s.to_dict() for s in specs]

    def get_spec_by_id(self, spec_id):
        spec = panel_spec_dao.get_by_id(spec_id)
        return spec.to_dict() if spec else None

    def create_spec(self, data):
        return panel_spec_dao.create(data).to_dict()

    def update_spec(self, spec_id, data):
        updated = panel_spec_dao.update(spec_id, data)
        return updated.to_dict() if updated else None

    def delete_spec(self, spec_id):
        return panel_spec_dao.delete(spec_id)