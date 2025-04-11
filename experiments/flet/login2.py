import flet as ft

# Definir colores como constantes para mejorar la legibilidad
COLOR_PRIMARIO = ft.colors.GREEN_200            # Color Primario
COLOR_SECUNDARIO = ft.colors.GREEN_600          # Color Secundario
COLOR_ERROR = ft.colors.RED_600                 # Color para errores
COLOR_BG01 = '#e6e6eb'                          # Color de fondo 1
# COLOR_BG01 = 'yellow'                         # Color de fondo 1


# Función para manejar el envío del formulario
def form_submit_function(e):
    tf_name.error_text = "Error en nombre"
    tf_email.error_text = "Error en email"
    tf_pass.error_text = "Error en password"
    form_container.update()
    print("Formulario enviado")
    # Aquí puedes agregar la lógica para enviar los datos, validar, etc.

# Usaremos varios TextField con el mismo estilo asi que para evitar
# estar escribiendo el mismo estilo 3 veces, usaremos una funcion:
def crear_textfield(label, password=False, **kwargs):
    return ft.TextField(                                        # Creamos un Campo de texto
        label=label,                                            # Le ponemos un label, el cual obtenemos del parametro label
        label_style=ft.TextStyle(color=COLOR_PRIMARIO),         # Colorea los labels
        text_style=ft.TextStyle(color=COLOR_PRIMARIO),          # Colorea el texto que se escriba en los textfield
        text_size=16,                                           # Tamaño de letra
        border_radius=14,                                       # Borde Redondeado al campo de texto
        cursor_color=COLOR_PRIMARIO,                            # Le damos un color al cursor de escritura
        border_width=0.6,                                       # Hacemos delgadito el borde del campo de texto
        border_color=COLOR_SECUNDARIO,                          # Le damos color al borde del campo de texto
        focused_border_color=COLOR_SECUNDARIO,                  # Color del borde cuando el campo esta seleccionado
        password=password,                                      # Si es un campo de contraseña, pasamos el parámetro como True
        can_reveal_password=True if password else False,        # Si es contraseña, activamos el ojito para mostrar contraseña
        **kwargs
    )

# Creamos 3 cuadros de texto con nuestra funcion personalizada
tf_name = crear_textfield("First Name")
tf_email = crear_textfield("Email")
tf_pass = crear_textfield("Password", password=True)




# Contenedor FUERA de la funcion main, para mantener todo mejor organizado
form_container = ft.Container(
    ft.Column([         # Creamos una columna en la que meteremos nuestros elementos
            # Creamos un Texto y le damos diseño basico (w600 es el tipo de negrita que queremos. 
            # weight= Va de 100 a 900 entre mayor numero, mas negrita)
            ft.Text("Sign Up", size=24, color=COLOR_PRIMARIO, weight='w600'),      

            # Colocamos nuestros TextField
            tf_name,
            tf_email,
            tf_pass,

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
                    ),
                    bgcolor=COLOR_SECUNDARIO  # Este bgcolor se aplica a todo el boton
                ),
                on_click=form_submit_function
            )
        ], 
        # Estilos de la columna
        horizontal_alignment='center',
        spacing=20
    ),
    # Estilos del contenedor
    width=400, 
    height=400,
    bgcolor='White',
    border_radius=18,
    padding=20
)

# Función principal
def main(page: ft.Page):
    page.window.height = 600                # Alto de la ventana
    page.window.width = 500                 # Ancho de la ventana
    page.bgcolor = COLOR_BG01                 # Color de fondo de la ventana
    page.vertical_alignment = ft.MainAxisAlignment.CENTER       # Alineación vertical al centro
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER    # Alineación horizontal al centro
    page.add(form_container)

ft.app(main)