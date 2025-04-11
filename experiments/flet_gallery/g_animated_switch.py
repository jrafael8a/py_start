import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.height = 300
    page.window.width = 300
    page.window.alignment = ft.alignment.center

    c1 = ft.Container(
        ft.Text("Hello!", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.Colors.GREEN,
    )
    c2 = ft.Container(
        ft.Text("Bye!", size=50),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.Colors.YELLOW,
    )
    c = ft.AnimatedSwitcher(
        c1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=5000,                                      # Duracion de la trancicion de entrada
        reverse_duration=5000,                              # Duracion de la trancicion de salida
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,       # Rebota al terminar de entrar
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,       # Rebota al termianr de salir
    )

    def animate(e):
        c.content = c2 if c.content == c1 else c1
        c.update()

    page.add(
        c,
        ft.ElevatedButton("Animate!", on_click=animate),
    )

ft.app(main)