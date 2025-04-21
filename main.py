import flet as ft

from experiments.SQLite.Gallery.gallery import gallery

if __name__ == "__main__":
    ft.app(target=gallery)

"""
if __name__ == "__main__":
    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window.height = 400
        page.window.width = 600
        page.window.alignment = ft.alignment.center

        # gallery(page)
        
    # ft.app(target=main)
"""