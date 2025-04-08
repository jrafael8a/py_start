import flet as ft

def main(page: ft.Page):
    page.window.height = 400
    page.window.width = 600
    page.window.alignment = ft.alignment.center

    scroll_container = ft.Column(scroll=True, expand=True)

    def on_keyboard(e: ft.KeyboardEvent):
        respuesta = ""
        if (e.ctrl):    respuesta += "Ctrol "
        if e.shift:     respuesta += "Shift "
        if e.alt:       respuesta += "Alt "
        if e.meta:      respuesta += "Meta "
        respuesta += e.key

        scroll_container.controls.append(ft.Text(respuesta))
        page.scroll_to(scroll_container.controls[-1])
        # f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
        page.update()

    page.on_keyboard_event = on_keyboard

    page.add(
        ft.Text("Press any key with a combination of CTRL, ALT, SHIFT and META keys...")
    )
    page.add(scroll_container)
    

ft.app(main)