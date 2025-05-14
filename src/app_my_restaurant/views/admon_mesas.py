import flet as ft

from src.app_my_restaurant.database.mesas_service import *
from src.app_my_restaurant.components.mesas import *
from src.app_my_restaurant.database.estados_service import *

class VistaAdmonMesas:
    def __init__ (self, gui):
        self.gui = gui
        self.mesa_seleccionada = None
        self.container_admon_mesas = ft.Column([], expand= True, scroll= True)
        self.tf_nombre_editar = None    # Aqui almacenaremos un TextField que necesitamos hacer focus()

    def crear_vista(self):
        exito, self.mesas = obtener_mesas_desde_db()

        if not exito:
            self.gui.alerts.Dialogo_Error(self.mesas)
            self.gui.alerts.Dialogo_Error(self.mesas)
            return self.container_admon_mesas
        else:
            self.container_admon_mesas.controls.clear()
            self.container_admon_mesas.controls.append(
                ft.Row([
                    self.componente_agregar_mesa(),
                    ft.VerticalDivider(),
                    self.componente_editar_estados(),
                    ft.VerticalDivider(),
                    self.componente_editar_mesa(),
                ],
                spacing=20,
                #expand=True,
                #alignment=ft.MainAxisAlignment.START
                )
            )
            self.container_admon_mesas.controls.append(ft.Divider())
            self.container_admon_mesas.controls.append(crear_grid_mesas(self.on_click_mesa))
            self.gui.page.update()
            return self.container_admon_mesas

    def componente_editar_estados(self):
        exito, self.estados = obtener_estados_desde_db()
        
        container_estados = ft.Column([
            ft.Text("Editar Estados", size=20, weight=ft.FontWeight.BOLD)
        ],expand=True, scroll=True, alignment=ft.MainAxisAlignment.END, height=300)
        
        tf_estado = ft.TextField(label="Agregar Estado", on_submit=lambda e: btn_agregar.focus())
        tf_habilitado = ft.Checkbox(value=True)
        btn_agregar = ft.IconButton(icon=ft.Icons.ADD, on_click=lambda e: agregar_estado(e))
        
        def agregar_estado(e):
            exito, mensaje = agregar_estado_db(tf_estado.value, tf_habilitado.value)

            if exito:
                self.gui.alerts.SnackBar(mensaje)
                self.crear_vista()

            else:
                self.gui.alerts.Dialogo_Error(mensaje)

        def eliminar_estado(self, id):
            exito, mensaje = eliminar_estado_db(id)

            if exito:
                self.gui.alerts.SnackBar(mensaje)
                self.crear_vista()

            else:
                self.gui.alerts.Dialogo_Error(mensaje)

        def confirmar_eliminar_estado(self, id, nom):
            dlg_alerta = ft.AlertDialog(
                    modal=True,
                    title=ft.Text("Confirmar Eliminar"),
                    content=ft.Text(f"Está a punto de eliminar el estado '{nom}' \n\n " \
                                    f"Está seguro que desea eliminar este estado?"),
                    actions=[
                        ft.TextButton("Eliminar", on_click=lambda e: (self.gui.page.close(dlg_alerta), eliminar_estado(self, id))),
                        ft.TextButton("Cancelar", on_click=lambda e: (self.gui.page.close(dlg_alerta)))
                    ],
                )
            self.gui.page.open(dlg_alerta)


        container_estados.controls.append(
            ft.Row([
                tf_estado, tf_habilitado, btn_agregar
            ],
            expand=True)
        )


        for estado in self.estados:
            container_estados.controls.append(
                ft.Row([
                    ft.Text(estado['id']),
                    ft.Text(estado['nombre'], expand=True),
                    ft.IconButton(icon=ft.Icons.EDIT),
                    ft.IconButton(icon=ft.Icons.DELETE, on_click=lambda e, id=estado['id'], nom=estado['nombre']: confirmar_eliminar_estado(self, id, nom))
                ],
                expand=True)
            )

        return container_estados



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
        self.tf_nombre_agregar.disabled = True
        self.tf_capacidad_agregar.disabled = True
        self.btn_agregar.disabled = True
        self.tf_nombre_agregar.update()
        self.tf_capacidad_agregar.update()
        self.btn_agregar.update()



    def componente_agregar_mesa(self):
        self.tf_nombre_agregar = ft.TextField(label="Nombre de la mesa", min_lines=2, max_lines=2,autofocus=True, on_submit=lambda e: self.capacidad_input.focus())
        self.tf_capacidad_agregar = ft.TextField(label="Capacidad Máxima", input_filter=ft.NumbersOnlyInputFilter(), on_submit=lambda e: self.btn_agregar.focus())
        self.btn_agregar = ft.ElevatedButton("Agregar", icon=ft.Icons.ADD, on_click=lambda e: on_agregar_mesa(e))

        def on_agregar_mesa(e):
            mensaje = ""
            exito = False

            if not self.tf_nombre_agregar.value.strip():
                mensaje = f"Por favor, ingrese un nombre de Mesa válido."
            elif not self.tf_capacidad_agregar.value.strip():
                mensaje = f"Por favor, asigne una capacidad a la Mesa"
            elif not self.tf_capacidad_agregar.value.isdigit() or int(self.tf_capacidad_agregar.value) <= 0:
                mensaje = f"Por favor, asigne una capacidad válida a la Mesa"
            else:
                exito, mensaje = agregar_mesa_db(self.tf_nombre_agregar.value, self.tf_capacidad_agregar.value)
                
            if exito:
                self.gui.alerts.SnackBar(mensaje)
                self.tf_nombre_agregar.value = ""
                self.tf_capacidad_agregar.value = ""
                self.tf_nombre_agregar.focus()
                self.crear_vista()

            else:
                self.gui.alerts.Dialogo_Error(mensaje)

        return ft.Column(
                [
                    ft.Text("Agregar nueva mesa", size=20, weight=ft.FontWeight.BOLD),
                    self.tf_nombre_agregar,
                    self.tf_capacidad_agregar,
                    self.btn_agregar,
                ], 
                spacing=10,
                expand=False,
                horizontal_alignment='center'
            )

    def componente_editar_mesa(self):
        exito, self.estados = obtener_estados_desde_db()
        lista_estados = []

        self.tf_nombre_editar = ft.TextField(label="Nombre", on_submit=lambda e: tf_capacidad_editar.focus())
        tf_capacidad_editar = ft.TextField(label="Capacidad", input_filter=ft.NumbersOnlyInputFilter(), on_submit=lambda e: dd_estado.focus())
        btn_actualizar =    ft.ElevatedButton("Actualizar", icon=ft.Icons.SAVE, on_click=lambda e: actualizar_mesa(e))
        btn_eliminar =      ft.ElevatedButton("Eliminar", icon=ft.Icons.DELETE, on_click=lambda e: confirmar_eliminar_mesa(e), bgcolor=ft.Colors.RED_500)
        btn_cancelar =      ft.ElevatedButton("Cancelar", icon=ft.Icons.CANCEL, on_click=lambda e: cancelar_click(e))
        
        if exito:
            for estado in self.estados:
                estado_id = str(estado['id'])       # Dropdown Option requiere str como value
                estado_nombre = estado['nombre']
                estado_habilitado = estado['habilitado']

                if estado_habilitado:
                    lista_estados.append(ft.dropdown.Option(estado_id, estado_nombre))

            dd_estado = ft.Dropdown(
                label="Estado",
                value=lista_estados[0] if lista_estados else None,
                expand=True,
                options=lista_estados
            )
        else:
                self.gui.alerts.Dialogo_Error(self.estados)

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
            btn_cancelar.disabled = True

        def cancelar_click(e):
            self.mesa_seleccionada = None
            self.crear_vista()
    
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
                self.gui.alerts.SnackBar(mensaje)
                self.mesa_seleccionada = None
                self.tf_nombre_editar.value = ""
                tf_capacidad_editar.value = ""
                dd_estado.value = 0
                self.tf_nombre_editar.focus()
                self.crear_vista()

        def confirmar_eliminar_mesa(e):
            dlg_alerta = ft.AlertDialog(
                    modal=True,
                    title=ft.Text("Confirmar Eliminar"),
                    content=ft.Text(f"Está a punto de eliminar la mesa '{self.tf_nombre_editar.value}' \n\n " \
                                    f"Está seguro que desea eliminar esta mesa?"),
                    actions=[
                        ft.TextButton("Eliminar", on_click=lambda e: (self.gui.page.close(dlg_alerta), eliminar_mesa(e))),
                        ft.TextButton("Cancelar", on_click=lambda e: (self.gui.page.close(dlg_alerta)))
                    ],
                )
            self.gui.page.open(dlg_alerta)
        
        def eliminar_mesa(e):
            exito, mensaje = eliminar_mesa_db(self.mesa_seleccionada["id"])
            
            if exito:
                self.gui.alerts.SnackBar(mensaje)
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
                btn_actualizar, btn_eliminar, btn_cancelar
            ],
            expand=False)
        ], 
        spacing=10,
        expand=True,                    # Si lo pongo en false, rompe la gui y se muestra todo sombremontado
        horizontal_alignment='center'
        )