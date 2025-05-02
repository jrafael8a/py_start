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
                    content = self.crear_vista_cocina()
                ),
                ft.Tab(
                    text = "Caja",
                    icon = ft.icons.POINT_OF_SALE,
                    content= self.crear_vista_caja()
                ),
                ft.Tab(
                    text = "Administracion",
                    icon = ft.icons.ADMIN_PANEL_SETTINGS,
                    content= self.crear_vista_admin()
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
    
    def crear_vista_cocina(self):
        self.lista_pedidos_cocina = ft.ListView(
            expand=True,
            spacing=10,
            padding=20,
            auto_scroll=True,
        )

        def cambiar_estado_pedido(e, pedido, nuevo_estado):
            pedido.cambiar_estado(nuevo_estado)
            self.actualizar_vista_cocina()
            self.actualizar_ui(e.page)
            e.page.update()

        def crear_item_pedido(pedido):
            return ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(f"Mesa {pedido.mesa.numero}", size=20, weight=ft.FontWeight.BOLD),
                        ft.Text(pedido.obtener_resumen()),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    text="En Preparacion",
                                    on_click=lambda e, p=pedido: cambiar_estado_pedido(e, p, "En Preparacion"),
                                    disabled=pedido.estado != "Pendiente",
                                    style=ft.ButtonStyle(
                                        bgcolor=ft.Colors.ORANGE_700,
                                        color=ft.Colors.WHITE,
                                    )
                                ),
                                ft.ElevatedButton(
                                    text="Listo",
                                    on_click=lambda e, p=pedido: cambiar_estado_pedido(e, p, "Listo"),
                                    disabled=pedido.estado != "En Preparacion",
                                    style=ft.ButtonStyle(
                                        bgcolor=ft.Colors.BLUE_700, 
                                        color=ft.Colors.WHITE,
                                    )
                                ),
                                ft.Text(f"Estado: {pedido.estado}", color=ft.Colors.BLUE_200),
                            ]
                        )
                    ],
                    spacing=5,
                ),
                padding=10,
                border_radius=10,
            )
        
        def actualizar_vista_cocina():
            self.lista_pedidos_cocina.controls.clear()
            for pedido in self.restaurante.pedidos_activos:
                if pedido.estado in ["Pendiente", "En Preparacion"]:
                    self.lista_pedidos_cocina.controls.append(crear_item_pedido(pedido))
        
        self.actualizar_vista_cocina = actualizar_vista_cocina

        return ft.Container(
            expand=True,
            content=ft.Column([
                ft.Text("Pedidos Pendientes", size=24, weight=ft.FontWeight.BOLD),
                self.lista_pedidos_cocina,
            ])
        )

    def crear_vista_caja(self):
        self.lista_caja = ft.ListView(
            expand=True,
            spacing=10,
            padding=20,
            auto_scroll=True,
        )

        def procesar_pago(e, mesa):
            if mesa.pedido_actual:
                self.restaurante.liberar_mesa(mesa.numero)
                self.actualizar_ui(e.page)

        def crear_item_cuenta(mesa):
            if not mesa.pedido_actual:
                return None
            
            return ft.Container(
                content=ft.Column([
                    ft.Text(f"Mesa {mesa.numero}", size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Cliente: {mesa.cliente.id}"),
                    ft.Text(mesa.pedido_actual.obtener_resumen()),
                    ft.ElevatedButton(
                        text="Procesar Pago",
                        on_click=lambda e, m=mesa: procesar_pago(e, m),
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.GREEN_700,
                            color=ft.Colors.WHITE,
                        )
                    )
                ]),
                bgcolor=ft.Colors.BLUE_GREY_900,
                padding=10,
                border_radius=10,
            )
        
        def actualizar_vista_caja():
            self.lista_caja.controls.clear()
            for mesa in self.restaurante.mesas:
                if mesa.ocupada and mesa.pedido_actual:
                    item = crear_item_cuenta(mesa)
                    if item:
                        self.lista_caja.controls.append(item)
        
        self.actualizar_vista_caja = actualizar_vista_caja

        return ft.Container(
            expand=True,
            content=ft.Column([
                ft.Text("Cuentas Activas", size=24, weight=ft.FontWeight.BOLD),
                self.lista_caja,
            ])
        )


    def crear_vista_admin(self):
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

    # Metodos Internos de vista
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
                            ft.Text(f"Capacidad: {mesa.capacidad} personas", size=14, weight=ft.FontWeight.BOLD),
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