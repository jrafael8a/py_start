import flet as ft


def main(page: ft.Page):
    page.window.width = 600
    page.window.height = 600
    page.window.alignment = ft.alignment.center
    page.horizontal_alignment = 'center'
    # page.vertical_alignment = 'center'


    page.title = "AlertDialog examples"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    dlg = ft.AlertDialog(
        title=ft.Text("Hi, this is a non-modal dialog!"),
        on_dismiss=lambda e: page.add(ft.Text("Non-modal dialog dismissed")),
    )

    def handle_close(e):
        dlg_modal.close()
        page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to delete all those files?"),
        actions=[
            ft.TextButton("Yes", on_click=handle_close),
            ft.TextButton("No", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(
            ft.Text("Modal dialog dismissed"),
        ),
    )

    page.add(
        ft.ElevatedButton("Open dialog", on_click=lambda e: dlg.open()),  # Abre el diálogo no modal
        ft.ElevatedButton("Open modal dialog", on_click=lambda e: dlg_modal.open()),  # Abre el diálogo modal
    )


ft.app(main)