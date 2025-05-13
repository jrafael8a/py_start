import flet as ft
from src.app_my_restaurant.database.menu_tipos_service import *
from src.app_my_restaurant.components.alerts import MyAlerts

class VistaAdmonMenuTipos:
    def __init__(self, page: ft.Page):
        self.page = page
        self.alerts = MyAlerts(self.page)
        self.container = ft.Column([], expand=True, scroll=True, spacing=10)

    def crear_vista(self):
        exito, tipos = obtener_tipos_menu_db()

        if not exito:
            MyAlerts(self.page).Dialogo_Error(tipos)
            return self.container

        self.container.controls.clear()

        tf_nuevo_tipo = ft.TextField(
            label="Nuevo tipo de ítem de menú",
            autofocus=True,
            on_submit=lambda e: btn_agregar.focus()
        )

        btn_agregar = ft.ElevatedButton(
            text="Agregar Item al Menu",
            icon=ft.icons.ADD,
            tooltip="Agregar",
            on_click=lambda e: agregar_tipo()
        )

        btn_actualizar = ft.ElevatedButton(
            text="Actualizar Vista",
            icon= ft.icons.UPDATE,
            tooltip="Actualizar",
            on_click=lambda e: self.crear_vista()
        )

        def agregar_tipo():
            nombre = tf_nuevo_tipo.value.strip()
            if not nombre:
                return self.alerts.SnackBar("Escriba un Nombre valido")

            exito, mensaje = agregar_tipo_menu_db(nombre)
            if exito:
                self.alerts.SnackBar(mensaje)
                self.crear_vista()
            else:
                self.alerts.Dialogo_Error(mensaje)
        
        self.container.controls.append(ft.Divider())
        self.container.controls.append(
            ft.Row([tf_nuevo_tipo, btn_agregar, ft.VerticalDivider(), btn_actualizar], spacing=10)
        )
        self.container.controls.append(ft.Divider())

        for tipo in tipos:
            tf_nombre = ft.TextField(
                value=tipo["nombre"],
                expand=True,
                on_submit=None  # se asigna luego
            )

            chk_estado = ft.Checkbox(
                label="Habilitado",
                value=tipo["estado"] == 1,
            )

            def crear_callbacks(id, tf, chk):
                tf.on_submit = lambda e: self.guardar_edicion(id, tf.value, chk.value)
                chk.on_change = lambda e: self.actualizar_estado_tipo_menu(id, chk.value)
                btn_guardar = ft.IconButton(
                    icon=ft.icons.SAVE,
                    tooltip="Guardar",
                    on_click=lambda e: self.guardar_edicion(id, tf.value, chk.value)
                )
                btn_eliminar = ft.IconButton(
                    icon=ft.icons.DELETE,
                    tooltip="Eliminar",
                    on_click=lambda e: self.confirmar_eliminar(id, tf.value)
                )
                return btn_guardar, btn_eliminar

            btn_guardar, btn_eliminar = crear_callbacks(tipo["id"], tf_nombre, chk_estado)

            self.container.controls.append(
                ft.Row([tf_nombre, chk_estado, btn_guardar, btn_eliminar], spacing=10)
            )


        self.page.update()
        return self.container

    def guardar_edicion(self, id, tf, chk):
        nuevo_nombre = tf
        nuevo_estado = int(chk)
        if not nuevo_nombre:
            return
        exito, mensaje = actualizar_tipo_menu_db(id, nuevo_nombre, nuevo_estado)
        self.alerts.SnackBar(mensaje)
        self.page.update()

    def actualizar_estado_tipo_menu(self, id, nuevo_estado):
        estado = 1 if nuevo_estado else 0
        exito, mensaje = actualizar_estado_tipo_menu_db(id, estado)
        if not exito:
            self.alerts.SnackBar(mensaje)
        else:
            self.alerts.SnackBar(mensaje)


    def confirmar_eliminar(self, id, nombre):
        def eliminar(e):
            exito, mensaje = eliminar_tipo_menu_db(id)
            if exito:
                self.alerts.SnackBar(mensaje)
                self.crear_vista()
            else:
                self.alerts.Dialogo_Error(mensaje)

        dlg = ft.AlertDialog(
            modal=False,
            title=ft.Text("Confirmar Eliminación"),
            content=ft.Text(f"¿Está seguro que desea eliminar el tipo '{nombre}'?"),
            actions=[
                ft.TextButton("Eliminar", on_click=lambda e: (self.page.close(dlg), eliminar(e))),
                ft.TextButton("Cancelar", on_click=lambda e: self.page.close(dlg))
            ],
        )
        self.page.open(dlg)
