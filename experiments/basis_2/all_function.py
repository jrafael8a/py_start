# Podriamos decir que es el operador AND pero de las listas.
# Ya que solo devuelve True si todos los elementos son True.

# `all()` devuelve `True` si todos los elementos del iterable son `True`.
# Si alguno de los elementos es `False`, devuelve `False`. Si el iterable está vacío, retorna `True`.

# Es parecida a `any()`, pero en lugar de verificar si al menos un elemento es `True`,
# verifica si todos los elementos son `True`.

# Ejemplo 1: Verificar si todos los números son positivos.
numeros = [1, 2, 3, 4]
resultado = all(x > 0 for x in numeros)
print(resultado)  # Salida: True (todos son positivos)

# Ejemplo 2: Verificar si todos los números son pares.
resultado = all(x % 2 == 0 for x in numeros)
print(resultado)  # Salida: False (porque 1 no es par)
