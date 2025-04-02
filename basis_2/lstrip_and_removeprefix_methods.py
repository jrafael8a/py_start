# El metodo lstrip() elimina los espacios en blanco de la izquierda de una cadena
# y devuelve una nueva cadena sin los espacios en blanco iniciales.
# Si se le pasa un argumento, elimina los caracteres especificados de la izquierda.
# Sintaxis:
#       str.lstrip([chars])
# Donde:
#     - chars: (opcional) una cadena de caracteres que se desea eliminar de la izquierda.
#     Si no se especifica, se eliminan los espacios en blanco.

print("Ejemplo 1: lstrip sin parámetros")
cadena = "   Hola Mundo"
print(cadena)  # "   Hola Mundo"
resultado = cadena.lstrip()
print(resultado)  # "Hola Mundo"

print("Ejemplo 2: lstrip con parámetros, eliminando caracteres específicos")
cadena2 = "xxxyyyHola Mundo"
resultado2 = cadena2.lstrip('xy')
print(resultado2)  # "Hola Mundo", elimina 'x' y 'y' al principio


# Se debe tener cuidado al usar lstrip() con caracteres específicos, ya que eliminará 
# todos los caracteres que coincidan con los especificados en el argumento.

print("")
print("Ejemplo 3: lstrip con parámetros, (sale mal)")
mis_links = [
    "www.b001.io",
    "www.youtube.com",
    "www.google.com",
    "www.wikipedia.org",
    "www.facebook.com",
    "www.twitter.com"
    "instagram.com",
    "linkedin.com",
    "whatsapp.com",
    "wechat.com",
    "wwchat.com"
]

for link in mis_links:
    # Elimina 'www.' al principio de cada link
    resultado3 = link.lstrip('www.')
    resultado4 = link.lstrip('w.')
    print(resultado3)
    print("") 
    print(resultado4) 
    # Salida:
    #   "ikipedia.org",     # FAIL 
    #   "echat.com",        # FAIL
    #   "hatsapp.com",       # FAIL

# Notese que ambos "www." y "w." eliminan no solo "www." sino tambien la 
# 'w' "ikipedia.org" de "hatsapp.com" y "echat.com".
# Pero no elimina la w de twitter.com porque no es el primer caracter
# para haer esto de forma correcta se puede usar el metodo removeprefix() 
# de la libreria urllib.parse

# Ya que Este método elimina un prefijo específico de la cadena, si existe. 
# Si no tiene el prefijo, devuelve la cadena original sin cambios.

# Sintaxis:
#       str.removeprefix(prefix)
# Donde:
#     - prefix: el prefijo que deseas eliminar de la cadena.
#     Si la cadena no comienza con este prefijo, se devuelve la cadena original sin cambios.

print("")
print("Ejemplo 5: Usando removeprefix() para eliminar 'www.'")
mis_links = [
    "www.b001.io",
    "www.youtube.com",
    "www.google.com",
    "www.wikipedia.org",
    "www.facebook.com",
    "www.twitter.com"
    "instagram.com",
    "linkedin.com",
    "whatsapp.com",
    "wechat.com",
    "wwchat.com"
]

for link in mis_links:
    resultado5 = link.removeprefix('www.')
    print(resultado5)  
    # Salida:
    #   "wikipedia.org",    # OK
    #   "wechat.com",       # OK
    #   "whatsapp.com",     # OK
    #   "wwchat.com"        # OK
