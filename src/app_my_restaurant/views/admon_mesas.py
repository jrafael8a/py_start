import flet as ft

from src.app_my_restaurant.database.mesas_service import *
from src.app_my_restaurant.components.mesas import *

class VistaAdmonMesas:
    def __init__ (self, page: ft.Page):
        self.page = page
        self.mesa_seleccionada = None
        self.container_admon_mesas = ft.Column([], expand= True, scroll= True)
        self.tf_nombre_editar = None    # Aqui almacenaremos un TextField que necesitamos hacer focus()
    

    def crear_vista(self):
        exito, self.mesas = obtener_mesas_desde_db()

        if not exito:
            dlg_alerta = ft.AlertDialog(
                    title=ft.Text("Error"),
                    content=ft.Text(self.mesas),
                    actions=[
                        ft.TextButton("OK", on_click=lambda e: self.page.close(dlg_alerta))
                    ],
                )
            self.page.open(dlg_alerta)
            return self.container_admon_mesas
        else:
            self.container_admon_mesas.controls.clear()
            self.container_admon_mesas.controls.append(
                ft.Row([
                    self.componente_agregar_mesa(),
                    ft.Column([], expand=True),         # Aqui funciona como una especie de Vertial Divider
                    self.componente_editar_mesa(),
                ],
                spacing=20,
                expand=True,
                )
            )
            self.container_admon_mesas.controls.append(ft.Divider())
            self.container_admon_mesas.controls.append(crear_grid_mesas(self.on_click_mesa))
            self.page.update()
            return self.container_admon_mesas


    def on_click_mesa(self, mesa_id):
        print(f"Click en mesa {mesa_id}")
        for mesa in self.mesas:
            if mesa["id"] == mesa_id:
                self.mesa_seleccionada = mesa
                break
        else:
            self.mesa_seleccionada = None
        self.crear_vista()
        self.tf_nombre_editar.focus()



    def componente_agregar_mesa(self):
        tf_nombre_agregar = ft.TextField(label="Nombre de la mesa", autofocus=True, on_submit=lambda e: self.capacidad_input.focus())
        tf_capacidad_agregar = ft.TextField(label="Capacidad Máxima", input_filter=ft.NumbersOnlyInputFilter(), on_submit=lambda e: btn_agregar.focus())
        btn_agregar = ft.ElevatedButton("Agregar", icon=ft.icons.ADD, on_click=lambda e: on_agregar_mesa(e))

        def on_agregar_mesa(e):
            mensaje = ""
            exito = False

            if not tf_nombre_agregar.value.strip():
                mensaje = f"Por favor, ingrese un nombre de Mesa válido."
            elif not tf_capacidad_agregar.value.strip():
                mensaje = f"Por favor, asigne una capacidad a la Mesa"
            elif not tf_capacidad_agregar.value.isdigit() or int(tf_capacidad_agregar.value) <= 0:
                mensaje = f"Por favor, asigne una capacidad válida a la Mesa"
            else:
                exito, mensaje = agregar_mesa_db(tf_nombre_agregar.value, tf_capacidad_agregar.value)
                
            if exito:
                self.page.open(ft.SnackBar(
                    content=ft.Text(mensaje),
                    action="OK",
                ))
                tf_nombre_agregar.value = ""
                tf_capacidad_agregar.value = ""
                tf_nombre_agregar.focus()
                self.crear_vista()

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
                    tf_nombre_agregar,
                    tf_capacidad_agregar,
                    btn_agregar,
                ], 
                spacing=10,
                expand=True,
            )



    def componente_editar_mesa(self):
        self.tf_nombre_editar = ft.TextField(label="Nombre", on_submit=lambda e: tf_capacidad_editar.focus())
        tf_capacidad_editar = ft.TextField(label="Capacidad", input_filter=ft.NumbersOnlyInputFilter(), on_submit=lambda e: dd_estado.focus())
        dd_estado = ft.Dropdown(
            label="Estado",
            value=9,
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
        btn_actualizar =    ft.ElevatedButton("Actualizar", icon=ft.icons.SAVE, on_click=lambda e: actualizar_mesa(e))
        btn_eliminar =      ft.ElevatedButton("Eliminar", icon=ft.icons.DELETE, on_click=lambda e: eliminar_mesa_click(e), bgcolor=ft.colors.RED_500)

        if self.mesa_seleccionada:        
            self.tf_nombre_editar.value = self.mesa_seleccionada["nombre"]
            tf_capacidad_editar.value=str(self.mesa_seleccionada["capacidad"])
            dd_estado.value=str(self.mesa_seleccionada["estado"])
        else:
            self.tf_nombre_editar.disabled = True
            tf_capacidad_editar.disabled = True
            dd_estado.disabled = True
            btn_actualizar.disabled = True
            btn_eliminar.disabled = True



        def actualizar_mesa(e):
            mensaje = ""
            exito = False

            if not self.tf_nombre_editar.value.strip():
                mensaje = f"Por favor, ingrese un nombre de Mesa válido."
            elif not tf_capacidad_editar.value.strip():
                mensaje = f"Por favor, asigne una capacidad a la Mesa"
            elif not tf_capacidad_editar.value.isdigit() or int(tf_capacidad_editar.value) <= 0:
                mensaje = f"Por favor, asigne una capacidad válida a la Mesa"
            else:
                exito, mensaje = actualizar_mesa_db(self.mesa_seleccionada["id"], self.tf_nombre_editar.value, tf_capacidad_editar.value, dd_estado.value)
            
            if exito:
                self.page.open(ft.SnackBar(
                    content=ft.Text(mensaje),
                    action="OK",
                ))
                self.mesa_seleccionada = None
                self.tf_nombre_editar.value = ""
                tf_capacidad_editar.value = ""
                dd_estado.value = 0
                self.tf_nombre_editar.focus()
                self.crear_vista()

        def eliminar_mesa_click(e):
            exito, mensaje = eliminar_mesa_db(self.mesa_seleccionada["id"])
            
            if exito:
                self.page.open(ft.SnackBar(
                    content=ft.Text(mensaje),
                    action="OK",
                ))
                self.mesa_seleccionada = None
                self.tf_nombre_editar.value = ""
                tf_capacidad_editar.value = ""
                dd_estado.value = 0
                self.tf_nombre_editar.focus()
                self.crear_vista()

        return ft.Column([
            ft.Text("Editar mesa", size=20, weight=ft.FontWeight.BOLD),
            self.tf_nombre_editar,
            tf_capacidad_editar,
            dd_estado,
            ft.Row([
                btn_actualizar,
                btn_eliminar
            ])
        ], 
        spacing=10,
        expand=True,
        )

