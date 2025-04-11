print("\nEjercicio 1: Validación con raise")
# Crea una función llamada verificar_contraseña(contraseña) que reciba una cadena y:
# Lance un ValueError si la contraseña tiene menos de 8 caracteres.
# Lance un TypeError si la contraseña no es una cadena de texto.
# Si la contraseña es válida, retorne "Contraseña válida".

def verificar_contra(contra):
    if len(contra) < 8:
        raise ValueError("La contraseña debe tener mas de 8 caracteres")
    elif str(type(contra)) != "<class 'str'>":
        raise TypeError("La contaseña debe ser una cadena de texto")
    else:
        print("Contraseña valida")

mi_contra = input("Digite una contraseña: ")
verificar_contra(mi_contra)


print("\nEjercicio 2: Uso de assert en una función matemática")
# Crea una función llamada raiz_cuadrada(n) que:
# Use assert para verificar que n sea un número positivo.
# Retorne la raíz cuadrada de n si la condición es verdadera.

import math
def raiz_cuadrada(n):
    assert n >= 0 , "Ingrese un numero entero positivo"
    return math.sqrt(n)

mi_raiz = float(input("Escriba un numero: "))
print(raiz_cuadrada(mi_raiz))


print("\nEjercicio 3: Mezclando raise y assert")
# Crea una función dividir(a, b) que:
# Use assert para verificar que a y b sean números.
# Use raise para lanzar un ZeroDivisionError si b es 0.
# Si todo es correcto, retorne la división a / b.

def dividir(a,b):
    try:
        a = float(a) 
        b = float(b)
    except:
        return "Por favor ingrese solo numeros"
    else:
        if b == 0: raise ZeroDivisionError("No se puede dividor por cero")
        return a / b
    
a = input("Ingrese un numero: ")
b = input("Ingrese otro numero: ")

print(dividir(a,b))