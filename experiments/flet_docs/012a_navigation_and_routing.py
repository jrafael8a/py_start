import flet as ft

def main(page: ft.Page):
    page.window.height = 600
    page.window.width = 900
    page.window.alignment = ft.alignment.center

    page.add(ft.Text(
        f"Cambie Manualmente la URL, (preservando lo que ya esta)" 
        f"agregando cualquier cosa, como:   \hola-mundo-web\   " 
        f"y podra ver como cambia el texto de la pagina, imprimiendo la nueva url."
        ))

    page.add(ft.Text(f"Initial route: {page.route}"))

    def route_change(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"New route: {e.route}"))

    page.on_route_change = route_change
    page.update()

ft.app(main, view=ft.AppView.WEB_BROWSER)