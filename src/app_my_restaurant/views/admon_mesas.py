import flet as ft

from src.app_my_restaurant.database.mesas_service import *
from src.app_my_restaurant.components.mesas import *

class VistaAdmonMesas:
    def __init__ (self, page: ft.Page):
        self.page = page
        self.mesa_seleccionada = None
        # self.mesas = []
        # self._view = None
        # self.refrescar_mesas()
    
    def obtener_mesas(self):
        exito, self.mesas = obtener_mesas_desde_db()
        #self.page.update()

    def on_click_mesa(self, mesa_id):
        print(f"Click en mesa {mesa_id}")
        for mesa in self.mesas:
            if mesa["id"] == mesa_id:
                self.mesa_seleccionada = mesa
                break
        else:
            self.mesa_seleccionada = None
        self.actualizar_vista()    

    def componente_editar_mesa(self):

        if not self.mesa_seleccionada:
            return ft.Container()  # No muestra nada si no hay mesa seleccionada

        mesa_seleccionada = self.mesa_seleccionada

        nombre_input = ft.TextField(label="Nombre", value=mesa_seleccionada["nombre"])
        capacidad_input = ft.TextField(label="Capacidad", value=str(mesa_seleccionada["capacidad"]), input_filter=ft.NumbersOnlyInputFilter())
        estado_input = ft.Dropdown(
            label="Estado",
            value=str(mesa_seleccionada["estado"]),
            options=[
                ft.dropdown.Option(str(i), text) for i, text in [
                    (0, "Libre"),
                    (1, "Reservada"),
                    (2, "Ocupada"),
                    (3, "Orden Tomada"),
                    (4, "En Preparación"),
                    (5, "Comiendo"),
                    (6, "Esperando Cuenta"),
                    (7, "Pago en Proceso"),
                    (8, "Necesita Limpieza"),
                    (9, "Fuera de Servicio")
                ]
            ]
        )

        def actualizar_mesa(e):
            mensaje = ""
            exito = False

            if not nombre_input.value.strip():
                mensaje = f"Por favor, ingrese un nombre de Mesa válido."
            elif not capacidad_input.value.strip():
                mensaje = f"Por favor, asigne una capacidad a la Mesa"
            elif not capacidad_input.value.isdigit() or int(capacidad_input.value) <= 0:
                mensaje = f"Por favor, asigne una capacidad válida a la Mesa"
            else:
                exito, mensaje = actualizar_mesa_db(mesa_seleccionada["id"], nombre_input.value, capacidad_input.value, estado_input.value)
            
            if exito:
                self.page.open(ft.SnackBar(
                    content=ft.Text(mensaje),
                    action="OK",
                ))
                self.mesa_seleccionada = None
                nombre_input.value = ""
                capacidad_input.value = ""
                estado_input.value = 0
                nombre_input.focus()
                self.actualizar_vista()

        def eliminar_mesa_click(e):
            exito, mensaje = eliminar_mesa_db(mesa_seleccionada["id"])
            
            if exito:
                self.page.open(ft.SnackBar(
                    content=ft.Text(mensaje),
                    action="OK",
                ))
                self.mesa_seleccionada = None
                nombre_input.value = ""
                capacidad_input.value = ""
                estado_input.value = 0
                nombre_input.focus()
                self.actualizar_vista()

        return ft.Column([
            ft.Text("Editar mesa", size=20, weight=ft.FontWeight.BOLD),
            nombre_input,
            capacidad_input,
            estado_input,
            ft.Row([
                ft.ElevatedButton("Actualizar", icon=ft.icons.SAVE, on_click=actualizar_mesa),
                ft.ElevatedButton("Eliminar", icon=ft.icons.DELETE, on_click=eliminar_mesa_click, bgcolor=ft.colors.RED_500),
            ])
        ], 
        spacing=10,
        expand=True,
        )

    def componente_agregar_mesa(self):
        #self.grid_container = crear_grid_mesas(self.on_clic_mesa)

        nombre_input = ft.TextField(label="Nombre de la mesa", autofocus=True, on_submit=lambda e: self.capacidad_input.focus())
        capacidad_input = ft.TextField(label="Capacidad Máxima", input_filter=ft.NumbersOnlyInputFilter(), on_submit=lambda e: self.boton_agregar.focus())

        def on_agregar_mesa(e):
            mensaje = ""
            exito = False

            if not nombre_input.strip():
                mensaje = f"Por favor, ingrese un nombre de Mesa válido."
            elif not capacidad_input.strip():
                mensaje = f"Por favor, asigne una capacidad a la Mesa"
            elif not capacidad_input.isdigit() or int(capacidad_input) <= 0:
                mensaje = f"Por favor, asigne una capacidad válida a la Mesa"
            else:
                exito, mensaje = agregar_mesa_db(nombre_input, capacidad_input)
                
            if exito:
                self.page.open(ft.SnackBar(
                    content=ft.Text(mensaje),
                    action="OK",
                ))
                nombre_input.value = ""
                capacidad_input.value = ""
                nombre_input.focus()
                self.actualizar_vista()

            else:
                dlg_alerta = ft.AlertDialog(
                    title=ft.Text("Error"),
                    content=ft.Text(mensaje),
                    actions=[
                        ft.TextButton("OK", on_click=lambda e: self.page.close(dlg_alerta))
                    ],
                )
                self.page.open(dlg_alerta)

        return ft.Column(
                [
                    ft.Text("Agregar nueva mesa", size=20, weight=ft.FontWeight.BOLD),
                    nombre_input,
                    capacidad_input,
                    ft.ElevatedButton("Agregar", icon=ft.icons.ADD, on_click=on_agregar_mesa)
                ], 
                spacing=10,
                expand=True,
            )

    def actualizar_vista(self):
        self.obtener_mesas()
        self.container_admon_mesas.controls.clear()
        self.container_admon_mesas.controls.append(
            ft.Row([
                self.componente_agregar_mesa(),
                ft.Column([], expand=True),
                self.componente_editar_mesa(),
            ],
            spacing=20,
            expand=True,
            )
        )
        self.container_admon_mesas.controls.append(ft.Divider())
        self.container_admon_mesas.controls.append(crear_grid_mesas(self.on_click_mesa))
        self.page.update()
    

    def crear_vista(self):
        self.container_admon_mesas = ft.Column([],
        expand= True,
        scroll= True,
        )
        self.actualizar_vista() 
        return self.container_admon_mesas

