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
#   'b': Modo binario (se utiliza junto con otros modos como 'rb' o 'wb' para trabajar con archivos binarios).
#   'x': Crear (crea un archivo, pero si ya existe, lanza un error).
#   't': Modo texto (modo por defecto, aunque explícitamente no se suele usar).

print("\nEjemplo 1: open()")

# Abre el archivo en modo lectura
archivo = open("comandos_git.txt", "r")

# Lee el contenido completo
contenido = archivo.read()

print(contenido)

# No olvides cerrar el archivo cuando termines
archivo.close()
