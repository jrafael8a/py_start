import flet as ft

from src.app_restaurante.restaurante import Restaurante
from src.app_restaurante.mesa import Mesa
from src.app_restaurante.cliente import Cliente

class RestauranteGUI:
    def __init__(self):
        self.restaurante = Restaurante()
        capacidades = [2,2,4,4,6,6]
        for i in range(0, 6):
            self.restaurante.agregar_mesa(Mesa(i+1, capacidades[i]))
    
    def main(self, page: ft.Page):
        page.title = "Restaurante"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        page.padding = 20
        page.theme_mode = "dark"

        self.tabs = ft.Tabs(
            selected_index = 0,
            animation_duration= 300,
            tabs = [
                ft.Tab(
                    text = "Mesera",
                    icon = ft.icons.PERSON,
                    content= 
                        ft.Column([
                            self.crear_vista_mesera()
                        ])
                ),
                ft.Tab(
                    text = "Cocina",
                    icon = ft.icons.RESTAURANT,
                    #content= ft.Column(

                    #    )
                ),
                ft.Tab(
                    text = "Caja",
                    icon = ft.icons.POINT_OF_SALE,
                    #content= ft.Column(

                    #    )
                ),
                ft.Tab(
                    text = "Administracion",
                    icon = ft.icons.ADMIN_PANEL_SETTINGS,
                    #content= ft.Column(

                    #    )
                ),

            ],
            expand=True,
        )
        page.add(self.tabs)

    # Metodos para crear las vistas de cada pestaña del ft.Tabs
    def crear_vista_mesera(self):
        self.grid_container = ft.Container(
            width=700,
            expand=True,
            content=self.crear_grid_mesas(),
        )
        
        return ft.Row(
            expand=True,
            spacing=0,
            controls=[
                ft.Container(
                    expand=True,
                    content=ft.Column(
                        expand=True,
                        controls=[
                            ft.Text("Mesas del Restaurante", size=20, weight=ft.FontWeight.BOLD),
                            self.grid_container,
                        ],
                    )
                ),
                ft.VerticalDivider(),
                ft.Container(
                    width=400,
                    expand=True,
                    content=ft.Column(
                        expand=True,
                        controls=[
                            self.crear_panel_gestion(),
                        ],
                    )
                ),
            ],
            
        )
    
    # Metodos Internos de vista
    def crear_grid_mesas(self):
        grid = ft.GridView(
            expand=True,
            runs_count=2,
            max_extent=200,             # Tamaño maximo permitido para cada elemento de la GridView
            child_aspect_ratio=1.0,     # Proporcion o Relacion de aspecto. En este caso 1:1
            spacing=10,                 # Espacio entre los elementos de la GridView
            run_spacing=10,             # Espacio entre las filas de la GridView
            padding=10,
        )

        for mesa in self.restaurante.mesas:
            color = ft.colors.GREEN_700 if not mesa.ocupada else ft.Colors.RED_700
            estado = "LIBRE" if not mesa.ocupada else "OCUPADA"

            grid.controls.append(
                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=5,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Icon(ft.Icons.TABLE_RESTAURANT, color =ft.colors.AMBER_400),
                                    ft.Text(f"Mesa {mesa.numero}", size=16, weight=ft.FontWeight.BOLD),
                                ]
                            ),
                            ft.Text(f"Capacidad: {mesa.numero}", size=14, weight=ft.FontWeight.BOLD),
                            ft.Text(estado, size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ]
                    ),
                    bgcolor=color,
                    border_radius=10,
                    padding=15,
                    ink=True,
                    on_click=lambda e, num=mesa.numero: self.seleccionar_mesa(e, num),
                )
            )

        return grid
    
    def seleccionar_mesa(self, e, numero_mesa):
        self.mesa_seleccionada = self.restaurante.buscar_mesa(numero_mesa)
        mesa = self.mesa_seleccionada

        self.mesa_info.value = f"Mesa {mesa.numero} - Capacidad: {mesa.tamaño}"
        self.btn_asignar.disabled = mesa.ocupada

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

        def asignar_cliente(self, e):
            if not self.mesa_seleccionada:
                return
            try:
                tamaño_grupo = int(self.tamaño_grupo_input.value)
                if tamaño_grupo <= 0:
                    return
                
                cliente = Cliente(tamaño_grupo)
                resultado = self.restaurante.asignar_cliente_a_mesa(cliente, self.mesa_seleccionada.numero)

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
                    self.tipo_item_dropdown,
                    self.items_dropdown,
                ]
            )
        )

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

def main():
    app = RestauranteGUI()
    ft.app(target=app.main)
    # ft.app(target=app.main, view=ft.WEB_BROWSER, assets_dir="assets")

if __name__ == "__main__":
    main()