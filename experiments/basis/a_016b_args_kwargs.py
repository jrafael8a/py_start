print("")
print("Ejercicio con *args y **kwargs")
# Crea una función que reciba una lista de números con *args y luego 
# imprima los números y sus cuadrados en forma de diccionario

def cuadrados(*args):
    mis_cuadrados = {}
    for num in args:
        mis_cuadrados[num] = num**2
    return mis_cuadrados

# Forma optimizada de la funcion:
# def cuadrados(*args):
#     return {num: num**2 for num in args}

print(cuadrados(1,2,3,4,7))
print("")

"""
En lugar de crear un diccionario vacío y llenarlo con un for, 
el diccionario por comprensión crea el diccionario en una sola línea.
    return {num: num**2 for num in args}

La sintaxis es 
    {clave: valor for elemento in iterable} 
permite construir un diccionario de manera más compacta.
"""

