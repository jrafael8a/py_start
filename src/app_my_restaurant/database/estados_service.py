from src.app_my_restaurant.database.db_connection import *

def obtener_estados_desde_db():
    try:   
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, habilitado FROM estados")
            return True, cursor.fetchall()
    except Exception as e:
        return False, f"Error al obtener estados de las mesas: {e}"
    
def obtener_nombre_estado_desde_db(id):
    try:   
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT nombre FROM estados WHERE id = ?", (id,))
            fila  = cursor.fetchone()
            return fila[0] if fila else None
    except Exception as e:
        print(e)
        return f"Error al obtener el nombre del estado: {e}"

def agregar_estado_db(nombre, habilitado):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO estados (nombre, habilitado) VALUES (?, ?)", 
                (nombre, habilitado)
            )
        return True, f"Estado '{nombre}' agregado con éxito."
    except Exception as e:
        return False, f"Error al agregar '{nombre}': {e}"

def actualizar_estado_db(estado_id, nombre, habilitado):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE estados
                SET nombre = ?, habilitado = ?
                WHERE id = ?
            """,
            (nombre, habilitado, estado_id))
        return True, f"Estado con ID {estado_id} actualizado correctamente"
    except Exception as e:
        return False, f"Error al actualizar estado con ID {estado_id}: {e}"

def eliminar_estado_db(estado_id):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM estados WHERE id = ?", (estado_id,))
        return True, f"Estado con ID {estado_id} eliminado exitosamente"
    except Exception as e:
        return False, f"Error al eliminar estado con ID {estado_id}: {e}"
