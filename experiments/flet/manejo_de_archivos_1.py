import flet as ft

def archivos(page: ft.Page):
    page.title = "Lector de Archivos"
    page.scroll = "auto"

    texto_archivo = ft.TextField(multiline=True, expand=True, label="Contenido del archivo", on_change=lambda e: actualizar_contador())
    contador = ft.Text("Líneas: 0 | Caracteres: 0")
    
    # Creamos el FilePicker y lo añadimos a la página
    file_picker_abrir = ft.FilePicker()
    file_picker_guardar = ft.FilePicker()
    page.overlay.append(file_picker_abrir)
    page.overlay.append(file_picker_guardar)


    def actualizar_contador():
        texto = texto_archivo.value
        lineas = texto.count("\n") + 1 if texto else 0
        caracteres = len(texto)
        contador.value = f"Líneas: {lineas} | Caracteres: {caracteres}"
        contador.update()

    def actualizar_todo():
        texto_archivo.focus()
        actualizar_contador()
        page.update()
    
    # Función cuando se selecciona un archivo para abrir
    def on_archivo_seleccionado(e: ft.FilePickerResultEvent):
        if e.files:
            try:
                with open(e.files[0].path, "r", encoding="utf-8") as my_file:
                    texto_archivo.value = my_file.read()
                    
            except Exception as err:
                texto_archivo.error_text = f"Error al abrir el archivo: {err}"
                page.open(ft.AlertDialog(
                    modal=False,
                    title=ft.Text("Error al abrir el archivo"),
                    content=ft.Text("Este programa solamente puede abir archivos de texto.\n\n" \
                    "Por favor seleccione un archivo de texto."),
                ))
        actualizar_todo()

    # Función cuando se selecciona ubicación para guardar
    def on_guardar_archivo(e: ft.FilePickerResultEvent):
        if e.path:
            path = e.path
            if not path.lower().endswith(".txt"):
                path += ".txt"

            try:
                with open(path, "w", encoding="utf-8") as my_file:
                    my_file.write(texto_archivo.value)
                texto_archivo.value = ""
                page.open(ft.SnackBar(content=ft.Text("El archivo se guardó correctamente")))
            except Exception as err:
                texto_archivo.error_text = f"Error al guardar el archivo: {err}"
                page.open(ft.AlertDialog(
                        modal=False,
                        title=ft.Text("Error al guardar el archivo"),
                        content=ft.Text("No se ha podido guardar el archivo"),
                    ))
        actualizar_todo()

    def cerrar_archivo():
        page.close(dl_cerrar)
        texto_archivo.value = ""
        actualizar_todo()

    dl_cerrar=ft.AlertDialog(
            title=ft.Text("Desea Cerrar el Archivo?"),
            content=ft.Text("Está a punto de cerrar el archivo sin guardar los cambios.\n" \
            "Todos los cambios sin guardar se perderán.\n\n" \
            "Está seguro que desea cerrar sin guardar los cambios?"),
            actions=[
                ft.ElevatedButton("Cerrar sin Guardar", on_click=lambda e: cerrar_archivo()),
                ft.ElevatedButton("Cancelar", on_click=lambda e: page.close(dl_cerrar)),
                ],
            on_dismiss=lambda e: page.close(dl_cerrar)
        )
    
    

    
    file_picker_abrir.on_result = on_archivo_seleccionado
    file_picker_guardar.on_result = on_guardar_archivo

    # Botones
    boton_abrir = ft.ElevatedButton(
        text="📂 Abrir archivo",
        on_click=lambda e: file_picker_abrir.pick_files(allow_multiple=False)
    )

    boton_guardar = ft.ElevatedButton(
        text="💾 Guardar archivo",
        on_click=lambda e: file_picker_guardar.save_file()
    )

    boton_cerrar = ft.ElevatedButton(
        text="✖️ Cerrar archivo",
        on_click=lambda e: page.open(dl_cerrar)
    )

    # Añadir elementos a la página
    page.add(
        ft.Row([boton_abrir, boton_guardar, boton_cerrar]),
        contador,
        texto_archivo,
    )
    texto_archivo.focus()

if __name__ == "__main__":
    ft.app(target=archivos)

# ✅ TL;DR  PAGE.OVERLAY
# ¿Qué es? page.overlay 
# es una lista de controles invisibles (como FilePicker) 
# 
# ¿Por qué se usa?
# Para registrar controles que no van en el layout principal
# 
# ¿Qué pasa si no lo uso?
# ⚠️ Error: "Control must be added to the page first"
# 
# ¿Qué tipo de controles van?
# Diálogos, pickers, notificaciones, etc.