import ast

# ------------------------------------------------------------
# 📌 Uso de ast.literal_eval() en Python
# ------------------------------------------------------------
#
# 🔹 ast.literal_eval() permite evaluar expresiones literales de forma SEGURA.
# 🔹 Convierte cadenas que representan estructuras de datos (listas, diccionarios, etc.)
#    en su tipo correspondiente en Python.
# 🔹 A diferencia de eval(), NO ejecuta código arbitrario, lo que evita riesgos de seguridad.
# ------------------------------------------------------------

# 📌 Ejemplo 1: Convertir una cadena en una lista real de Python
cadena_lista = "[1, 2, 3, 4, 5]"
lista = ast.literal_eval(cadena_lista)
print(lista)        # 👉 [1, 2, 3, 4, 5]
print(type(lista))  # 👉 <class 'list'>

# 📌 Ejemplo 2: Convertir una cadena en un diccionario
cadena_diccionario = "{'nombre': 'Alice', 'edad': 25}"
diccionario = ast.literal_eval(cadena_diccionario)
print(diccionario)        # 👉 {'nombre': 'Alice', 'edad': 25}
print(type(diccionario))  # 👉 <class 'dict'>

# ------------------------------------------------------------
# 🚨 Seguridad: ¿Qué pasa si intentamos ejecutar código malicioso?
# ------------------------------------------------------------
#
# Si intentamos evaluar código peligroso con eval(), se ejecutará y puede dañar el sistema.
# Pero con ast.literal_eval(), obtendremos un error en lugar de ejecutarse.

cadena_peligrosa = "__import__('os').system('rm -rf /')"

try:
    resultado = ast.literal_eval(cadena_peligrosa)
except ValueError as e:
    print("❌ Error detectado:", e)  # 👉 No se ejecuta el código, solo muestra un error

# ------------------------------------------------------------
# 📌 ¿Cuándo usar ast.literal_eval() en lugar de eval()?
# ------------------------------------------------------------
# ✅ Cuando necesitas convertir una cadena en estructuras de datos (listas, diccionarios, tuplas, etc.).
# ✅ Cuando los datos provienen de archivos de texto, bases de datos o entradas de usuario.
# ✅ Cuando quieres seguridad y evitar la ejecución de código arbitrario.
# ❌ No usarlo si necesitas evaluar expresiones matemáticas o ejecutar código Python.
# ------------------------------------------------------------
