# `zip()` combina múltiples iterables en tuplas, agrupando los elementos en orden.

# Ejemplo 1: Emparejar elementos de dos listas.
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
resultado = zip(lista1, lista2)
print(list(resultado))  # Salida: [(1, 'a'), (2, 'b'), (3, 'c')]

# Ejemplo 2: Combinar tres listas.
lista3 = [10, 20, 30]
resultado = zip(lista1, lista2, lista3)
print(list(resultado))  # Salida: [(1, 'a', 10), (2, 'b', 20), (3, 'c', 30)]

# `zip()` detiene la combinación al llegar al final del iterable más corto.
print("Ejemplo 3: Diferentes longitudes de listas.")
lista1 = [1, 2, 3, 4]
lista2 = ['a', 'b']
resultado = zip(lista1, lista2)
print(list(resultado))  # Salida: [(1, 'a'), (2, 'b')]
# Solo se combinan hasta el segundo elemento de la segunda lista.

# zip() se puede usar para crear diccionarios.
print("Ejemplo 4: Crear un diccionario.")
lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]
resultado = dict(zip(lista1, lista2))
print(resultado)  # Salida: {'a': 1, 'b': 2, 'c': 3}

print("Ejemplo 5: Creando otro diccionario")
nombres = ['Juan', 'Ana', 'Pedro', 'Maria']
edades = [25, 30, 22, 28]
resultado = dict(zip(nombres, edades))
print(resultado)  # Salida: {'Juan': 25, 'Ana': 30, 'Pedro': 22, 'Maria': 28}
# En este caso, los nombres son las claves y las edades son los valores.