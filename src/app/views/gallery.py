import flet as ft
from src.app.database.gallery_db import *
from datetime import datetime

def gallery(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.height = 600
    page.window.width = 800
    page.window.alignment = ft.alignment.center

    page.title = "Mi Galería de Imágenes"
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO


    # ---------- Declaracion de Variables y Controles ----------
    titulo = ft.Text(value="Galeria de Imagenes",
                    style=ft.TextStyle(size=30, font_family='Arial', weight='w600'),
                    text_align='center')

    grid_view = ft.GridView(
        expand=True,
        runs_count=3,
        max_extent=400,
        spacing=10,
        run_spacing=10,
        padding=20
    )

    
    # ---------- Funciones ----------

    def cargar_imagenes_desde_db():
        """Carga todas las imágenes de la base de datos y las muestra en la cuadrícula"""
        grid_view.controls.clear()
        
        for imagen in get_img_db():
            id_imagen, nombre_img, ruta, fecha, desc, hidden = imagen
            
            # Crear un Container con la imagen y su nombre
            imagen_control = ft.Image(
                src=ruta,
                width=300,
                height=200,
                fit=ft.ImageFit.COVER,
                border_radius=10
            )
            
            # Crear tarjeta para cada imagen
            card = ft.Card(
                ft.Container(
                    content=ft.Column([
                        imagen_control,
                        ft.Row([
                            ft.Text(
                                nombre_img, 
                                size=14, 
                                overflow=ft.TextOverflow.ELLIPSIS,
                                max_lines=2,
                                expand=True,
                                ),
                            ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, id=id_imagen, nombre=nombre_img: eliminar_imagen(id, nombre))
                        ],
                        )
                    ],
                    alignment='center',
                    horizontal_alignment='center',
                    ),
                    padding=10
                )
            )
            
            grid_view.controls.append(card)
        #page.update()


    def subir_imagen(e: ft.FilePickerResultEvent):
        """Maneja el evento de seleccionar una imagen para subir"""
        if not e.files:
            return
        
        for f in e.files:
            # Guardar la imagen en la base de datos
            save_img_db(
                nombre = f.name, 
                ruta = f.path, 
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                desc = "",
                hidden = 0
            )
                    
        # Refrescar la cuadrícula con las nuevas imágenes
        cargar_imagenes_desde_db()
        grid_view.update()
        
        # Mostrar mensaje de confirmación
        page.open(ft.SnackBar(
            content=ft.Text(f"Se han subido {len(e.files)} imagen(es) correctamente"),
            action="OK!"
        ))
        page.update()
    
    def eliminar_imagen(id_imagen, nombre_img):
        """Elimina una imagen de la base de datos y actualiza la galería"""
        # Eliminar la imagen de la base de datos
        del_img_db(int(id_imagen))
        
        # Refrescar la cuadrícula sin la imagen eliminada
        cargar_imagenes_desde_db()
        grid_view.update()
        
        # Mostrar mensaje de confirmación
        page.open(ft.SnackBar(
            content=ft.Text(f"Imagen eliminada correctamente: {nombre_img}"),
            action="OK!"
        ))
        page.update()
    
    
    
    # ---------- Construyendo la Interfas ----------    
    # Configurar el selector de archivos
    file_picker = ft.FilePicker(on_result=subir_imagen)
    page.overlay.append(file_picker)
    
    # Botón para subir imágenes
    boton_subir = ft.ElevatedButton(
        "Subir imágenes",
        icon=ft.icons.UPLOAD_FILE,
        on_click=lambda _: file_picker.pick_files(
            allow_multiple=True,
            allowed_extensions=["png", "jpg", "jpeg", "gif", "webp"]
        )
    )
    
    # Inicializar la base de datos
    init_db()
    
    # Cargar imágenes existentes al iniciar
    cargar_imagenes_desde_db()

    page.add(
        ft.Container(
            content=ft.Column([
                titulo,
                ft.Container(height=10),
                boton_subir,
                ft.Container(height=10),
                ft.Divider(),
                ft.Container(height=10),
                ft.Text("Mis imágenes", size=20, weight=ft.FontWeight.BOLD),
                ft.Container(height=10),
                grid_view
            ]),
            padding=10
        )
    )

if __name__ == "__main__":
    ft.app(target=gallery)