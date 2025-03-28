# -----------------------------
# Uso de eval() en Python
# -----------------------------

# La función eval() evalúa una expresión de Python representada como una cadena.
# Puede ser útil para ejecutar código dinámico, pero debe usarse con cuidado debido a los riesgos de seguridad.

print("Ejemplo básico")
x = 10
resultado = eval('x + 5')
print("Resultado de 'x + 5':", resultado)  # Salida esperada: 15

# Explicación:
# En el ejemplo anterior, 'x + 5' se evalúa como una expresión de Python,
# donde la variable 'x' es reemplazada por su valor (10), resultando en 15.

# -----------------------------
print("")
print("Ejemplo usando globals y locals")

global_vars = {'x': 10}
local_vars = {'y': 5}

# En este caso, pasamos diccionarios como espacios de nombres para 'x' y 'y'.
resultado = eval('x + y', global_vars, local_vars)
print("Resultado de 'x + y' usando globals y locals:", resultado)  # Salida esperada: 15

# -----------------------------
print("")
print("Ejercicio 1: Evalúa una expresión con múltiples variables")

# Crea un diccionario con los valores de las variables a utilizar.
# Usa eval() para calcular la expresión 'a * b + c', con a=3, b=7 y c=2.
variables = {'a': 3, 'b': 7, 'c': 2}
expresion = 'a * b + c'

resultado = eval(expresion, {}, variables)
print("Resultado de 'a * b + c' con a=3, b=7, c=2:", resultado)  # Salida esperada: 23


# -----------------------------
# Ejemplo de uso peligroso de eval() (con advertencia)
# -----------------------------

# IMPORTANTE: **NO** usar eval() con datos no confiables.
# El siguiente código puede ser peligroso, ya que ejecuta comandos maliciosos si se le pasa código malicioso.

# eval('__import__("os").system("rm -rf /")')

# ¡Nunca uses eval() con entradas no confiables de usuarios o datos externos!
# Si necesitas evaluar solo literales seguros, utiliza 'ast.literal_eval()' como alternativa.


# -----------------------------
print("")
print("Ejercicio 2: Usar ast.literal_eval() para evaluar literales seguros")

import ast

# Usa ast.literal_eval para evaluar una lista representada como cadena.
cadena_lista = "[1, 2, 3, 4, 5]"
resultado_literal = ast.literal_eval(cadena_lista)
print("Resultado de ast.literal_eval() en lista:", resultado_literal)  # Salida esperada: [1, 2, 3, 4, 5]

# -----------------------------
# Conclusiones:
# -----------------------------
# - eval() es útil para ejecutar código dinámico, pero tiene riesgos de seguridad si se usa con datos no confiables.
# - Para evitar riesgos, se recomienda usar ast.literal_eval() cuando se necesitan evaluar expresiones simples y seguras.
