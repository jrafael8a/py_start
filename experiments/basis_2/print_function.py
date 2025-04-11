# Explicacion un poco mas avanzada de la funcion print()
# Sabemoso que el uso normalmente es 
# print("Una cadena de texto aqui")
# print("Y que tambien " + "se pueden concatenar " + str(1) + " o mas cadenas")

# print("Pero tambien", "se puede concatenar", "separando por comas")
# Y de esa forma se pueden concatenar varios tipos de datos

print("Ejemplo 1:")
age = 23
name = "Tim"

print("My name is", name, "and I am", age, "years old")
# Salida:
# My name is Tim and I am 23 years old
# La función print() convierte automáticamente los argumentos en cadenas,
# por lo que no es necesario convertirlos manualmente.
# Tambien agrega un espacio entre cada argumento.
# A menos que se especifique lo contrario con el parametro sep.

print("")
print("Ejemplo 2: Uso del parametro sep=")
# Si queremos cambiar el separador entre los argumentos, podemos usar el parámetro sep.
# Por defecto, sep es un espacio en blanco (" ") pero podemos cambiarlo
# Por ejemplo, si queremos usar una coma como separador:
print("My name is", name, "and I am", age, "years old", sep=",")
# Salida:
# My name is,Tim,and I am,23,years old

# Tambien podemos usar un | como separador:
print("My name is", name, "and I am", age, "years old", sep="|")
# Salida:
# My name is|Tim|and I am|23|years old

# Es muy util para depurar el código, ya que podemos ver los valores de las variables

print("")
print("Ejemplo 3: Uso del parametro end=")
# Si queremos cambiar el final de la cadena, podemos usar el parámetro end.
# Por defecto, end es un salto de línea ("\n") pero podemos cambiarlo
# Es decir, si escribimos un print() y luego otro print(), cada print() 
# se imprime en una nueva línea. # Si queremos que el segundo print() 
# se imprima en la misma línea que el primero, podemos usar end="" en el primero 
# para evitar el salto de línea.
# Por ejemplo:
print("Esta es una Linea, del primer print.", end="")
print(" Y esta es otra linea, del segundo print.")
print("Si no uso el end, se imprime en una nueva linea")
print("")
print("Por supesto, tambien puedo usar otoss caracteres como separador", end="|||")
print("y este es el siguiente print.")
# Salida:
# My name is Tim and I am 23 years old and I live in Madrid