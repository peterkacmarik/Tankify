import flet as ft

from components.buttons import floating_action_button
from components.navigations import app_bar, navigation_bottom_bar, left_drawer
from core.page_classes import ManageDialogWindow
from locales.language_manager import LanguageManager
from views.base_page import BaseView


class SettingsView(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__("/settings/general", page)
        self.page = page
        self.lang_manager = LanguageManager()
        
        self.appbar = app_bar(self.page)
        
        self.page.drawer = left_drawer(self.page)
        self.drawer = self.page.drawer
        
        self.navigation_bar = navigation_bottom_bar(self.page)
        
        self.dialog_window = ManageDialogWindow(self.page).dialog_window
        self.floating_action_button = floating_action_button(self.dialog_window)
        self.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
                
        self.controls = [
            ft.Container(
                alignment=ft.alignment.center,
                padding=ft.padding.only(20, 30, 20, 0),
                content=ft.Column(
                    controls=[
                        
                    ]
                )
            ),
        ]

    def update_texts(self) -> None:
        # Aktualizácia textov v settings view
        self.title_text.value = LanguageManager.get_text("intro_texto_05")
        self.update()
        
