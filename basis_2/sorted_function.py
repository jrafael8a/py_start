# La funcion sorted() es una funcion incorporada en Python que se utiliza para ordenar 
# los elementos de un iterable, como una lista, tupla o conjunto.
# La funcion sorted() toma dos argumentos:
#     - el iterable que contiene los elementos a ordenar
#     - una funcion (opcional) que se utiliza para definir el criterio de ordenamiento.

# `sorted()` devuelve una LISTA de los elementos ordenados de un iterable.
# Puedes especificar un criterio de ordenación usando el argumento `key` y también definir el orden con el argumento `reverse`.

print("Ejemplo 1: Ordenar una lista de números de menor a mayor.")
numeros = [4, 2, 9, 1]
resultado = sorted(numeros)
print(resultado)  # Salida: [1, 2, 4, 9]

print("")
print("Ejemplo 2: Ordenar una lista de cadenas por su longitud.")
palabras = ["banana", "manzana", "cereza"]
resultado = sorted(palabras, key=lambda x: len(x))
print(resultado)  # Salida: ['cereza', 'banana', 'manzana']

print("")
print("Ejemplo 3: Ordenar en orden descendente.")
resultado = sorted(numeros, reverse=True)
print(resultado)  # Salida: [9, 4, 2, 1]

print("")
print("Ejemplo 4: Ordenar un objeto por el segundo elemento.")
personas = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "Ana", "edad": 22},
    {"nombre": "Pedro", "edad": 30},
    {"nombre": "Maria", "edad": 28},
]

personas_ordenadas = sorted(personas, key=lambda persona: persona["edad"])
print(personas_ordenadas)


print("")
print("Ejemplo 5: Combinar y Ordenar dos listas. sorted() y set()")
def merge_arrays(arr1, arr2):
    # Combina el Array 1 y el Array 2
    # Set remueve los duplicados
    # sorted() ordena el array combinado
    # y devuelve una lista ordenada
    return sorted(set(arr1 + arr2))

a = [1,2,3,3,4,5,6]
b = [4,4,5,6,7,8,9]

c = merge_arrays(a, b)
print(c)  # Salida: [1, 2, 3, 4, 5, 6, 7, 8, 9]