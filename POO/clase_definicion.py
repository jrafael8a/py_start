# Una Clase → Es como un molde o plantilla. Define propiedades y acciones.
# Objeto    → Es una instancia de la clase. Es un "ejemplar" con sus propios datos.
# Atributos → Datos o características del objeto.
# Métodos   → Acciones o comportamientos del objeto


class Persona:  # Nombre de la clase (Empieza con mayúscula por convención)
#   def __init__(self, ....... )    # Estructura fija
    def __init__(self, nomb, ed):   # Constructor (inicializa atributos)
        self.nombre = nomb          # Al Atributo nombre se le asigna el valor del parametro nomb
        self.edad = ed              # al Atributo edad se le asigna lo recibido en ed

    def presentarse(self):          # Método (acción)
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

#   __init__ es el constructor, un método especial que se ejecuta cuando creamos un objeto.
#   self representa la instancia del objeto, es decir, el propio objeto.



# Crear un objeto (instancia de la clase)
# Una vez que tenemos la clase, podemos crear objetos así:

persona1 = Persona("Juan", 30)  # Creamos un objeto
persona2 = Persona("María", 25)  # Otro objeto

persona1.presentarse()  # Llama al método presentarse()
persona2.presentarse()

print(persona1.edad)
# Aquí persona1 y persona2 son objetos de la clase Persona.
# Cada uno tiene su propio nombre y edad, pero comparten la misma estructura de la clase.