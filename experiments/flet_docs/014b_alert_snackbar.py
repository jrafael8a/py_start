import flet as ft


def main(page: ft.Page):
    page.window.width = 500
    page.window.height = 300
    page.window.alignment = ft.alignment.center
    page.horizontal_alignment = 'center'
    # page.vertical_alignment = 'center'

    counter = 0

    def on_click(e):
        nonlocal counter
        page.open(ft.SnackBar(ft.Text(f"Counter value at {counter}")))
        counter += 1
        page.update()

    page.add(ft.ElevatedButton("Open SnackBar", on_click=on_click))


ft.app(target=main)