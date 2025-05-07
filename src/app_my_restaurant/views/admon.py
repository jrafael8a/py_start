import flet as ft

from src.app_my_restaurant.database import *
from src.app_my_restaurant.components.mesas_grid import *
from src.app_my_restaurant.components.mesas_agregar import *

class VistaAdmon:
    def __init__ (self, page: ft.Page):
        self.page = page
    
    def crear_vista(self):
        self.tabs = ft.Tabs(
            selected_index=0,
            animation_duration=200,
            expand=True,
            tabs=[
                ft.Tab(
                    text="Menú",
                    icon=ft.icons.RESTAURANT_MENU,
                    content=ft.Column([
                        ft.Text("Gestión del menú: agregar, editar, eliminar productos")
                    ])
                ),
                ft.Tab(
                    text="Mesas",
                    icon=ft.icons.TABLE_BAR,
                    content=ft.Column([
                        crear_componente_agregar_mesa(self.page),  # componente de gestion de mesas
                        ft.Divider,
                        crear_grid_mesas()
                        ])
                ),
                ft.Tab(
                    text="Usuarios",
                    icon=ft.icons.SUPERVISED_USER_CIRCLE,
                    content=ft.Column([
                        ft.Text("Gestión de usuarios y roles de acceso")
                    ])
                ),
                ft.Tab(
                    text="Caja",
                    icon=ft.icons.ATTACH_MONEY,
                    content=ft.Column([
                        ft.Text("Historial de caja, arqueo, reportes")
                    ])
                ),
                ft.Tab(
                    text="Configuración",
                    icon=ft.icons.SETTINGS,
                    content=ft.Column([
                        ft.Text("Configuración general del sistema")
                    ])
                ),
            ]
        )

        return self.tabs
        #self.page.add(self.tabs)

if __name__ == "__main__":
    def main(page: ft.Page):
          page.add(VistaAdmon.crear_vista())
    
    ft.app(target=main)