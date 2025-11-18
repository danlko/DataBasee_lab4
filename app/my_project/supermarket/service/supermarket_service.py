from app.my_project.supermarket.dao import supermarket_dao


class SupermarketService:
    def get_all_supermarkets(self):
        supermarkets = supermarket_dao.get_all()
        return [s.to_dict() for s in supermarkets]

    def get_supermarket_by_id(self, supermarket_id):
        supermarket = supermarket_dao.get_by_id(supermarket_id)
        return supermarket.to_dict() if supermarket else None

    def create_supermarket(self, data):
        created_supermarket = supermarket_dao.create(data)
        return created_supermarket.to_dict()

    def update_supermarket(self, supermarket_id, data):
        updated_supermarket = supermarket_dao.update(supermarket_id, data)
        return updated_supermarket.to_dict() if updated_supermarket else None

    def delete_supermarket(self, supermarket_id):
        return supermarket_dao.delete(supermarket_id)

    def get_departments_for_supermarket(self, supermarket_id):
        departments = supermarket_dao.get_departments_for_supermarket(supermarket_id)
        if departments is not None:
            return [d.to_dict() for d in departments]
        return None