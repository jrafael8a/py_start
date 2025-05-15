import flet as ft

from src.app_my_restaurant.database.menu_categorias_service import obtener_categorias_menu_db
from src.app_my_restaurant.components.alerts import MyAlerts

class MiniComponentes:
    def __init__(self, gui):
        self.gui = gui

    def dropdown_categorias_menu(self, on_change_handler=None):
        dd_categoria = ft.Dropdown(
            label="Categorias", 
            options=[], 
            enable_filter=True, 
            editable=True, 
            expand=True, 
            on_change=on_change_handler
        )

        exito, categorias = obtener_categorias_menu_db()
        if not exito:
            self.gui.alerts.Dialogo_Error(categorias)
            return
        
        # Este es un ejemplo de comprension de Listas (list comprehension). Sintaxis:
        # lista = [EXPRESION for ITEM in ITERABLE if CONDICION]
        # Yo decidi mejor solo usar una sola comprenhesion list en lugar de crear una y luego recorrerla:
        dd_categoria.options = [                                    # [     El corchete abre la comprenhesion list
            ft.dropdown.Option(key=cat["id"], text=cat["nombre"])   # Esto es la EXPRESION
            for cat in categorias                                   # Aqui tenemos el for ITEM in ITERABLE
            if cat["estado"] == 1                                   # Y yo agregue la condicion aqui directamente, para no usar una lista intermedia
        ]                                                           # ]     El corchite cierra la comprenhesion list

        return dd_categoria
        
    # Este es un ejemplo de comprension de Listas (list comprehension). Sintaxis:
        # lista = [EXPRESION for ITEM in ITERABLE if CONDICION]
        # habilitados = [t for t in tipos if t["estado"] == 1]    

        # Es equivalente a escribir el siguente cidigo mas tradicional (sin comprensión de listas):
        # habilitados = []                    # Creamos una variable
        # for t in tipos:                     # Recorremos la lista tipos, para cada elemento "t"
        #     if t["estado"] == 1:            # Si el estado de "t" es == a 1
        #         habilitados.append(t)       # Agregamos "t" a la variable "habilitados"

        
        # Esta es otra compresion de listas que usa la lista anterio
        # self.dd_tipo.options = [                                # [     El corchete abre la comprenhesion list
        #     ft.dropdown.Option(key=t["id"], text=t["nombre"])   # Esto es la EXPRESION
        #     for t in habilitados                                # Aqui tenemos el for ITEM in ITERABLE
        # ]                                                       # ]     El corchite cierra la comprenhesion list


if __name__ == "__main__":
    def main(page: ft.Page):
        alerts = MyAlerts(page)
