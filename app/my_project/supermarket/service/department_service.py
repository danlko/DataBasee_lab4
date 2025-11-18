from app.my_project.supermarket.dao import department_dao

class DepartmentService:
    def get_all_departments(self):
        departments = department_dao.get_all()
        return [d.to_dict() for d in departments]

    def get_department_by_id(self, department_id):
        department = department_dao.get_by_id(department_id)
        return department.to_dict() if department else None

    def create_department(self, data):
        created_department = department_dao.create(data)
        return created_department.to_dict()

    def update_department(self, department_id, data):
        updated_department = department_dao.update(department_id, data)
        return updated_department.to_dict() if updated_department else None

    def delete_department(self, department_id):
        return department_dao.delete(department_id)