import flet as ft
from reportlab.pdfgen import canvas                 # Importamos Canvas, para "dibujar" nuestro PDF
from reportlab.lib.pagesizes import LETTER          # Importamos el tamaño de papel
from reportlab.lib.utils import simpleSplit         # Importamos una funcion para dividir lineas
import os                                           # Si queremos trabajar rutas
from platformdirs import user_downloads_dir         # Permite acceder a la ruta de la carpeta de descargas. Es Multiplataforma
import sys                                          # Para detectar que sistema estamos usando
import subprocess                                   # Para Abrir el PDF si estamos en macOS o Linux
import datetime


def archivos(page: ft.Page):
    page.title = "Lector de Archivos"
    page.scroll = "auto"

    texto_archivo = ft.TextField(multiline=True, expand=True, label="Contenido del archivo", on_change=lambda e: actualizar_contador())
    contador = ft.Text("Líneas: 0 | Caracteres: 0")
    buscar_input = ft.TextField(label="Buscar", width=200)
    boton_buscar = ft.ElevatedButton("Buscar", on_click=lambda e:buscar_texto())
    boton_tema = ft.IconButton(icon=ft.Icons.DARK_MODE, on_click=lambda e: cambiar_tema())
    boton_exportar = ft.ElevatedButton("📄 Exportar a PDF", on_click=lambda e: exportar_pdf())
    ancho_pag, alto_pag = LETTER
    ruta_archivo_actual = None  

    # Creamos el FilePicker y lo añadimos a la página
    file_picker_abrir = ft.FilePicker()
    file_picker_guardar = ft.FilePicker()
    page.overlay.append(file_picker_abrir)
    page.overlay.append(file_picker_guardar)
    
    # Boton Cambiar Tema
    boton_tema = ft.IconButton(icon=ft.Icons.DARK_MODE, on_click=lambda e: cambiar_tema())
    def cambiar_tema():
        if page.theme_mode != ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.DARK
            boton_tema.icon=ft.Icons.LIGHT_MODE
        else: 
            page.theme_mode = ft.ThemeMode.LIGHT
            boton_tema.icon=ft.Icons.DARK_MODE
        page.update()

    # Funcion para exportar como PDF
    def exportar_pdf():
        texto = texto_archivo.value
        if not texto:
            page.open(ft.SnackBar(ft.Text("Nada que exportar")))
            return

        # Guardamos la ruta donde se alojara nuestro PDF
        # pdf_path = os.path.join(os.environ["USERPROFILE"], "Downloads", "texto_exportado.pdf")
        # Usamos os.environ para obtener la variable de entorno USERPROFILE de Windows
        # Y luego solo le concatenamos la carpeta de descargas y el nombre que deseamos.

        # De esta forma se vuelve multiplataforma:          # ✅ multiplataforma
        downloads_dir = user_downloads_dir()
        pdf_path = os.path.join(downloads_dir, "texto_exportado.pdf")

        c = canvas.Canvas(pdf_path, pagesize=LETTER)
        y = alto_pag - 50                       # 50 px de margen superior
        max_line_width = ancho_pag -100         # 50 px de margen a cada lado

        for linea in texto.splitlines():
            if linea.strip() == "":
                y -= 15
            else:
                # Divide la linea si es muy larga
                lineas_divididas = simpleSplit(linea, "Helvetica", 12, max_line_width)

                for sublinea in lineas_divididas:
                    c.drawString(50, y, sublinea)
                    y -= 15
                    if y < 100:                 # 100 px de margen inferior
                        c.showPage()            # Crea una nueva pagina
                        y = alto_pag - 50       # Vuelve al principio de la pagina con un margen de 50px
        c.save()
        page.open(ft.SnackBar(ft.Text(f"PDF exportado como {pdf_path}")))
        abrir_archivo(pdf_path)

    # Funcion para abrir el pdf despues de crearlo
    def abrir_archivo(path):
        if sys.platform.startswith("win"):
            os.startfile(path)                      # ✅ Windows
        elif sys.platform.startswith("darwin"):
            subprocess.run(["open", path])          # ✅ macOS
        else:
            subprocess.run(["xdg-open", path])      # ✅ Linux


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

    def buscar_texto():
        texto = texto_archivo.value
        buscar = buscar_input.value
        if buscar:
            if buscar in texto:
                index = texto.find(buscar)
                texto_archivo.focus()
                texto_archivo.cursor_position = index + len(buscar)
                page.open(ft.SnackBar(ft.Text(f'"{buscar}" encontrado')))
            else:
                page.open(ft.SnackBar(ft.Text(f'"{buscar}" no encontrado')))
        else:
            page.open(ft.SnackBar(ft.Text("Ingrese texto para buscar")))


    # Función cuando se selecciona un archivo para abrir
    def on_archivo_seleccionado(e: ft.FilePickerResultEvent):
        if e.files:
            ruta_archivo_actual = e.files[0].path
            try:
                with open(ruta_archivo_actual, "r", encoding="utf-8") as my_file:
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
        global ruta_archivo_actual
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
        ruta_archivo_actual = None
        actualizar_todo()

    def cerrar_archivo():
        global ruta_archivo_actual
        page.close(dl_cerrar)
        texto_archivo.value = ""
        ruta_archivo_actual = None
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
    
    def auto_guardar(e):
        if ruta_archivo_actual:
            with open(ruta_archivo_actual, "w", encoding="utf-8") as f:
                f.write(texto_archivo.value)
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            page.open(ft.SnackBar(ft.Text(f"Guardado automático a las {ahora}")))


    
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
        ft.Row([boton_tema, boton_abrir, boton_guardar, boton_cerrar, buscar_input, boton_buscar, boton_exportar]),
        contador,
        texto_archivo,
    )
    texto_archivo.focus()

    auto_guardar_timer = ft.Timer(interval=10, on_tick=auto_guardar, repeat=True)
    page.overlay.append(auto_guardar_timer)
    auto_guardar_timer.start()

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