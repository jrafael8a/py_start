# La funcion range() es una funcion incorporada en Python que se utiliza para generar 
# una secuencia de numeros enteros.
# La funcion range() es muy util para crear bucles for, ya que permite iterar
# sobre una secuencia de numeros enteros de manera eficiente.

# La funcion range() genera una secuencia de numeros enteros,
# que puede ser utilizada en bucles for o convertida a una lista.
# La sintaxis de range() es:
#   range(start, stop[, step])
# donde:
#   start: el valor inicial de la secuencia (opcional, por defecto es 0).
#   stop: el valor final de la secuencia (no incluido).
#   step: el incremento entre cada valor de la secuencia (opcional, por defecto es 1).
# si solo se le provee 1 parametro, se considera como el valor de stop y el valor de start es 0.
# si se le proveen 2 parametros, el primero es el valor de start y el segundo es el valor de stop.
# si se le proveen 3 parametros, el primero es el valor de start, el segundo es el valor de stop y el tercero es el valor de step.

# El valor inicial se incluye en la secuencia, pero el valor final no se incluye.
# Por ejemplo, si usamos range(5, 10), la secuencia generada será [5, 6, 7, 8, 9].

print("Ejemplo 1: UN SOlO PARAMETRO   range(10)")
rng1 = range(10)
print(rng1)             # Salida: range(0, 10)
print(list(rng1))       # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Notese que el numero 10 no se incluye en la secuencia.

# print(rng) no imprime la lista, sino un objeto range.
# Para ver la lista, debemos convertirlo a una lista con list(rng).

print("")
print("Ejemplo 2: DOS PARAMETROS   range(5, 10)")
rng2 = range(5, 10)     # start=5, stop=10
print(rng2)             # Salida: range(5, 10)
print(list(rng2))       # Salida: [5, 6, 7, 8, 9]
# Notese que el numero inicial, el 5, se incluye en la secuencia, pero el 10 no se incluye.

print("")
print("Ejemplo 3: TRES PARAMETROS   range(2, 20, 4)")
rng3 = range(2, 20, 4)  # start=2, stop=20, step=4
print(rng3)             # Salida: range(2, 20, 4)
print(list(rng3))       # Salida: [2, 6, 10, 14, 18]
# El incremento es de 4, por lo que la secuencia es [2, 6, 10, 14, 18].
# Notese que el 20 no se incluye en la secuencia.

print("")
print("Ejemplo 4: STEP NEGATIVO   range(10, 0, -2)")
# El valor de step puede ser negativo, lo que significa que la secuencia será decreciente.
rng4 = range(20, 10, -2) # start=20, stop=10, step=-2
# La secuencia es decreciente, por lo que el valor de step es negativo.
print(rng4)             # Salida: range(20, 10, -2)
print(list(rng4))       # Salida: [20, 18, 16, 14, 12]
# Notese que el 10 no se incluye en la secuencia.

print("")
print("Ejemplo 5: STEP NEGATIVO   range(10, -10, -2)")
rng5 = range(10, -10, -2) # start=10, stop=-10, step=-2
print(rng5)             # Salida: range(10, -10, -2)
print(list(rng5))       # Salida: [10, 8, 6, 4, 2, 0, -2, -4, -6, -8]
# Notese que el -10 se incluye en la secuencia.