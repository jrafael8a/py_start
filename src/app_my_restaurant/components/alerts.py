import flet as ft

class MyAlerts:
    def __init__(self, gui):
        self.gui = gui

    def Dialogo_Error(self, msg):
        dlg_alerta = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text(msg),
                actions=[ft.TextButton("OK", on_click=lambda e: self.gui.page.close(dlg_alerta))],
            )
        if self.gui.vista_creada:
            self.gui.page.open(dlg_alerta)
        else:
            print("MyAlerts().DialogoError dice: Vista No Creada. No se puede agregar el dialogo")
    
    def SnackBar(self, msg):
        if self.gui.vista_creada:
            self.gui.page.open(ft.SnackBar(
                    content=ft.Text(msg),
                    action="OK",
                ))
        else:
            print("MyAlerts().SnackBar dice: Vista No Creada. No se puede agregar el snackbar")