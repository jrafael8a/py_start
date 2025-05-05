import flet as ft

class VistaMesera:
    def __init__ (self, page: ft.Page):
        self.page = page
    
    

    def crear_vista(self):
            self.grid_container = ft.Container(
                width=700,
                expand=True,
                content=self.crear_grid_mesas(),
            )
            
            return ft.Row(
                expand=True,
                spacing=0,
                controls=[
                    ft.Container(
                        expand=True,
                        content=ft.Column(
                            expand=True,
                            controls=[
                                ft.Text("Mesas del Restaurante", size=20, weight=ft.FontWeight.BOLD),
                                self.grid_container,
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
                                self.crear_panel_gestion(),
                            ],
                        )
                    ),
                ],
                
            )

if __name__ == "__main__":
    def main(page: ft.Page):
          page.add(crear_vista_mesera())
    
    ft.app(target=main)