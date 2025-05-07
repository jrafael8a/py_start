import sqlite3
import os
from src.app_my_restaurant.database.db_connection import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_DB = os.path.join(BASE_DIR, "restaurant.db")


# -------------------- Base de datos --------------------

def init_db():
    with get_connection() as mi_conexion:
        cursor = mi_conexion.cursor()
        
        # Habilitar las claves foráneas
        cursor.execute('''PRAGMA foreign_keys = ON''') 
        
        # Tabla de usuarios (login)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL UNIQUE,
                pass TEXT NOT NULL,
                rol TEXT NOT NULL
            )
        ''')


        # Tabla de mesas
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS mesas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                capacidad INTEGER NOT NULL,
                estado INTEGER NOT NULL DEFAULT 0
            )
            '''
        )
        
        # Estado de las mesas como: 
            # 0: Libre, 
            # 1: Reservada, 
            # 2: Ocupada,
            # 3: Orden Tomada,
            # 4: En preparación,
            # 5: Comiendo, o En Servicio,
            # 6: Esperando cuenta,
            # 7: Pago en proceso,
            # 8: Necesita limpieza,
            # 9: Fuera de servicio

        # Flujo de trabajo de los estados:             DE → A       ESTADO
        # Mesa libre:                                   * - 0       Libre
        # Mesa reservada:                               0 → 1       Reservada
        # Mesa asignada a cliente	                    0 → 2       Ocupada
        # Mesero toma orden	                            2 → 3       Orden Tomada
        # Cocina marca pedido como "en preparacion"	    3 → 4       En Preparacion
        # Cocina marca pedido como “listo”	            4 → 5       Comiendo
        # Cliente pide la cuenta	                    5 → 6       Esparando cuenta
        # Pago rechazado	                            6 → 7       Pago en proceso
        # Pago exitoso	                                6 → 8       Necesita Limpieza
        # Mesa limpiada y lista de nuevo	            8 → 0       Libre de nuevo
        # Mesa inhabilitada por alguna razón	        * → 9       Fuera de servicio


        # Tabla de items del menu
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS menu_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                tipo TEXT NOT NULL,
                precio REAL NOT NULL,
                estado INTEGER NOT NULL DEFAULT 1
            )
            '''
        )
        # Estado de los items del menu como: 0: Inactivo, 1: Activo


        # Tabla de pedidos
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS pedidos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_mesa INTEGER NOT NULL,
                fecha_hora TEXT NOT NULL,
                estado INTEGER NOT NULL,
                FOREIGN KEY (id_mesa) REFERENCES mesas(id)
            )
            '''
        )
        # fecha_hora: En formato ISO 8601, es decir: YYYY-MM-DD HH:MM:SS
        # Estado de los pedidos como: 0: Pendiente, 1: En preparación, 2: Listo, 3: Entregado


         # Tabla de ítems en un pedido
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS pedido_items(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_pedido INTEGER NOT NULL,
                id_menu_item INTEGER NOT NULL,
                cantidad INTEGER NOT NULL,
                FOREIGN KEY (id_pedido) REFERENCES pedidos(id)
                FOREIGN KEY (id_menu_item) REFERENCES menu_items(id)
            )
            '''
        )


        # Tabla de pagos
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS pagos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_pedido INTEGER NOT NULL,
                fecha_hora TEXT NOT NULL,
                monto REAL NOT NULL,
                metodo_pago TEXT NOT NULL,
                FOREIGN KEY (id_pedido) REFERENCES pedidos(id)
            )
            '''
        )
        # fecha_hora: En formato ISO 8601, es decir: YYYY-MM-DD HH:MM:SS
        # metodo_pago: Efectivo, Tarjeta de crédito, Tarjeta de débito, Transferencia bancaria


    # Fin del with get_connection()
        
def get_img_db():
    try:
        with sqlite3.connect(RUTA_DB) as mi_conexion:
            cursor = mi_conexion.cursor()
            cursor.execute('''
                SELECT id, nombre, ruta, fecha, desc, hidden FROM images_db
            ''')
            rows = cursor.fetchall()
            return rows
    except sqlite3.Error as e:
        print(f"Error al obtener imagen(es): {e}")

def save_img_db(nombre, ruta, fecha="", desc="", hidden=0):
    try:
        with sqlite3.connect(RUTA_DB) as mi_conexion:
            cursor = mi_conexion.cursor()
            cursor.execute('''
                INSERT INTO images_db (nombre, ruta, fecha, desc, hidden) 
                VALUES (?, ?, ?, ?, ?)
                ''',
                (nombre, ruta, fecha, desc, hidden))
            mi_conexion.commit()
    except sqlite3.Error as e:
        print(f"Error al guardar imagen(es): {e}")

def hidde_img_db(id_img, hidden):
    try:
        with sqlite3.connect(RUTA_DB) as mi_conexion:
            cursor = mi_conexion.cursor()
            cursor.execute('''
                UPDATE images_db 
                SET hidden = ?
                WHERE id = ?
            ''',
            (not hidden, id_img))
            mi_conexion.commit()
    except sqlite3.Error as e:
        print(f"Error al eliminar imagen: {e}")



def del_img_db(id_img):
    try:
        with sqlite3.connect(RUTA_DB) as mi_conexion:
            cursor = mi_conexion.cursor()
            cursor.execute('''
                DELETE FROM images_db WHERE id = ?
            ''',
            (id_img,))
            mi_conexion.commit()
    except sqlite3.Error as e:
        print(f"Error al eliminar imagen: {e}")
