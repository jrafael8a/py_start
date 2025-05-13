import flet as ft

class MyAlerts:
    def __init__(self, page: ft.Page):
        self.page = page

    def Dialogo_Error(self, msg):
        dlg_alerta = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text(msg),
                actions=[ft.TextButton("OK", on_click=lambda e: self.page.close(dlg_alerta))],
            )
        self.page.open(dlg_alerta)
    
    def SnackBar(self, msg):
        self.page.open(ft.SnackBar(
                    content=ft.Text(msg),
                    action="OK",
                ))