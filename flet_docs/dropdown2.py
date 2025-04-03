import flet as ft                           # Importa el módulo 'flet' como 'ft' para usar su funcionalidad en la creación de la interfaz de usuario.

def main(page: ft.Page):                    # Define la función principal que recibe una instancia de página de la aplicación.
    page.window.width = 300                 # Establece el ancho de la ventana de la página a 200 píxeles.
    page.window.height = 400                # Establece la altura de la ventana de la página a 300 píxeles.
    page.window.alignment = ft.alignment.center     # Establece la alineación de la ventana en el centro de la pantalla.
    page.horizontal_alignment = 'center'    # Establece la alineación horizontal de los elementos dentro de la página al centro.
    # page.vertical_alignment = 'center'    # (Esta línea está comentada) Si estuviera activa, alinearía los elementos verticalmente al centro.

    colors = [  # Crea una lista de colores utilizando las constantes predefinidas de Flet.
        ft.Colors.RED,      # Rojo.
        ft.colors.BLUE,     # Azul.
        ft.Colors.YELLOW,   # Amarillo.
        ft.Colors.PURPLE,   # Púrpura.
        ft.Colors.LIME,     # Lima.
    ]

    def get_options():                      # Define una función para generar opciones de dropdown basadas en la lista de colores.
        options = []                        # Inicializa una lista vacía para almacenar las opciones del dropdown.
        for color in colors:                # Itera sobre cada color en la lista de colores.
            options.append(                 # Agrega una nueva opción al dropdown.
                ft.DropdownOption(          # Crea una nueva opción de dropdown.
                    key=color.value,        # Usa el valor del color como clave única para la opción.
                    content=ft.Text(        # El contenido de la opción es un texto que muestra el nombre del color.
                        value=color.value,  # El texto es el valor del color.
                        color=color,        # El color del texto es el mismo que el color de la opción.
                    ),
                )
            )
        return options                      # Devuelve la lista de opciones del dropdown.

    def dropdown_changed(e):                # Define una función que se ejecutará cuando el valor del dropdown cambie.
        e.control.color = e.control.value   # Cambia el color del control (dropdown) al valor seleccionado.
        page.update()                       # Actualiza la página para reflejar los cambios.

    dd = ft.Dropdown(                       # Crea un control de tipo Dropdown (menú desplegable).
        editable=True,                      # Establece que el dropdown no sea editable, es decir, solo se puede seleccionar de las opciones predefinidas.
        label="Color",                      # Etiqueta que se mostrará sobre el dropdown.
        options=get_options(),              # Asigna las opciones generadas por la función get_options().
        on_change=dropdown_changed,         # Establece la función que se ejecutará cuando cambie la selección en el dropdown.
    )

    page.add(dd)                            # Agrega el dropdown a la página.

ft.app(main)                                # Inicia la aplicación Flet y ejecuta la función 'main' como la función principal.
