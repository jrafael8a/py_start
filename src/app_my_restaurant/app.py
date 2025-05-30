import flet as ft

from src.app_my_restaurant.database.restaurant_db import *
from src.app_my_restaurant.views.mesera import VistaMesera
from src.app_my_restaurant.views.admon import VistaAdmon


class RestauranteGUI:
    def __init__(self, page: ft.Page):
        self.page = page
        

    def main(self):
        init_db() # Inicializa la base de datos al iniciar la app
        self.vista_admon = VistaAdmon(self.page)  # ⬅️ Instancia pasando la page
        self.page.window.width = 1200
        self.page.window.height = 900

        self.main_tabs = ft.Tabs(
            selected_index = 3,
            animation_duration= 300,
            tabs = [
                ft.Tab(
                    text = "Mesera",
                    icon = ft.icons.PERSON,
                    content= VistaMesera(self.page).crear_vista()
                        
                ),
                ft.Tab(
                    text = "Cocina",
                    icon = ft.icons.RESTAURANT,
                    #content = self.crear_vista_cocina()
                ),
                ft.Tab(
                    text = "Caja",
                    icon = ft.icons.POINT_OF_SALE,
                    #content= self.crear_vista_caja()
                ),
                ft.Tab(
                    text = "Administracion",
                    icon = ft.icons.ADMIN_PANEL_SETTINGS,
                    content= self.vista_admon.crear_vista()  # ⬅️ Llamada al método que crea la vista de administración
                ),

            ],
            expand=True,
        )
        self.page.add(self.main_tabs)

    #def mostrar_vista_admon(self):
    #    self.vista_admon = VistaAdmon(self.page)
    #    self.vista_admon.crear_vista()


if __name__ == "__main__":
    def main(page: ft.Page):
        RestauranteGUI(page).main()
    
    ft.app(target=main)
        # ft.app(target=app.main, view=ft.WEB_BROWSER, assets_dir="assets")