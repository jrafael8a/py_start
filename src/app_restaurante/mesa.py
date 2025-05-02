class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupada = False
        self.cliente = None
        self.pedido = None
    
    def asignar_cliente(self, cliente):
        if cliente.tamaño_grupo <= self.capacidad:
            self.cliente = cliente
            self.ocupada = True
            return True
        return False
    
    def liberar(self):
        self.cliente = None
        self.ocupada = False
        self.pedido_actual = None

    def tiene_pedido_activo(self):
        return self.pedido_actual is not None