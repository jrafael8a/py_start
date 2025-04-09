import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.height = 400
    page.window.width = 600
    page.window.alignment = ft.alignment.center
    page.horizontal_alignment = 'center'

    scroll_container = ft.Column(
        spacing=5,                      # Espacio entre los elementos
        scroll=ft.ScrollMode.AUTO,      # Activa la capacidad de scroll. Tambien puede ser simpemente scroll=True
        auto_scroll=True,               # Permite el desplazamiento automático al agregar nuevos elementos
        # Para que el scroll funcione, el contenedor debe tener una altura definida. Ya sea con expand=True o height=200
        # expand=True,                    # Expand hasta ocupar todo el espacio del contenedor padre. Si es una columna, la expande en vertical
        height=200,                     # Altura de la culumna. Si expand esta activado, height no tiene efecto
        width=300,
        
        alignment='center'
        )                      # Ancho de la columna.

    # Creamos una funcion que se ejecutara cada vez que se presione una tecla
    def on_keystroke(e: ft.KeyboardEvent):          # "e" es el evento de teclado. ": ft.KeyboardEvent" se puede omitir. Pero es recomendado escribirlo, para documentacion
    # def on_keystroke(e):                          # esto es perfectamente valido, pero menos recomendado
        respuesta = ""                              # Creamos una variable vacia tipo string para concatenar nuestros ket stroke
        if e.ctrl:      respuesta += "Ctrol + "     # e.ctrl devuelve un booleano que es True si la tecla Ctrol fue presionada.
        if e.shift:     respuesta += "Shift + "     # lo mismo e.shift, e.alt y e.meta (Meta es la tecla windows,  o comando en MAC)
        if e.alt:       respuesta += "Alt + "       # Asi que en estas lineas simplemente concatenamos si la tecla especial
        if e.meta:      respuesta += "Meta + "      # Fue presionada, y al final agregamos la tecla
        respuesta += e.key                          # alfanumerica o de funcion que fue presionada

        scroll_container.controls.append(ft.Text(respuesta))
        # f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
        # page.scroll_to(scroll_container.controls[-1])
        page.update()

    page.on_keyboard_event = on_keystroke            # Este es el manejador o handler de eventos. Desde el cual mandamos a llamar a nuestra funcion on_keystroke

    page.add(
        ft.Text("Presiona cualquier tecla y se mostrará aquí. La vista se desplazará automáticamente.")
    )
    page.add(
        ft.Container(
            scroll_container,
            border=ft.border.all(1, ft.colors.BLACK),
            border_radius=10,
            padding=10,
            )
    )
    page.update()
    

ft.app(main)

# Si queremos que haya autoscroll, debemos usar un Control scrollable, 
# como (Page, View, Column, Row, ListView and GridView) y debemos activar la propiedad 