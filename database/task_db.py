import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_DB = os.path.join(BASE_DIR, "to-do.db")


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
        cursor.execute("SELECT id, title, done FROM tasks ORDER BY done ASC, id DESC")
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

def edit_task(task_id, title):
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute("UPDATE tasks SET title=? WHERE id=?", (title, task_id))
        mi_conexion.commit()


def delete_task(task_id):
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        mi_conexion.commit()


def count_done():
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute('SELECT done, COUNT(*) AS cantidad FROM tasks GROUP BY done')
        resultados = cursor.fetchall()

        realizadas = 0
        no_realizadas = 0

        for done, cantidad in resultados:
            if done == 1:
                realizadas = cantidad
            elif done == 0:
                no_realizadas = cantidad
        total = realizadas + no_realizadas

        return {"realizadas": realizadas, "no_realizadas": no_realizadas, "total": total}

