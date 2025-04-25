# ItemMenu es la clase base para los diferentes tipos de items del menu
class ItemMenu:
    def __init__(self, nombre, precio, cantidad=1):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.precio * self.cantidad
        
    
class Entrada(ItemMenu):
    def __init__(self, nombre, precio, cantidad=1):
        super().__init__(nombre, precio, cantidad)          # Esta linea llama al constructor de la clase base ItemMenu 
        self.tipo = "Entrada"                               # Es decir, hereda los atribuutos de ItemMenu, como nombre, precio y cantidad, 
                                                            # y luego le agregamos el atributo tipo

"""
# Ejemplo de como quedaria la clase Entrada sin usar el constructor de la clase base ItemMenu

class Entrada(ItemMenu):
    def __init__(self, nombre, precio, cantidad=1):
        self.nombre = nombre                                # Estas con las 3 lineas que nos ahorramos
        self.precio = precio                                # porque llamamos al constructor de la clase base ItemMenu          
        self.cantidad = cantidad                            # asi no tenemos que repetir el mismo codigo para cada tipo de item
        self.tipo = "Entrada"



🔍 ¿Y qué pasa cuando creas un objeto?

    entrada1 = Entrada("Bruschetta", 4.50, 2)
    print(entrada1.nombre)                              # "Bruschetta"
    print(entrada1.precio)                              # 4.50
    print(entrada1.cantidad)                            # 2
    print(entrada1.tipo)                                # "Entrada"
    print(entrada1.calcular_subtotal())                 # 9.0

✔️ Esto funciona porque super().__init__() se encargó de inicializar los atributos que vienen de ItemMenu, 
y luego self.tipo = "Entrada" añadió lo específico de la subclase.


"""

class PlatoPrincipal(ItemMenu):
    def __init__(self, nombre, precio, cantidad=1):
        super().__init__(nombre, precio, cantidad)
        self.tipo = "Plato Principal"

class Postre(ItemMenu):
    def __init__(self, nombre, precio, cantidad=1):
        super().__init__(nombre, precio, cantidad)
        self.tipo = "Postre"

class Bebida(ItemMenu):
    def __init__(self, nombre, precio, cantidad=1):
        super().__init__(nombre, precio, cantidad)
        self.tipo = "Bebida"

class Menu:
    def __init__(self):
        self.entradas = []
        self.platos_principales = []
        self.postres = []
        self.bebidas = []

    def agregar_entrada(self, nombre, precio):
        entrada = Entrada(nombre, precio)
        self.entradas.append(entrada)
        return entrada
    
    def agregar_plato_principal(self, nombre, precio):
        plato = PlatoPrincipal(nombre, precio)
        self.platos_principales.append(plato)
        return plato
    
    def agregar_postre(self, nombre, precio):
        postre = Postre(nombre, precio)
        self.entradas.append(postre)
        return postre
    
    def agregar_bebida(self, nombre, precio):
        bebida = Bebida(nombre, precio)
        self.entradas.append(bebida)
        return bebida
    
    def eliminar_item(self, tipo, nombre):
        if tipo == "Entrada":
            items = self.entradas
        elif tipo == "Plato Principal":
            items = self.platos_principales
        elif tipo == "Postre":
            items =  self.postres
        elif tipo == "Bebida":
            items = self.bebidas
        else:
            return False
        
        for item in items:
            if item.nombre == nombre:
                items.remove(item)
                return True
        return False
    
    def eliminar_entrada(self, nombre):
        return self.eliminar_item("Entrada", nombre)
    
    def eliminar_plato_principal(self, nombre):
        return self.eliminar_item("Plato Principal", nombre)
    
    def eliminar_postre(self, nombre):
        return self.eliminar_item("Postre", nombre)
    
    def eliminar_bebida(self, nombre):
        return self.eliminar_item("Bebida", nombre)
    
    def obtener_item(self, tipo, nombre):
        if tipo == "Entrada":
            items = self.entradas
        elif tipo == "Plato Principal":
            items = self.platos_principales
        elif tipo == "Postre":
            items =  self.postres
        elif tipo == "Bebida":
            items = self.bebidas
        else:
            return None
        
        for item in items:
            if item.nombre == nombre:
                return item
        return None