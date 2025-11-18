from app.my_project.supermarket.dao import retail_network_dao


class RetailNetworkService:


    def get_all_networks(self):
        networks = retail_network_dao.get_all()

        return [network.to_dict() for network in networks]

    def get_network_by_id(self, network_id):
        network = retail_network_dao.get_by_id(network_id)

        if network:
            return network.to_dict()
        return None

    def create_network(self, data):
        created_network = retail_network_dao.create(data)
        return created_network.to_dict()

    def update_network(self, network_id, data):
        updated_network = retail_network_dao.update(network_id, data)

        if updated_network:
            return updated_network.to_dict()
        return None

    def delete_network(self, network_id):
        return retail_network_dao.delete(network_id)