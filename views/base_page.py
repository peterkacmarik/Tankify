import flet as ft
from locales.language_manager import LanguageManager



class BaseView(ft.View):
    """Základná trieda pre všetky views s podporou viacjazyčnosti"""
    def __init__(self, route: str, page: ft.Page):
        super().__init__(route=route)
        self.page = page
        LanguageManager.add_observer(self)

    def update_language(self) -> None:
        self.update_texts()
        self.page.update()

    def update_texts(self) -> None:
        pass

    def __del__(self):
        LanguageManager.remove_observer(self)