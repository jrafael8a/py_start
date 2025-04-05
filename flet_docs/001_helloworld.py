import flet as ft
import time

def main(page: ft.Page):
    page.window.height = 400
    page.window.width = 600
    page.window.alignment = ft.alignment.center

    t = ft.Text(value="Hello, world!", color="green")
    t.text_align=ft.TextAlign.CENTER
    page.controls.append(t)
    page.update()


    t = ft.Text()
    page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()

    # Se pueden modificar controles, y la interfas se actualizara en el siguienre papge.update()
    for i in range(5, 0, -1):
        t.value = f"Wait for it  {i:02d}..."
        # page.update()     # En lugar de actualizar toda la pagina podemos actualizar solo un elemento
        t.update()
        time.sleep(0.2)

    # Esta fila se agregara DESPUES de que termine el for de arriba de imprimir todos los numeros
    filita = ft.Row(controls=[
            ft.Text("A"), 
            ft.Text("B"),
            ft.Text("C")
        ])
    filita.alignment = ft.alignment.center
    page.add(
        filita
    )

    # Puedo agregar pausas entre page.add() para que no se muestre todo de una sola vez
    time.sleep(1)
    
    # Aqui tenemos un boton elevado
    textbox2 = ft.TextField(label="EL NOMBRE!!!", text_align=ft.TextAlign.CENTER)
    
    page.add(
        ft.Row(controls=[
            textbox2,
            ft.ElevatedButton(text="DEME EL MALDITO NOMBRE!")
        ])
    )

    # El page.update() es lo suficientemente listo para idetificar solo los cambios
    # que es han realizado y actualizar eso controles especificos

    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0)        # Elimina el primer control 
        page.update()
        time.sleep(0.1)

    # page.controls.pop(0) 
    # Esta linea hace lo siguiente:
    # page.controls contiene una lista con todos los controles de la pagina
    # el metodo pop() eliminan elementos de una lista
    # al pasarle el parametro 0 pop(0), lo que hara es eliminar el primer elemento de la lista
    # Esto significa que eliminara  
    #   el Hello World, 
    #   el Wait for it, 
    #   el A  B  C
    #   Y la fila de la caja de texto y el boton.


    # Ahora veamos los eventos
    def button_clicked(e):
        page.add(ft.Text("Yamete Kudasai ! ! !"))

    page.add(ft.ElevatedButton(text="Touch me 😏", on_click=button_clicked))
    page.add(ft.Button(text="Touch me 😏", on_click=button_clicked))





ft.app(main)