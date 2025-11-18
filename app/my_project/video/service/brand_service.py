from app.my_project.video.dao import brand_dao

class BrandService:
    def get_all_brands(self):
        brands = brand_dao.get_all()
        return [b.to_dict() for b in brands]

    def get_brand_by_id(self, brand_id):
        brand = brand_dao.get_by_id(brand_id)
        return brand.to_dict() if brand else None

    def create_brand(self, data):
        return brand_dao.create(data).to_dict()

    def update_brand(self, brand_id, data):
        updated_brand = brand_dao.update(brand_id, data)
        return updated_brand.to_dict() if updated_brand else None

    def delete_brand(self, brand_id):
        return brand_dao.delete(brand_id)