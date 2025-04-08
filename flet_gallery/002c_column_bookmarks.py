import flet as ft  # Importa el módulo de Flet, una biblioteca para crear aplicaciones web de manera interactiva.

# Nombre de la aplicación
name = "Controlling scroll position for Column"

# Definición de la función principal que crea los componentes y la interacción.
def example():
    # Se crea una columna (cl = ft.Column) que contendrá varios elementos dentro de ella.
    cl = ft.Column(
        spacing=10,                     # Define el espacio entre los elementos de la columna.
        height=180,                     # Establece la altura de la columna.
        width=300,                      # Establece el ancho de la columna.
        scroll=ft.ScrollMode.ALWAYS,    # Permite que la columna tenga scroll siempre que sea necesario.
        controls=[                      # Lista de los controles (widgets) que estarán dentro de la columna.
            # Cuatro contenedores (ft.Container) que representan secciones con un color de fondo distinto.
            ft.Container(
                ft.Text("Section A"),               # Texto que indica el nombre de la sección.
                alignment=ft.alignment.top_left,    # Alinea el contenido al lado superior izquierdo.
                bgcolor=ft.Colors.YELLOW_200,       # Establece un color de fondo amarillo claro.
                height=100,                         # Establece la altura de este contenedor.
                key="A",                            # Asigna una clave para este contenedor, 
                # Las claves seran utilizadas para hacer scroll a cada sección.
            ),
            ft.Container(
                ft.Text("Section B"),
                alignment=ft.alignment.top_left,
                bgcolor=ft.Colors.GREEN_200,        # Color de fondo verde claro.
                height=100,
                key="B",                            # Clave para la sección B.
            ),
            ft.Container(
                ft.Text("Section C"),
                alignment=ft.alignment.top_left,
                bgcolor=ft.Colors.BLUE_200,         # Color de fondo azul claro.
                height=100,
                key="C",                            # Clave para la sección C.
            ),
            ft.Container(
                ft.Text("Section D"),
                alignment=ft.alignment.top_left,
                bgcolor=ft.Colors.PINK_200,         # Color de fondo rosa claro.
                height=100,
                key="D",                            # Clave para la sección D.
            ),
        ],
    )

    # Funciones que permiten desplazarse a las secciones específicas cuando se hace clic en un botón.
    def scroll_to_a(_):
        cl.scroll_to(key="A", duration=1000)  # Desplaza la vista a la sección A con una duración de 1000 ms.

    def scroll_to_b(_):
        cl.scroll_to(key="B", duration=1000)  # Desplaza la vista a la sección B.

    def scroll_to_c(_):
        cl.scroll_to(key="C", duration=1000)  # Desplaza la vista a la sección C.

    def scroll_to_d(_):
        cl.scroll_to(key="D", duration=1000)  # Desplaza la vista a la sección D.

    # Crea una columna que contiene los elementos de la interfaz.
    return ft.Column(
        [
            # Agrega un contenedor con un borde alrededor de la columna "cl".
            ft.Container(cl, border=ft.border.all(1)),
            # Crea otra columna con un texto que indica a qué sección hacer scroll.
            ft.Text("Scroll to:"),  # Texto indicando que puedes hacer scroll a una sección.
            ft.Row(  # Crea una fila con botones que permitirán hacer scroll a las secciones.
                [
                    # Cada botón tiene un texto y una acción (on_click) asociada a cada sección.
                    ft.ElevatedButton(
                        "Section A",  # Nombre del botón.
                        on_click=scroll_to_a,  # Acción que se ejecuta cuando se hace clic en este botón.
                    ),
                    ft.ElevatedButton(
                        "Section B",  # Nombre del botón.
                        on_click=scroll_to_b,  # Acción para desplazarse a la sección B.
                    ),
                    ft.ElevatedButton(
                        "Section C",  # Nombre del botón.
                        on_click=scroll_to_c,  # Acción para desplazarse a la sección C.
                    ),
                    ft.ElevatedButton(
                        "Section D",  # Nombre del botón.
                        on_click=scroll_to_d,  # Acción para desplazarse a la sección D.
                    ),
                ]
            ),
        ]
    )

# Esta es la función principal que se ejecuta cuando la aplicación se inicia.
if __name__ == "__main__":
    def main(page: ft.Page):
        # Configura las opciones de la página, como el modo de tema y el tamaño de la ventana.
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window.height = 400    # Establece la altura de la ventana.
        page.window.width = 600     # Establece el ancho de la ventana.
        page.window.alignment = ft.alignment.center     # Centra la ventana en la pantalla.

        page.add(example())         # Agrega el contenido de la función example() a la página.

    # Inicia la aplicación Flet.
    ft.app(target=main)
