import flet as ft
import sqlite3
import os
import base64
from datetime import datetime
import io

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Mi Galería de Imágenes"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    # Conectar a la base de datos SQLite
    conn = sqlite3.connect('galeria.db')
    cursor = conn.cursor()

    # Crear tabla si no existe
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS imagenes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        datos BLOB,
        fecha TEXT
    )
    ''')
    conn.commit()

    # Contenedor para la cuadrícula de imágenes
    grid_view = ft.GridView(
        expand=True,
        runs_count=3,
        max_extent=300,
        spacing=10,
        run_spacing=10,
        padding=20
    )

    def cargar_imagenes_desde_db():
        """Carga todas las imágenes de la base de datos y las muestra en la cuadrícula"""
        grid_view.controls.clear()
        cursor.execute("SELECT id, nombre, datos, fecha FROM imagenes")
        for imagen in cursor.fetchall():
            id_imagen, nombre, datos_blob, fecha = imagen
            
            # Crear un Container con la imagen y su nombre
            imagen_control = ft.Image(
                src_base64=base64.b64encode(datos_blob).decode('utf-8'),
                width=250,
                height=250,
                fit=ft.ImageFit.COVER,
                border_radius=10
            )
            
            # Crear tarjeta para cada imagen
            card = ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        imagen_control,
                        ft.Container(
                            content=ft.Text(nombre, size=14),
                            padding=10,
                            alignment=ft.alignment.center
                        )
                    ]),
                    width=250,
                    height=300,
                    padding=5
                )
            )
            
            grid_view.controls.append(card)
        
        page.update()

    def subir_imagen(e: ft.FilePickerResultEvent):
        """Maneja el evento de seleccionar una imagen para subir"""
        if not e.files:
            return
        
        for f in e.files:
            # Leer los datos del archivo
            file_path = f.path
            with open(file_path, 'rb') as file:
                file_data = file.read()
            
            # Guardar la imagen en la base de datos
            cursor.execute(
                "INSERT INTO imagenes (nombre, datos, fecha) VALUES (?, ?, ?)",
                (f.name, file_data, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            )
            conn.commit()
        
        # Refrescar la cuadrícula con las nuevas imágenes
        cargar_imagenes_desde_db()
        
        # Limpiar el mensaje de estado
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Se han subido {len(e.files)} imagen(es) correctamente"),
            action="OK!"
        )
        page.snack_bar.open = True
        page.update()

    # Configurar el selector de archivos
    file_picker = ft.FilePicker(on_result=subir_imagen)
    page.overlay.append(file_picker)

    # Encabezado
    titulo = ft.Text("Mi Galería de Imágenes", size=32, weight=ft.FontWeight.BOLD)
    
    # Botón para subir imágenes
    boton_subir = ft.ElevatedButton(
        "Subir imágenes",
        icon=ft.icons.UPLOAD_FILE,
        on_click=lambda _: file_picker.pick_files(
            allow_multiple=True,
            allowed_extensions=["png", "jpg", "jpeg", "gif", "webp"]
        )
    )

    # Cargar imágenes existentes al iniciar
    cargar_imagenes_desde_db()

    # Construir la interfaz
    page.add(
        ft.Container(
            content=ft.Column([
                titulo,
                ft.Container(height=20),
                boton_subir,
                ft.Container(height=20),
                ft.Divider(),
                ft.Container(height=10),
                ft.Text("Mis imágenes", size=20, weight=ft.FontWeight.BOLD),
                ft.Container(height=10),
                grid_view
            ]),
            padding=10
        )
    )

    # Manejar la limpieza al cerrar
    def page_dispose():
        conn.close()
    
    page.on_dispose = page_dispose

ft.app(target=main)