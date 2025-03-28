# El manejo de excepciones en Python se hace con 
# try, except, else y finally.

try:
    numero = int(input("Ingresa un número: "))
    print(f"El doble de {numero} es {numero * 2}")
except ValueError:
    print("Error: Debes ingresar un número válido.")


# Ahora, veamos algo más avanzado
try:
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    resultado = a / b  # Puede generar un ZeroDivisionError
except ValueError:
    print("Error: Debes ingresar un número válido.")
except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")
else:
    print(f"El resultado de la división es: {resultado}")
finally:
    print("Este mensaje siempre se muestra, haya o no error.")

# 🔹 Explicación:
# except ValueError: Se ejecuta si el usuario no ingresa un número válido.
# except ZeroDivisionError: Se ejecuta si intenta dividir entre cero.
# else: Se ejecuta si NO hay errores.
# finally: Siempre se ejecuta, ocurra o no una excepción.