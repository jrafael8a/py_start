import flet as ft
from src.app_my_restaurant.database.menu_tipos_service import *

class VistaAdmonMenuTipos:
    def __init__(self, page: ft.Page):
        self.page = page
        self.container = ft.Column([], expand=True, scroll=True)

    def crear_vista(self):
        self.container.controls.clear()

        exito, tipos = obtener_tipos_menu_db()

        if not exito:
            dlg_alerta =ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text(tipos),
                actions=[ft.TextButton("OK", on_click=lambda e: self.page.close(dlg_alerta))]
            )
            self.page.open(dlg_alerta)
            return self.container

        # Formulario agregar nuevo tipo
        tf_nombre = ft.TextField(label="Nombre del tipo de menú", autofocus=True)
        cb_estado = ft.Checkbox(label="Habilitado", value=True)
        btn_agregar = ft.ElevatedButton("Agregar", icon=ft.icons.ADD)

        def on_agregar(e):
            nombre = tf_nombre.value.strip()
            estado = 1 if cb_estado.value else 0

            if not nombre:
                self.page.open(ft.SnackBar(content=ft.Text("El nombre no puede estar vacío")))
                return

            exito, mensaje = agregar_tipo_menu_db(nombre)

            if exito:
                tf_nombre.value = ""
                cb_estado.value = True
                self.page.open(ft.SnackBar(content=ft.Text(mensaje)))
                self.crear_vista()
            else:
                self.page.open(ft.AlertDialog(
                    title=ft.Text("Error"),
                    content=ft.Text(mensaje),
                    actions=[ft.TextButton("OK", on_click=lambda e: self.page.close(dlg_alerta))]
                ))
            self.page.update()

        btn_agregar.on_click = on_agregar

        self.container.controls.append(
            ft.Text("Administrar Tipos de Ítems del Menú", size=24, weight=ft.FontWeight.BOLD)
        )
        self.container.controls.append(ft.Row([tf_nombre, cb_estado, btn_agregar], expand=True))

        self.container.controls.append(ft.Divider())

        # Lista de tipos ya existentes
        for tipo in tipos:
            tf_nombre_editar = ft.TextField(value=tipo["nombre"], expand=True)
            cb_estado_editar = ft.Checkbox(label="Habilitado", value=(tipo["estado"] == 1))
            btn_guardar = ft.IconButton(icon=ft.icons.SAVE, tooltip="Guardar cambios")
            btn_eliminar = ft.IconButton(icon=ft.icons.DELETE, tooltip="Eliminar", icon_color=ft.colors.RED)

            def on_guardar(e, id=tipo["id"], tf=tf_nombre_editar, cb=cb_estado_editar):
                exito, mensaje = actualizar_tipo_menu_db(id, tf.value.strip(), 1 if cb.value else 0)
                if exito:
                    self.page.open(ft.SnackBar(content=ft.Text("Tipo actualizado")))
                    self.crear_vista()
                else:
                    self.page.open(ft.AlertDialog(
                        title=ft.Text("Error"),
                        content=ft.Text(mensaje),
                        actions=[ft.TextButton("OK", on_click=lambda e: self.page.close(dlg_alerta))]
                    ))

            def on_eliminar(e, id=tipo["id"]):
                exito, mensaje = eliminar_tipo_menu_db(id)
                if exito:
                    self.page.open(ft.SnackBar(content=ft.Text("Tipo eliminado")))
                    self.crear_vista()
                else:
                    self.page.open(ft.AlertDialog(
                        title=ft.Text("Error"),
                        content=ft.Text(mensaje),
                        actions=[ft.TextButton("OK", on_click=lambda e: self.page.close(dlg_alerta))]
                    ))

            btn_guardar.on_click = lambda e, id=tipo["id"], tf=tf_nombre_editar, cb=cb_estado_editar: on_guardar(e, id, tf, cb)
            btn_eliminar.on_click = lambda e, id=tipo["id"]: on_eliminar(e, id)

            self.container.controls.append(
                ft.Row([
                    tf_nombre_editar,
                    cb_estado_editar,
                    btn_guardar,
                    btn_eliminar
                ], expand=True)
            )

        return self.container
