# ListView es un widget que te permite mostrar listas de elementos de manera ordenada.
# Es preferible usar ListView en lugar de Column o Row para listas largas,
# ya que ListView es mas eficiente y permite desplazamiento.

# Ejemplo de un ListView con 5000 elementos
# 
import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.height = 400
    page.window.width = 600
    page.window.alignment = ft.alignment.center

    mi_list_view = ft.ListView(expand=True, spacing=10)

    # Crear una lista de elementos
    items = [ft.Text(f"Item {i}") for i in range(50000)]     # Buble for compacto para Crear 5000 elementos de texto
    mi_list_view.controls.extend(items)                     # extend en lugar de append

    # Agregar el ListView a la página
    page.add(mi_list_view)

ft.app(main)


# NOTA:
# El método extend es una función en Python que se usa para agregar múltiples elementos a una lista 
# o cualquier objeto iterable. A diferencia de append, que solo agrega un único elemento al final de la lista, 
# extend toma un iterable (como otra lista, un conjunto o una tupla) 
# y agrega cada uno de sus elementos individualmente a la lista original.