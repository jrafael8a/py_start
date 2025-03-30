print("")
print("Ejercicio lambda:")
print("Crea una función lambda que devuelva True si un número es múltiplo de 3 y False en caso contrario.")

multriplo = lambda x: not bool(x % 3)
# multriplo = lambda x: x % 3 == 0      # suggerencia mejorada 


try:
    num = int(input("Escriba un numero:"))
except ValueError:
    print("Por favor ingrese un numero Entero valido")
else:
    print(multriplo(num))

print("")
