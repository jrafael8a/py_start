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

