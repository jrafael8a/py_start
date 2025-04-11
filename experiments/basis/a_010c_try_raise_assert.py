# RAISE
# El comando raise se usa para lanzar una excepción manualmente. 
# Esto es útil cuando quieres forzar un error en ciertas condiciones.

# Ejemplo de uso:
# Si estás validando la edad de un usuario y quieres asegurarte de que 
# no ingrese un número negativo, podrías hacer algo así:

print("\nEjemplo de raise")
def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    print("Edad válida:", edad)

# validar_edad(-5)  # Esto generará un error

# ¿Por qué usar raise?
#   Para detectar y detener errores específicos en tu código.
#   Para enviar mensajes de error personalizados cuando algo no cumple con una condición esperada.
#   Para evitar datos incorrectos en un programa antes de que causen problemas más adelante.




# ASSERT
# assert es una forma rápida de verificar si una condición es verdadera mientras estás programando. 
# Si la condición es falsa, lanza automáticamente un AssertionError.

print("\nEjemplo de assert")
def dividir(a, b):
    assert b != 0, "No se puede dividir por cero"
    return a / b

print(dividir(10, 2))  # Funciona bien
print(dividir(10, 0))  # Lanza un AssertionError

# ¿Cuándo usar assert?
#   Para comprobar condiciones que siempre deberían ser verdaderas durante el desarrollo.
#   Para detectar errores más rápido mientras pruebas tu código.
#   Se usa más en fase de desarrollo y generalmente se elimina en producción.


# ✅ Usa raise cuando quieres manejar errores en producción.
# ✅ Usa assert cuando estás desarrollando y necesitas validar supuestos.