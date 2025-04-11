import flet as ft
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_DB = os.path.join(BASE_DIR, "nombres.db")

def init_db():
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS personas (
                id INTEGER PRIMARY KEY,
                nombre TEXT
            )
        """)
        mi_conexion.commit()

def guardar_nombre(nombre):
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute("INSERT INTO personas (nombre) VALUES (?)", (nombre,))
        mi_conexion.commit()

def obtener_nombres():
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute("SELECT nombre FROM personas")
        nombres = [row[0] for row in cursor.fetchall()]
        return nombres

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.height = 700
    page.window.width = 500
    page.window.alignment = ft.alignment.center
    page.title = "Flet + Base de Datos"
    
    nombre_input = ft.TextField(label="Escribe tu nombre")
    lista_nombres = ft.Column()

    def actualizar_lista():
        lista_nombres.controls.clear()
        for nombre in obtener_nombres():
            lista_nombres.controls.append(ft.Text(nombre))
        page.update()

    def on_submit(e):
        if nombre_input.value.strip():
            guardar_nombre(nombre_input.value.strip())
            nombre_input.value = ""
            actualizar_lista()

    boton_guardar = ft.ElevatedButton("Guardar nombre", on_click=on_submit)
    page.add(nombre_input, boton_guardar, lista_nombres)
    actualizar_lista()

if __name__ == "__main__":
    init_db()
    ft.app(target=main)
