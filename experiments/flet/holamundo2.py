import flet as ft

def main(page: ft.Page):
    page.window.alignment = ft.alignment.center
    page.window.height = 400
    page.window.width = 600

    texto1 = ft.Text("Hola Mundo!!!", text_align = ft.TextAlign.CENTER)
    texto2 = ft.Text(value="Me encata usar Flet", color="green")
    textbox1 = ft.TextField("Este es un campo de texto")
    boton1 = ft.Button("Boton 1")
    boton2 = ft.Button("Boton 2")
    boton3 = ft.Button("Boton 3")
    
    page.add(
        ft.Row([
            texto1, texto2, textbox1, boton1, boton2, boton3
            ]
        )
    )


ft.app(main)