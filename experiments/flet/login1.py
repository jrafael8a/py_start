import flet as ft

# Creamos la funcion que se ejecutara en el evento on_clic del boton Enviar
def form_submit_function(e):
    print("Form Submited")


# Usaremos varios TextField con el mismo estilo asi que para evitar
# estar escribiendo el mismo estilo 3 veces, usaremos una funcion:
def crear_textfield(label, **kwargs):
    return ft.TextField(                                       # Creamos un Campo de texto
        label=label,                                    # Le ponemos un label, el cual obtenemos del parametro label
        text_size=16,                                   # Tamaño de letra
        border_radius=14,                               # Borde Redondeado al campo de texto
        # focused_border_color='#0a85ff'                # Color de letra usando hexadecimal
        focused_border_color=ft.Colors.BLUE_600,        # Color de letra usando los colores de flet
        cursor_color=ft.Colors.BLUE_400,                # Le damos un color al cursor de escritura
        border_width=0.6,                               # Hacemos delgadito que el borde del campo de texto
        border_color='black',                            # Le damos color al borde del campo de texto
        **kwargs
    )

# Creamos un contenedor FUERA de la funcion main, para mantener todo mejor organizado
form_container = ft.Container(
    ft.Column([         # Creamos una columna en la que meteremos nuestros elementos
        # Creamos un Texto y le damos diseño basico (w600 es el tipo de negrita que queremos. 
        # weight= Va de 100 a 900 entre mayor numero, mas negrita)
        ft.Text("Sign Up", size=24, color=ft.Colors.BLUE_400, weight='w600'),      

        # Creamos 3 cuadros de texto con nuestra funcion personalizada
        crear_textfield("First Name"),
        crear_textfield("Email"),
        crear_textfield("Password",password=True,can_reveal_password=True),

        # Creamos el boton de Enviar
        ft.Button(
            "Submit",                       # El label
            color='white',                  # Color de la letra del boton
            width=700,                      # Largo del boton
            height=40,                      # Ancho del boton
            style=ft.ButtonStyle(           # Abrimos estilos del boton
                text_style=ft.TextStyle(        # Estilos del texto
                    size=16,                    # Tamaño del texto
                    weight='w600',              # Grosor del texto
                    # color='green',            # Esta linea no funcina ni cambia nada
                    # bgcolor='black'             # Si colocamos el bgcolor aqui, sera un fondo solo para el texto
                    ),
                # color=ft.Colors.AMBER_600,  # Aplicamos el color al texto del botón
                bgcolor=ft.Colors.BLUE_400  # Este bgcolor se aplica a todo el boton
            ),
            on_click=form_submit_function
        )

    ], horizontal_alignment='center'),
    # Estos son los estilos
    width=400, 
    height=400,
    bgcolor='White',
    border_radius=18,
    padding=20
)

def main(page: ft.Page):
    page.window.height = 600                # Alto de la ventana
    page.window.width = 500                 # Ancho de la ventana
    page.bgcolor = '#e6e6eb'                # Color de fondo de la ventana
    # page.bgcolor = ft.Colors.WHITE30
    # page.vertical_alignment = 'center'      # Alinear verticalmente al centro
    # page.horizontal_alignment = 'center'    # Alinear horizontalmente al centro
    page.vertical_alignment = ft.MainAxisAlignment.CENTER       # esta es una forma mas larga
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER    # pero es igual que usar solo 'center'
    page.add(
        form_container
    )


ft.app(main)