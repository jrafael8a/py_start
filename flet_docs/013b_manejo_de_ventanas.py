import flet as ft  # Importa la librería Flet para crear la interfaz gráfica.

def main(page: ft.Page):  # Función principal que recibe un objeto `page`, que representa la página de la app.
    page.title = "Routes Example"  # Establece el título de la página.

    # Define la función para manejar los cambios de ruta en la aplicación.
    def route_change(route):
        # page.views.clear()  # Elimina todas las vistas actuales de la página.

        # Agrega una vista de inicio ("/").
        page.views.append(
            ft.View(
                "/",  # Ruta de esta vista.
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),  # Barra superior con título.
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.launch_url("/store")),  # Botón que al hacer clic navega a la ruta "/store".
                ],
            )
        )
        
        # Si la ruta es "/store", muestra la vista de la tienda.
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",  # Ruta para la vista de la tienda.
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),  # Barra superior con título "Store".
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),  # Botón que al hacer clic navega a la ruta "/".
                    ],
                )
            )
        
        page.update()  # Actualiza la página para reflejar los cambios realizados en las vistas.

    # Define la función que maneja cuando se elimina una vista.
    def view_pop(view):
        # print(f"View popped: {page.route}")  # Imprime en la consola la ruta de la vista eliminada.
        # page.add(ft.Text(f"New route: {page.route}"))
        page.views.pop()  # Elimina la vista actual.
        top_view = page.views[-1]  # Obtiene la vista superior después de eliminar la actual.
        page.go(top_view.route)  # Navega hacia la ruta de la vista superior.

    page.on_route_change = route_change  # Asocia la función `route_change` al evento de cambio de ruta.
    page.on_view_pop = view_pop  # Asocia la función `view_pop` al evento de eliminación de vista.
    page.go(page.route)  # Navega a la ruta actual al cargar la página.

# Inicia la aplicación web utilizando Flet y la función `main` como punto de entrada.
ft.app(main)

