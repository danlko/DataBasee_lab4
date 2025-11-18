from app.my_project import db
from app.my_project.supermarket.domain.models import RetailNetwork


class RetailNetworkDAO:

    def get_all(self):
        return db.session.query(RetailNetwork).all()

    def get_by_id(self, network_id):
        return db.session.query(RetailNetwork).get(network_id)

    def create(self, data):
        new_network = RetailNetwork(name=data.get('name'))

        db.session.add(new_network)

        db.session.commit()
        return new_network

    def update(self, network_id, data):
        network = self.get_by_id(network_id)

        if network:
            if 'name' in data:
                network.name = data['name']

            db.session.commit()
            return network
        return None

    def delete(self, network_id):
        network = self.get_by_id(network_id)

        if network:
            db.session.delete(network)
            db.session.commit()
            return True
        return False