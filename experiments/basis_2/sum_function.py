# La funcion sum() es una funcion incorporada en Python que se utiliza para sumar los 
# elementos de un iterable, como una lista, tupla o conjunto.
# siempre y cuando los elementos sean numeros.
# La funcion sum() toma dos argumentos:
#     - el iterable que contiene los elementos a sumar
#     - un valor inicial (opcional) que se suma al resultado final.

numeros = {1, 4.5, 5, 23, 2}
print(sum(numeros))
# Salida: 35.5
print(sum(numeros, 10))
# Salida: 45.5
print(sum(numeros, -12))
# Salida: 23.5
