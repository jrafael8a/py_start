import flet as ft


def main(page: ft.Page):
    page.title = "Mi aplicacion con Flet"
    page.vertical_alignment = ft.MainAxisAlignment.START
    
    mi_txt = ft.TextField(value=f"Texto", text_align=ft.TextAlign.CENTER)
    # mi_txt.value = "Hola Mundo"

    page.add(
        ft.Text("Helloooo!!!", text_align=ft.TextAlign.CENTER),
        mi_txt
    )
    page.update()

ft.app(main)
