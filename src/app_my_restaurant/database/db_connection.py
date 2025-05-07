import os
import sqlite3
from contextlib import contextmanager

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_DB = os.path.join(BASE_DIR, "restaurant.db")

@contextmanager
def get_connection():
    conn = sqlite3.connect(RUTA_DB)
    conn.row_factory = sqlite3.Row  # ⬅️ Esto permite acceso tipo diccionario
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
