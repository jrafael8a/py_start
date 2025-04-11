# `reversed()` devuelve un iterable que recorre los elementos de un iterable en orden inverso.
# A diferencia de `sorted()`, no cambia el orden de los elementos, simplemente los recorre en reversa.

# Ejemplo 1: Invertir una lista de números.
numeros = [1, 2, 3, 4]
resultado = reversed(numeros)
print(list(resultado))  # Salida: [4, 3, 2, 1]

# Ejemplo 2: Invertir una cadena de texto.
texto = "Hola"
resultado = reversed(texto)
print(''.join(resultado))  # Salida: "aloH"
