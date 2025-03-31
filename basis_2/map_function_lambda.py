# La funcion map() aplica una función a cada elemento de un iterable (como una lista) 
# y devuelve un nuevo iterable con los resultados.
# Se suele combinar con lambda para crear funciones anónimas y aplicar transformaciones rápidas.

strings = ["my", "world", "apple", "electroencefalografia", "pear",]

longitudes = map(len, strings)
# La función len() devuelve la longitud de cada palabra en la lista strings.
# la funcion map() devuelve un objeto map, que es un iterable.
# Para convertirlo a una lista, se puede usar list()
print(list(longitudes))  # Salida: [2, 5, 5, 4, 6]

print("")
print("Ejemplo 2: map() con lambda")

# La función lambda permite crear funciones anónimas de una sola línea.

plurales = map(lambda x: x + "S", strings)
# La función lambda toma cada palabra y le agrega una "S" al final.
print(list(plurales))  
# Salida: ['myS', 'worldS', 'appleS', 'electroencefalografiaS', 'pearS']
# Notese que la función lambda se define en una sola línea y no tiene nombre.

print("")
print("Ejemplo 3: map() con filter()")
def longer_than_10(word):
    """ La función longer_than_5 toma una palabra y devuelve True si su longitud es mayor a 5. """
    return len(word) > 10

filtrado = filter(longer_than_10, strings)
# La función filter() toma una función y un iterable y devuelve un nuevo iterable con los elementos 
# que cumplen la condición. En este caso, las palabras que tienen mas de 10 letras.
print(list(filtrado))
# Salida: ['electroencefalografia']

print("")
print("Ejemplo 4: map() con filter()")
# Ahora filtremos las palabras que tienen menos de 4 letras
def shorter_than_5(word):
    """ La función shorter_than_5 toma una palabra y devuelve True si su longitud es menor a 5. """
    return len(word) < 5

filtra2 = filter(shorter_than_5, strings)
print(list(filtra2))
# Salida: ['my', 'pear']
# Notese que no se incluyen las palabras que tienen 5 letras, ya que el parametro
# de la funcion filter() es menor a 5. No menor o igual a 5.
# Por eso solo tenemos las palabras de 4 letras o menos.

print("")
print("Ejemplo 5: map() con filter() y lambda")
# Ahora hagamos lo mismo pero con lambda
filtra3 = filter(lambda x: len(x) < 5, strings)
print(list(filtra3))
# Salida: ['my', 'pear']
# La función lambda toma cada palabra y devuelve True si su longitud es menor a 5.