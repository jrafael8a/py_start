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
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),  # Botón que al hacer clic navega a la ruta "/store".
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
ft.app(main, view=ft.AppView.WEB_BROWSER)


# Análisis y notas sobre el código original:

# 1. **Lógica de navegación (route_change):**
#    - Cada vez que cambia la URL (por ejemplo, de "/" a "/store"), el evento `on_route_change` se dispara.
#    - Se elimina la vista actual con `page.views.clear()` y se agrega una nueva vista correspondiente a la ruta.
#    - Esto garantiza que solo se muestre la vista actual, pero también elimina cualquier vista anterior, 
#       lo cual puede no ser ideal en aplicaciones más grandes, ya que implica crear las vistas desde cero cada vez 
#       que la URL cambia.
#    - **Posible inconveniente:** Esto puede ser ineficiente si se tienen muchas vistas o si la vista requiere 
#       ser reconstruida frecuentemente.

# 2. **Comportamiento de la flecha en el AppBar:**
#    - La flecha hacia atrás (en el AppBar) aparece automáticamente cuando hay más de una vista en la pila de vistas.
#    - Flet maneja este comportamiento por defecto, y al presionar la flecha se dispara el evento `on_view_pop`, 
#       lo que normalmente debería eliminar la vista actual y volver a la vista anterior.
#    - **Curiosidad:** Si se comenta la línea `page.on_view_pop = view_pop`, la flecha no funcionará como se espera. 
#       Esto ocurre porque sin el manejador `on_view_pop`, Flet no sabe cómo manejar el retroceso de vista y, 
#       por lo tanto, la flecha no tiene un efecto.

# 3. **Eventos `on_route_change` y `on_view_pop`:**
#    - `on_route_change` es un evento que se activa cuando cambia la ruta (cuando la URL cambia). 
#       Se usa para actualizar las vistas y realizar otras acciones cuando el usuario navega entre páginas.
#    - `on_view_pop` es un evento que se activa cuando se elimina una vista de la pila, generalmente al retroceder 
#       (como al presionar la flecha de retroceso en el AppBar). Si no se asigna un manejador para este evento, 
#       Flet usará su comportamiento predeterminado, que debería funcionar en la mayoría de los casos.
#    - **Curiosidad:** Aunque Flet tiene un comportamiento predeterminado para el retroceso de vistas, 
#       al comentar la línea `page.on_view_pop = view_pop`, la flecha deja de funcionar. 
#       Esto indica que la asignación manual de este evento influye en cómo se maneja el retroceso y la pila de vistas.

# 4. **Comportamiento inesperado al comentar `page.views.clear()`:**
#    - Al comentar la línea `page.views.clear()`, la pila de vistas no se limpia, 
#       lo que significa que las vistas se acumulan.
#    - Esto provoca que la flecha de retroceso aparezca desde el principio (ya que la vista principal nunca se elimina) 
#       y puede causar problemas de navegación, como redirecciones múltiples o navegación incorrecta entre vistas.
#    - **Posible solución:** Evitar que se acumulen vistas innecesarias y solo agregar la vista correspondiente 
#       a la ruta actual, sin duplicarla.

# 5. **Comportamiento de la pila de vistas:**
#    - Flet mantiene una pila de vistas (por ejemplo, cuando navegas de "/" a "/store").
#    - La eliminación de vistas con `page.views.clear()` limpia la pila y asegura que solo se muestre la vista actual. 
#       Sin embargo, esto también puede interferir con la pila de navegación y afectar la funcionalidad de la flecha de retroceso.
#    - **Curiosidad:** Si no se controla correctamente el manejo de las vistas (como evitar agregar vistas duplicadas), 
#       se pueden generar problemas de navegación, como redirecciones inesperadas o la aparición de vistas redundantes.

# 6. **Sugerencia de manejo eficiente de rutas:**
#    - En aplicaciones grandes, recrear todas las vistas cada vez que cambia la ruta no es eficiente. 
#       Sería mejor mantener las vistas en memoria y solo actualizar las partes necesarias de la interfaz.
#    - **Optimización:** Usar un enrutador que administre mejor la pila de vistas y actualice solo 
#       los elementos necesarios en lugar de recrear todas las vistas al cambiar la ruta.
