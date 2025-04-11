#  Los atributos de instancia son específicos para cada objeto (instancia) que creas 
# a partir de la clase. Esto significa que cada instancia tendrá su propia copia de i, 
# y los cambios realizados en una instancia no afectarán a otras.

# self.i: 
# Este es un atributo de instancia, lo que significa que se asocia 
# con una instancia específica de la clase, no con la clase en general. 
# Cada vez que creas una nueva instancia de State, se crea un nuevo self.i para esa instancia.

class MiClaseEstado:
    def __init__(self):
        self.i = 0          # Atributo de instancia

    def increment(self):
        self.i += 1
        return self.i

# Crear dos instancias diferentes de State
estado1 = MiClaseEstado()
estado2 = MiClaseEstado()

print(estado1.i)        # Imprime 0
estado1.increment()     # Incrementa el atributo de estado1
print(estado1.i)        # Imprime 1

print(estado2.i)        # Imprime 0 (estado2 tiene su propio atributo `i` independiente de estado1)
