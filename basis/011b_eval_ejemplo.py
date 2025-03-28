# ------------------------------------------------------------
# 🛒 Simulación de un sistema de descuentos dinámicos en una tienda online
# ------------------------------------------------------------

# 📌 Fórmula definida por el administrador en la configuración
# Representa la regla de negocio para calcular el precio final de un producto.
# En este caso, aplica un descuento porcentual.
formula_descuento = "precio * (1 - descuento / 100)"

# 📌 Datos de un producto
# Diccionario que almacena la información del producto, como su nombre, precio y descuento aplicable.
producto = {
    "nombre": "Laptop Gamer",
    "precio": 1500,  # Precio original en dólares
    "descuento": 10   # Descuento en porcentaje
}

# 📌 Definimos un diccionario con las variables permitidas para eval()
# Esto es importante por varias razones:
# 1️⃣ 🔒 **Seguridad**: Restringimos el acceso solo a estas variables,
#    evitando que eval() pueda acceder a otras partes del código o ejecutar comandos peligrosos.
# 2️⃣ ⚡ **Eficiencia**: Python no tiene que buscar las variables en todo el espacio global,
#    solo en este diccionario, lo que mejora el rendimiento.
# 3️⃣ 🎯 **Control sobre el entorno**: Nos aseguramos de que eval() solo utilice las variables necesarias.
variables_permitidas = {
    "precio": producto["precio"],
    "descuento": producto["descuento"]
}

# 📌 Evaluamos la fórmula con eval() en un entorno controlado
# En este caso:
#   - formula_descuento = "precio * (1 - descuento / 100)"
#   - precio = 1500
#   - descuento = 10
#   - Se evaluará como: 1500 * (1 - 10 / 100) -> 1500 * 0.9 -> 1350
#
# NOTA: No pasamos variables globales (usamos `{}` en eval()),
#       lo que impide que se acceda a funciones peligrosas.
precio_final = eval(formula_descuento, {}, variables_permitidas)

# 📌 Mostramos el resultado
print(f"Producto: {producto['nombre']}")
print(f"Precio original: ${producto['precio']}")
print(f"Descuento aplicado: {producto['descuento']}%")
print(f"Precio final: ${precio_final:.2f}")

# ------------------------------------------------------------
# 🔍 ¿Qué pasaría si NO usamos variables_permitidas y hacemos eval(formula_descuento) directamente?
#
# precio_final = eval(formula_descuento)
#
# 1️⃣ 🔴 **Riesgo de seguridad**: eval() tendría acceso a TODAS las variables globales y locales.
#    Un usuario malintencionado podría hacer algo como:
#    eval("__import__('os').system('rm -rf /')")  # ⚠ Borraría todo el sistema en Linux/Mac
#
# 2️⃣ 🔴 **Ineficiencia**: Python buscaría 'precio' y 'descuento' en todo el código,
#    lo que podría ser más lento si el programa tiene muchas variables.
#
# 3️⃣ 🔴 **Falta de control**: eval() podría acceder a cualquier variable del programa,
#    incluyendo datos sensibles como claves de API.
#    Ejemplo:
#    api_key = "secreto123"
#    print(eval("api_key"))  # 😱 Imprimiría "secreto123", lo que es un problema de seguridad.
#
# 📌 Conclusión: SIEMPRE usa eval() con un entorno controlado para evitar riesgos.
# ------------------------------------------------------------
