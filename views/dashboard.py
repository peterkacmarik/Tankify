import flet as ft
from components.navigations import app_bar, bottom_navigation_bar, left_drawer
from locales.open_files import get_translation
from components.fields import (
    model_field,
    vehicle_name_field,
    vehicle_type_field,
    manufacturer_field
)
from components.buttons import (
    google_login_button, 
    facebook_login_button,
    login_button
)
from components.logo import (
    page_logo
)
from components.links_separator_text import (
    line_separator,
    main_login_text,
    forgot_password_link,
    create_account_link
)
from locales.language_manager import LanguageManager
from supabase import Client
from core.supa_base import get_supabese_client


class DashboardView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/dashboard")
        self.page = page
        
        self.drawer = left_drawer(self.handle_change)
        self.appbar = app_bar(self.open_drawer, self.switch_theme)
        self.navigation_bar = bottom_navigation_bar()
        
        # self.bgcolor = ft.colors.WHITE
        # self.supabase: Client = get_supabese_client()
        
        self.scroll = ft.ScrollMode.HIDDEN
        self.fullscreen_dialog = True
        
        LanguageManager.subscribe(self.update_language)
        self.current_language = LanguageManager.get_current_language()
        self.translation = get_translation(self.current_language)
        self.init_components()
        
        # Snack bar
        self.snack_bar = ft.SnackBar(
            content=ft.Text(""),
            show_close_icon=True
        )
        self.page.overlay.append(self.snack_bar)

    
    def init_components(self):
        # Tvorba prepínača jazyka a prihlasovacieho formulára
        self.language_switch_button = self.language_switch()
        # self.page_logo = page_logo()
        # self.vehicle_type_fields = vehicle_type_field(self.translation)
        # search_input, search_results = manufacturer_field(self.translation, self.page)
        # self.model_field = model_field(self.translation)
        # self.vehicle_name_field = vehicle_name_field(self.translation)
        
        # Pridanie komponentov do hlavnej časti stránky
        self.controls = [
            ft.Container(
                alignment=ft.alignment.center,
                padding=ft.padding.only(20, 30, 20, 0),
                content=ft.Column(
                    controls=[
                        self.language_switch_button,
                    ]
                )
            ), 
            self.drawer,
            self.appbar,
            self.navigation_bar
        ]
    
    
    def handle_change(self, e):
        selected_index = e.control.selected_index
        if selected_index == 0:   # Domov
            self.page.go("/dashboard")
        elif selected_index == 1:   # Kalkulačka
            self.page.go("/login")
        elif selected_index == 2:   # Nastavenia
            self.page.go("/register")
        elif selected_index == 3:   # O aplikácií
            self.page.go("/forgot-password")
        self.page.update()
        
    
    def switch_theme(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        self.page.update()
    
    
    def open_drawer(self, e):
        """Otvorenie drawer menu"""
        self.drawer.open = True
        self.drawer.update()
        
        
    def close_drawer(self, e):
        """Zatvorenie drawer menu"""
        self.drawer.open = False
        self.drawer.update()
        
    
    def validate_fields(self, e=None):
        # Získame hodnoty z polí
        email = self.login_fields.content.controls[0].value
        password = self.login_fields.content.controls[1].value
    
        # Aktivujeme tlačidlo len ak sú obe polia vyplnené
        if email and password:
            self.login_button.content.disabled = False
        else:
            self.login_button.content.disabled = True
            
        # Aktualizujeme UI
        self.login_button.update()
    
    
    def language_switch(self):
        return ft.Container(
            # padding=ft.padding.only(left=20),
            alignment=ft.Alignment(x=-1.0, y=0.0),
            content=ft.Dropdown(
                bgcolor=ft.colors.TRANSPARENT,
                options=[
                    ft.dropdown.Option(
                        key="en", 
                        # text="English",
                        content=ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Image(
                                        src="/icons/us.svg",
                                        width=24,
                                        height=24,
                                        fit=ft.ImageFit.CONTAIN,
                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                    ),
                                    ft.Text("English"),
                                ]
                            )
                        ),
                    ),
                    ft.dropdown.Option(
                        key="sk", 
                        # text="Slovenčina"
                        content=ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Image(
                                        src="/icons/sk.svg",
                                        width=24,
                                        height=24,
                                        fit=ft.ImageFit.CONTAIN,
                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                    ),
                                    ft.Text("Slovenčina"),
                                ]
                            )
                        ),
                    ),
                    ft.dropdown.Option(
                        key="cs", 
                        # text="Čeština"
                        content=ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Image(
                                        src="/icons/cz.svg",
                                        width=24,
                                        height=24,
                                        fit=ft.ImageFit.CONTAIN,
                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                    ),
                                    ft.Text("Čeština"),
                                ]
                            )
                        ),
                    ),
                ],
                width=150,
                # padding=ft.padding.only(left=0),
                border=ft.InputBorder.NONE,
                value=self.current_language,
                border_radius=10,
                on_change=self.change_language
            )
        )
        
        
    def change_language(self, e):
        # Update the global language through the manager
        LanguageManager.set_language(e.control.value)
        # The update_language method will be called automatically through the subscription
    

    def did_mount(self):
        LanguageManager.subscribe(self.update_language)
        
        
    def will_unmount(self):
        LanguageManager.unsubscribe(self.update_language)
        
        
    def update_language(self):
        self.current_language = LanguageManager.get_current_language()
        self.translation = get_translation(self.current_language)
        self.update_ui()
        
        
    def update_ui(self):
        # Update all UI components with new translation
        self.controls.clear()
        self.init_components()
        self.page.update()
        
        
        
    # def handle_drawer_item_click(self, e, index):
    #     """Spracovanie kliknutia na položku v draweri"""
    #     # Aktualizácia vizuálneho stavu položiek
    #     for i, control in enumerate(self.page.drawer.controls):
    #         if isinstance(control, ft.NavigationDrawerDestination):
    #             control.selected = (i == index)
        
    #     # Zatvorenie drawera
    #     self.close_drawer(e)
        
    #     # Navigácia alebo akcia podľa vybranej položky
    #     if index == 0:  # Domov
    #         self.show_snack_bar_message("Navigácia na domovskú obrazovku")
    #     elif index == 1:  # Kalkulačka
    #         self.show_snack_bar_message("Otvorenie kalkulačky")
    #     elif index == 2:  # Nastavenia
    #         self.show_snack_bar_message("Otvorenie nastavení")
    #     elif index == 3:  # O aplikácii
    #         self.show_snack_bar_message("Zobrazenie informácií o aplikácii")
        
    #     self.page.update()
        