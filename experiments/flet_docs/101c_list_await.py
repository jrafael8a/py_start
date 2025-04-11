import flet as ft
import asyncio

async def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.height = 400
    page.window.width = 600
    page.window.alignment = ft.alignment.center

    mi_columna = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS, spacing=10)
    async def contenido():
        
        for i in range (50000+1):
            mi_columna.controls.append(ft.Text(f"Item {i}"))
            if i % 100 == 0:
                mi_columna.update()

    page.add(mi_columna)
    
    await contenido()
    
ft.app(main)
