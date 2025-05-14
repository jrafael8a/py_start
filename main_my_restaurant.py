import flet as ft

from src.app_my_restaurant.app import RestauranteGUI
       
if __name__ == "__main__":
    def main(page: ft.Page):
        RestauranteGUI(page).main()
    
    ft.app(target=main)
    # ft.app(target=app.main, view=ft.WEB_BROWSER, assets_dir="assets")

#if __name__ == "__main__":
#    ft.app(target=RestauranteGUI().main)