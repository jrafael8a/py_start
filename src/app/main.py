import flet as ft

from src.app.views.gallery import gallery

# from src.app.views.to_do import to_do

                     
if __name__ == "__main__":
    ft.app(target=gallery)

"""
if __name__ == "__main__":
    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window.height = 400
        page.window.width = 600
        page.window.alignment = ft.alignment.center

        to_do(page)
        
    ft.app(target=main)
"""