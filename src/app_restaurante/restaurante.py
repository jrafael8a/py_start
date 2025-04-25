from src.app_restaurante.menu import Menu
from src.app_restaurante.mesa import Mesa

class Restaurate:
    def __init__ (self):
        self.mesas = []
        self.clientes = []
        self.pedidos_activos = []
        self.menu = Menu()
        self._inicializar_menu()

    def _inicializar_menu(self):
        #Agregar algunas entradas, platos principales, postres y bebidas al menú
        self.menu.agregar_entrada(nombre="Ensalada Cesar", precio=8.50)
        self.menu.agregar_entrada(nombre="Sopa del dia", precio=6.00)
        
        self.menu.agregar_plato_principal(nombre="Filete Mignon", precio=25.99)
        self.menu.agregar_plato_principal(nombre="Salmon a la parrilla", precio=22.50)
        
        self.menu.agregar_postre(nombre="Tiramisu", precio=6.99)
        self.menu.agregar_postre(nombre="Flan Casero", precio=5.50)
        
        self.menu.agregar_bebida(nombre="Vino Tinto", precio=12.00)
        self.menu.agregar_bebida(nombre="Agua Mineral", precio=2.50)
    
    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)
        return f"Mesa {mesa.numero} agregada exitosamente."