# Ejercicios corregidos

def verificar_contra(contra):
    if not isinstance(contra, str):  # Verifica si es un string antes de cualquier operación
        raise TypeError("La contraseña debe ser una cadena de texto")
    if len(contra) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres")
    print("Contraseña válida")

mi_contra = input("Digite una contraseña: ")
verificar_contra(mi_contra)





import math

def raiz_cuadrada(n):
    try:
        assert n >= 0, "Ingrese un número entero positivo"
        return math.sqrt(n)
    except AssertionError as e:
        return f"Error: {e}"

mi_raiz = float(input("Escriba un número: "))
print(raiz_cuadrada(mi_raiz))





def dividir(a, b):
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "Ambos valores deben ser números"
    
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    
    return a / b

a = input("Ingrese un número: ")
b = input("Ingrese otro número: ")

try:
    a, b = float(a), float(b)
    print(dividir(a, b))
except ValueError:
    print("Por favor, ingrese solo números.")
except ZeroDivisionError as e:
    print(f"Error: {e}")
