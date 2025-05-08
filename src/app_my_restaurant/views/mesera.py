import flet as ft

from src.app_my_restaurant.components.mesas import crear_grid_mesas

class VistaMesera:
    def __init__ (self, page: ft.Page):
        self.page = page
    
    

    def crear_vista(self):
        return ft.Row(
            expand=True,
            spacing=0,
            controls=[
                ft.Container(
                    expand=True,
                    content=ft.Column(
                        expand=True,
                        scroll=True,
                        controls=[
                            ft.Text("Mesas del Restaurante", size=20, weight=ft.FontWeight.BOLD),
                            crear_grid_mesas(None)
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
                            self.panel_gestion(),
                        ],
                    )
                ),
            ],
            
        )
    
    def panel_gestion(self):






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
            #on_change=self.actualizar_items_menu
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
            #on_click=self.asignar_cliente,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.GREEN_700,
                color=ft.Colors.WHITE,
            )
        )

        self.btn_agregar_item = ft.ElevatedButton(
            text = "Agregar Item",
            #on_click = self.agregar_item_pedido,
            disabled=True,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.BLUE_700,
                color=ft.Colors.WHITE,
            )
        )

        self.btn_liberar = ft.ElevatedButton(
            text="Liberar Mesa",
            #on_click=self.liberar_mesa,
            disabled=True,
            style=ft.ButtonStyle(
                bgcolor = ft.Colors.RED_700,
                color = ft.Colors.WHITE,
            )
        )

        self.resumen_pedido = ft.Text("", size=14)
        

        return ft.Container(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
                expand=True,
                scroll=True,
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
            ),
            padding=20,
            expand=True,
        )


























        return

if __name__ == "__main__":
    def main(page: ft.Page):
          page.add(VistaMesera(page).crear_vista())
    
    ft.app(target=main)