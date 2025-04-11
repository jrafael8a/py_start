# 1. Definición de una tupla con varios tipos de datos
mi_tupla = (1, 2, 3, 'a', 'b')

# 2. Acceder a un elemento por su índice (similar a las listas)
print(mi_tupla[0])  # Imprime: 1
print(mi_tupla[3])  # Imprime: 'a'
print(mi_tupla[-1]) # Imprime: 'b'

# 3. Slicing (Corte) para obtener una subtupla
# Esto selecciona los elementos desde el índice 1 hasta el índice 3 (sin incluir el índice 3)
subtupla = mi_tupla[1:3]
print(subtupla)  # Imprime: (2, 3)

# 4. Acceder a los elementos desde el final de la tupla usando índices negativos
# El índice -1 es el último elemento
print(mi_tupla[-1])  # Imprime: 'b'
print(mi_tupla[-2])  # Imprime: 'a'
print(mi_tupla[-3])  # Imprime: 3

# 5. Iterar sobre una tupla (como con listas)
for elemento in mi_tupla:
    print(elemento)
# Imprime:
# 1
# 2
# 3
# a
# b

# 6. Desempaquetado de una tupla
# Desempaquetamos los valores de la tupla en variables
x, y, z, a, b = mi_tupla
print(x, y, z, a, b)  # Imprime: 1 2 3 a b

# 7. Verificar si un elemento está en la tupla
# Usamos el operador `in` para comprobar si un elemento está presente en la tupla
print('a' in mi_tupla)  # Imprime: True
print(4 in mi_tupla)    # Imprime: False

# 8. Obtener el índice de un elemento (solo el primero que aparece)
# Usamos `index()` para encontrar la primera aparición de un valor
indice_a = mi_tupla.index('a')
print(indice_a)  # Imprime: 3 (el índice donde aparece 'a')

# 9. Contar cuántas veces aparece un valor en la tupla
# Usamos `count()` para contar las repeticiones de un valor
contar_3 = mi_tupla.count(3)
print(contar_3)  # Imprime: 1 (solo aparece una vez el 3)

# 10. Tupla con un solo elemento (importante agregar la coma)
tupla_un_elemento = (5,)
print(type(tupla_un_elemento))  # Imprime: <class 'tuple'>

# 11. Concatenacion de tuplas (unir dos o más tuplas)
otra_tupla = ('x', 'y', 'z')
tupla_concatenada = mi_tupla + otra_tupla
print(tupla_concatenada)  # Imprime: (1, 2, 3, 'a', 'b', 'x', 'y', 'z')

# 12. Repetir una tupla
# Podemos repetir una tupla un número específico de veces con el operador `*`
tupla_repetida = mi_tupla * 2
print(tupla_repetida)  # Imprime: (1, 2, 3, 'a', 'b', 1, 2, 3, 'a', 'b')

# 13. Longitud de la tupla
# Usamos `len()` para obtener la cantidad de elementos en la tupla
print(len(mi_tupla))  # Imprime: 5 (tiene 5 elementos)
