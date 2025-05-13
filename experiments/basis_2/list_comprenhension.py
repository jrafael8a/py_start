"""
La "comprensión de listas" (o list comprehensions en inglés) es una característica muy potente y popular en Python. 
Te permite crear listas de una manera muy concisa y legible, basándote en listas existentes u otros iterables.

Sintaxis General
                            nueva_lista = [EXPRESION for ELEMENTO in ITERABLE if CONDICION]

Desglosemos cada parte:

expresion: 
    Es lo que se evaluará y se añadirá a la nueva_lista por cada elemento. 
    Puede ser el elemento mismo, una operación sobre el elemento (ej. elemento * 2), una llamada a una función con el elemento 
    (ej. elemento.upper()), o incluso otro objeto.

for elemento in iterable: 
    Esta es la parte del bucle. Itera sobre cada elemento en un iterable (como una lista, tupla, cadena, rango, etc.).

if condicion (Opcional): 
    Esta es la parte del filtro. Solo si la condicion se evalúa como verdadera (True) para el elemento actual, 
    la expresion se evaluará y su resultado se añadirá a la nueva_lista. 
    Si omites la parte if, todos los elementos del iterable serán procesados por la expresion.

¿Por qué usarlas?
Concisión y Legibilidad: 
    Una vez que te acostumbras, las comprensiones de listas son a menudo más fáciles de leer y entender que los bucles for equivalentes con append.

Eficiencia: 
    En muchos casos, pueden ser más rápidas que construir una lista manualmente con un bucle for y append(), ya que algunas optimizaciones se realizan internamente en Python.

"Pythónico": 
    Es una forma idiomática de escribir código en Python.
""" 
# Ejemplos
# Veamos algunos ejemplos para ilustrarlo mejor:

# 1. Crear una lista de cuadrados de números del 0 al 9:

# Forma tradicional
cuadrados = []
for x in range(10):
    cuadrados.append(x**2)
print(cuadrados)  # Salida: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Con comprensión de listas
cuadrados_comp = [x**2 for x in range(10)]
print(cuadrados_comp) # Salida: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# expresion: x**2
# elemento: x
# iterable: range(10)








#2. Filtrar números pares de una lista:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Forma tradicional
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
print(pares)  # Salida: [2, 4, 6, 8, 10]

# Con comprensión de listas
pares_comp = [num for num in numeros if num % 2 == 0]
print(pares_comp) # Salida: [2, 4, 6, 8, 10]

"""
expresion: num (queremos el número mismo)
elemento: num
iterable: numeros
condicion: num % 2 == 0
"""





#3. Convertir una lista de cadenas a mayúsculas:
palabras = ["hola", "mundo", "python"]

# Forma tradicional
mayusculas = []
for palabra in palabras:
    mayusculas.append(palabra.upper())
print(mayusculas) # Salida: ['HOLA', 'MUNDO', 'PYTHON']

# Con comprensión de listas
mayusculas_comp = [palabra.upper() for palabra in palabras]
print(mayusculas_comp) # Salida: ['HOLA', 'MUNDO', 'PYTHON']
"""
expresion: palabra.upper()
elemento: palabra
iterable: palabras
"""





#4. Extraer nombres de una lista de diccionarios (similar a tu caso):
#Supongamos que tienes una lista de usuarios, donde cada usuario es un diccionario:
usuarios = [
    {"id": 1, "nombre": "Alice", "activo": True},
    {"id": 2, "nombre": "Bob", "activo": False},
    {"id": 3, "nombre": "Charlie", "activo": True}
]

# Obtener solo los nombres de los usuarios activos
nombres_activos = [usuario["nombre"] for usuario in usuarios if usuario["activo"]]
print(nombres_activos) # Salida: ['Alice', 'Charlie']

"""
expresion: usuario["nombre"]
elemento: usuario
iterable: usuarios
condicion: usuario["activo"] (que es lo mismo que usuario["activo"] == True)
"""






# Volviendo a tu código:
habilitados = [t for t in tipos if t["estado"] == 1]

"""
expresion: 
    t (quieres el diccionario completo t)

elemento: 
    t

iterable: 
    tipos (la lista de diccionarios de tipos de menú)

condicion: 
    t["estado"] == 1 (solo si el estado del tipo de menú es 1)


Como puedes ver, es una herramienta muy versátil. 
También existen comprensiones para conjuntos ({expresion for ...}) y diccionarios ({clave: valor for ...}), que siguen una lógica similar.

¡Espero que esta explicación más detallada te sea útil! 
Es una de esas cosas que, una vez que las dominas, te preguntas cómo vivías sin ellas en Python.
"""