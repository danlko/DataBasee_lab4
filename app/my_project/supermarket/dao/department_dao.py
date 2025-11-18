from app.my_project import db
from app.my_project.supermarket.domain.models import Department

class DepartmentDAO:
    def get_all(self):
        return db.session.query(Department).all()

    def get_by_id(self, department_id):
        return db.session.query(Department).get(department_id)

    def create(self, data):
        new_department = Department(**data)
        db.session.add(new_department)
        db.session.commit()
        return new_department

    def update(self, department_id, data):
        department = self.get_by_id(department_id)
        if department:
            for key, value in data.items():
                setattr(department, key, value)
            db.session.commit()
            return department
        return None

    def delete(self, department_id):
        department = self.get_by_id(department_id)
        if department:
            db.session.delete(department)
            db.session.commit()
            return True
        return False