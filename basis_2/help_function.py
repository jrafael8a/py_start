# la funcion help() es una funcion incorporada en Python que se utiliza para mostrar 
# la documentacion de un objeto, incluyendo modulos, clases, funciones y metodos.
# La documentacion es el codigo que se coloca dentro de un docstring, 
# es decir, con triples comillas dobles o simples, justo despues de la definicion de la funcion.

print("Ejemplo de docstring")
# El docstring debe estar en la primera línea de la función
def test_function(a, b):
    """
    Este es un ejemplo de documentacion de una funcion.
    a: valor 1      # Es el primer argumento de la funcion.
    b: valor 2      # Es el segundo argumento de la funcion.

    return: int     # Devuelve un numero entero que es la suma de a y b.

    Este texto tambien aparecera al colocar el mouse sobre la funcion en el IDE.
    """
    return a + b

print(test_function(5, 8))
# Salida:
# 13

help(test_function)
# La función help() mostrará el docstring de la función test_function

