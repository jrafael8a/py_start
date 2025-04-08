import flet as ft

name = "Card example"


def example():
    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.ALBUM),
                        title=ft.Text("The Enchanted Nightingale"),
                        subtitle=ft.Text(
                            "Music by Julie Gable. Lyrics by Sidney Stein."
                        ),
                    ),
                    ft.Row(
                        [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )

# A partir del codigo de Github, solo se agrega esto para que este modulo pueda correr por si solo
# Primero nos aseguramos de que el modulo se ejecute como un script independiente y no como modulo importado
# Luego agregamos la funcion example() a la pagina y la ejecutamos con el ft.app(main)

if __name__ == "__main__":
    def main(page: ft.Page):
        page.window.height = 400
        page.window.width = 600
        page.window.alignment = ft.alignment.center

        page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)
        page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE)
        page.add(example())
        
        
        
    ft.app(target=main)