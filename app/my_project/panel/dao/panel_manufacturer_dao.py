from app.my_project import db
from app.my_project.panel.domain.models import PanelManufacturer

class PanelManufacturerDAO:
    def get_all(self):
        return db.session.query(PanelManufacturer).all()

    def get_by_id(self, manufacturer_id):
        return db.session.query(PanelManufacturer).get(manufacturer_id)

    def create(self, data):
        new_manufacturer = PanelManufacturer(**data)
        db.session.add(new_manufacturer)
        db.session.commit()
        return new_manufacturer

    def update(self, manufacturer_id, data):
        manufacturer = self.get_by_id(manufacturer_id)
        if manufacturer:
            for key, value in data.items():
                setattr(manufacturer, key, value)
            db.session.commit()
            return manufacturer
        return None

    def delete(self, manufacturer_id):
        manufacturer = self.get_by_id(manufacturer_id)
        if manufacturer:
            db.session.delete(manufacturer)
            db.session.commit()
            return True
        return False