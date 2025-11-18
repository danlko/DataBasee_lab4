# app/my_project/supermarket/dao/retail_network_dao.py

from app.my_project import db
from app.my_project.supermarket.domain.models import RetailNetwork


class RetailNetworkDAO:
    """
    Клас Data Access Object для моделі RetailNetwork.
    Виконує базові CRUD-операції.
    """

    def get_all(self):
        """
        Отримує всі записи RetailNetwork з БД.
        :return: список об'єктів RetailNetwork
        """
        # db.session.query(RetailNetwork) - створює запит
        # .all() - виконує його та повертає всі результати
        return db.session.query(RetailNetwork).all()

    def get_by_id(self, network_id):
        """
        Отримує один запис RetailNetwork за його ID.
        :param network_id: ID мережі
        :return: об'єкт RetailNetwork або None, якщо не знайдено
        """
        # .get(network_id) - це найшвидший спосіб отримати об'єкт за primary_key
        return db.session.query(RetailNetwork).get(network_id)

    def create(self, data):
        """
        Створює новий запис RetailNetwork в БД.
        :param data: словник з даними (наприклад, {'name': 'Нова Мережа'})
        :return: створений об'єкт RetailNetwork
        """
        # Створюємо новий об'єкт Python
        new_network = RetailNetwork(name=data.get('name'))

        # Додаємо його в "сесію" SQLAlchemy
        db.session.add(new_network)

        # "Комітимо" (зберігаємо) зміни в БД
        db.session.commit()
        return new_network

    def update(self, network_id, data):
        """
        Оновлює існуючий запис RetailNetwork в БД.
        :param network_id: ID мережі для оновлення
        :param data: словник з новими даними
        :return: оновлений об'єкт RetailNetwork або None
        """
        # Спочатку знаходимо об'єкт
        network = self.get_by_id(network_id)

        if network:
            # Оновлюємо його поля
            if 'name' in data:
                network.name = data['name']

            # Комітимо зміни
            db.session.commit()
            return network
        return None

    def delete(self, network_id):
        """
        Видаляє запис RetailNetwork з БД.
        :param network_id: ID мережі для видалення
        :return: True, якщо видалення пройшло успішно, False - якщо ні
        """
        network = self.get_by_id(network_id)

        if network:
            # Видаляємо об'єкт з сесії
            db.session.delete(network)
            # Комітимо зміни
            db.session.commit()
            return True
        return False