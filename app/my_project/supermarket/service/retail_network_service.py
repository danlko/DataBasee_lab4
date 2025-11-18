# app/my_project/supermarket/service/retail_network_service.py

# Імпортуємо наш готовий DAO
from app.my_project.supermarket.dao import retail_network_dao


class RetailNetworkService:
    """
    Клас сервісу для моделі RetailNetwork.
    Містить бізнес-логіку та викликає DAO.
    """

    def get_all_networks(self):
        """
        Отримує всі мережі та перетворює їх у DTO (словники).
        :return: список словників (DTO)
        """
        # 1. Отримуємо об'єкти з DAO
        networks = retail_network_dao.get_all()

        # 2. Перетворюємо їх у словники (DTO)
        # Це і є наша "бізнес-логіка" на даному етапі
        return [network.to_dict() for network in networks]

    def get_network_by_id(self, network_id):
        """
        Отримує одну мережу за ID та перетворює її в DTO.
        :param network_id: ID мережі
        :return: словник (DTO) або None
        """
        network = retail_network_dao.get_by_id(network_id)

        if network:
            return network.to_dict()
        return None

    def create_network(self, data):
        """
        Створює нову мережу.
        :param data: словник з даними
        :return: словник (DTO) створеного об'єкта
        """
        created_network = retail_network_dao.create(data)
        return created_network.to_dict()

    def update_network(self, network_id, data):
        """
        Оновлює існуючу мережу.
        :param network_id: ID мережі
        :param data: словник з новими даними
        :return: словник (DTO) оновленого об'єкта або None
        """
        updated_network = retail_network_dao.update(network_id, data)

        if updated_network:
            return updated_network.to_dict()
        return None

    def delete_network(self, network_id):
        """
        Видаляє мережу.
        :param network_id: ID мережі
        :return: True/False
        """
        return retail_network_dao.delete(network_id)