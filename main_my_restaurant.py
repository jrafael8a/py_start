import flet as ft

from src.app_my_restaurant.app import RestauranteGUI


#def main(page: ft.Page):
    #app = RestauranteGUI(page)
    #app.main(page)

    # app.mostrar_vista_admon()
    
    # ft.app(target=app.main, view=ft.WEB_BROWSER, assets_dir="assets")   # Iniciar la App en el navegador web
    # ft.app(target=app.main)   # Iniciar la App como aplicacion de escritorio



    #ft.app(target=main)   # Iniciar la App como aplicacion de escritorio
 
if __name__ == "__main__":
    def main(page: ft.Page):
        RestauranteGUI(page).main()
    
    ft.app(target=main)
    # ft.app(target=app.main, view=ft.WEB_BROWSER, assets_dir="assets")

#if __name__ == "__main__":
#    ft.app(target=RestauranteGUI().main)