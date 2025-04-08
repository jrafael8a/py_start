import flet as ft

name = "Column wrapping"

def example():
    mi_altura = 400

    def items(count):
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    content=ft.Text(value=str(i)),
                    alignment=ft.alignment.center,
                    width=50,
                    height=30,
                    bgcolor=ft.Colors.AMBER,
                    border_radius=ft.border_radius.all(5),
                )
            )
        return items

    def slider_change(e):
        col.height = float(e.control.value)
        col.update()

    width_slider = ft.Slider(
        min=0,
        max=mi_altura,
        divisions=20,
        value=mi_altura,
        label="{value}",
        width=500,
        on_change=slider_change,
    )

    col = ft.Column(
        wrap=True,                  # Permite el ajuste de los elementos en varias columnas
        spacing=10,                 # Espacio entre los elementos
        run_spacing=10,             # Espacio entre las filas de columnas
        controls=items(10),         # Lista de elementos a mostrar
        height=mi_altura,           # Altura inicial de la columna
    )

    return ft.Column(
        [
            ft.Column(
                [
                    ft.Text(
                        "Change the column height to see how child items wrap onto multiple columns:"
                    ),
                    width_slider,
                ]
            ),
            ft.Container(content=col, bgcolor=ft.Colors.AMBER_100),
        ]
    )

if __name__ == "__main__":
    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window.height = 400
        page.window.width = 600
        page.window.alignment = ft.alignment.center

        page.add(example())
        
    ft.app(target=main)