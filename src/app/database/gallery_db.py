import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_DB = os.path.join(BASE_DIR, "gallery.db")


# -------------------- Base de datos --------------------

def init_db():
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS images_db (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                ruta TEXT NOT NULL,
                fecha TEXT,
                desc TEXT,
                hidden INTEGER NOT NULL DEFAULT 0
            )
        ''')
        mi_conexion.commit()

def get_img_db():
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute('''
            SELECT id, nombre, ruta, fecha, desc, hidden FROM images_db
        ''')
        rows = cursor.fetchall()
        return rows

def save_img_db(nombre, ruta, fecha="", desc="", hidden=0):
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute('''
            INSERT INTO images_db (nombre, ruta, fecha, desc, hidden) 
            VALUES (?, ?, ?, ?, ?)
            ''',
            (nombre, ruta, fecha, desc, hidden))
        mi_conexion.commit()