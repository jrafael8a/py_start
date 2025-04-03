import flet as ft

def main(page):
    page.window.height = 600
    page.window.width = 400
    page.window.alignment = ft.alignment.center
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Escriba una Nueva Tarea", width=300)
    titulo = ft.Text("TO - DO   LIST", 
        size=40,                           # Tamaño de fuente
        weight=ft.FontWeight,              # Negrita
        color=ft.colors.BLUE_900,          # Color Azul Oscuro
        text_align=ft.TextAlign.CENTER,    # Centrar el texto
        font_family="Arial"                # Funte de letra)
    )

    page.add(
        ft.Column(
            controls=[titulo],
            alignment=ft.MainAxisAlignment.CENTER,           # Alinea Verticalmente al centro 
            horizontal_alignment= ft.CrossAxisAlignment.CENTER      # Alinea Horizontalmente al centro
        )
    )
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

ft.app(main)