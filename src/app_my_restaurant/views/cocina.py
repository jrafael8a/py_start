import flet as ft


class VistaCocina:
    def __init__ (self, page: ft.Page):
        self.page = page
    
    def crear_vista(self):
            self.lista_pedidos_cocina = ft.ListView(
                expand=True,
                spacing=10,
                padding=20,
                auto_scroll=True,
            )

            def cambiar_estado_pedido(e, pedido, nuevo_estado):
                pedido.cambiar_estado(nuevo_estado)
                self.actualizar_vista_cocina()
                self.actualizar_ui(e.page)
                e.page.update()

            def crear_item_pedido(pedido):
                return ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(f"Mesa {pedido.mesa.numero}", size=20, weight=ft.FontWeight.BOLD),
                            ft.Text(pedido.obtener_resumen()),
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        text="En Preparacion",
                                        on_click=lambda e, p=pedido: cambiar_estado_pedido(e, p, "En Preparacion"),
                                        disabled=pedido.estado != "Pendiente",
                                        style=ft.ButtonStyle(
                                            bgcolor=ft.Colors.ORANGE_700,
                                            color=ft.Colors.WHITE,
                                        )
                                    ),
                                    ft.ElevatedButton(
                                        text="Listo",
                                        on_click=lambda e, p=pedido: cambiar_estado_pedido(e, p, "Listo"),
                                        disabled=pedido.estado != "En Preparacion",
                                        style=ft.ButtonStyle(
                                            bgcolor=ft.Colors.BLUE_700, 
                                            color=ft.Colors.WHITE,
                                        )
                                    ),
                                    ft.Text(f"Estado: {pedido.estado}", color=ft.Colors.BLUE_200),
                                ]
                            )
                        ],
                        spacing=5,
                    ),
                    padding=10,
                    border_radius=10,
                )
            
            def actualizar_vista_cocina():
                self.lista_pedidos_cocina.controls.clear()
                for pedido in self.restaurante.pedidos_activos:
                    if pedido.estado in ["Pendiente", "En Preparacion"]:
                        self.lista_pedidos_cocina.controls.append(crear_item_pedido(pedido))
            
            self.actualizar_vista_cocina = actualizar_vista_cocina

            return ft.Container(
                expand=True,
                content=ft.Column([
                    ft.Text("Pedidos Pendientes", size=24, weight=ft.FontWeight.BOLD),
                    self.lista_pedidos_cocina,
                ])
            )

if __name__ == "__main__":
    def main(page: ft.Page):
          page.add(crear_vista_cocina())
    
    ft.app(target=main)