# "Dunder" es un término coloquial que viene de Double UNDERscore (doble guion bajo). 
# Se refiere a las variables y métodos especiales en Python que están rodeados 
# por dos guiones bajos (__). Como por ejemplo:
# __name__
# __init__
# __str__
# __call__
# __dict__

# Estas variables y métodos no son elegidos arbitrariamente; forman parte del diseño 
# interno de Python y suelen tener un significado especial en el comportamiento del lenguaje.

# Algunos Casos de Uso:

# if __name__ == "__main__"

# sirve para asegurarse de que cierto código solo se ejecute cuando el archivo 
# es ejecutado directamente, y no cuando es importado como módulo.

print("Ejemplo del uso de if __name__ == '__main__'")

def saludar():
    print("Hola desde dunder_1.py")

if __name__ == "__main__":
    print("Este script se ejecutó directamente")
    saludar()

