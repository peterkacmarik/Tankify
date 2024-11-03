import flet as ft
from components.links_separator_text import home_page_box
from core.page_classes import LanguageSwitcher
from locales.language_manager import LanguageManager
from views.base_page import BaseView


class HomeView(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__(route="/", page=page)
        self.page = page
        self.lang_manager = LanguageManager()
        
        self.language_switch_button = LanguageSwitcher(self.page).language_switch_button
        self.home_page_box = home_page_box(self.page)

        # Pridanie komponentov do hlavnej časti stránky
        self.controls = [
            ft.Container(
                # border=ft.border.all(5, ft.colors.BLACK),
                alignment=ft.alignment.center,
                padding=ft.padding.only(20, 30, 20, 0),
                content=ft.Column(
                    controls=[
                        self.language_switch_button,
                        self.home_page_box,
                    ]
                )
            )
        ]
    
    def update_texts(self) -> None:
        # Aktualizácia textov v settings view
        # self.home_page_box.content.controls.controls.content.controls.value = LanguageManager.get_text("home_personal_use_desc")
        
        self.update()
    
    
    def handle_home_page(self):
        pass
    