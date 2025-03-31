# Las funciones son pequeños trozos de codigo recurrente.
# Se meten dentro de una funcion para mandarlo a llamar mas facilmente
# en lugar de estarlo escribiendo de nuevo cada vez que se necesita

def mi_suma(a, b):
    return a + b

resultado = mi_suma(3, 4)       # 7
print(resultado)                # 7

# El codigo dentro de una funcion no se ejecuta al principio, solo se lee la definicion
# Se ejecuta hasta que la funcion se manda a llamar.
