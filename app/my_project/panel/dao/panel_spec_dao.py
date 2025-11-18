from app.my_project import db
from app.my_project.panel.domain.models import PanelSpec

class PanelSpecDAO:
    def get_all(self):
        return db.session.query(PanelSpec).all()

    def get_by_id(self, spec_id):
        return db.session.query(PanelSpec).get(spec_id)

    def create(self, data):
        new_spec = PanelSpec(**data)
        db.session.add(new_spec)
        db.session.commit()
        return new_spec

    def update(self, spec_id, data):
        spec = self.get_by_id(spec_id)
        if spec:
            for key, value in data.items():
                setattr(spec, key, value)
            db.session.commit()
            return spec
        return None

    def delete(self, spec_id):
        spec = self.get_by_id(spec_id)
        if spec:
            db.session.delete(spec)
            db.session.commit()
            return True
        return False