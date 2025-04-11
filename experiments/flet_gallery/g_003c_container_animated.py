import flet as ft

name = "Animate container"


def example():
    mi_contenedor = ft.Container(
        width=200,
        height=200,
        bgcolor="red",
        # animate=ft.animation.Animation(1000, "bounceOut"),
    )

    def animate_container(e):
        mi_contenedor.width = 100 if mi_contenedor.width == 200 else 200
        mi_contenedor.height = 100 if mi_contenedor.height == 200 else 200
        mi_contenedor.bgcolor = "blue" if mi_contenedor.bgcolor == "red" else "red"
        mi_contenedor.update()

    return ft.Column(
        controls=[mi_contenedor, ft.ElevatedButton("Animate container", on_click=animate_container)]
    )

if __name__ == "__main__":
    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window.height = 700
        page.window.width = 600
        page.window.alignment = ft.alignment.center

        page.add(example())
        
    ft.app(target=main)