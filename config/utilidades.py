import os
import time  # Importamos el módulo time para medir el tiempo

def clear_screen():
    if os.name == 'posix':  # Para Linux o macOS
        os.system('clear')
    elif os.name == 'nt':   # Para Windows
        os.system('cls')


# Decorador para medir el tiempo de ejecución de una función
def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Marca el tiempo de inicio
        resultado = func(*args, **kwargs)  # Llama a la función original
        end_time = time.time()  # Marca el tiempo de finalización
        print(f"Tiempo de ejecución de {func.__name__}: {end_time - start_time:.6f} segundos")
        return resultado  # Retorna el resultado de la función
    return wrapper