# app/my_project/panel/service/__init__.py
from .panel_manufacturer_service import PanelManufacturerService
from .panel_spec_service import PanelSpecService
from .panel_service import PanelService

panel_manufacturer_service = PanelManufacturerService()
panel_spec_service = PanelSpecService()
panel_service = PanelService()