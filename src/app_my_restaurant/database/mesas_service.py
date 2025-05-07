from src.app_my_restaurant.database.db_connection import *

def obtener_mesas_desde_db():
    try:   
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, capacidad, estado FROM mesas")
            return True, cursor.fetchall()
    except Exception as e:
        return False, f"Error al obtener mesas: {e}"

def agregar_mesa_db(nombre, capacidad):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO mesas (nombre, capacidad) VALUES (?, ?)", 
                (nombre, capacidad)
            )
        return True, f"'{nombre}' agregada con éxito."
    except Exception as e:
        return False, f"Error al agregar '{nombre}': {e}"

def actualizar_mesa_db(mesa_id, nombre, capacidad, estado):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE mesas
                SET nombre = ?, capacidad = ?, estado = ?
                WHERE id = ?
            """,
            (nombre, capacidad, estado, mesa_id))
        return True, f"Mesa con ID {mesa_id} actualizada correctamente"
    except Exception as e:
        return False, f"Error al actualizar mesa con ID {mesa_id}: {e}"

def eliminar_mesa_db(mesa_id):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM mesas WHERE id = ?", (mesa_id,))
        return True, f"Mesa con ID {mesa_id} eliminada exitosamente"
    except Exception as e:
        return False, f"Error al eliminar mesa con ID {mesa_id}: {e}"
