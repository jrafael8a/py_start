import flet as ft               # Importamos Flet para construir la interfaz gráfica
import sqlite3                  # Importamos sqlite3, que ya viene con Python, para manejar la base de datos

# Con estas 3 lineas nos aseguramos de que la base de datos se cree en la misma carpeta que el script
import os                       # Importamos os para manejar las rutas de archivos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # Obtiene el directorio actual del archivo
RUTA_DB = os.path.join(BASE_DIR, "nombres.db")          # Crea la ruta completa para la base de datos


# --- Funciones de backend (base de datos) ---

def init_db():
    """
    Esta función crea la base de datos y la tabla si no existen.
    """
    
    conn = sqlite3.connect(RUTA_DB)                         # Crea una conexión con el archivo .db (si no existe, se crea)

    # Comente esta linea porque crea la base en la ruta actual de la terminal y no en la carpeta del proyecto
    # conn = sqlite3.connect("nombres.db")    # Crea una conexión con el archivo .db (si no existe, se crea) 

    
    cursor = conn.cursor()                  # Creamos un cursor para ejecutar comandos SQL
    # Un cursor es un objeto que te permite ejecutar comandos SQL y recuperar resultados

    # cursor.execute(...) para correr comandos SQL.
    # cursor.fetchall() para traer resultados de consultas.
    # cursor.fetchone() para traer solo una fila.
    # cursor.lastrowid para saber el ID del último insert.


    # Creamos la tabla 'personas' si no existe aún
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS personas (
            id INTEGER PRIMARY KEY,
            nombre TEXT
        )
    """)
    conn.commit()                           # Guardamos los cambios
    conn.close()                            # Cerramos la conexión a la base de datos

def guardar_nombre(nombre):
    """
    Inserta un nombre en la tabla personas.
    """
    conn = sqlite3.connect(RUTA_DB)         # Abrimos la base de datos
    cursor = conn.cursor()                  # Creamos un cursor

    # Insertamos el nombre usando un placeholder [?] (para evitar inyecciones SQL)
    cursor.execute("INSERT INTO personas (nombre) VALUES (?)", (nombre,))
    # El ? lo que hará es pasar todo el contenido de la variable nombre como cadena a SQL
    # Asi, aunque alguien escriba una inyeccion SQL, esta no tendra efecto. 
    # Solo sera guardada como texto en el campo nombre, sin afectar a la DB
    # Importante, el metodo execute espera una tupla, asi que DEBE llevar esa coma (nombre,)
    
    conn.commit()                           # Guardamos los cambios
    conn.close()                            # Cerramos la conexión

def obtener_nombres():
    """
    Recupera todos los nombres almacenados en la base de datos.
    """
    conn = sqlite3.connect(RUTA_DB)         # Abrimos la base de datos
    cursor = conn.cursor()                  # Creamos el cursor

    # Ejecutamos una consulta para obtener todos los nombres
    cursor.execute("SELECT nombre FROM personas")
    nombres = [row[0] for row in cursor.fetchall()]  # Extraemos los nombres desde los resultados

    conn.close()                            # Cerramos la conexión
    return nombres                          # Devolvemos la lista de nombres


# --- Interfaz de usuario (Flet) ---

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.height = 700
    page.window.width = 500
    page.window.alignment = ft.alignment.center

    page.title = "Flet + Base de Datos"
    
    # Campo de entrada para el nombre
    nombre_input = ft.TextField(label="Escribe tu nombre")

    # Contenedor tipo Columna para mostrar los nombres guardados
    lista_nombres = ft.Column()

    def actualizar_lista():
        """
        Refresca la lista de nombres mostrados en pantalla.
        """
        lista_nombres.controls.clear()      # Borra los controles actuales
        for nombre in obtener_nombres():    # Obtiene los nombres de la BD
            lista_nombres.controls.append(ft.Text(nombre))  # Los muestra como texto
        page.update()

    def on_submit(e):
        """
        Se ejecuta cuando el usuario hace clic en el botón para guardar.
        """
        if nombre_input.value.strip():      # Verifica que el campo no esté vacío
            guardar_nombre(nombre_input.value.strip())  # Guarda el nombre en la BD
            nombre_input.value = ""         # Limpia el campo
            actualizar_lista()              # Refresca la lista en pantalla

    # Botón para guardar el nombre
    boton_guardar = ft.ElevatedButton("Guardar nombre", on_click=on_submit)

    # Añadimos los elementos a la página
    page.add(nombre_input, boton_guardar, lista_nombres)

    # Al iniciar, mostramos los nombres guardados
    actualizar_lista()


# --- Ejecutar la aplicación ---

if __name__ == "__main__":
    init_db()                               # Inicializa la base de datos al comenzar
    ft.app(target=main)                     # Lanza la app con Flet
