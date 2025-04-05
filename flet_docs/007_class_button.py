import flet as ft 

#           Styled controls
# The most simple custom control you can create is a styled control, for example, a button 
# of a certain color and behaviour that will be used multiple times throughout your app.

# To create a styled control, you need to create a new class in Python that inherits from the Flet control 
# you are going to customize, ElevatedButton in this case:

class MyButton(ft.ElevatedButton):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.bgcolor = ft.Colors.ORANGE_300     #Sobre escribira lo que se le haya pasado por **kwargs
        self.color = ft.Colors.GREEN_800
        self.text = text
        
        # super().__init__(**kwargs) pasa esos parámetros a ft.ElevatedButton, 
        # que es la clase base de MyButton. Esto permite que ft.ElevatedButton 
        # reciba y maneje esos parámetros como si los hubieras pasado directamente a su constructor.

# Your control has a constructor to customize properties and events and pass custom data. 
# Note that you must call super().__init__() in your own constructor to have access to the properties and methods of the Flet control from which you inherit.


#Now you can use your brand-new control in your app:

def main(page: ft.Page):

    def ok_clicked(e):
        print("OK clicked")
    
    def cancel_clicked(e):
        print("Cancel clicked")

    page.add(
        MyButton("OK", on_click=ok_clicked, bgcolor=ft.Colors.RED_400),
        MyButton("Cancel", on_click=cancel_clicked),
    )

ft.app(main)

# En resumen, si voy a usar varios botones (como en este ejemplo) 
# Creo una clase, en la que le pongo el estilo que yo quiero.           class MyButton(ft.ElevatedButton):
# Recibira como parametros un texto, y lo demas que yo quiera           def __init__(self, text, **kwargs):
# pasara todos los argumentos adicionales al boton nuevo                super().__init__(**kwargs)
# pero