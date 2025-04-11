
print("\nEjemplo 5: Modo lectura y agregar 'a+'")
archivo = open("basis_2/open_ejemplo2.txt", "a+")
archivo.write("\nEste otro es un texto agregado en el ejemplo 5")
archivo.seek(0)             # El método seek(0) mueve el cursor al principio del archivo 
print(archivo.read())
archivo.close()


# Para poder leer el contenido del archivo después de haberlo abierto en modo 'a+', 
# necesitas mover el cursor de vuelta al inicio del archivo utilizando el método seek(). 
# El método seek(0) mueve el cursor al principio del archivo, 
# lo que permite que puedas usar read() para leer desde el principio.