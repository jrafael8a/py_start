"""
*args: Arguments
Permite pasar una cantidad variable de argumentos no clave (posicionales) a una función.

**kwargs: Keyword Arguments
Permite pasar una cantidad variable de argumentos clave (con nombre) a una función.
"""

# *args recoge todos los valores pasados a la función como una tupla.
def sumar(*args):
    return sum(args)

print(sumar(1, 2, 3))  # Salida: 6
print(sumar(10, 20))    # Salida: 30


# **kwargs recoge todos los argumentos como un diccionario.
def presentar_persona(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

presentar_persona(nombre="Juan", edad=30, ciudad="Madrid")


# Combinación de ambos: *args y **kwargs
# Primero se pasan los argumentos posicionales con *args y luego los argumentos con nombre con **kwargs.

def mostrar_datos(*args, **kwargs):
    print("Argumentos posicionales:", args, type(args))
    print("Argumentos clave:", kwargs, type(kwargs))

mostrar_datos(1, 2, 3, nombre="Juan", edad=25)
