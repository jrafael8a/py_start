import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.height = 400
    page.window.width = 600
    page.window.alignment = ft.alignment.center

    page.title = "Ejemplo de Slider"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Texto para mostrar el valor actual del slider
    value_text = ft.Text(
        value="50",
        size=20,
        text_align=ft.TextAlign.CENTER,
    )

    # Función que se llama cuando el valor del slider cambia
    def slider_changed(e):
        value_text.value = str(int(e.control.value))
        page.update()

    # Crear el slider
    slider = ft.Slider(
        min=0,              # Valor mínimo
        max=100,            # Valor máximo
        value=50,           # Valor inicial
        divisions=10,       # Divisiones (marcas en el slider)
        label="{value}",    # Etiqueta que aparece al deslizar
        width=400,          # Ancho del slider
        on_change=slider_changed  # Función que se ejecuta al cambiar el valor
    )

    # Añadir título, slider y texto a la página
    page.add(
        ft.Text("Mueve el slider para cambiar el valor:", size=16),
        slider,
        value_text
    )

ft.app(target=main)