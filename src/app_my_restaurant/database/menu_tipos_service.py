import sqlite3
from src.app_my_restaurant.database.db_connection import *

def obtener_tipos_menu_db():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM menu_tipos WHERE estado = 1 ORDER BY nombre")
            resultados = cursor.fetchall()
            return True, [{"id": r[0], "nombre": r[1], "estado": bool(r[2])} for r in resultados]
    except Exception as e:
        return False, str(e)

def agregar_tipo_menu_db(nombre):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO menu_tipos (nombre) VALUES (?)", (nombre,))
            return True, f"Tipo agregado correctamente: {nombre}"
    except Exception as e:
        return False, str(e)

def eliminar_tipo_menu_db(id):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM menu_tipos WHERE id = ?", (id,))
            return True, f"Tipo eliminado correctamente. ID: {id}"
    except Exception as e:
        return False, str(e)

def actualizar_tipo_menu_db(id, nuevo_nombre, estado):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE menu_tipos SET nombre = ?, estado = ? WHERE id = ?", (nuevo_nombre, int(estado), id))
            return True, f"Tipo actualizado correctamente: {nuevo_nombre}"
    except Exception as e:
        return False, str(e)

def actualizar_estado_tipo_menu_db(id, estado):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE menu_tipos SET estado = ? WHERE id = ?", (int(estado), id))
            return True, f"Estado actualizado"
    except Exception as e:
        return False, str(e)
