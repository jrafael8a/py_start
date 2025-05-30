import flet as ft
from src.app_my_restaurant.views.admon_menu import VistaAdmonMenu
from src.app_my_restaurant.views.admon_menu_tipos import VistaAdmonMenuTipos
from src.app_my_restaurant.views.admon_mesas import VistaAdmonMesas
from src.app_my_restaurant.views.formulario_menu import FormularioMenu

class VistaAdmon:
    def __init__ (self, page: ft.Page):
        self.page = page
        
    
    def crear_vista(self):
        self.grid_container = ft.Column()

        self.sub_tabs = ft.Tabs(
            selected_index=1,
            animation_duration=200,
            expand=True,
            tabs=[
                ft.Tab(
                    text="Menú",
                    icon=ft.icons.RESTAURANT_MENU,
                    content=VistaAdmonMenu(self.page).crear_vista()
                ),
                ft.Tab(
                    text="Items",
                    icon=ft.icons.RESTAURANT_MENU,
                    content=FormularioMenu(self.page).crear_vista()
                ),
                ft.Tab(
                    text="Tipos de Items del Menú",
                    icon=ft.icons.MENU_BOOK,
                    content=VistaAdmonMenuTipos(self.page).crear_vista()
                ),
                ft.Tab(
                    text="Mesas",
                    icon=ft.icons.TABLE_BAR,
                    content=VistaAdmonMesas(self.page).crear_vista()
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
            ],
        )

        return self.sub_tabs
        #self.page.add(self.tabs)

if __name__ == "__main__":
    def main(page: ft.Page):
          page.add(VistaAdmon.crear_vista())
    
    ft.app(target=main)