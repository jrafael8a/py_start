import flet as ft
import os
from datetime import datetime
from src.app.database.gallery_db import *
from src.app.utils.utilidades import obtener_carpeta_raiz


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

    # Botón para subir imágenes
    boton_subir = ft.ElevatedButton(
        "Subir imágenes",
        icon=ft.Icons.UPLOAD_FILE,
        on_click=lambda _: file_picker.pick_files(
            allow_multiple=True,
            allowed_extensions=["png", "jpg", "jpeg", "gif", "webp"]
        )
    )

    # Botón para mostrar imágenes ocultas
    boton_mostrar = ft.ElevatedButton(
        "Mostrar imágenes ocultas",
        icon=ft.Icons.VISIBILITY,
        on_click=lambda _: mostrar_ocultas()
    )

    # Botón para mostrar imágenes ocultas
    boton_ocultar = ft.ElevatedButton(
        "Volver a Ocultar",
        icon=ft.Icons.VISIBILITY_OFF,
        on_click=lambda _: cargar_imgs()
    )
    boton_ocultar.visible = False
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
                            ft.IconButton(icon=
                                        ft.Icons.VISIBILITY if hidden else ft.Icons.VISIBILITY_OFF, 
                                        on_click=lambda e, id=id_imagen, nombre=nombre_img, hidden=hidden: ocultar_imagen(id, nombre, hidden)),
                            ft.IconButton(icon=ft.Icons.DELETE, on_click=lambda e, id=id_imagen, nombre=nombre_img, ruta=ruta: confirmar_eliminar_imagen(id, nombre, ruta)),
                        ],
                        )
                    ],
                    alignment='center',
                    horizontal_alignment='center',
                    ),
                    padding=10,
                    on_click=lambda e, id=id_imagen, nombre=nombre_img, ruta=ruta, hidden=hidden: img_preview(id,nombre,ruta,hidden)
                ),
                visible=not hidden,
            )
            
            grid_view.controls.append(card)


    def img_preview(id,nombre,ruta,hidden):
        dlg_preview = ft.AlertDialog(
            modal=False,
            title=ft.Text(nombre),
            content=ft.Container(
                ft.Row([
                    ft.Image(
                        src=ruta,
                        expand=True,
                        fit=ft.ImageFit.COVER,
                        border_radius=10
                    ),
                    ]),
            ),
            actions=[
                ft.ElevatedButton("Ocultar", on_click=lambda e: (ocultar_imagen(id, nombre, hidden), page.close(dlg_preview))),
                ft.ElevatedButton("Eliminar", on_click= lambda e: (confirmar_eliminar_imagen(id, nombre, ruta), page.close(dlg_preview))),
                ft.ElevatedButton("Cancelar", on_click= lambda e: page.close(dlg_preview)),
            ],
            on_dismiss=lambda e: page.close(dlg_preview),
        )
        page.open(dlg_preview)


    def subir_imagen(e: ft.FilePickerResultEvent):
        """Maneja el evento de seleccionar una imagen para subir"""
        if not e.files:
            return
        
        # Obtener la carpeta raíz del proyecto
        carpeta_raiz = obtener_carpeta_raiz()
        
        for f in e.files:
            # Verificar si la ruta está dentro de la carpeta raíz del proyecto
            ruta_absoluta = os.path.abspath(f.path)
            if ruta_absoluta.startswith(carpeta_raiz):
                # Convertir a ruta relativa
                ruta_guardar = os.path.relpath(ruta_absoluta, carpeta_raiz)
            else:
                # Usar ruta absoluta
                ruta_guardar = ruta_absoluta

            # Guardar la imagen en la base de datos
            save_img_db(
                nombre = f.name, 
                ruta = ruta_guardar, 
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                desc = "",
                hidden = 0
            )
                    
        # Refrescar la cuadrícula con las nuevas imágenes
        cargar_imgs()

        
        # Mostrar mensaje de confirmación
        page.open(ft.SnackBar(
            content=ft.Text(f"Se han subido {len(e.files)} imagen(es) correctamente"),
            action="OK!"
        ))
        page.update()
    
    def ocultar_imagen(id_imagen, nombre_img, hidden):
        """Oculta una imagen de la base de datos y actualiza la galería"""
        hidde_img_db(id_imagen, hidden)
        # accion = "Ocultada" if hidden == 0 else "Mostrada"

        cargar_imagenes_desde_db()
        grid_view.update()
        
        if boton_ocultar.visible:
            mostrar_ocultas()


    def mostrar_ocultas():
        for item in grid_view.controls:
            item.visible = True
        grid_view.update()
       
        boton_mostrar.visible = False
        boton_ocultar.visible = True
        boton_mostrar.update()
        boton_ocultar.update()

    def cargar_imgs():
        cargar_imagenes_desde_db()
        grid_view.update()

        boton_mostrar.visible = True
        boton_ocultar.visible = False
        boton_mostrar.update()
        boton_ocultar.update()

    def confirmar_eliminar_imagen(id_imagen, nombre_imagen, ruta):
        dlg_eliminar = ft.AlertDialog(
            modal=False,
            title=ft.Text("Confirmar Eliminar"),
            content=ft.Container(
                ft.Row([
                    ft.Image(
                        src=ruta,
                        width=300,
                        height=200,
                        fit=ft.ImageFit.COVER,
                        border_radius=10
                    ),
                    ft.Text(f"Esta seguro que desea eliminar la imagen \n" \
                            f"{nombre_imagen}", 
                            expand=True, 
                            max_lines=2, 
                            overflow=ft.TextOverflow.ELLIPSIS),
                    ]),
            ),
            actions=[
                ft.ElevatedButton("Si", on_click= lambda e: (eliminar_imagen(id_imagen, nombre_imagen), page.close(dlg_eliminar))),
                ft.ElevatedButton("No", on_click= lambda e: page.close(dlg_eliminar))
            ],
            on_dismiss=lambda e: page.close(dlg_eliminar),
        )
        page.open(dlg_eliminar)
        

    def eliminar_imagen(id_imagen, nombre_img):
        """Elimina una imagen de la base de datos y actualiza la galería"""
        # Eliminar la imagen de la base de datos
        del_img_db(id_imagen)
        
        # Refrescar la cuadrícula sin la imagen eliminada
        cargar_imgs()

        # Mostrar mensaje de confirmación
        page.open(ft.SnackBar(
            content=ft.Text(f"Imagen eliminada correctamente: {nombre_img}", expand=True, max_lines=2, overflow=ft.TextOverflow.ELLIPSIS),
            action="OK!"
        ))
        page.update()
    
    
    
    # ---------- Construyendo la Interfas ----------    
    # Configurar el selector de archivos
    file_picker = ft.FilePicker(on_result=subir_imagen)
    page.overlay.append(file_picker)
    
    
    
    # Inicializar la base de datos
    init_db()
    
    # Cargar imágenes existentes al iniciar
    cargar_imagenes_desde_db()

    page.add(
        ft.Container(
            content=ft.Column([
                titulo,
                ft.Container(height=10),
                boton_subir, boton_mostrar, boton_ocultar,
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