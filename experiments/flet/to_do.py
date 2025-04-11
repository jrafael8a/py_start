import flet as ft

def main(page):
    page.window.height = 600
    page.window.width = 400
    page.window.alignment = ft.alignment.center
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def centrar_fila(fila):
        """Recibe una fila y la centra en el eje X (Horizontal)"""
        fila.alignment=ft.MainAxisAlignment.CENTER
        return fila

    def add_clicked(e):
        c_content.controls.append(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()
        c_content.update()

    titulo = ft.Text("TO - DO   LIST", 
        size=40,                           # Tamaño de fuente
        weight=ft.FontWeight,              # Negrita
        color=ft.colors.BLUE_900,          # Color Azul Oscuro
        text_align=ft.TextAlign.CENTER,    # Centrar el texto
        font_family="Arial"                # Funte de letra)
    )
    fila_titulo =  centrar_fila(ft.Row([titulo]))
    
    new_task = ft.TextField(hint_text="Escriba una Nueva Tarea", width=250)
    fila_entrada = centrar_fila(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))
    
    piepagina = ft.Text("Bytes 2025 - All right reserved ®", 
        size=14,                            # Tamaño de fuente
        weight=ft.FontWeight,               # Negrita
        italic=True,                        # Cursiva
        color=ft.colors.WHITE30,            # Color Azul Oscuro
        text_align=ft.TextAlign.CENTER,     # Centrar el texto
        font_family="Arial"                 # Funte de letra)
    )
    fila_pie =  centrar_fila(ft.Row([piepagina]))










    f_header = ft.Row()
    c_content = ft.Column([],height=250, width=300)
    f_content = ft.Row([c_content])
    f_footer = ft.Row()

    f_header.controls.append(ft.Column([fila_titulo, fila_entrada]))
    f_footer.controls.append(fila_pie)

    f_footer.alignment = ft.alignment.bottom_center

    page.add(
        ft.Column(controls=[
                centrar_fila(f_header),
                centrar_fila(f_content),
                centrar_fila(f_footer)
            ],
            # alignment=ft.MainAxisAlignment.CENTER,                  # Alinea Verticalmente al centro 
            #horizontal_alignment= ft.CrossAxisAlignment.CENTER      # Alinea Horizontalmente al centro
        )
        
    )
    new_task.focus()
    
ft.app(main)