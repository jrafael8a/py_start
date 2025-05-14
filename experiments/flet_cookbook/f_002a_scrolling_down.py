import flet as ft

def main(page: ft.Page):
    page.title = "Capturador de Teclas"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Contenedor para mostrar las teclas presionadas
    key_log = ft.Column(
        spacing=5,
        scroll=ft.ScrollMode.AUTO,
        auto_scroll=True,  # Para hacer scroll automáticamente
        height=400,
        width=400
    )
    
    def on_key_down(e: ft.KeyboardEvent):
        # Crear un nuevo texto con la tecla presionada
        key_text = ft.Text(f"Tecla presionada: {e.key}", size=14)
        key_log.controls.append(key_text)
        page.update()
    
    # Configurar la captura de teclas a nivel de página
    page.on_keyboard_event = on_key_down
    
    # Agregar los elementos a la página
    page.add(
        ft.Text("Presiona cualquier tecla y se mostrará aquí. La vista se desplazará automáticamente.",
        size=16, color=ft.Colors.BLUE),
        ft.Container(
            content=key_log,
            border=ft.border.all(1, ft.Colors.BLACK),
            border_radius=10,
            padding=10
        )
    )
    
    # Asegurar que la página tenga el foco para capturar eventos de teclado
    page.update()

ft.app(target=main)