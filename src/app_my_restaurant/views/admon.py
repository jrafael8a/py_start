import flet as ft

from src.app_my_restaurant.database import *
from src.app_my_restaurant.components.grid_mesas import crear_grid_mesas

class VistaAdmon:
    def __init__ (self, page: ft.Page):
        self.page = page
    
    def vista_grid_mesas(self):
        mesas = obtener_mesas_desde_db()  # debería devolverte lista de dicts o modelos
        grid = crear_grid_mesas(mesas, on_mesa_click=self.manejar_click_mesa)
            
        return ft.Column([
            ft.Text("Gestión de mesas"),
            grid
        ])

    def manejar_click_mesa(self, numero_mesa):
        print(f"Click en mesa {numero_mesa}")

    
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
                        ft.Text("Gestión de mesas: agregar, editar, eliminar mesas")
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