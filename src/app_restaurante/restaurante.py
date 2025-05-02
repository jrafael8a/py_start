from src.app_restaurante.menu import Menu
from src.app_restaurante.mesa import Mesa
from src.app_restaurante.pedido import Pedido

class Restaurante:
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
    
    def asignar_cliente_a_mesa(self, cliente, numero_mesa):
        mesa = self.buscar_mesa(numero_mesa)
        if not mesa:
            return f"Mesa {numero_mesa} no encontrada."
        elif mesa.ocupada:
            return f"Mesa {numero_mesa} no disponible."
        elif cliente.tamaño_grupo > mesa.capacidad:
            return f"Grupo demasiado grande para la mesa {numero_mesa}. (Capacidad Macima: {mesa.capacidad})"
        elif mesa.asignar_cliente(cliente):
            self.clientes.append(cliente)
            return f"Cliente {cliente} asignado a la mesa {mesa.numero}"
        else:
            return f"No se pudo asignar el cliente a la mesa {mesa.numero}."
        

    def buscar_mesa(self, numero_mesa):
        for mesa in self.mesas:
            if mesa.numero == numero_mesa:
                return mesa
        return None
    
    def crear_pedido(self, numero_mesa):
        # Busca la mesa con el número proporcionado
        mesa = self.buscar_mesa(numero_mesa)
      
        # Verifica si la mesa existe y está ocupada
        if mesa and mesa.ocupada:

            # Crea un nuevo pedido asociado a la mesa
            pedido = Pedido(mesa)
            
            # Agrega el pedido a la lista de pedidos activos del restaurante
            self.pedidos_activos.append(pedido)
            
            # Asigna el pedido actual a la mesa
            mesa.pedido_actual = pedido
            
            # Asigna el pedido al cliente que está en la mesa
            mesa.cliente.asignar_pedido(pedido)
            
            # Devuelve el pedido creado
            return pedido
        
        # Si la mesa no existe o no está ocupada, devuelve None
        return None
    
    def liberar_mesa(self, numero_mesa):
        mesa = self.buscar_mesa(numero_mesa)
        if mesa:
            cliente = mesa.cliente
            if cliente:
                cliente.limpiar_pedido()
                if cliente in self.clientes:
                    self.clientes.remove(cliente)
                if mesa.pedido_actual in self.pedidos_activos:
                    self.pedidos_activos.remove(mesa.pedido_actual)
            mesa.liberar()
            return f"Mesa {mesa.numero} liberada exitosamente."
        return f"Mesa {numero_mesa} no encontrada."

    def obtener_item_menu(self, tipo, nombre):
        return self.menu.obtener_item(tipo, nombre)