import flet as ft

def main(page: ft.Page):
    page.window.height = 200
    page.window.width = 300
    
    page.add(
        ft.Text("Hola Mundo! (con Flet)")
        )

ft.app(main)