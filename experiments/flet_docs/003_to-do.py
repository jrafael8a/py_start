import flet as ft

def main(page):
    page.window.height = 600
    page.window.width = 400
    page.window.alignment = ft.alignment.center
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def centrar_fila(fila):
        """Recibe una fila y la centra en el eje X (Horizontal)"""
        fila.alignment=ft.MainAxisAlignment.START
        return fila

    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    titulo = ft.Text("TO - DO   LIST", 
        size=40,                           # Tamaño de fuente
        weight=ft.FontWeight,              # Negrita
        color=ft.Colors.BLUE_900,          # Color Azul Oscuro
        text_align=ft.TextAlign.CENTER,    # Centrar el texto
        font_family="Arial"                # Funte de letra)
    )
    fila_titulo =  centrar_fila(ft.Row([titulo]))
    
    new_task = ft.TextField(hint_text="Escriba una Nueva Tarea", width=250)
    fila_entrada = centrar_fila(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))
    
    
    page.add(
        ft.Column(controls=[
                fila_titulo, 
                fila_entrada
            # alignment=ft.MainAxisAlignment.CENTER,                  # Alinea Verticalmente al centro 
            # horizontal_alignment= ft.CrossAxisAlignment.CENTER      # Alinea Horizontalmente al centro
        ])
    )
    
ft.app(main)