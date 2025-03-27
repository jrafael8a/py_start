# Este es un juego de "Adivina el numero"
import random   # Primero debemos importar el modulo random para usas sus funciones

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilidades import clear_screen     # Aqui estoy importando una funcion desde un archivo propio
clear_screen()                          # Y aqui la mando a llamar


# print("Hola. Cual es tu nombre?")
# name = input()  # Aqui capturamos la entrada del usuario
name = "invitado"

secret_number = random.randint(1, 20)   # Un numero entero aleatorio entre 1 y 20
print("Bueno, " + name + " Estoy pensando un numero entre 1 y 20")

# Pregunta al usuario para adivinar en 6 intentos
for intentosTomados in range (1, 7):
    print("Intenta adivinar:")
    intento = int(input())
    print("")

    if intento < secret_number:
        print("Muy bajo.")
    elif intento > secret_number:
        print("Muy alto.")
    else:
        print("Eso es!")
        break    # Solo entrara aqui si adivino

if intento == secret_number:
    print("Buen Trabajo " + name + "! Adivinaste mi numero en " + str(intentosTomados) + " intentos")
else:
    print("")
    print("Perdiste!. El numero que estaba pensando era " + str(secret_number))

