import ast

# ------------------------------------------------------------
# Ejemplo práctico con ast.literal_eval() para convertir datos de texto a estructuras de datos
# ------------------------------------------------------------

# 📌 Supón que tenemos una cadena que contiene una lista de precios de productos
productos_precios_cadena = "[{'nombre': 'Laptop', 'precio': 1500}, {'nombre': 'Auriculares', 'precio': 150}, {'nombre': 'Mouse', 'precio': 50}]"

# 📌 Usamos ast.literal_eval() para convertir la cadena en una lista de diccionarios
# 🚨 ast.literal_eval() es seguro, solo convierte estructuras literales de Python (listas, diccionarios, tuplas, etc.)
productos_precios = ast.literal_eval(productos_precios_cadena)

# 📌 Ahora tenemos una lista de diccionarios de productos con sus precios
print("Lista de productos y precios:")
for producto in productos_precios:
    print(f"{producto['nombre']} - ${producto['precio']}")

# ------------------------------------------------------------
# 🔍 ¿Qué sucede si usamos eval() en lugar de ast.literal_eval()?
# ------------------------------------------------------------
# Si usáramos eval() en este caso, estaría permitiendo la ejecución de cualquier código,
# lo que podría ser muy peligroso si los datos provienen de una fuente no confiable.
# eval(productos_precios_cadena)  # 🚨 ¡Peligroso! Podría ejecutar código malicioso.
# ------------------------------------------------------------
