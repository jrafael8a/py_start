# En Python existen diferentes tipos de conjuntos de datos, como por ejemplo:
#     - listas
#     - sets o colecciones
#     - tuplas
#     - diccionarios

print("Una lista es un conjunto MUTABLE de elementos.")
# Posee un index que permite acceder a los elementos de la lista.
# Se define con corchetes [] y los elementos se separan por comas.
# Por ejemplo:
mi_lista = [1, 3, 2, 3, 4, 5]
print(mi_lista)         # Salida: [1, 3, 2, 3, 4, 5]
print(mi_lista[0])      # Salida: 1
# Es mutable, por lo que se pueden modificar los elementos de la lista.
# Por ejemplo:
mi_lista[0] = 10
print(mi_lista)         # Salida: [10, 3, 2, 3, 4, 5]
# Se pueden agregar elementos a la lista con el metodo append()
mi_lista.append(6)
print(mi_lista)         # Salida: [10, 3, 2, 3, 4, 5, 6]
# Se pueden eliminar elementos de la lista con el metodo remove()
mi_lista.remove(3)
print(mi_lista)         # Salida: [10, 2, 3, 4, 5, 6]
# Se pueden eliminar elementos de la lista con el metodo pop()
mi_lista.pop(0)
print(mi_lista)         # Salida: [2, 3, 4, 5, 6]
# Se pueden eliminar elementos de la lista con el metodo clear()
mi_lista.clear()
print(mi_lista)         # Salida: []



print("")
print("Un Set es un conjunto de elementos UNICOS pero es MUTABLE. \n"
"Un SET No puede tener datos repetidos. Y es mas eficiente a la hora de buscar elementos.")
# Se define con llaves {} y los elementos se separan por comas.
# Por ejemplo:
mi_set = {1, 2, 3, 4, 5}
print(mi_set)         # Salida: {1, 2, 3, 4, 5}
# print(mi_set[0])      # Salida: ERROR, no se puede acceder a los elementos por index.
# En Python, los sets no tienen un indice definido, por lo que no se puede acceder a los elementos por index.
# Sin embargo, se pueden convertir a una lista para acceder a los elementos por index.

# Al ser un conjunto mutable, se pueden agregar elementos al set con el metodo add()
mi_set.add(6)
print(mi_set)         # Salida: {1, 2, 3, 4, 5, 6}



print("")
print("Una tupla es un conjunto de elementos INMUTABLES.")
# Se define con paréntesis () y los elementos se separan por comas.
# Por ejemplo:
mi_tupla = (5, 2, 8, 13, 23)
print(mi_tupla)         # Salida: (5, 2, 8, 13, 23)
print(mi_tupla[0])      # Salida: 5
# print(mi_tupla[5])      # Salida: ERROR, no se puede acceder a los elementos por index.
# En Python, las tuplas tienen un indice definido, por lo que se puede acceder a los elementos por index.
# Sin embargo, no se pueden modificar los elementos de la tupla.
# Por ejemplo:
# mi_tupla[0] = 10      # Salida: ERROR, no se puede modificar los elementos de la tupla.



print("")
print("Un FROZENSET es un conjunto de elementos INMUTABLE.")
# Se define con la funcion frozenset() y los elementos se separan por comas.
# Puede ser creado a partir de un set o una lista o una tupla.
# Por lo que su definicion puede variar dependiendo de la fuente de datos.
# Asi, si se define a partir de un set, la sintaxis es:
#     frozenset({5, 2, 8, 13, 23})
# Si se define a partir de una lista, la sintaxis es:
#     frozenset([5, 2, 8, 13, 23])
# Si se define a partir de una tupla, la sintaxis es:
#     frozenset((5, 2, 8, 13, 23))


# Por ejemplo:
mi_frozenset = frozenset({1, 2, 3, 4, 5})
print(mi_frozenset)         # Salida: frozenset({1, 2, 3, 4, 5})
# print(mi_frozenset[0])      # Salida: ERROR, no se puede acceder a los elementos por index.
# En Python, los frozensets no tienen un indice definido, por lo que no se puede acceder a los elementos por index.



print("")
print("Un diccionario es un conjunto de elementos en pares clave-valor.")
# Se define con llaves {} y los elementos se separan por comas.
# Por ejemplo:
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(mi_diccionario)         # Salida: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
print(mi_diccionario["nombre"])      # Salida: Juan
# print(mi_diccionario[0])      # Salida: ERROR, no se puede acceder a los elementos por index.

# Es un conjunto MUTABLE, por lo que se pueden modificar los elementos del diccionario.
# Por ejemplo:
mi_diccionario["nombre"] = "Pedro"
print(mi_diccionario)         # Salida: {'nombre': 'Pedro', 'edad': 30, 'ciudad': 'Madrid'}
# Se pueden agregar elementos al diccionario con el metodo update()
mi_diccionario.update({"pais": "España"})
print(mi_diccionario)         # Salida: {'nombre': 'Pedro', 'edad': 30, 'ciudad': 'Madrid', 'pais': 'España'}
# Se pueden eliminar elementos del diccionario con el metodo pop()
mi_diccionario.pop("pais")
print(mi_diccionario)         # Salida: {'nombre': 'Pedro', 'edad': 30, 'ciudad': 'Madrid'}
# Se pueden eliminar elementos del diccionario con el metodo clear()
mi_diccionario.clear()
print(mi_diccionario)         # Salida: {}
