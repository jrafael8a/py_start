# La función zip() en Python Se usa para agrupar elementos de varios iterables 
# (como listas, tuplas, cadenas, etc.) de tal manera que se combinan de forma paralela. 
# Es decir, empareja los elementos de los iterables según sus posiciones.

# `zip()` combina múltiples iterables en tuplas, agrupando los elementos en orden.

print("\nEjemplo 1: Emparejar elementos de dos listas.")
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
resultado = zip(lista1, lista2)
print(list(resultado))  # Salida: [(1, 'a'), (2, 'b'), (3, 'c')]


print("\nEjemplo 2: Combinar tres listas.")
lista3 = [10, 20, 30]
resultado = zip(lista1, lista2, lista3)
print(list(resultado))  # Salida: [(1, 'a', 10), (2, 'b', 20), (3, 'c', 30)]


# `zip()` detiene la combinación al llegar al final del iterable más corto.
print("\nEjemplo 3: Diferentes longitudes de listas.")
lista1 = [1, 2, 3, 4]
lista2 = ['a', 'b']
resultado = zip(lista1, lista2)
print(list(resultado))  # Salida: [(1, 'a'), (2, 'b')]
# Solo se combinan hasta el segundo elemento de la segunda lista.


# zip() se puede usar para crear diccionarios.
print("\nEjemplo 4: Crear un diccionario.")
lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]
resultado = dict(zip(lista1, lista2))
print(resultado)  # Salida: {'a': 1, 'b': 2, 'c': 3}


print("\nEjemplo 5: Creando otro diccionario")
nombres = ['Juan', 'Ana', 'Pedro', 'Maria']
edades = [25, 30, 22, 28]
resultado = dict(zip(nombres, edades))
print(resultado)  # Salida: {'Juan': 25, 'Ana': 30, 'Pedro': 22, 'Maria': 28}
# En este caso, los nombres son las claves y las edades son los valores.


print("\nEjemplo 6: Sin usar zip()")
names = ["Alice", "Bob", "Charlie", "David", "Elizabeth"]
ages = [30, 25, 35, 20]

for idx in range(min(len(names), len(ages))):
    name = names[idx]
    age = ages[idx]
    print(f"{name} is {age} years old")
# Se usa min(len(names), len(ages)) en este caso porque, si una lista 
# es mas grande que la otra, dara un error "index out of bounds exception"
# Asi que esa linea hace que solo se imprima hasta la lista con menos items

print("\nEjemplo 7: Usando zip nuevamente")
combined = list(zip(names, ages))

for name, age in combined:
    print(f"{name} is {age} years old")
# Aqui ya no tenemos que hacer especificaciones de la lista con menos elementos
# eso lo hace zip automaticamente

print("\nEjemplo 8: Podemos combinar mas listas")
genders = ["Female", "Male", "Male"]

combined2   = list(zip(names, ages, genders))

for name, age, gender in combined2:
    print(f"{name} is {age} years old and is {gender}")
