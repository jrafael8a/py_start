import flet as ft

def main(page: ft.Page):
    page.window.width = 300
    page.window.height = 300
    page.window.alignment = ft.alignment.center
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    page.bgcolor = ft.Colors.WHITE12

    def button_clicked(e):
        output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=120,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
        
        color='green',
        bgcolor='red'
    )
    page.add(color_dropdown, submit_btn, output_text)

ft.app(main)