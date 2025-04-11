# Podriamos decir que es el operador OR pero de las listas.
# Ya que devuelve True si al menos un elemento es True.

# `any()` devuelve `True` si al menos un elemento del iterable es `True`.
# Si el iterable está vacío, retorna `False`.

# Estructura de la función:
# any(iterable)
# - iterable: cualquier objeto que se pueda recorrer (listas, tuplas, conjuntos, etc.)
# Se puede usar con una función generadora o una expresión generadora para evaluar
# condiciones en los elementos del iterable.

# Ejemplo 1: Verificar si algún número en la lista es positivo.
numeros = [0, -1, -2, 3]
resultado = any(x > 0 for x in numeros)
print(resultado)  # Salida: True (porque 3 > 0)

# Ejemplo 2: Verificar si hay algún número par.
resultado = any(x % 2 == 0 for x in numeros)
print(resultado)  # Salida: True (porque -2 es par)
