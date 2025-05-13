# src/app_my_restaurant/views/admon_menu.py

import flet as ft
from src.app_my_restaurant.database.menu_service import *
from src.app_my_restaurant.components.alerts import MyAlerts

class VistaAdmonMenu:
    def __init__(self, page: ft.Page):
        self.page = page
        self.alerts = MyAlerts(self.page)
        self.item_seleccionado = None
        self.container_admon_menu = ft.Column([], expand=True, scroll=True)
        self.tf_nombre_editar = None

    def crear_vista(self):
        exito, self.menu_items = obtener_menu_items_desde_db()

        if not exito:
            self.alerts.Dialogo_Error(self.menu_items)
            return self.container_admon_menu

        self.container_admon_menu.controls.clear()
        self.container_admon_menu.controls.append(
            ft.Row([
                self.componente_agregar_item(),
                ft.Column([], expand=True),
                self.componente_editar_item()
            ], spacing=20, expand=True)
        )
        self.container_admon_menu.controls.append(ft.Divider())

        for item in self.menu_items:
            self.container_admon_menu.controls.append(
                ft.ListTile(
                    title=ft.Text(item["nombre"]),
                    subtitle=ft.Text(f"{item['tipo']} - ${item['precio']:.2f}"),
                    trailing=ft.Icon(ft.icons.EDIT),
                    on_click=lambda e, id=item["id"]: self.on_click_item(id)
                )
            )

        self.page.update()
        return self.container_admon_menu

    def on_click_item(self, item_id):
        for item in self.menu_items:
            if item["id"] == item_id:
                self.item_seleccionado = item
                break
        else:
            self.item_seleccionado = None

        self.crear_vista()

    def componente_agregar_item(self):
        tf_nombre = ft.TextField(label="Nombre", autofocus=True)
        tf_tipo = ft.TextField(label="Tipo")
        tf_precio = ft.TextField(label="Precio", input_filter=ft.NumbersOnlyInputFilter())
        btn_agregar = ft.ElevatedButton("Agregar", icon=ft.icons.ADD)

        def agregar_item(e):
            if not tf_nombre.value or not tf_tipo.value or not tf_precio.value:
                self.page.open(ft.SnackBar(content=ft.Text("Todos los campos son obligatorios")))
                return

            exito, mensaje = agregar_menu_item_db(tf_nombre.value, tf_tipo.value, float(tf_precio.value))
            if exito:
                self.page.open(ft.SnackBar(content=ft.Text(mensaje)))
                self.crear_vista()
            else:
                self.page.open(ft.AlertDialog(title=ft.Text("Error"), content=ft.Text(mensaje)))

        btn_agregar.on_click = agregar_item

        return ft.Column([ft.Text("Agregar nuevo ítem", size=20), tf_nombre, tf_tipo, tf_precio, btn_agregar], spacing=10, expand=True)

    def componente_editar_item(self):
        tf_nombre = ft.TextField(label="Nombre")
        tf_tipo = ft.TextField(label="Tipo")
        tf_precio = ft.TextField(label="Precio", input_filter=ft.NumbersOnlyInputFilter())
        cb_estado = ft.Checkbox(label="Activo", value=True)
        btn_actualizar = ft.ElevatedButton("Actualizar", icon=ft.icons.SAVE)
        btn_eliminar = ft.ElevatedButton("Eliminar", icon=ft.icons.DELETE, bgcolor=ft.colors.RED)

        if self.item_seleccionado:
            tf_nombre.value = self.item_seleccionado["nombre"]
            tf_tipo.value = self.item_seleccionado["tipo"]
            tf_precio.value = str(self.item_seleccionado["precio"])
            cb_estado.value = bool(self.item_seleccionado["estado"])
        else:
            tf_nombre.disabled = True
            tf_tipo.disabled = True
            tf_precio.disabled = True
            cb_estado.disabled = True
            btn_actualizar.disabled = True
            btn_eliminar.disabled = True

        def actualizar_item(e):
            exito, mensaje = actualizar_menu_item_db(
                self.item_seleccionado["id"],
                tf_nombre.value,
                tf_tipo.value,
                float(tf_precio.value),
                int(cb_estado.value)
            )
            if exito:
                self.page.open(ft.SnackBar(content=ft.Text(mensaje)))
                self.item_seleccionado = None
                self.crear_vista()
            else:
                self.page.open(ft.AlertDialog(title=ft.Text("Error"), content=ft.Text(mensaje)))

        def eliminar_item(e):
            exito, mensaje = eliminar_menu_item_db(self.item_seleccionado["id"])
            if exito:
                self.page.open(ft.SnackBar(content=ft.Text(mensaje)))
                self.item_seleccionado = None
                self.crear_vista()
            else:
                self.page.open(ft.AlertDialog(title=ft.Text("Error"), content=ft.Text(mensaje)))

        btn_actualizar.on_click = actualizar_item
        btn_eliminar.on_click = eliminar_item

        return ft.Column([
            ft.Text("Editar ítem", size=20),
            tf_nombre,
            tf_tipo,
            tf_precio,
            cb_estado,
            ft.Row([btn_actualizar, btn_eliminar])
        ], spacing=10, expand=True)
