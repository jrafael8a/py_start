# Las funciones lambda son funciones anónimas (sin nombre) y de una sola línea. 
# Se usan cuando necesitas una función pequeña sin definirla con def.

# Sintaxis:
# lambda argumentos: expresión

print("Ejemplo de función lambda")
doble = lambda x: x * 2
print(doble(5))  # Salida: 10

print("lo cual es equivalente a:")
def doble(x):
    return x * 2
print(doble(5))  # Salida: 10

print("")
print("Ejemplo de función lambda con múltiples argumentos (Suma)")
suma = lambda a, b: a + b
print(suma(3, 7))  # Salida: 10

print("Aplicar una funcion que eleve al cuadrado a cada elemento de una lista")
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]

"""
La funcion map() aplica una funcion a cada item de un terable (una lista o una tupla) y devuelve un objeto map.
Esta funcion permite transformar los elementos de una lista o tupla de manera eficiente
sin necesidad de usar un bucle explicito.

La sintaxis de la funcion map() es la siguiente:
map(funcion, iterable)
Donde:
- funcion: es la funcion que se aplicara a cada elemento del iterable.
- iterable: es la lista o tupla a la que se aplicara la funcion.

Al devolver un objeto map, es necesario convertirlo a una lista o tupla para ver los resultados.
o podemos usar un bucle for para iterar sobre el objeto map.

usamos la funcion list() si queremos almacenar todos los resultados en memoria.
usamos un bucle for si queremos hacer una evaluacion perezosa (lazy evaluation) y no queremos almacenar todos los resultados en memoria.
La evaluacion perezosa (lazy evaluation) es una tecnica de programacion donde los valores no se calculan hasta que son necesarios.
Esto permite ahorrar memoria y tiempo de procesamiento, ya que no se calculan valores innecesarios.
"""