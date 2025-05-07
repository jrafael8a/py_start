import flet as ft
from src.app_my_restaurant.database.mesas_service import agregar_mesa_db

def on_agregar_mesa(nombre_mesa, capacidad_mesa, page):
    page = page
    mensaje = ""
    exito = False

    if not nombre_mesa.strip():
        mensaje = f"Por favor, ingrese un nombre de Mesa válido."
    elif not capacidad_mesa.strip():
        mensaje = f"Por favor, asigne una capacidad a la Mesa"
    elif not capacidad_mesa.isdigit() or int(capacidad_mesa) <= 0:
        mensaje = f"Por favor, asigne una capacidad válida a la Mesa"
    else:
        exito, mensaje = agregar_mesa_db(nombre_mesa, capacidad_mesa)
        
    if exito:
        page.open(ft.SnackBar(
            content=ft.Text(mensaje),
            action="OK",
        ))
    else:
        dlg_alerta = ft.AlertDialog(
            title=ft.Text("Error"),
            content=ft.Text(mensaje),
            actions=[
                ft.TextButton("OK", on_click=lambda e: page.close(dlg_alerta))
            ],
        )
        page.open(dlg_alerta)
    

def crear_componente_agregar_mesa(page):
    nombre_input = ft.TextField(label="Nombre de la mesa", autofocus=True)
    capacidad_input = ft.TextField(label="Capacidad Máxima", input_filter=ft.NumbersOnlyInputFilter())
    boton_agregar = ft.ElevatedButton(
        text="Agregar mesa",
        icon=ft.icons.ADD,
        on_click=lambda e: on_agregar_mesa(nombre_input.value, capacidad_input.value, page)  # Llama a la función de agregar mesa
    )

    return ft.Column(
        controls=[
            ft.Text("Agregar nueva mesa", size=20, weight=ft.FontWeight.BOLD),
            nombre_input,
            capacidad_input,
            boton_agregar
        ],
        spacing=10
    )
