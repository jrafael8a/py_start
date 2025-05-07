import flet as ft

from src.app_my_restaurant.database.mesas_service import *
from src.app_my_restaurant.components.mesas import *

class VistaAdmonMesas:
    def __init__ (self, page: ft.Page):
        self.page = page
        exito, self.mesas = obtener_mesas_desde_db()
        
    def on_click_mesa(self, mesa_id):
        print(f"Click en mesa {mesa_id}")
        for mesa in self.mesas:
            if mesa["id"] == mesa_id:
                self.mesa_seleccionada = mesa
                break
        else:
            self.mesa_seleccionada = None
        

    def componente_editar_mesa(self, mesa_seleccionada=None):

        if not mesa_seleccionada:
            return ft.Container()  # No muestra nada si no hay mesa seleccionada

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

            if not nombre_input.strip():
                mensaje = f"Por favor, ingrese un nombre de Mesa válido."
            elif not capacidad_input.strip():
                mensaje = f"Por favor, asigne una capacidad a la Mesa"
            elif not capacidad_input.isdigit() or int(capacidad_input) <= 0:
                mensaje = f"Por favor, asigne una capacidad válida a la Mesa"
            else:
                exito, mensaje = actualizar_mesa_db(mesa_seleccionada["id"], nombre_input.value, capacidad_input.value, estado_input.value)
            
            if exito:
                self.page.open(ft.SnackBar(
                    content=ft.Text(mensaje),
                    action="OK",
                ))
                nombre_input.value = ""
                capacidad_input.value = ""
                estado_input.value = 0
                nombre_input.focus()

        def eliminar_mesa_click(e):
            exito, mensaje = eliminar_mesa_db(mesa_seleccionada["id"])
            
            if exito:
                self.page.open(ft.SnackBar(
                    content=ft.Text(mensaje),
                    action="OK",
                ))
                nombre_input.value = ""
                capacidad_input.value = ""
                estado_input.value = 0
                nombre_input.focus()
            # Podrías también limpiar la mesa seleccionada y refrescar el grid

        return ft.Column([
            ft.Text("Editar mesa", size=20, weight=ft.FontWeight.BOLD),
            nombre_input,
            capacidad_input,
            estado_input,
            ft.Row([
                ft.ElevatedButton("Actualizar", icon=ft.icons.SAVE, on_click=actualizar_mesa),
                ft.ElevatedButton("Eliminar", icon=ft.icons.DELETE, on_click=eliminar_mesa_click, bgcolor=ft.colors.RED_500),
            ])
        ], spacing=10)

    def componente_agregar_mesa(self):
        #self.grid_container = crear_grid_mesas(self.on_clic_mesa)

        nombre_input = ft.TextField(label="Nombre de la mesa", autofocus=True, on_submit=lambda e: self.capacidad_input.focus())
        capacidad_input = ft.TextField(label="Capacidad Máxima", input_filter=ft.NumbersOnlyInputFilter(), on_submit=lambda e: self.boton_agregar.focus())
        boton_agregar = ft.ElevatedButton(
            text="Agregar mesa",
            icon=ft.icons.ADD,
            on_click=lambda e: on_agregar_mesa(self, nombre_input.value, capacidad_input.value)  # Llama a la función de agregar mesa
        )

        def on_agregar_mesa(e, self, nombre_mesa, capacidad_mesa):
            mensaje = ""
            exito = False

            if not nombre_mesa.strip():
                mensaje = f"Por favor, ingrese un nombre de Mesa válido."
            elif not capacidad_mesa.strip():
                mensaje = f"Por favor, asigne una capacidad a la Mesa"
            elif not capacidad_mesa.isdigit() or int(capacidad_mesa) <= 0:
                mensaje = f"Por favor, asigne una capacidad válida a la Mesa"
            else:
                exito, mensaje = agregar_mesa_db(nombre_mesa, capacidad_mesa)
                
            if exito:
                self.page.open(ft.SnackBar(
                    content=ft.Text(mensaje),
                    action="OK",
                ))
                nombre_input.value = ""
                capacidad_input.value = ""
                nombre_input.focus()
                #self.grid_container = crear_grid_mesas()
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
                    boton_agregar,
                ]
            ),
        
    def crear_vista(self):
        return ft.Column([
            ft.Row([
                self.componente_agregar_mesa(),
                self.componente_editar_mesa()
            ]),
            ft.Divider(),
            crear_grid_mesas(self.on_click_mesa),
        ])

