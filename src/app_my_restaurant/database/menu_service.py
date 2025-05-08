# src/app_my_restaurant/database/menu_service.py

from src.app_my_restaurant.database.db_connection import *

def obtener_menu_items_desde_db():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, tipo, precio, estado FROM menu_items")
            return True, cursor.fetchall()
    except Exception as e:
        return False, f"Error al obtener los ítems del menú: {e}"

def agregar_menu_item_db(nombre, tipo, precio, estado=1):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO menu_items (nombre, tipo, precio, estado) VALUES (?, ?, ?, ?)",
                (nombre, tipo, precio, estado)
            )
        return True, f"Ítem '{nombre}' agregado con éxito."
    except Exception as e:
        return False, f"Error al agregar ítem '{nombre}': {e}"

def actualizar_menu_item_db(item_id, nombre, tipo, precio, estado):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE menu_items SET nombre = ?, tipo = ?, precio = ?, estado = ? WHERE id = ?",
                (nombre, tipo, precio, estado, item_id)
            )
        return True, f"Ítem con ID {item_id} actualizado correctamente."
    except Exception as e:
        return False, f"Error al actualizar ítem con ID {item_id}: {e}"

def eliminar_menu_item_db(item_id):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM menu_items WHERE id = ?", (item_id,))
        return True, f"Ítem con ID {item_id} eliminado exitosamente."
    except Exception as e:
        return False, f"Error al eliminar ítem con ID {item_id}: {e}"
