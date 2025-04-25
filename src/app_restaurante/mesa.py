class Mesa:
    def __init__(self, numero, tamaño):
        self.numero = numero
        self.tamaño = tamaño
        self.ocupada = False
        self.cliente = None
        self.pedido = None