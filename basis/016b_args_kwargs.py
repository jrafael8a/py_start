print("")
print("Ejercicio con *args y **kwargs")
# Crea una función que reciba una lista de números con *args y luego 
# imprima los números y sus cuadrados en forma de diccionario

def cuadrados(*args, **mis_cuadrados):
    # mis_cuadrados = {}
    for num in args:
        mis_cuadrados[num] = num**2
    return mis_cuadrados

print(cuadrados(1,2,3,4,7))
print("")