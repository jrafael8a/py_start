import flet as ft

from src.app_my_restaurant.database import *

class RestauranteGUI:
    
    def __init__(self, page):
        self.page = page
        
        # self.restaurante = Restaurante()
        # capacidades = [2,2,4,4,6,6]
        # for i in range(0, 6):
        #     self.restaurante.agregar_mesa(Mesa(i+1, capacidades[i]))
    
    def main(self, page):
        self.page = page
        
        self.page.title = "Restaurante"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.page.padding = 20
        self.page.theme_mode = "dark"

        self.tabs = ft.Tabs(
            selected_index = 0,
            animation_duration= 300,
            tabs = [
                ft.Tab(
                    text = "Mesera",
                    icon = ft.Icons.PERSON,
                    content= 
                        ft.Column([
                            self.crear_vista_mesera()
                        ])
                ),
                ft.Tab(
                    text = "Cocina",
                    icon = ft.Icons.RESTAURANT,
                    content = self.crear_vista_cocina()
                ),
                ft.Tab(
                    text = "Caja",
                    icon = ft.Icons.POINT_OF_SALE,
                    content= self.crear_vista_caja()
                ),
                ft.Tab(
                    text = "Administracion",
                    icon = ft.Icons.ADMIN_PANEL_SETTINGS,
                    content= self.crear_vista_admin()
                ),

            ],
            expand=True,
        )
        self.page.add(self.tabs)
    
    
    def actualizar_ui(self, page):
        nuevo_grid = self.crear_grid_mesas()
        self.grid_container.content = nuevo_grid

        if self.mesa_seleccionada:
            if self.mesa_seleccionada.ocupada and self.mesa_seleccionada.pedido_actual:
                self.resumen_pedido.value = self.mesa_seleccionada.pedido_actual.obtener_resumen()
            else:
                self.resumen_pedido.value = ""
            
            self.btn_asignar.disabled = self.mesa_seleccionada.ocupada
            self.btn_agregar_item.disabled = not self.mesa_seleccionada.ocupada
            self.btn_liberar.disabled = not self.mesa_seleccionada.ocupada

        self.actualizar_vista_cocina()
        self.actualizar_vista_caja()
        
        page.update()
    
    def seleccionar_mesa(self, e, numero_mesa):
        self.mesa_seleccionada = self.restaurante.buscar_mesa(numero_mesa)
        mesa = self.mesa_seleccionada

        self.mesa_info.value = f"Mesa {mesa.numero} - Capacidad: {mesa.capacidad}"
        self.btn_asignar.disabled = mesa.ocupada
        self.btn_agregar_item.disabled = not mesa.ocupada
        self.btn_liberar.disabled = not mesa.ocupada

        if mesa.ocupada and mesa.pedido_actual:
            self.resumen_pedido.value = mesa.pedido_actual.obtener_resumen()
        else:
            self.resumen_pedido.value = ""

        e.page.update()

        if mesa.ocupada and mesa.pedido_actual:
            return None

    def crear_panel_gestion(self):
        self.mesa_seleccionada = None
        self.mesa_info = ft.Text("", size=16, weight=ft.FontWeight.BOLD)
        self.tamaño_grupo_input = ft.TextField(
            label="Tamaño del grupo",
            input_filter=ft.NumbersOnlyInputFilter(),
            prefix_icon=ft.Icons.PEOPLE,
        )

        self.tipo_item_dropdown = ft.Dropdown(
            label="Tipo de Item",
            width=200,
            options=[
                ft.dropdown.Option("Entrada"),
                ft.dropdown.Option("Plato Principal"),
                ft.dropdown.Option("Postre"),
                ft.dropdown.Option("Bebida"),
            ],
            on_change=self.actualizar_items_menu
        )

        self.items_dropdown = ft.Dropdown(
            label="Seleccionar Item",
            width=200,
            options=[

            ]
        )

        self.btn_asignar = ft.ElevatedButton(
            text="Asignar Cliente",
            disabled=True,
            on_click=self.asignar_cliente,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.GREEN_700,
                color=ft.Colors.WHITE,
            )
        )

        self.btn_agregar_item = ft.ElevatedButton(
            text = "Agregar Item",
            on_click = self.agregar_item_pedido,
            disabled=True,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.BLUE_700,
                color=ft.Colors.WHITE,
            )
        )

        self.btn_liberar = ft.ElevatedButton(
            text="Liberar Mesa",
            on_click=self.liberar_mesa,
            disabled=True,
            style=ft.ButtonStyle(
                bgcolor = ft.Colors.RED_700,
                color = ft.Colors.WHITE,
            )
        )

        self.resumen_pedido = ft.Text("", size=14)
        

        return ft.Container(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        padding=10,
                        border_radius=10,
                        bgcolor=ft.Colors.BLUE_GREY_900,
                        content=self.mesa_info,
                    ),
                    ft.Container(height=20),
                    self.tamaño_grupo_input,
                    self.btn_asignar,
                    ft.Divider(),
                    self.tipo_item_dropdown,
                    self.items_dropdown,
                    self.btn_agregar_item,
                    ft.Divider(),
                    self.btn_liberar,
                    ft.Divider(),
                    ft.Text("Resumen del Pedido", size=16, weight=ft.FontWeight.BOLD),
                    ft.Container(
                        content=self.resumen_pedido,
                        bgcolor=ft.Colors.BLUE_GREY_900,
                        padding=10,
                        border_radius=10,
                    ),
                ],
                spacing=10,
                expand=True,
            ),
            padding=20,
            expand=True,
        )

    def asignar_cliente(self, e):
            if not self.mesa_seleccionada:
                return
            try:
                tamaño_grupo = int(self.tamaño_grupo_input.value)
                if tamaño_grupo <= 0:
                    return
                
                cliente = Cliente(tamaño_grupo)
                resultado = self.restaurante.asignar_cliente_a_mesa(cliente, self.mesa_seleccionada.numero)

                if "asignado" in resultado:
                    self.restaurante.crear_pedido(self.mesa_seleccionada.numero)
                    self.tamaño_grupo_input.value = ""
                    self.actualizar_ui(e.page)
                
            except ValueError:
                pass
    
    
    
    
    def agregar_item_pedido(self, e):
        if not self.mesa_seleccionada or not self.mesa_seleccionada.pedido_actual:
            return
        
        tipo = self.tipo_item_dropdown.value
        nombre_item = self.items_dropdown.value

        if tipo and nombre_item:
            item = self.restaurante.obtener_item_menu(tipo, nombre_item)
            if item:
                self.mesa_seleccionada.pedido_actual.agregar_item(item)
                self.actualizar_ui(e.page)


    def liberar_mesa(self, e):
        if self.mesa_seleccionada:
            self.restaurante.liberar_mesa(self.mesa_seleccionada.numero)
            self.actualizar_ui(e.page)
            

def main():
    app = RestauranteGUI()
    ft.app(target=app.main)
    # ft.app(target=app.main, view=ft.WEB_BROWSER, assets_dir="assets")

if __name__ == "__main__":
    main()