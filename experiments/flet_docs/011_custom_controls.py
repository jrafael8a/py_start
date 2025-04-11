import flet as ft

class AdaptiveNavigationBarDestination(ft.NavigationBarDestination):
    def __init__(self, ios_icon, android_icon, label):
        super().__init__()
        self._ios_icon = ios_icon
        self._android_icon = android_icon
        self.label = label

    def build(self):
        # we can check for platform in build method because self.page is known
        self.icon = (
            self._ios_icon
            if self.page.platform == ft.PagePlatform.IOS
            or self.page.platform == ft.PagePlatform.MACOS
            else self._android_icon
        )

# from adaptive_navigation_destination import AdaptiveNavigationBarDestination

def main(page):
    page.window.height = 400
    page.window.width = 600
    page.window.alignment = ft.alignment.center

    page.adaptive = True

    page.navigation_bar = ft.NavigationBar(
        selected_index=2,
        destinations=[
            AdaptiveNavigationBarDestination(
                ios_icon=ft.cupertino_icons.PERSON_3_FILL,
                android_icon=ft.Icons.PERSON,
                label="Contacts",
            ),
            AdaptiveNavigationBarDestination(
                ios_icon=ft.cupertino_icons.CHAT_BUBBLE_2,
                android_icon=ft.Icons.CHAT,
                label="Chats",
            ),
            AdaptiveNavigationBarDestination(
                ios_icon=ft.cupertino_icons.SETTINGS,
                android_icon=ft.Icons.SETTINGS,
                label="Settings",
            ),
        ],
    )

    page.update()


ft.app(main)

# Esta pagina mostrata una barra de navegacion adaptativa, 
# que cambia el icono dependiendo del sistema operativo
# Si es iOS/MacOS Mostrara los iconos de Cupertino (IOS/Apple) o
# Si es Android/Windows/Linux mostara los iconos de Material Design (Android/Google)