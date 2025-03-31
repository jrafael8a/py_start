# `all()` devuelve `True` si todos los elementos del iterable son `True`.
# Si alguno de los elementos es `False`, devuelve `False`. Si el iterable está vacío, retorna `True`.

# Ejemplo 1: Verificar si todos los números son positivos.
numeros = [1, 2, 3, 4]
resultado = all(x > 0 for x in numeros)
print(resultado)  # Salida: True (todos son positivos)

# Ejemplo 2: Verificar si todos los números son pares.
resultado = all(x % 2 == 0 for x in numeros)
print(resultado)  # Salida: False (porque 1 no es par)
