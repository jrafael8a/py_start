import flet as ft
import sqlite3
import os

# -------------------- Variables Globales --------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_DB = os.path.join(BASE_DIR, "to-do.db")

ALTURA = 700
ANCHURA = 500

# -------------------- Base de datos --------------------

def init_db():
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0
            )
        ''')
        mi_conexion.commit()

def get_tasks():
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute("SELECT id, title, done FROM tasks")
        rows = cursor.fetchall()
        return rows

def add_task(title):
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        mi_conexion.commit()

def update_done(task_id, done):
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute("UPDATE tasks SET done=? WHERE id=?", (done, task_id))
        mi_conexion.commit()

def delete_task(task_id):
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        mi_conexion.commit()





# -------------------- Interfaz Flet --------------------

def main(page: ft.Page):
    # ----- Estilo para la Interfaz -----
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.height = ALTURA
    page.window.width = ANCHURA
    page.window.alignment = ft.alignment.center
    
    page.title = "To-Do List"
    page.scroll = "auto"
    

    # ----- Definicion de variables -----
    task_input = ft.TextField(label="Nueva tarea", expand=True)
    task_list = ft.Column(width=(ANCHURA*0.95))

    # ----- Funciones de GUI -----
    def load_tasks():
        task_list.controls.clear()
        for task_id, title, done in get_tasks():
            checkbox = ft.Checkbox(
                label=title,
                value=bool(done),
                on_change=lambda e, id=task_id: toggle_done(e, id)
            )
            delete_btn = ft.IconButton(
                icon=ft.icons.DELETE,
                on_click=lambda e, id=task_id: delete(id)
            )
            task_list.controls.append(ft.Row([checkbox, delete_btn]))
        page.update()

    def toggle_done(e, task_id):
        update_done(task_id, int(e.control.value))
        load_tasks()

    def delete(task_id):
        delete_task(task_id)
        load_tasks()

    def add_clicked(e):
        if task_input.value.strip():
            add_task(task_input.value.strip())
            task_input.value = ""
            load_tasks()
            page.update()

    # ----- Construccion de la Intefaz de Usuario -----
    page.add(
        ft.Row([task_input, ft.ElevatedButton("Agregar", on_click=add_clicked)]),
        task_list
    )

    init_db()
    load_tasks()


# -------------------- Corremos nuestra aplicacion --------------------
ft.app(target=main)
