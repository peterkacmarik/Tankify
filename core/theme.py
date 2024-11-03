import flet as ft

class BgColor(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.light_bgcolor = ft.colors.WHITE
        self.dark_bgcolor = "#2e3b4e"
    
    def get_background_color(self):
        return self.light_bgcolor if self.page.theme_mode == ft.ThemeMode.LIGHT else self.dark_bgcolor