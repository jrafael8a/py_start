import flet as ft

def main(page: ft.Page):
    page.title = "Ventana Principal"
    page.window.width = 300
    page.window.height = 300
    page.window.alignment = ft.alignment.center
    # page.horizontal_alignment = 'center'
    # page.vertical_alignment = 'center'

    def abrir_ventana_secundaria(e):
        # Crear una nueva ventana
        print("Abriendo ventana secundaria...")
        page.launch_url("/ventana_secundaria", web_window_name="ventana_secundaria", window_height=100, window_width=200)

    # Crear un botón en la ventana principal
    boton_abrir = ft.ElevatedButton(
        text="Abrir Ventana Secundaria",
        on_click=abrir_ventana_secundaria,
        width=200,
        height=50
    )

    # Diseño de la ventana principal
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Ventana Principal", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Presiona el botón para abrir una ventana secundaria"),
                    boton_abrir
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            alignment=ft.alignment.center,
            expand=True
        )
    )

def vista_secundaria(page: ft.Page):
    page.title = "Ventana Secundaria"
    page.window.width = 300
    page.window.height = 200
    page.window.alignment = 'center'
    
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("¡Ventana Secundaria!", size=20, weight=ft.FontWeight.BOLD),
                    ft.Text("Esta es la segunda ventana"),
                    ft.ElevatedButton(
                        text="Cerrar",
                        on_click=lambda _: page.window_close(),
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            ),
            alignment=ft.alignment.center,
            expand=True
        )
    )


ft.app(main)


"""
# Registrar vistas y ejecutar la aplicación
if __name__ == "__main__":
    ft.app(target=main, view="window", routes={
        "/": main,
        "/ventana_secundaria": vista_secundaria
    })
"""