from app.my_project import db
from app.my_project.video.domain.models import Brand

class BrandDAO:
    def get_all(self):
        return db.session.query(Brand).all()

    def get_by_id(self, brand_id):
        return db.session.query(Brand).get(brand_id)

    def create(self, data):
        new_brand = Brand(**data)
        db.session.add(new_brand)
        db.session.commit()
        return new_brand

    def update(self, brand_id, data):
        brand = self.get_by_id(brand_id)
        if brand:
            for key, value in data.items():
                setattr(brand, key, value)
            db.session.commit()
            return brand
        return None

    def delete(self, brand_id):
        brand = self.get_by_id(brand_id)
        if brand:
            db.session.delete(brand)
            db.session.commit()
            return True
        return False