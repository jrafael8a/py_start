# En Python los objetos pueden ser mutables o inmutables.
# Un objeto mutable puede ser modificado después de su creación.
# Un objeto inmutable no puede ser modificado después de su creación.

# Algunos ejemplos de objetos mutables son:
# Listas
# Diccionarios
# Conjuntos
# Algunos ejemplos de objetos inmutables son:
# Tuplas
# Cadenas de caracteres
# Números

print("Ejemplo de objeto mutable:")
x = [1, 2]      # Se crea una nueva lista en memoria
y = x           # Se asigna la referencia de la lista a y
x[0] = 100      # Se modifica el primer elemento de la lista en memoria
print(x,y)      # Se imprimen ambas refencias a memoria, pero es la misma lista
# Salida:
# [100, 2] [100, 2]
# Esto es porque x y y apuntan al mismo objeto en memoria

print("si queremos crear una copia de la lista, debemos usar el método copy()")

x = [1, 2]
y = x.copy()    # Se crea una nueva lista en memoria
x[0] = 100      # Se modifica el primer elemento de la lista en memoria
print(x,y)      # Se imprimen ambas refencias a memoria, pero son diferentes listas
# Salida:
# [100, 2] [1, 2]
# Esto es porque x y y apuntan a diferentes objetos en memoria
