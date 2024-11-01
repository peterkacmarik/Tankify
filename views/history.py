import flet as ft
from components.navigations import app_bar, navigation_bottom_bar, left_drawer
from locales.open_files import get_translation

from locales.language_manager import LanguageManager
from supabase import Client
from core.supa_base import get_supabese_client


class HistoryView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/history")
        self.page = page
        
        # Definuj farby pre svetlý a tmavý režim
        self.light_bgcolor = ft.colors.WHITE # "#eaf0f5"
        self.dark_bgcolor = "#2e3b4e"
        self.bgcolor = self.get_background_color()
        
        # self.supabase: Client = get_supabese_client()
        
        self.scroll = ft.ScrollMode.HIDDEN
        self.fullscreen_dialog = True
        
        LanguageManager.subscribe(self.update_language)
        self.current_language = LanguageManager.get_current_language()
        self.translation = get_translation(self.current_language)
        self.init_components()
        
        self.drawer = left_drawer(self.translation, self.handle_change_drawer)
        self.appbar = app_bar(self.page, self.open_drawer, self.switch_theme, self.translation)
        self.navigation_bar = navigation_bottom_bar(self.page,self.translation, self.handle_change_bottom_nav)
        # self.bottom_appbar = bottom_appbar_nav(self.translation)
        
        # Snack bar
        self.snack_bar = ft.SnackBar(
            content=ft.Text(""),
            show_close_icon=True
        )
        self.page.overlay.append(self.snack_bar)

        
    def init_components(self):
        # self.language_switch_button = self.language_switch()
        
        self.floating_action_button = ft.FloatingActionButton(
            icon=ft.icons.ADD, 
            shape=ft.CircleBorder(type="circle"), 
            on_click=self.dialog_window,
        )
        
        self.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
        
        # Pridanie komponentov do hlavnej časti stránky
        self.controls = [
            ft.Container(
                alignment=ft.alignment.center,
                padding=ft.padding.only(20, 30, 20, 0),
                content=ft.Column(
                    controls=[
                        # self.language_switch_button,
                        # self.popup_menu,
                    ]
                )
            ), 
            # self.drawer,
            # self.appbar,
            # self.navigation_bar
        ]
    
    
    def handle_change_drawer(self, e):
        selected_index = e.control.selected_index
        if selected_index == 0:   # History
            self.page.go("/history")
        elif selected_index == 1:   # Add new
            self.page.go("/add-new")
        elif selected_index == 2:   # Reminders
            self.page.go("/reminders")
        elif selected_index == 3:   # Report
            self.page.go("/report")
        elif selected_index == 4:   # Vehicles
            self.page.go("/vehicles")
        elif selected_index == 5:   # Users
            self.page.go("/users")
        elif selected_index == 6:   # Settings
            self.page.go("/settings")
        elif selected_index == 7:   # Contact
            self.page.go("/contact")
        self.page.update()

    
    def dialog_window(self, e=None):  # Parameter e je pridaný pre podporu on_click
        # Vytvorenie dialógového okna
        dialog = ft.AlertDialog(
            bgcolor=ft.colors.SURFACE_VARIANT,
            shape=ft.RoundedRectangleBorder(radius=10),
            open=False,
            # actions=[ft.TextButton(self.translation["btn_cancelar"], on_click=self.close_dialog)],
            # actions_alignment=ft.MainAxisAlignment.END,
            # title=ft.Text("Add new item"),
            content=ft.Container(
                # border=ft.border.all(0),
                padding=ft.padding.only(left=10, right=10, top=0, bottom=0),
                margin=ft.margin.only(left=10, right=10, top=0, bottom=0),
                alignment=ft.alignment.center,
                # width=50,
                height=340,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.ElevatedButton(
                            text=self.translation["abastecimento"],
                            icon=ft.icons.LOCAL_GAS_STATION_OUTLINED,
                            color="#5d93b5",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                shadow_color=ft.colors.TRANSPARENT,
                                bgcolor=ft.colors.TRANSPARENT,
                                text_style=ft.TextStyle(
                                    size=16,
                                ),
                                icon_size=28,
                                icon_color=ft.colors.ORANGE,
                            ),
                            width=200,
                            on_click=self.close_dialog
                        ),
                        ft.ElevatedButton(
                            text=self.translation["servico"],
                            icon=ft.icons.MISCELLANEOUS_SERVICES_OUTLINED,
                            color="#5d93b5",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                shadow_color=ft.colors.TRANSPARENT,
                                bgcolor=ft.colors.TRANSPARENT,
                                text_style=ft.TextStyle(
                                    size=16,
                                ),
                                icon_size=28,
                                icon_color=ft.colors.BROWN,
                            ),
                            width=200,
                            on_click=self.close_dialog
                        ),
                        ft.ElevatedButton(
                            text=self.translation["despesa"],
                            icon=ft.icons.CREDIT_CARD_OFF_OUTLINED,
                            color="#5d93b5",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                shadow_color=ft.colors.TRANSPARENT,
                                bgcolor=ft.colors.TRANSPARENT,
                                text_style=ft.TextStyle(
                                    size=16,
                                ),
                                icon_size=28,
                                icon_color=ft.colors.BLUE,
                            ),
                            width=200,
                            on_click=self.close_dialog
                        ),
                        ft.ElevatedButton(
                            text=self.translation["receita"],
                            icon=ft.icons.ADD_CARD_OUTLINED,
                            color="#5d93b5",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                shadow_color=ft.colors.TRANSPARENT,
                                bgcolor=ft.colors.TRANSPARENT,
                                text_style=ft.TextStyle(
                                    size=16,
                                ),
                                icon_size=28,
                                icon_color=ft.colors.GREEN,
                            ),
                            width=200,
                            on_click=self.close_dialog
                        ),
                        ft.ElevatedButton(
                            text=self.translation["percurso"],
                            icon=ft.icons.ROUTE_OUTLINED,
                            color="#5d93b5",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                shadow_color=ft.colors.TRANSPARENT,
                                bgcolor=ft.colors.TRANSPARENT,
                                text_style=ft.TextStyle(
                                    size=16,
                                ),
                                icon_size=28,
                                icon_color=ft.colors.RED,
                            ),
                            width=200,
                            on_click=self.close_dialog
                        ),
                        ft.ElevatedButton(
                            text=self.translation["checklist"],
                            icon=ft.icons.CHECKLIST_OUTLINED,
                            color="#5d93b5",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                shadow_color=ft.colors.TRANSPARENT,
                                bgcolor=ft.colors.TRANSPARENT,
                                text_style=ft.TextStyle(
                                    size=16,
                                ),
                                icon_size=28,
                                icon_color=ft.colors.PURPLE,
                            ),
                            width=200,
                            on_click=self.close_dialog
                        ),
                        ft.ElevatedButton(
                            text=self.translation["lembrete"],
                            icon=ft.icons.NOTIFICATIONS_OUTLINED,
                            color="#5d93b5",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                shadow_color=ft.colors.TRANSPARENT,
                                bgcolor=ft.colors.TRANSPARENT,
                                text_style=ft.TextStyle(
                                    size=16,
                                ),
                                icon_size=28,
                                icon_color=ft.colors.YELLOW_700,
                            ),
                            width=200,
                            on_click=self.close_dialog
                        )
                    ],
                ),
            ),
        )
        
        # Pridanie dialógu do overlay a jeho otvorenie
        if dialog not in self.page.overlay:
            self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()
    

    def close_dialog(self, e):  
        # Zatvorenie dialógu v overlay
        for dialog in self.page.overlay:
            if isinstance(dialog, ft.AlertDialog):
                dialog.open = False
        self.page.update()


    def handle_change_bottom_nav(self, e):
        selected_index = e.control.selected_index
        if selected_index == 0:   # History
            self.page.go("/history")
        elif selected_index == 1:   # Report
            self.page.go("/report")
            
            
        elif selected_index == 2:   # Add new
            # self.page.go("/add-new")
            # self.check_item_clicked(e)
            pass
            
            
        elif selected_index == 3:   # Reminders
            self.page.go("/reminders")
        elif selected_index == 4:   # More
            self.page.go("/settings")
        self.page.update()
    
    
    def switch_theme(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        self.update_theme()  # Aktualizácia pozadia pre nový režim
        self.page.update()


    def get_background_color(self):
        # Vráti farbu podľa aktuálneho theme_mode stránky
        return self.light_bgcolor if self.page.theme_mode == ft.ThemeMode.LIGHT else self.dark_bgcolor


    def update_theme(self):
        self.bgcolor = self.get_background_color()
        self.page.update()
        
    
    def open_drawer(self, e):
        """Otvorenie drawer menu"""
        self.drawer.open = True
        self.drawer.update()
        
        
    def close_drawer(self, e):
        """Zatvorenie drawer menu"""
        self.drawer.open = False
        self.drawer.update()
    
    
    def language_switch(self):
        return ft.Container(
            # padding=ft.padding.only(left=20),
            alignment=ft.Alignment(x=-1.0, y=0.0),
            content=ft.Dropdown(
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
        
        
        
        