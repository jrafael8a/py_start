import flet as ft

def main(page):
    page.window.height = 800
    page.window.width = 500
    page.window.alignment = ft.alignment.center

    page.adaptive = True            # Esta linea le indica a flet que el programa es adaptativo

    page.appbar = ft.AppBar(        # Creamos una AppBar, que es la barra superior
        leading=ft.TextButton("New", style=ft.ButtonStyle(padding=0)),
        title=ft.Text("Adaptive AppBar"),
        actions=[
            ft.IconButton(ft.cupertino_icons.ADD, style=ft.ButtonStyle(padding=0))  # Icono de +
        ],
        bgcolor=ft.Colors.with_opacity(0.04, ft.CupertinoColors.SYSTEM_BACKGROUND),
    )

    # Luego creamos una barra de navegación, que es la barra inferior
    # Tambien existe una bottom_appbar, que tambien es una barra inferior
    # Pero si appbar y navigation_bar estan definidas, la que se mostrara sera la nanigation_bar
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explore"),    # Icono de brujula
            ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Commute"),    # Icono de cochee
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,        # Icono de Marcador
                label="Bookmark",
            ),
        ],
        border=ft.Border(
            top=ft.BorderSide(color=ft.CupertinoColors.SYSTEM_GREY2, width=0)
        ),
    )

    # Agregamos todo a la pagina
    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Checkbox(value=False, label="Dark Mode"),
                    ft.Text("First field:"),
                    ft.TextField(keyboard_type=ft.KeyboardType.TEXT),
                    ft.Text("Second field:"),
                    ft.TextField(keyboard_type=ft.KeyboardType.TEXT),
                    ft.Switch(label="A switch"),
                    ft.FilledButton(content=ft.Text("Adaptive button")),
                    ft.Text("Text line 1"),
                    ft.Text("Text line 2"),
                    ft.Text("Text line 3"),
                ]
            )
        )
    )


ft.app(main)