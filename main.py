import flet as ft

# from experiments.flet_gallery.g_003c_container_animated import *
from experiments.SQLite.To_Do.to_do_06 import to_do




if __name__ == "__main__":
    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window.height = 400
        page.window.width = 600
        page.window.alignment = ft.alignment.center

        page.add(to_do())
        
    ft.app(target=main)