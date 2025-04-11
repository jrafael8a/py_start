# El docstring en Python es un tipo especial de comentario utilizado para documentar módulos, 
# clases, funciones y métodos. Se escribe entre tres comillas dobles """ o simples ''', 
# y se utiliza para explicar el propósito y comportamiento del código. 
# A diferencia de los comentarios normales (que son ignorados por el interprete), 
# los docstrings son accesibles en tiempo de ejecución y se pueden recuperar mediante 
#la función help() o accediendo a la propiedad __doc__

# Se usa para describir la función, los parámetros que recibe, y lo que devuelve.

#Ejemplo de docstring
# El docstring debe estar en la primera línea de la función

def sumar(a, b):
    """
    Esta función toma dos números como entrada y devuelve su suma.
    
    Parámetros:
    a (int o float): El primer número a sumar.
    b (int o float): El segundo número a sumar.

    Retorna:
    int o float: La suma de los dos números.
    """
    return a + b

# Uso de la función
resultado = sumar(3, 5)
print(resultado)  # Output: 8

# Acceder al docstring
print(sumar.__doc__)
