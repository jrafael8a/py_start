from src.app_my_restaurant.database.db_connection import *

def obtener_menu_items_desde_db():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, id_cat, nombre, descripcion, precio, estado, image FROM menu_items")
            return True, cursor.fetchall()
    except Exception as e:
        return False, f"Error al obtener los ítems del menú: {e}"

def agregar_menu_item_db(nombre, descripcion, precio, categoria_id, estado=1):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO menu_items (id_cat, nombre, descripcion, precio, estado) VALUES (?, ?, ?, ?, ?)",
                (categoria_id, nombre, descripcion, precio, estado)
            )
        return True, f"Ítem '{nombre}' agregado con éxito."
    except Exception as e:
        return False, f"Error al agregar ítem '{nombre}': {e}"

def actualizar_menu_item_db(categoria_id, nombre, descripcion, precio, tipo_id, estado):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE menu_items SET id_cat = ?, nombre = ?, descripcion = ?, precio = ?, estado = ? WHERE id = ?",
                ( tipo_id, nombre, descripcion, precio, estado, categoria_id)
            )
        return True, f"Ítem con ID {categoria_id} actualizado correctamente."
    except Exception as e:
        return False, f"Error al actualizar ítem con ID {categoria_id}: {e}"

def eliminar_menu_item_db(item_id):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM menu_items WHERE id = ?", (item_id,))
        return True, f"Ítem con ID {item_id} eliminado exitosamente."
    except Exception as e:
        return False, f"Error al eliminar ítem con ID {item_id}: {e}"
