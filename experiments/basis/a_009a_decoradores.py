# Los decoradores en Python son funciones que modifican 
# el comportamiento de otras funciones o métodos sin cambiar su código fuente.
# Se usan comúnmente para añadir funcionalidad antes o 
# después de la ejecución de una función.

# Un decorador en Python es simplemente una función 
# que recibe otra función como argumento, le añade funcionalidad y 
# devuelve la función modificada.

# Ejemplo Basico
print("Ejemplo Basico")

def decorador(func):
    def nueva_funcion():
        print("Antes de ejecutar la función")
        func()
        print("Después de ejecutar la función")
    return nueva_funcion

@decorador
def saludo():
    print("¡Hola, mundo!")

saludo()

# Salida:
# Antes de ejecutar la función
# ¡Hola, mundo!
# Después de ejecutar la función



print("")
print("")
print("Ejemplo 1: Decorador para medir el tiempo de ejecución de una función")
# Este decorador es útil cuando queremos saber cuánto tarda una función en ejecutarse.
# Ideal para medir el rendimiento de funciones en programas grandes.

import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()  # Guarda el tiempo de inicio
        resultado = func(*args, **kwargs)  # Ejecuta la función original
        fin = time.time()  # Guarda el tiempo de finalización
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def tarea_pesada():
    time.sleep(2)  # Simula una tarea que tarda 2 segundos
    print("Tarea completada")

tarea_pesada()

# Salida esperada:
# Tarea completada
# Tiempo de ejecución: 2.0001 segundos




print("")
print("")
print("Ejemplo 2: Decorador para verificar permisos")
# Este decorador es útil cuando queremos restringir 
# el acceso a ciertas funciones según el usuario.

def requiere_permiso(func):
    def wrapper(usuario, *args, **kwargs):
        if usuario != "admin":
            print("Acceso denegado: No tienes permisos")
            return
        return func(usuario, *args, **kwargs)
    return wrapper

@requiere_permiso
def borrar_archivo(usuario, archivo):
    print(f"{usuario} ha borrado el archivo {archivo}")

borrar_archivo("invitado", "datos.txt")  # No tiene permiso
borrar_archivo("admin", "datos.txt")  # Sí tiene permiso

# Salida:
# Acceso denegado: No tienes permisos
# admin ha borrado el archivo datos.txt




print("")
print("")
print("Ejemplo 3: Decorador para registrar llamadas a funciones")
# Este decorador es útil cuando queremos hacer seguimiento 
# de qué funciones se están ejecutando y con qué argumentos.

def registrar_llamada(func):
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__} con argumentos {args} y {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@registrar_llamada
def suma(a, b):
    return a + b

resultado = suma(3, 5)
print(f"Resultado: {resultado}")

# Salida:
# Llamando a suma con argumentos (3, 5) y {}
# Resultado: 8



# POR QUE NECESITAMOS UN WRAPPER?

# El símbolo @decorador no solo define la función, 
# sino que también llama al decorador en ese mismo momento.

# Veámoslo con un ejemplo más claro

def decorador(func):
    print("¡Ejecutando el decorador!")  # Esto se ejecuta inmediatamente
    return func  # Devolvemos la función original sin modificarla

@decorador
def suma(a, b):
    return a + b

print("Después de definir suma")
print(suma(3, 4))

# Salida:
# ¡Ejecutando el decorador!
# Después de definir suma
# 7

# En este caso, el decorador se ejecuta antes de que llamemos a la función suma.
# Esto puede ser útil para inicializar algo o
# configurar el entorno antes de que la función sea llamada.

# Sin embargo, si solo devolvemos la función sin un wrapper, no podremos modificar su comportamiento.
# En resumen, el wrapper es esencial para poder modificar 
# el comportamiento de la función original.


print("")
print("")
print("Decoradores con argumentos")
# A veces, es posible que queramos pasar argumentos a un decorador.
# Esto se hace creando una función que devuelve un decorador.
# Veamos un ejemplo:
def decorador_con_argumentos(arg):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"Argumento del decorador: {arg}")
            return func(*args, **kwargs)
        return wrapper
    return decorador

@decorador_con_argumentos("Hola")
def suma(a, b):
    return a + b

resultado = suma(3, 4)
print(f"Resultado: {resultado}")
# Salida:
# Argumento del decorador: Hola
# Resultado: 7

# En este caso, el decorador_con_argumentos recibe un argumento
# y devuelve un decorador que a su vez modifica la función original.


print("")
print("")
print("Decoradores en clases")
# Los decoradores también se pueden usar en métodos de clases.
# Veamos un ejemplo de cómo usar un decorador en un método de clase.
class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre

    @decorador
    def saludar(self):
        print(f"Hola, {self.nombre}")
mi_objeto = MiClase("Juan")
mi_objeto.saludar()
# Salida:
# ¡Ejecutando el decorador!
# Hola, Juan

# En este caso, el decorador se aplica al método saludar de la clase MiClase.


print("")
print("")
print("Decoradores de clase")
# También podemos usar decoradores para modificar el comportamiento de clases enteras.
# Por ejemplo, podemos crear un decorador que registre la creación de instancias de una clase.
def registrar_clase(cls):
    class NuevaClase(cls):
        def __init__(self, *args, **kwargs):
            print(f"Creando instancia de {cls.__name__}")
            super().__init__(*args, **kwargs)
    return NuevaClase
@registrar_clase
class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print(f"Hola, {self.nombre}")
mi_objeto = MiClase("Juan")
# Salida:
# Creando instancia de MiClase
# Hola, Juan

# En este caso, el decorador registrar_clase modifica la clase MiClase
# para registrar la creación de instancias.


print("")
print("")
print("Decoradores de métodos de clase")
# También podemos usar decoradores en métodos de clase.
# Por ejemplo, podemos crear un decorador que convierta
# un método de instancia en un método de clase.
def metodo_de_clase(func):
    def wrapper(cls, *args, **kwargs):
        return func(cls, *args, **kwargs)
    return classmethod(wrapper)
class MiClase:
    @metodo_de_clase
    def metodo_clase(cls, arg):
        print(f"Soy un método de clase. Argumento: {arg}")
# Llamamos al método de clase
MiClase.metodo_clase("Hola")
# Salida:
# Soy un método de clase. Argumento: Hola

# En este caso, el decorador metodo_de_clase convierte
# el método metodo_clase en un método de clase.


print("")
print("")
print("Decoradores de propiedades")
# También podemos usar decoradores para definir propiedades en clases.
# Las propiedades son atributos que se comportan como métodos.
# Por ejemplo, podemos crear un decorador para definir una propiedad
# que calcule el área de un rectángulo.
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self):
        return self.ancho * self.alto
    @area.setter
    def area(self, valor):
        self.ancho = valor / self.alto
    @area.deleter
    def area(self):
        print("Eliminando área")
        del self.ancho
        del self.alto
# Creamos un rectángulo
rectangulo = Rectangulo(5, 10)
# Imprimimos el área
print(rectangulo.area)  # Salida: 50
# Cambiamos el área
rectangulo.area = 100
# Imprimimos el nuevo ancho
print(rectangulo.ancho)  # Salida: 10.0
# Eliminamos el área
del rectangulo.area
# Imprimimos el ancho
print(rectangulo.ancho)  # Salida: 10.0
# En este caso, el decorador @property define una propiedad
# llamada area que calcula el área del rectángulo.
# También definimos un setter y un deleter para poder
# modificar y eliminar el área.



print("")
print("")
print("Decoradores de clase abstracta")
# También podemos usar decoradores para definir clases abstractas.
# Las clases abstractas son clases que no se pueden instanciar
# y que deben ser heredadas por otras clases.
from abc import ABC, abstractmethod
class MiClaseAbstracta(ABC):
    @abstractmethod
    def metodo_abstracto(self):
        pass
class MiClaseConcreta(MiClaseAbstracta):
    def metodo_abstracto(self):
        print("Implementación del método abstracto")
# Creamos una instancia de la clase concreta
mi_objeto = MiClaseConcreta()
mi_objeto.metodo_abstracto()  # Salida: Implementación del método abstracto
# En este caso, el decorador @abstractmethod define un método
# abstracto que debe ser implementado por las clases concretas.