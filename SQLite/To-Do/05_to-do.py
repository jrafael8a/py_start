import flet as ft
import sqlite3
import os

# -------------------- Variables Globales --------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_DB = os.path.join(BASE_DIR, "to-do.db")

ALTURA = 700
ANCHURA = 500

# -------------------- Base de datos --------------------

def init_db():
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0
            )
        ''')
        mi_conexion.commit()

def get_tasks():
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute("SELECT id, title, done FROM tasks ORDER BY done ASC, id DESC")
        rows = cursor.fetchall()
        return rows

def add_task(title):
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        mi_conexion.commit()

def update_done(task_id, done):
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute("UPDATE tasks SET done=? WHERE id=?", (done, task_id))
        mi_conexion.commit()

def edit_task(task_id, title):
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute("UPDATE tasks SET title=? WHERE id=?", (title, task_id))
        mi_conexion.commit()


def delete_task(task_id):
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        mi_conexion.commit()


def count_done():
    with sqlite3.connect(RUTA_DB) as mi_conexion:
        cursor = mi_conexion.cursor()
        cursor.execute('SELECT done, COUNT(*) AS cantidad FROM tasks GROUP BY done')
        resultados = cursor.fetchall()

        realizadas = 0
        no_realizadas = 0

        for done, cantidad in resultados:
            if done == 1:
                realizadas = cantidad
            elif done == 0:
                no_realizadas = cantidad
        total = realizadas + no_realizadas

        return {"realizadas": realizadas, "no_realizadas": no_realizadas, "total": total}


# -------------------- Interfaz Flet --------------------

def main(page: ft.Page):
    # ----- Estilo para la Interfaz -----
    page.theme_mode = ft.ThemeMode.DARK
    page.window.height = ALTURA
    page.window.width = ANCHURA
    page.window.alignment = ft.alignment.center
    
    page.title = "To-Do List"
    page.scroll = "auto"


    # ----- Definicion de variables -----
        # TextField de Entrada de Datos
    task_input = ft.TextField(label="Nueva tarea", expand=True)
        # Columna donde se mostraran las tareas
    task_list = ft.Column(scroll=ft.ScrollMode.ALWAYS, auto_scroll=True, expand=True)
        # TextField para el Dialogo de Edicion de Tareas
    task_editing = ft.TextField(expand=True, multiline=True)

    # ----- Funciones de GUI -----
    # Cargar Lista de Tareas
    def load_tasks():
        task_list.controls.clear()
        sumario_tareas = count_done()
        task_list.controls.append(
            ft.Row([
                ft.Text(style=ft.TextStyle(size=10),
                    value=f"Tareas pendientes:\n" \
                    f"Numero de Tareas Completadas:"),
                ft.Text(style=ft.TextStyle(size=10),
                    value=f"{sumario_tareas['no_realizadas']:^6} de {sumario_tareas['total']:^6} \n" \
                    f"{sumario_tareas['realizadas']:^20}"),
                ],
                spacing=0,
                expand=True,
                alignment=ft.MainAxisAlignment.END
            )
        )
        
        if not get_tasks():
            task_list.controls.append(ft.Text("No hay tareas todavía.", italic=True, color=ft.colors.GREY))
        else:
            for task_id, title, done in get_tasks():
                t_checkbox = ft.Checkbox(
                    # label=title,                  # Se elimina esta linea porque se agrego un ft.Text
                    value=bool(done),
                    on_change=lambda e, id=task_id: toggle_done(e, id)
                )
                t_texto = ft.Text(
                    value=title,
                    expand=True,
                    no_wrap=False,
                    max_lines=5,                        # Limita la altura a 5 lineas
                    overflow=ft.TextOverflow.ELLIPSIS   # Muestra "..." Si supera las lineas
                    )
                
                t_edit_btn = ft.IconButton(
                    icon=ft.icons.EDIT,
                    on_click=lambda e, id=task_id, title=title, done=done: btn_edit(id, title, done)
                )
                t_delete_btn = ft.IconButton(
                    icon=ft.icons.DELETE,
                    on_click=lambda e, id=task_id, title=title: btn_delete(id, title)
                )

                if done:
                    t_texto.style = ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH)     # Tacha las tareas completadas
                    t_edit_btn.icon_color = ft.colors.GREY          # Cambia el color del
                    # t_edit_btn.disabled = True
                    # t_edit_btn.visible = False

                task_list.controls.append(ft.Row([
                    t_checkbox, t_texto, t_edit_btn, t_delete_btn
                    ],
                    ))
            
            page.update()
            task_input.focus()

    # Enviar "Agregar una tarea" a la DB
    def add_clicked(e):
        if task_input.value.strip():
            add_task(task_input.value.strip())
            task_input.value = ""
            load_tasks()
            page.update()

    # Enviar "Marcar / Descarmar el chechbox" a la DB 
    def toggle_done(e, task_id):
        update_done(task_id, int(e.control.value))
        load_tasks()

    # Enviar "Eliminar Tarea" a la DB
    def btn_delete(task_id, title):
        def delete_ok(id):
            page.close(dlg_eliminar)
            delete_task(id)
            load_tasks()

        dlg_eliminar = ft.AlertDialog(
            modal=False,
            title=ft.Text("Confirmar Eliminar"),
            content=ft.Container(ft.Column([
                ft.Text(f"Va a eliminar la tarea"),
                ft.TextField(value=title, disabled=True, expand=False, max_lines=3),
                ft.Text(f"¿Está seguro de que desea proceder?")
                ]),expand=False,
                ),
            actions=[
                ft.TextButton("Yes", on_click=lambda e: delete_ok(task_id)),
                ft.TextButton("No", on_click=lambda e: page.close(dlg_eliminar))
            ],
            on_dismiss=lambda e: page.close(dlg_eliminar)
        )
        page.open(dlg_eliminar)

    # Gestionar Edicion antes de enviarlo a la DB
    def btn_edit(task_id, task_text, task_done):
        # Actualizamos el TextField de edicion.
        task_editing.value = task_text

        # Gestionamos y Validamos el Envio de Datos a la DB
        def guardar(tf_texto):
            if not tf_texto.strip():
                # page.close(dlg_edit)
                page.open(ft.SnackBar(ft.Text(
                    "El texto no puede estar vacío.\n" \
                    "Si lo que desea es Eliminar la tarea, puede hacerlo desde el boton eliminar")))
                page.update()
                return
            
            task_text = tf_texto
            page.close(dlg_edit)
            page.open(ft.SnackBar(ft.Text(f"Tarea Actualizada con Exito")))
            edit_task(task_id, task_text)
            load_tasks()
            task_input.focus()

        # Cierra un Cuadro de dialogo de confirmacion y abre el de edicion.
        def si_editar(e):
            page.close(dlg_confirm_edit)
            page.open(dlg_edit)

        # Captura la tecla ESC, para rechazar el cuadro de dialogo con ESC
        def keystroke_esc(e: ft.KeyboardEvent):
            if e.key == "Escape":
                if dlg_edit.open: page.close(dlg_edit)
                if dlg_confirm_edit.open: page.close(dlg_confirm_edit)

        # Crea un cuadro de dialogo para la edicion de la tarea.
        dlg_edit = ft.AlertDialog(
            modal=True,
            title=ft.Text("Editar Tarea"), 
            content=task_editing,
            actions=[
                ft.TextButton("Guardar", on_click=lambda e: guardar(task_editing.value)),
                ft.TextButton("Cancelar", on_click=lambda e: page.close(dlg_edit)),
            ],
            on_dismiss=lambda e: page.close(dlg_edit),
            actions_alignment=ft.MainAxisAlignment.END
        )

        # Crea un cuadro de dialogo de confirmacion para editar tareas finalizadas
        dlg_confirm_edit = ft.AlertDialog(
            modal=False,
            title=ft.Text("¿Editar Tarea Finalizada?"),
            content=ft.Text("Está tratando de editar una tarea que ya ha sido marcada como completada\n" \
            " \n" \
            "¿Está seguro que desea editarla?"),
            actions=[
                ft.TextButton("Yes", on_click=lambda e: si_editar(e)),
                ft.TextButton("No", on_click=lambda e: page.close(dlg_confirm_edit))
            ],
            on_dismiss=lambda e: page.close(dlg_confirm_edit),
            actions_alignment=ft.MainAxisAlignment.END
        )

        # Llama a nuestra funcion keystroke con cada pulsacion de teclas
        page.on_keyboard_event = keystroke_esc
        
        # Si la tarea esta marcada como completada (done) llama al cuadro de confirmacion
        # para alertarnos que estamos a punto de editar una tarea ya finalizada.
        # Pero si no esta marcada como done, entonces directamente llama al dialogo de edicion
        page.open(dlg_confirm_edit) if task_done else page.open(dlg_edit)    


    # ----- Construccion de la Intefaz de Usuario -----
    page.add(
        ft.Text(value="To-Do | Organizador de Tareas",
                style=ft.TextStyle(
                    size=30,
                    font_family='Arial',
                    weight='w600'
                ),
                text_align='center'),
        ft.Row([task_input, ft.ElevatedButton("Agregar", on_click=add_clicked)]),
        task_list
    )
    task_input.on_submit = add_clicked      # Permite agregar la tarea al pulsar ENTER
    # task_input.focus()                      # Enfoca el TextField de insercion.
    
    init_db()                               # Inicializa la Base de Datos
    load_tasks()                            # Carga toda la lista de tareas
    
    

# -------------------- Corremos nuestra aplicacion --------------------
ft.app(target=main)                                 # Ejecuta la Aplicacion de Escritorio
# ft.app(main, view=ft.AppView.WEB_BROWSER)         # Ejecuta la Aplicacion en Web