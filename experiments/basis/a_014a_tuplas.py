"""
Tupla:
Es un tipo de dato que se utiliza para almacenar una colección de elementos. 
A diferencia de las listas, las tuplas son inmutables, lo que significa que 
una vez que se crean, no se pueden modificar (agregar, eliminar ni cambiar sus elementos).

Las tuplas se definen utilizando paréntesis () y sus elementos están separados por comas.
"""

print("Ejemplo de objeto inmutable:")
tupla = (1, 2, 3)
nueva_tupla = tupla + (4, 5)
print(nueva_tupla)  # Salida: (1, 2, 3, 4, 5)


# Tupla
mi_tupla = (1, 2, 3)

# Intentar agregar un elemento a la tupla (esto causará un error)
# mi_tupla.append(4)  # Esto no funciona porque las tuplas no tienen el método append.

# Sin embargo, puedes crear una nueva tupla CON EL MISMO NOMBRE y concatenar
mi_tupla = mi_tupla + (4,)  # Se crea una nueva tupla con el elemento agregado.
print(mi_tupla)  # Salida: (1, 2, 3, 4)
print(type(mi_tupla))  # <class 'tuple'>


""""
(4,)
notese que se agrego una coma despues del 4.
Eso es porque estamos creando una tupla de un solo elemento.
En Python, cuando escribimos algo entre paréntesis, por lo general 
se interpreta como una expresión entre paréntesis, no necesariamente como una tupla
Pero si queremos crear una tupla con un solo elemento, debemos poner 
una coma al final para que Python lo reconozca como una tupla de un solo elemento.
"""

