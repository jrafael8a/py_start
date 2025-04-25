from src.app_restaurante.menu import ItemMenu

class Pedido:
    def __init__(self, mesa):
        self.mesa = mesa
        self.item = {
            "entradas": [],
            "platos_principales": [],
            "postres": [],
            "bebidas": [],
        }
        self.estado = "Pendiente"

    def agregar_item(self, item):
        if isinstance(item, ItemMenu):
            if item.tipo == "Entrada":
                self.items["entradas"].append(item)
            elif item.tipo == "Plato Principal":
                self.items["platos_principales"].append(item)
            elif item.tipo == "Postre":
                self.items["postres"].append(item)
            elif item.tipo == "Bebida":
                self.items["bebidas"].append(item)
            
    def calcular_total(self):
        total = 0
        for categoria in self.item.values():
            for item in categoria:
                total += item.calcular_precio()
            return round(total, 2)
        return False
    
    def cambiar_estado(self, nuevo_estado):
        estados_validos = ["Pendiente", "En Preparacion", "Listo", "Entregado"]
        if nuevo_estado in estados_validos:
            self.estado = nuevo_estado
            return True
        return False
    
    def obtener_resumen(self):
        resumen = []
        for categoria, items in self.item.items():
            if items:
                resumen.append(f"\n{categoria.replace('_', ' ').title()}:")
                for item in items:
                    resumen.append(f"- {item.nombre} x {item.cantidad}: ${item.calcular_subtotal():.2f}")
        
        resumen.append(f"\nTotal: ${self.calcular_total():.2f}")
        return "\n".join(resumen)