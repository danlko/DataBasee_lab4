from app.my_project import db
from app.my_project.supermarket.domain.models import Supermarket, Department

class SupermarketDAO:
    def get_all(self):
        return db.session.query(Supermarket).all()

    def get_by_id(self, supermarket_id):
        return db.session.query(Supermarket).get(supermarket_id)

    def create(self, data):
        new_supermarket = Supermarket(**data) # **data розпакує словник
        db.session.add(new_supermarket)
        db.session.commit()
        return new_supermarket

    def update(self, supermarket_id, data):
        supermarket = self.get_by_id(supermarket_id)
        if supermarket:
            for key, value in data.items():
                setattr(supermarket, key, value)
            db.session.commit()
            return supermarket
        return None

    def delete(self, supermarket_id):
        supermarket = self.get_by_id(supermarket_id)
        if supermarket:
            db.session.delete(supermarket)
            db.session.commit()
            return True
        return False

    def get_departments_for_supermarket(self, supermarket_id):
        supermarket = self.get_by_id(supermarket_id)
        if supermarket:
            return supermarket.departments
        return None