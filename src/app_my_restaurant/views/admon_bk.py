import flet as ft

class VistaAdmon:
    def __init__ (self, page: ft.Page):
        self.page = page
    
    def actualizar_items_menu(self, e):
        tipo_item = self.tipo_item_dropdown.value
        self.items_dropdown.options = []

        if tipo_item == "Entrada":
            items = self.restaurante.menu.entradas
        elif tipo_item == "Plato Principal":
            items = self.restaurante.menu.platos_principales
        elif tipo_item == "Postre":
            items = self.restaurante.menu.postres
        elif tipo_item == "Bebida":
            items = self.restaurante.menu.bebidas
        else:
            items = []

        # Actualizar el Dropdown con los items del menu seleccionados
        self.items_dropdown.options = [
            ft.dropdown.Option(item.nombre) for item in items
            ]
        
        if e and e.page:
            e.page.update()

    def actualizar_items_eliminar(self, e):
        tipo = self.tipo_item_eliminar.value
        self.item_eliminar.options = []

        if tipo == "Entrada":
            items = self.restaurante.menu.entradas
        elif tipo == "Plato Principal":
            items = self.restaurante.menu.platos_principales
        elif tipo == "Postre":
            items = self.restaurante.menu.postres
        elif tipo == "Bebidas":
            items = self.restaurante.menu.bebidas
        else:
            items = []

        self.item_eliminar.options = [
            ft.dropdown.Option(item.nombre) for item in items
        ]

        if e and e.page:
            e.page.update()

    def crear_vista(self):
            # Campos para agregar items
            self.tipo_item_admin = ft.Dropdown(
                label="Tipo de Item",
                options=[
                    ft.dropdown.Option("Entrada"),
                    ft.dropdown.Option("Plato Principal"),
                    ft.dropdown.Option("Postre"),
                    ft.dropdown.Option("Bebida"),
                ], 
                width=200,
            )

            self.nombre_item = ft.TextField(
                label="Nombre del Item",
                width=200,
            )

            self.precio_item = ft.TextField(
                label="Precio del Item",
                width=200,
                input_filter=ft.NumbersOnlyInputFilter(),
            )

            # Campos para eliminar items
            self.tipo_item_eliminar = ft.Dropdown(
                label="Tipo de Item",
                options=[
                    ft.dropdown.Option("Entrada"),
                    ft.dropdown.Option("Plato Principal"),
                    ft.dropdown.Option("Postre"),
                    ft.dropdown.Option("Bebida"),
                ], 
                width=200,
                on_change=self.actualizar_items_eliminar
            )

            self.item_eliminar = ft.Dropdown(
                label="Seleccionar Item a Eliminar",
                width=200,
            )

            def agregar_item(e):
                tipo = self.tipo_item_admin.value
                nombre = self.nombre_item.value

                try:
                    precio = float(self.precio_item.value)
                    if tipo and nombre and precio > 0:
                        if tipo == "Entrada":
                            self.restaurante.menu.agregar_entrada(nombre, precio)
                        elif tipo == "Plato Principal":
                            self.restaurante.menu.agregar_plato_principal(nombre, precio)
                        elif tipo == "Postre":
                            self.restaurante.menu.agregar_postre(nombre, precio)
                        elif tipo == "Bebida":
                            self.restaurante.menu.agregar_bebida(nombre, precio)

                        # Limpiar campos
                        self.nombre_item.value = ""
                        self.precio_item.value = ""

                        #Actializar Dropdowns
                        self.actualizar_items_menu(None)
                        self.actualizar_items_eliminar(None)
                        e.page.update()
                except ValueError:
                    pass

            def eliminar_item(e):
                tipo = self.tipo_item_eliminar.value
                nombre = self.item_eliminar.value

                if tipo and nombre:
                    self.restaurante.menu.eliminar_item(tipo, nombre)
                    
                    # Actualizar Dropdowns
                    self.actualizar_items_menu(None)
                    self.actualizar_items_eliminar(None)
                    e.page.update()

            return ft.Container(
                content=ft.Column([
                    ft.Text("Agregar Item al Menu", size=20, weight=ft.FontWeight.BOLD),
                    self.tipo_item_admin,
                    self.nombre_item,
                    self.precio_item,
                    ft.ElevatedButton(
                        text="Agregar Item",
                        on_click=agregar_item,
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.GREEN_700,
                            color=ft.Colors.WHITE,
                        )
                    ),
                    ft.Divider(),
                    ft.Text("Eliminar Item del Menu", size=20, weight=ft.FontWeight.BOLD),
                    self.tipo_item_eliminar,
                    self.item_eliminar,
                    ft.ElevatedButton(
                        text="Eliminar Item",
                        on_click=eliminar_item,
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.RED_700,
                            color=ft.Colors.WHITE,
                        )
                    ),
                ], spacing=20),
                padding=20,
                bgcolor=ft.Colors.BLUE_GREY_900,
            )

if __name__ == "__main__":
    def main(page: ft.Page):
          page.add(VistaAdmon.crear_vista())
    
    ft.app(target=main)