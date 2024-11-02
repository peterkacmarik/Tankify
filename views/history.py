import flet as ft
from components.buttons import floating_action_button
from components.navigations import app_bar, navigation_bottom_bar, left_drawer
from core.page_classes import BgColor, ManageDialogWindow
from locales.language_manager import LanguageManager

from supabase import Client
from core.supa_base import get_supabese_client
from views.base_page import BaseView


class HistoryView(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__("/history", page)
        self.page = page
        self.lang_manager = LanguageManager()

        self.bgcolor = BgColor(self.page).get_background_color()
        
        self.scroll = ft.ScrollMode.HIDDEN
        self.fullscreen_dialog = True
        
        self.appbar = app_bar(self.page, self.switch_theme)
        self.drawer = left_drawer(self.handle_change_drawer)
        self.navigation_bar = navigation_bottom_bar(self.handle_change_bottom_nav)
        
        self.dialog_window = ManageDialogWindow(self.page).dialog_window
        self.floating_action_button = floating_action_button(self.dialog_window)
        self.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
        
        self.snack_bar = ft.SnackBar(
            content=ft.Text(""),
            show_close_icon=True
        )
        self.page.overlay.append(self.snack_bar)
        
        self.controls = [
            ft.Container(
                alignment=ft.alignment.center,
                padding=ft.padding.only(20, 30, 20, 0),
                content=ft.Column(
                    controls=[
                        
                    ]
                )
            )
        ]
        
    
    def switch_theme(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        self.update_theme()  # Aktualizácia pozadia pre nový režim
        self.page.update()


    def update_theme(self):
        self.bgcolor = self.bgcolor = BgColor(self.page).get_background_color()
        self.page.update()
    
    
    def open_drawer(self, e):
        """Otvorenie drawer menu"""
        self.drawer.open = True
        self.drawer.update()
        self.page.update()

    
    def handle_change_bottom_nav(self, e):
        selected_index = e.control.selected_index
        if selected_index == 0:   # History
            self.page.go("/history")
        elif selected_index == 1:   # Report
            self.page.go("/report")
        elif selected_index == 2:   # Reminders
            self.page.go("/reminders")
        elif selected_index == 3:   # More
            self.open_drawer(e)
        self.page.update()
    
    
    def handle_change_drawer(self, e):
        selected_index = e.control.selected_index
        if selected_index == 0:   # History
            self.page.go("/history")
        elif selected_index == 1:   # Report
            self.page.go("/report")
        elif selected_index == 2:   # Reminders
            self.page.go("/reminders")
        elif selected_index == 3:   # Vehicles
            self.page.go("/vehicles")
        elif selected_index == 4:   # Users
            self.page.go("/users")
        elif selected_index == 5:   # Settings
            self.page.go("/settings/general")
        elif selected_index == 6:   # Contact
            self.page.go("/contact")
        self.page.update()


    