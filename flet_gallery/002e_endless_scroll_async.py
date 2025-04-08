import flet as ft
import asyncio

mi_contador = 0  # Variable global

async def long_running_task():
    global mi_contador
    for i in range(1):
        mi_contador += 1
        cl.controls.append(ft.Text(f"Text line {mi_contador}", key=str(mi_contador)))
    cl.update()

# Función que se ejecuta cuando se hace scroll
async def on_scroll(e: ft.OnScrollEvent):
    if e.pixels >= e.max_scroll_extent - 100:
        await long_running_task()

# Crear la columna principal con la función de scroll
def example():
    global mi_contador
    global cl
    cl = ft.Column(
        spacing=10,
        height=200,
        width=200,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
        on_scroll=on_scroll,
    )
    
    for i in range(50):
        cl.controls.append(ft.Text(f"Text line {mi_contador}", key=str(mi_contador)))
        mi_contador += 1

    return ft.Container(cl, border=ft.border.all(1))


if __name__ == "__main__":
    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window.height = 400
        page.window.width = 600
        page.window.alignment = ft.alignment.center

        page.add(example())
        
    ft.app(target=main)