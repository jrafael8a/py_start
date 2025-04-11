import flet as ft

name = "Scrolling column programmatically"

def example():
    cl = ft.Column(
        spacing=10,
        height=200,
        # width=float("inf"),
        width=200,
        scroll=ft.ScrollMode.ALWAYS,
    )

    # Creamos una lista de 100 elementos de texto
    for i in range(0, 100):
        cl.controls.append(ft.Text(f"Text line {i}", key=str(i)))

    # Esta funcion hace scroll hasta la posicion offset 100, qu eson 100 pixeles desde el inicio de la columna
    def scroll_to_offset(e):
        cl.scroll_to(offset=100, duration=100)

    # Esta funcion hace scroll hasta el inicio de la columna
    # Podemos modificar cuanto tiempo tardara en hacer el scroll con el parametro duration en milisegundos
    def scroll_to_start(e):
        cl.scroll_to(offset=0, duration=10000, curve=ft.AnimationCurve.SLOW_MIDDLE)

    # Esta funcion hace scroll hasta el final de la columna con una animacion de aceleracion
    def scroll_to_end(e):
        cl.scroll_to(offset=-1, duration=10000, curve=ft.AnimationCurve.EASE_IN_OUT)
    # curve=ft.AnimationCurve.EASE_IN_OUT define la curva de aceleracion del scroll
    # Ease_In: Al inicio de la animación, la velocidad es más lenta
    # Ease_Out: Al final de la animación, la velocidad también disminuye
    # Ease_In_Out: La velocidad es lenta al inicio, acelera a mediacion y vuelve a disminuir al final
    # SLOW_MIDDLE: La velocidad es rapida al inicio, casi se detiene al medio, y vuelve a acelerar hasta el final


    def scroll_to_delta(e):
        cl.scroll_to(delta=500, duration=200)

    def scroll_to_minus_delta(e):
        cl.scroll_to(delta=-500, duration=200)

    return ft.Column(
        [
            ft.Container(cl, border=ft.border.all(1)),
            ft.ElevatedButton("Scroll to offset 100", on_click=scroll_to_offset),
            ft.Row(
                [
                    ft.ElevatedButton("Scroll to start", on_click=scroll_to_start),
                    ft.ElevatedButton("Scroll to end", on_click=scroll_to_end),
                ]
            ),
            ft.Row(
                [
                    ft.ElevatedButton("Scroll -500", on_click=scroll_to_minus_delta),
                    ft.ElevatedButton("Scroll +500", on_click=scroll_to_delta),
                ]
            ),
        ]
    )


if __name__ == "__main__":
    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window.height = 400
        page.window.width = 600
        page.window.alignment = ft.alignment.center

        page.add(example())
        
    ft.app(target=main)