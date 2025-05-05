import flet as ft

class VistaCaja:
    def __init__ (self, page: ft.Page):
        self.page = page
    

    def crear_vista(self):
            self.lista_caja = ft.ListView(
                expand=True,
                spacing=10,
                padding=20,
                auto_scroll=True,
            )

            def procesar_pago(e, mesa):
                if mesa.pedido_actual:
                    self.restaurante.liberar_mesa(mesa.numero)
                    self.actualizar_ui(e.page)

            def crear_item_cuenta(mesa):
                if not mesa.pedido_actual:
                    return None
                
                return ft.Container(
                    content=ft.Column([
                        ft.Text(f"Mesa {mesa.numero}", size=20, weight=ft.FontWeight.BOLD),
                        ft.Text(f"Cliente: {mesa.cliente.id}"),
                        ft.Text(mesa.pedido_actual.obtener_resumen()),
                        ft.ElevatedButton(
                            text="Procesar Pago",
                            on_click=lambda e, m=mesa: procesar_pago(e, m),
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.GREEN_700,
                                color=ft.Colors.WHITE,
                            )
                        )
                    ]),
                    bgcolor=ft.Colors.BLUE_GREY_900,
                    padding=10,
                    border_radius=10,
                )
            
            def actualizar_vista_caja():
                self.lista_caja.controls.clear()
                for mesa in self.restaurante.mesas:
                    if mesa.ocupada and mesa.pedido_actual:
                        item = crear_item_cuenta(mesa)
                        if item:
                            self.lista_caja.controls.append(item)
            
            self.actualizar_vista_caja = actualizar_vista_caja

            return ft.Container(
                expand=True,
                content=ft.Column([
                    ft.Text("Cuentas Activas", size=24, weight=ft.FontWeight.BOLD),
                    self.lista_caja,
                ])
            )

if __name__ == "__main__":
    def main(page: ft.Page):
          page.add(crear_vista_caja())
    
    ft.app(target=main)