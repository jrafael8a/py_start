# Los atributos de clase son variables que pertenecen a la propia clase, 
# no a las instancias de la clase

# Atributo de clase: 
# i es una variable compartida por todas las instancias de la clase State. 
# Si creas varias instancias de State, todas compartirán el mismo valor de i.

# Acceso: 
# Puedes acceder a i a través de la clase misma o de una instancia de la clase. 
# Si lo accedes a través de una instancia, no es necesario usar el prefijo State.i, 
# pero lo modificas de la misma manera.

# Ejemplo 1:
# Creamos nuestra clase llamada MiClaseEstado
class MiClaseEstado:
    i = 0               # Atributo de clase

estado1 = MiClaseEstado()
estado2 = MiClaseEstado()

print(estado1.i)  # Imprime 0

estado1.i += 1    # Modifica el atributo de clase a 1

print(estado2.i)  # Imprime 1 (estado2 también tiene el mismo valor de i porque es un atributo de clase)
print(estado1.i)  # Imprime 1 (cambio reflejado en todas las instancias)

# En este caso, todas las instancias de State comparten la misma variable i. 
# Si estado1.i se cambia, ese cambio afecta también a estado2.i 
# porque ambas están referenciando la misma variable de clase.