# `reduce()` aplica una función acumulativa sobre los elementos de un iterable, 
# reduciendo el iterable a un solo valor.
# Funciona tomando dos elementos a la vez y aplicando la función de manera acumulativa.

from functools import reduce

# Ejemplo 1: Sumar todos los números de una lista.
numeros = [1, 2, 3, 4, 5]
resultado = reduce(lambda x, y: x + y, numeros)
print(resultado)  # Salida: 15 (1+2+3+4+5)

# Ejemplo 2: Multiplicar todos los números de una lista.
resultado = reduce(lambda x, y: x * y, numeros)
print(resultado)  # Salida: 120 (1*2*3*4*5)
