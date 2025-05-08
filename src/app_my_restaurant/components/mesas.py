import flet as ft
from src.app_my_restaurant.database.mesas_service import agregar_mesa_db, obtener_mesas_desde_db

#def manejar_click_mesa(numero_mesa):
#    print(f"Click en mesa {numero_mesa}")


def crear_grid_mesas(manejar_click_mesa: callable):
    exito, mesas = obtener_mesas_desde_db()  # debería devolverte lista de dicts o modelos
    
    if exito:
        grid = grid_mesas(mesas, on_mesa_click=manejar_click_mesa)
    else:
        grid = ft.Text(f"Error al cargar las mesas: {mesas}")

        
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

    # exito, mesas = obtener_mesas_desde_db()  # debería devolverte lista de dicts o modelos

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
        m_id = mesa['id']
        m_nombre = mesa['nombre']
        m_capacidad = mesa['capacidad']
        m_estado = mesa['estado']
        icon = ft.Icon(ft.icons.TABLE_RESTAURANT, color=ft.colors.AMBER_400),

        if m_estado == 0:       # Libre
            m_estado_t = "Mesa Libre"
            color = ft.colors.GREEN_700
            icon = ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE, color=ft.colors.WHITE)

        elif m_estado == 1:     # Reservada
            m_estado_t = "Mesa Reservada"
            color = ft.colors.ORANGE_800
            icon = ft.Icon(ft.icons.EVENT_AVAILABLE, color=ft.colors.WHITE)

        elif m_estado == 2:     # Ocupada
            m_estado_t = "Mesa Ocupada"
            color = ft.colors.RED_800
            icon = ft.Icon(ft.icons.PERSON, color=ft.colors.WHITE)

        elif m_estado == 3:     # Orden Tomada
            m_estado_t = "Orden Tomada"
            color = ft.colors.RED_600
            icon = ft.Icon(ft.icons.RECEIPT_LONG, color=ft.colors.WHITE)

        elif m_estado == 4:     # En Preparación
            m_estado_t = "En Preparacion..."
            color = ft.colors.RED_400
            icon = ft.Icon(ft.icons.RESTAURANT, color=ft.colors.WHITE)

        elif m_estado == 5:     # Comiendo
            m_estado_t = "Comiendo..."
            color = ft.colors.RED_200
            icon = ft.Icon(ft.icons.RESTAURANT, color=ft.colors.WHITE)

        elif m_estado == 6:     # Esperando Cuenta
            m_estado_t = "Esperando Cuenta..."
            color = ft.colors.PURPLE_700
            icon = ft.Icon(ft.icons.RECEIPT, color=ft.colors.WHITE)

        elif m_estado == 7:     # Pago en Proceso
            m_estado_t = "Pagando..."
            color = ft.colors.GREEN_400
            icon = ft.Icon(ft.icons.PAYMENTS, color=ft.colors.WHITE)

        elif m_estado == 8:     # Necesita Limpieza
            m_estado_t = "Necesita Limpieza!!"
            color = ft.colors.GREY_700
            icon = ft.Icon(ft.icons.CLEANING_SERVICES, color=ft.colors.WHITE)

        elif m_estado == 9:     # Fuera de Servicio
            m_estado_t = "Fuera de Servicio"
            color = ft.colors.BLACK
            icon = ft.Icon(ft.icons.BLOCK, color=ft.colors.RED_400)

        else:
            color = ft.colors.GREY_900
            icon = ft.Icon(ft.icons.HELP, color=ft.colors.WHITE)


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
                                icon,
                                ft.Text(f"{m_nombre}", size=16, weight=ft.FontWeight.BOLD, max_lines=2, expand=True, text_align=ft.TextAlign.CENTER, overflow=ft.TextOverflow.ELLIPSIS),
                            ]
                        ),
                        ft.Text(f"Capacidad: {m_capacidad} personas", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text(m_estado_t, size=16, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
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