import flet as ft
from src.app_my_restaurant.database.menu_tipos_service import *

class VistaAdmonMenuCategorias:
    def __init__(self, gui):
        self.gui = gui
        self.container = ft.Column([], expand=True, scroll=True, spacing=10)

    def crear_vista(self):
        exito, categorias = obtener_tipos_menu_db()

        if not exito:
            self.gui.alerts.Dialogo_Error(categorias)
            return self.container

        self.container.controls.clear()

        tf_nueva_cat = ft.TextField(
            label="Nuevo categoria del menú",
            autofocus=True,
            on_submit=lambda e: btn_agregar.focus()
        )

        btn_agregar = ft.ElevatedButton(
            text="Agregar Categoria al Menu",
            icon=ft.Icons.ADD,
            tooltip="Agregar",
            on_click=lambda e: agregar_cat()
        )

        btn_actualizar = ft.ElevatedButton(
            text="Actualizar Vista",
            icon= ft.Icons.UPDATE,
            tooltip="Actualizar",
            on_click=lambda e: self.crear_vista()
        )

        def agregar_cat():
            nombre = tf_nueva_cat.value.strip()
            if not nombre:
                return self.gui.alerts.SnackBar("Escriba un Nombre valido")

            exito, mensaje = agregar_tipo_menu_db(nombre)
            if exito:
                self.gui.alerts.SnackBar(mensaje)
                self.crear_vista()
            else:
                self.gui.alerts.Dialogo_Error(mensaje)
        
        self.container.controls.append(ft.Divider())
        self.container.controls.append(
            ft.Row([tf_nueva_cat, btn_agregar, ft.VerticalDivider(), btn_actualizar], spacing=10)
        )
        self.container.controls.append(ft.Divider())

        for tipo in categorias:
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
                    icon=ft.Icons.SAVE,
                    tooltip="Guardar",
                    on_click=lambda e: self.guardar_edicion(id, tf.value, chk.value)
                )
                btn_eliminar = ft.IconButton(
                    icon=ft.Icons.DELETE,
                    tooltip="Eliminar",
                    on_click=lambda e: self.confirmar_eliminar(id, tf.value)
                )
                return btn_guardar, btn_eliminar

            btn_guardar, btn_eliminar = crear_callbacks(tipo["id"], tf_nombre, chk_estado)

            self.container.controls.append(
                ft.Row([tf_nombre, chk_estado, btn_guardar, btn_eliminar], spacing=10)
            )


        self.gui.page.update()
        return self.container

    def guardar_edicion(self, id, tf, chk):
        nuevo_nombre = tf
        nuevo_estado = int(chk)
        if not nuevo_nombre:
            return
        exito, mensaje = actualizar_tipo_menu_db(id, nuevo_nombre, nuevo_estado)
        self.gui.alerts.SnackBar(mensaje)
        self.gui.page.update()

    def actualizar_estado_tipo_menu(self, id, nuevo_estado):
        estado = 1 if nuevo_estado else 0
        exito, mensaje = actualizar_estado_tipo_menu_db(id, estado)
        if not exito:
            self.gui.alerts.SnackBar(mensaje)
        else:
            self.gui.alerts.SnackBar(mensaje)


    def confirmar_eliminar(self, id, nombre):
        def eliminar(e):
            exito, mensaje = eliminar_tipo_menu_db(id)
            if exito:
                self.gui.alerts.SnackBar(mensaje)
                self.crear_vista()
            else:
                self.gui.alerts.Dialogo_Error(mensaje)

        dlg = ft.AlertDialog(
            modal=False,
            title=ft.Text("Confirmar Eliminación"),
            content=ft.Text(f"¿Está seguro que desea eliminar el tipo '{nombre}'?"),
            actions=[
                ft.TextButton("Eliminar", on_click=lambda e: (self.gui.page.close(dlg), eliminar(e))),
                ft.TextButton("Cancelar", on_click=lambda e: self.gui.page.close(dlg))
            ],
        )
        self.gui.page.open(dlg)
