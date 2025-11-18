# app/my_project/supermarket/dao/__init__.py
from .retail_network_dao import RetailNetworkDAO
from .supermarket_dao import SupermarketDAO
from .department_dao import DepartmentDAO

retail_network_dao = RetailNetworkDAO()
supermarket_dao = SupermarketDAO()
department_dao = DepartmentDAO()