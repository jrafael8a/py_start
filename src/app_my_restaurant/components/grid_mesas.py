# components/grid_mesas.py

import flet as ft

def crear_grid_mesas(mesas: list, on_mesa_click: callable) -> ft.GridView:
    """
    Crea un grid de mesas.

    Parámetros:
    - mesas: lista de diccionarios u objetos con .numero, .capacidad y .ocupada
    - on_mesa_click: función que recibe el número de mesa al hacer click
    """
    # USO: A la hora de llamar esta funcion se debe llamar con algo asi:
    # crear_grid_mesas(mesas, on_mesa_click=mi_funcion_click)

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
        color = ft.colors.GREEN_700 if not mesa["ocupada"] else ft.colors.RED_700
        estado = "LIBRE" if not mesa["ocupada"] else "OCUPADA"

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
                                ft.Text(f"Mesa {mesa['numero']}", size=16, weight=ft.FontWeight.BOLD),
                            ]
                        ),
                        ft.Text(f"Capacidad: {mesa['capacidad']} personas", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text(estado, size=16, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                    ]
                ),
                bgcolor=color,
                border_radius=10,
                padding=15,
                ink=True,
                on_click=lambda e, num=mesa["numero"]: on_mesa_click(num),
            )
        )

    return grid
