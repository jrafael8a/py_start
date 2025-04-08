import flet as ft
import threading                # Importando la libreria threading para el uso de semaforos

name = "Infinite scroll list"
mi_contador = 0                 # Variable Global para llevar el conteo de las lineas

def example():
    global mi_contador          # Aqui le digo a python que voy a usar la variable global mi_contador
    

    sem = threading.Semaphore()

    def on_scroll(e: ft.OnScrollEvent):
        if e.pixels >= e.max_scroll_extent - 100:
            if sem.acquire(blocking=False):
                try:
                    for i in range(0, 100):
                        global mi_contador
                        cl.controls.append(ft.Text(f"Text line {mi_contador}", key=str(mi_contador)))
                        mi_contador += 1
                        # time.sleep(1)
                    cl.update()
                finally:
                    sem.release()

    cl = ft.Column(
        spacing=10,
        height=200,
        width=200,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
        on_scroll=on_scroll,
    )
    for i in range(0, 50):
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