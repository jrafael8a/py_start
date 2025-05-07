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

def eliminar_mesa(mesa_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM mesas WHERE id = ?", (mesa_id,))
