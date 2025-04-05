import flet as ft

def main(page: ft.Page):

    def button_clicked(e):
        page.add(ft.Text("Yamete Kudasai ! ! !"))

    page.add(ft.ElevatedButton(text="Touch me 😏", on_click=button_clicked))

ft.app(main)