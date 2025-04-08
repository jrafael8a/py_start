import flet as ft

name = "Containers with different alignment"


def example():

    container_1 = ft.Container(
        content=ft.Text("Center"),              # ft.Text. Para ver graficamente la alineacion
        alignment=ft.alignment.center,          # Alineacion Interior: Centro
        bgcolor=ft.Colors.BLUE_GREY_100,
        width=150,
        height=150,
    )

    container_2 = ft.Container(
        content=ft.Text("Top left"),            # ft.Text. Para ver graficamente la alineacion
        alignment=ft.alignment.top_left,        # Alineacion Interior: Arriba a la izquierda
        bgcolor=ft.Colors.BLUE_GREY_200,
        width=150,
        height=150,
    )

    container_3 = ft.Container(
        content=ft.Text("-0.5, -0.5"),
        alignment=ft.alignment.Alignment(-0.5, -0.5),   # Sistema de alineacion de coordenadas
        bgcolor=ft.Colors.BLUE_GREY_300,
        width=150,
        height=150,
    )

    container_4 = ft.Container(
        content=ft.Text("C4. -1, -1"),
        alignment=ft.alignment.Alignment(-1, -1),
        bgcolor=ft.Colors.BLUE_GREY_400,
        width=150,
        height=150,
    )

    container_5 = ft.Container(
        content=ft.Text("C5. -1, 0"),
        alignment=ft.alignment.Alignment(-1, 0),
        bgcolor=ft.Colors.BLUE_GREY_500,
        width=150,
        height=150,
    )

    container_6 = ft.Container(
        content=ft.Text("C6. 0, 1"),
        alignment=ft.alignment.Alignment(0, 1),
        bgcolor=ft.Colors.BLUE_GREY_600,
        width=150,
        height=150,
    )

    container_7 = ft.Container(
        content=ft.Text("C7. 1, 1.5"),
        alignment=ft.alignment.Alignment(1, 1.5),
        bgcolor=ft.Colors.BLUE_GREY_700,
        width=150,
        height=150,
    )

    container_8 = ft.Container(
        content=ft.Text("C8. -1.5, 1.5"),
        alignment=ft.alignment.Alignment(-2.5, 0),
        bgcolor=ft.Colors.BLUE_GREY_800,
        width=150,
        height=150,
    )

    container_9 = ft.Container(
        content=ft.Text("C9. -2, 2.5"),
        alignment=ft.alignment.Alignment(-2, 2.5),
        bgcolor=ft.Colors.BLUE_GREY_900,
        width=150,
        height=150,
    )

    # Sistema de Coordenadas: (x, y) donde x es el eje horizontal y y es el eje vertical
    # (0, 0) es el centro del contenedor
    # (-1, -1)  izquierda, arriba   = esquina superior izquierda
    # (-1, 0)   izquierda, centro
    # (-1, 1)   izquierda, abajo    = esquina inferior izquierda
    # (0, -1)   centro, arriba
    # (0, 0)   centro, centro
    # (0, 1)   centro, abajo
    # (1, -1)  derecha, arriba     = esquina superior derecha
    # (1, 0)  derecha, centro
    # (1, 1)  derecha, abajo      = esquina inferior derecha
    
    # Tambien acepta cualquier numero decimal entre -1 y 1, como por ejemplo, -0.5. -0.5
    # Lo cual seria un poco a la izquierda, sin tocar el borde, y un poco arriba sin llegar hasta el techo
    
    # Ademas acepta tambien valores mayores a 1 o menores a -1, 
    #   pero eso provoca que el elemento salga del contenedor

    return ft.Column([
        ft.Row(controls=[container_1, container_2, container_3]),
        ft.Row(controls=[container_4, container_5, container_6]),
        ft.Row(controls=[container_7, container_8, container_9]),
    ])


if __name__ == "__main__":
    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window.height = 700
        page.window.width = 600
        page.window.alignment = ft.alignment.center

        page.add(example())
        
    ft.app(target=main)