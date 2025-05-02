import flet as ft

from src.app_restaurante.app import RestauranteGUI


#if __name__ == "__main__":
def main():
    app = RestauranteGUI()
    
    # ft.app(target=app.main, view=ft.WEB_BROWSER, assets_dir="assets")   # Iniciar la App en el navegador web
    ft.app(target=app.main)   # Iniciar la App como aplicacion de escritorio

if __name__ == "__main__":
    main()
