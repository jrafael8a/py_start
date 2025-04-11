inventario = [None]
# inventario = []

# INDICACIONES:
# Descomenta alguna de las siguientes lineas (solo una a la vez) para probar el codigo:

# inventario = ["Espada", "Manzana,", "Capa", None, None, None]
# inventario = [None, None, None, None, None, None]
# inventario = [None, "Espada", None, None, None, None]
# inventario = ["Capa", "Espada", "Martillo", "Escududo", "Manzana", "Pocion"]

if all(inventario):
    print("El inventario está lleno")
elif any(inventario):
    print("El inventario tiene algunos elementos")
else:
    print("El inventario está vacío")

# En resumen:
# cuando se evalua None en un contexto booleano, se considera False.
# Cuando se evalua cualquier otro valor, se considera True.

# Si el arreglo inventario[] tiene elemento y ninguno es None, entonces
# se considera que el inventario está lleno.

# Si el arreglo inventario[] tiene solo elementos None, entonces
# se considera que el inventario esta vacio.

# Si el arreglo tiene elementos None y otros elementos, entonces
# se considera que el inventario tiene algunos elementos, pero que no esta lleno

# OJO: Si el inventario esta completamente vacio [] aun asi se evalua como True