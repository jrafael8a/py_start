# La funcion filter() permite filtrar los elementos de un iterable (lista, tupla, etc.)
# en base a una condición dada por una función.
# La función filter() toma una función y un iterable y devuelve un nuevo iterable 
# con los elementos que cumplen la condición. 

strings = ["my", "world", "apple", "electroencefalografia", "pear",]

print("")
print("Ejemplo 1: con filter()")
def longer_than_10(word):
    """ La función longer_than_5 toma una palabra y devuelve True si su longitud es mayor a 5. """
    return len(word) > 10

filtrado = filter(longer_than_10, strings)
print(list(filtrado))
# Salida: ['electroencefalografia']

print("")
print("Ejemplo 2: con filter()")
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
print("Ejemplo 3: con filter() y lambda")
# Ahora hagamos lo mismo pero con lambda
filtra3 = filter(lambda x: len(x) < 5, strings)
print(list(filtra3))
# Salida: ['my', 'pear']
# La función lambda toma cada palabra y devuelve True si su longitud es menor a 5.
