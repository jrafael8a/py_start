import flet as ft
from src.app_my_restaurant.database.menu_categorias_service import obtener_categorias_menu_db
from src.app_my_restaurant.database.menu_service import agregar_menu_item_db, actualizar_menu_item_db, eliminar_menu_item_db
from src.app_my_restaurant.components.mini_componentes import MiniComponentes


class FormularioMenu():
    def __init__(self, gui, modo='crear', item_data=None, on_guardar=None, on_cancelar=None):
        # super().__init__()
        self.gui = gui
        self.minicomponentes = MiniComponentes(gui)


        self.modo = modo  # 'crear' o 'editar'
        self.item_data = item_data or {}
        self.on_guardar = on_guardar
        self.on_cancelar = on_cancelar

        # Campos del formulario
        self.tf_nombre =        ft.TextField(label="Nombre", autofocus=True, on_submit=lambda e: self.tf_descripcion.focus())
        self.tf_descripcion =   ft.TextField(label="Descripción", min_lines=2, max_lines=2, on_submit=lambda e: self.tf_precio.focus())
        self.tf_precio =        ft.TextField(label="Precio", input_filter=ft.InputFilter(allow=True, regex_string=r"^\d+(\.\d{0,2})?$"), on_submit=lambda e: self.dd_categoria.focus())
        self.dd_categoria =     self.minicomponentes.dropdown_categorias_menu(on_change_handler=lambda e: self.btn_guardar.focus())
        self.sw_estado =        ft.Switch(label="Habilitado", value=True)

        self.btn_limpiar = ft.ElevatedButton("Limpiar", on_click=self.limpiar_formulario)
        self.btn_cancelar = ft.ElevatedButton("Cancelar", on_click=self.cancelar)
        self.btn_guardar = ft.ElevatedButton("Guardar", on_click=self.guardar)

        self.contenedor = ft.Column(
                controls=[
                    ft.Divider(),               # El Tab superior se come parte del textfield, por eso pongo este divider
                    self.tf_nombre,
                    self.tf_descripcion,
                    self.tf_precio,
                    self.dd_categoria,
                    self.sw_estado,
                    ft.Row(
                        [self.btn_limpiar, self.btn_cancelar, self.btn_guardar],
                        alignment=ft.MainAxisAlignment.END,
                        spacing=10
                    )
                ],
                spacing=15,
                expand=True,
                scroll=True,
            )

    def crear_vista(self) -> ft.Column:
        self.dd_categoria =     self.minicomponentes.dropdown_categorias_menu(on_change_handler=lambda e: self.btn_guardar.focus())

        if self.modo == 'editar' and self.item_data:
            self.tf_nombre.value = self.item_data.get("nombre", "")
            self.tf_descripcion.value = self.item_data.get("descripcion", "")
            self.tf_precio.value = str(self.item_data.get("precio", ""))
            self.dd_categoria.value = self.item_data.get("tipo_id", None)
            self.sw_estado.value = self.item_data.get("estado", 1) == 1

        return self.contenedor

    def limpiar_formulario(self, e=None):
        self.tf_nombre.value = ""
        self.tf_descripcion.value = ""
        self.tf_precio.value = ""
        self.dd_categoria.value = None
        self.sw_estado.value = True
        self.gui.page.update()

    def cancelar(self, e=None):
        self.crear_vista()
        self.gui.page.update()

    def guardar(self, e=None):
        nombre = self.tf_nombre.value.strip()
        descripcion = self.tf_descripcion.value.strip()
        categoria_id = self.dd_categoria.value
        estado = 1 if self.sw_estado.value else 0

        print (nombre, descripcion, categoria_id, estado, sep=" | ")

        try:
            precio = float(self.tf_precio.value.strip())
        except ValueError:
            return self.gui.alerts.SnackBar("Precio inválido. Debe ser un número.")

        
        if not nombre:    
            return self.gui.alerts.SnackBar("Por favor asigne un nombre a este platillo.")
        elif not categoria_id:
            return self.gui.alerts.SnackBar("Seleccione una categoria del menú.")


        if self.modo == "crear":
            exito, mensaje = agregar_menu_item_db(nombre, descripcion, precio, categoria_id, estado)
        else:
            id = self.item_data.get("id")
            exito, mensaje = actualizar_menu_item_db(id, nombre, descripcion, precio, categoria_id, estado)

        if exito:
            self.gui.alerts.SnackBar(mensaje)
            if self.on_guardar:
                self.on_guardar()
            # self.gui.page.go_back()  # o cerrar modal si se usa modal
        else:
            self.gui.alerts.Dialogo_Error(mensaje)

if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(FormularioMenu(page).crear_vista())
    
    ft.app(target=main)
# else:
#    print("FormularioMenu() ejecutandose como modulo, desde otro lado, no desde el mismo archivo")