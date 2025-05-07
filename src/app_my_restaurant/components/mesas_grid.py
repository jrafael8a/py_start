import flet as ft
from src.app_my_restaurant.database.mesas_service import *

def manejar_click_mesa(numero_mesa):
    print(f"Click en mesa {numero_mesa}")


def crear_grid_mesas():
    exito, mesas = obtener_mesas_desde_db()  # debería devolverte lista de dicts o modelos
    grid = grid_mesas(mesas, on_mesa_click=manejar_click_mesa)
        
    return ft.Column([
        ft.Text("Gestión de mesas"),
        grid
    ])


def grid_mesas(mesas: list, on_mesa_click: callable) -> ft.GridView:
    """
    Crea un grid de mesas.

    Parámetros:
    - mesas: lista de diccionarios u objetos con .numero, .capacidad y .ocupada
    - on_mesa_click: función que recibe el número de mesa al hacer click
    """
    # USO: A la hora de llamar esta funcion se debe llamar con algo asi:
    # crear_grid_mesas(mesas, on_mesa_click=mi_funcion_click)

    exito, mesas = obtener_mesas_desde_db()  # debería devolverte lista de dicts o modelos

    grid = ft.GridView(
        expand=True,
        runs_count=2,
        max_extent=200,
        child_aspect_ratio=1.0,
        spacing=10,
        run_spacing=10,
        padding=10,
    )


    for mesa in mesas:
        color = ft.colors.GREEN_700 if not mesa else ft.colors.RED_700
        print(mesa)
        m_id = mesa['id']
        m_nombre = mesa['nombre']
        m_capacidad = mesa['capacidad']
        m_estado = mesa['estado']
        

        grid.controls.append(
            ft.Container(
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Icon(ft.icons.TABLE_RESTAURANT, color=ft.colors.AMBER_400),
                                ft.Text(f"Mesa {m_nombre}", size=16, weight=ft.FontWeight.BOLD),
                            ]
                        ),
                        ft.Text(f"Capacidad: {m_capacidad} personas", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text(m_estado, size=16, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                    ]
                ),
                bgcolor=color,
                border_radius=10,
                padding=15,
                ink=True,
                on_click=lambda e, id=m_id: on_mesa_click(id),
            )
        )

    return grid


if __name__ == "__main__":
    def main(page: ft.Page):
          page.add(crear_grid_mesas())
    
    ft.app(target=main)