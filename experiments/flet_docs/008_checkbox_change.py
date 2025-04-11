import flet as ft


def main(page):
    page.window.width = 500
    page.window.height = 300
    page.window.alignment = ft.alignment.center
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    def checkbox_changed(e):
        output_text.value = (
            f"You have learned how to ski :  {todo_check.value}."
        )
        page.update()

    output_text = ft.Text()
    todo_check = ft.Checkbox(label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed)
    page.add(todo_check, output_text)

ft.app(main)