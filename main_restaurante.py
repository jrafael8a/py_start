import flet as ft

from src.app_restaurante.app import RestauranteGUI


#if __name__ == "__main__":
def main():
    app = RestauranteGUI()
    
    # ft.app(target=app.main, view=ft.WEB_BROWSER, assets_dir="assets")
    ft.app(target=app.main)

if __name__ == "__main__":
    main()
