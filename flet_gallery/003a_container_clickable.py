import flet as ft

name = "Clickable containers"

def example():
    return ft.Row(
        [
            ft.Container(       # Contenedor no clickeable
                content=ft.Text("Non clickable"),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.AMBER,
                width=150,
                height=150,
                border_radius=10,
            ),
            ft.Container(       # Contenedor clickeable sin efecto
                content=ft.Text("Clickable without Ink"),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.GREEN_200,
                width=150,
                height=150,
                border_radius=10,
                on_click=lambda e: print("Clickable without Ink clicked!"),     # Imprime en consola que el contenedor fue cliqueado
            ),
            ft.Container(       # Contenedor clickeable con efecto de Tinta
                content=ft.Text("Clickable with Ink"),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.CYAN_200,
                width=150,
                height=150,
                border_radius=10,
                ink=True,         # Esto es lo que hace que el contenedor tenga un efecto cuando es clickeado
                on_click=lambda e: print("Clickable with Ink clicked!"),
            ),
            ft.Container(       # Contenedor clickeable sin fondo pero con efecto de tinta
                content=ft.Text("Clickable transparent with Ink"),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                width=150,
                height=150,
                border_radius=10,
                ink=True,
                on_click=lambda e: print("Clickable transparent with Ink clicked!"),
            ),
        ],
    )

if __name__ == "__main__":
    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window.height = 400
        page.window.width = 800
        page.window.alignment = ft.alignment.center

        page.add(example())
        
    ft.app(target=main)