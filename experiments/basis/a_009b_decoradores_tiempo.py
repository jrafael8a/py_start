import time  # Importamos el módulo time para medir el tiempo

# Decorador para medir el tiempo de ejecución de una función
def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Marca el tiempo de inicio
        resultado = func(*args, **kwargs)  # Llama a la función original
        end_time = time.time()  # Marca el tiempo de finalización
        print(f"Tiempo de ejecución de {func.__name__}: {end_time - start_time:.6f} segundos")
        return resultado  # Retorna el resultado de la función
    return wrapper

# Función que verifica si un número es primo (con tu código de ejemplo)
@medir_tiempo  # Aplicamos el decorador para medir el tiempo de ejecución
def verificar_primos(numeros):
    for x in numeros:
        if x == 1:  # El 1 no es primo
            continue
        
        es_primo = True
        for y in range(2, int(math.sqrt(x)) + 1):  # Solo hasta la raíz cuadrada de x
            if x % y == 0:  # Si es divisible por y, no es primo
                es_primo = False
                break

        if es_primo: 
            print(x, end=", ")

# Ejecutamos la función y medimos el tiempo
import math
numeros = range(1, 200)
verificar_primos(numeros)
