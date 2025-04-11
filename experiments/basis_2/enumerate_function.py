# La función enumerate() en Python es una función que permite iterar sobre un iterable 
# (como una lista, tupla o cadena de texto) y obtener tanto el índice de cada elemento 
# como su valor. Es muy útil cuando necesitas tener acceso tanto al índice (la posición) 
# como al valor del elemento durante un bucle.

# Sintaxis:
# enumerate(iterable, start=0)

# Donde:
#       - iterable: El objeto que vas a iterar (como una lista, tupla, cadena, etc.).
#       -start: Es el valor desde el cual quieres que comience el índice (por defecto es 0).

print("\nEjemplo basico 1:")
frutas = ["manzana", "plátano", "cereza"]

print(list(enumerate(frutas)))

for indice, fruta in enumerate(frutas):
    print(indice, fruta)

# Si nos fijamos, el indice comienza en 0, 0 manzana
# Pero podemos cambiar el valor inicial del índice utilizando el argumento start.

print("\nEjemplo basico 2: Cambiando el indice")
for indice, fruta in enumerate(frutas, start=1):
    print(indice, fruta)


# NOTA:
# En el caso de     for indice, fruta in enumerate(frutas):
# estamos utilizando dos variables (indice y fruta) porque enumerate() genera tuplas con dos elementos 
# en cada iteración: el índice y el valor. Entonces, al hacer el for, Python desempaqueta 
# automáticamente esas tuplas en las dos variables que hemos indicado: indice y fruta.


tareas = [
    "Escribir reporte",
    "Asistir a una reunion",
    "Revisar Codigo",
    "Enviar hoja de calculo"
]

print("\nEjemplo 1: Sin enumerate()")

for indice in range(len(tareas)):
    tarea = tareas[indice]
    print(f"{indice +1}. {tarea}")

# Enumerate nos ayuda en casos como el ejemplo anterior
# Ahora hagamoslo de nuevo pero esta vez usando enumerate()

print("\nEjemplo 2: Usando enumerate()")

for indice, tarea in enumerate (tareas):
    print(f"{indice + 1}. {tarea}")

# Y obtentremos el mismo resultado pero con menos codigo