# a función open() en Python se utiliza para abrir archivos para leer, escribir o manipular 
# datos dentro de esos archivos. 

# Sintaxis:
# open(nombre_del_archivo, modo, buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# Donde:
# nombre_del_archivo: Especifica el nombre del archivo que quieres abrir, o la ruta completa si no está en el mismo directorio.
# modo: Especifica el modo en el que deseas abrir el archivo. Algunos de los modos más comunes son:
#   'r': Leer (modo por defecto). El archivo debe existir.
#   'w': Escribir (sobrescribe el archivo si ya existe, o crea uno nuevo si no existe).
#   'a': Agregar (añade contenido al final del archivo sin sobrescribirlo).
#   'b': Modo binario (por ejemplo, imágenes o audio) 
#         (se utiliza junto con otros modos como 'rb' o 'wb').
#   'x': Crear (crea un archivo, pero si ya existe, lanza un error).
#   't': Modo texto (modo por defecto, aunque explícitamente no se suele usar).

print("\nEjemplo 1: Abrir un archivo en modo LECTURA")

# Abre el archivo en modo lectura 'r' (Debe llevar la ruta desde la raiz)
archivo = open("basis_2/open_ejemplo.txt", "r")     
contenido = archivo.read()      # Lee el contenido completo                  
print(contenido)                # Imprime en consola el contenido
archivo.close()                 # Cierra el archivo 
# es importante cerrar el archivo para liberar recursos.



print("\nEjemplo 2: Escribir en un archivo. Modo ESCRITURA")
# Abre el archivo en modo escritura (esto sobrescribe el archivo si ya existe)
archivo = open("basis_2/open_ejemplo.txt", "w")
# Escribe algo en el archivo
archivo.write("\nEste es un nuevo contenido en el archivo.")
# print(archivo.read()) # No podemos leer el archivo ya que fue abierto en modo escritura
archivo.close()         # Cierra el archivo después de escribir



print("\nEjemplo 3: Agregar texto sin sobreescribir. MODO APPEND")
# Abre el archivo en modo agregar 'a' (append):
archivo = open("basis_2/open_ejemplo.txt", "a")
# Agrega texto al final del archivo
archivo.write("\nEste es un texto adicional. Sin sobre escribir el archivo original")
archivo.write("\nPodria ser una nota o algo asi.")
# print(archivo.read()) # No podemos leer el archivo ya que fue abierto en modo agregar
archivo.close()             # Cierra el archivo


print("\nEjemplo 4: Modo lectura y escritura 'r+'")
archivo = open("basis_2/open_ejemplo.txt", "r+")
archivo.write("Este es un texto agregado en el ejemplo 4")
print(archivo.read())
archivo.close()


print("\nEjemplo 5: Modo lectura y agregar 'a+'")
archivo = open("basis_2/open_ejemplo.txt", "a+")
archivo.write("Este otro es un texto agregado en el ejemplo 5")
print(archivo.read())
archivo.close()


# USANDO WITH
# Cuando abres archivos con open(), es muy recomendable usar la declaración with. 
# Esto asegura que el archivo se cierre automáticamente una vez que hayas 
# terminado de trabajar con él, incluso si ocurre un error.

print("\nEjemplo 6: Usamos 'with' para abrir el archivo en modo lectura")
with open("basis_2/open_ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
    print("No es necesario llamar a archivo.close(), "
    "ya que 'with' lo hace automáticamente")
