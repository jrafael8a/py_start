import flet as ft

from src.app_my_restaurant.database import *
from src.app_my_restaurant.components.mesas import *

class VistaAdmonMesas:
    def __init__ (self, page: ft.Page):
        self.page = page
        
    
    def crear_vista(self):
        return ft.Column([
            componente_agregar_mesa(self),  # componente de gestion de mesas
            ft.Divider(),
            self.grid_container,
            crear_grid_mesas()
            ])