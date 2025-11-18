# app/my_project/supermarket/service/__init__.py
from .retail_network_service import RetailNetworkService
from .supermarket_service import SupermarketService
from .department_service import DepartmentService

retail_network_service = RetailNetworkService()
supermarket_service = SupermarketService()
department_service = DepartmentService()