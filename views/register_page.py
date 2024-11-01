import flet as ft

from locales.open_files import get_translation
from locales.language_manager import LanguageManager
from components.logo import page_logo
from components.buttons import (
    register_button_facebook,
    register_button_google,
    register_button,
    cancel_button
)
from components.links_separator_text import (
    main_register_text,
    sub_register_text,
    line_separator,
)
from components.fields import (
    first_name_field,
    last_name_field,
    email_field,
    password_field,
    repeat_password_field
)
from supabase import Client
from core.supa_base import get_supabese_client


class RegisterView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/register")
        self.page = page
        
        self.bgcolor = ft.colors.WHITE
        self.supabase: Client = get_supabese_client()
        
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
        # Create language switch button
        self.language_switch_button = self.language_switch()
        
        # Create header page
        self.page_logo = page_logo()
        self.register_text = ft.Container(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    main_register_text(self.translation),
                    sub_register_text(self.translation)
                ]
            )
        )
        
        # Create social buttons
        self.social_buttons = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                register_button_facebook(self.translation, self.page),
                register_button_google(self.translation, self.page)
            ]
        )
        
        self.line_separator = line_separator(self.translation)
        
        # Create account form fields
        self.first_name_value = first_name_field(self.translation, self.validate_fields)
        self.last_name_value = last_name_field(self.translation, self.validate_fields)
        
        self.email_value = email_field(self.translation, self.validate_fields)
        self.password_value = password_field(self.translation, self.validate_fields)
        self.repeat_password_value = repeat_password_field(self.translation, self.validate_fields)
        
        # Registration button and cancel button
        self.registration = register_button(self.translation, self.handle_register)
        self.cancel_button = cancel_button(self.translation, self.page)
        
        # Setup controls
        self.controls = [
            ft.Container(
                # border=ft.border.all(5),
                alignment=ft.alignment.center,
                padding=ft.padding.only(20, 30, 20, 0),
                expand=True,
                content=ft.Column(
                    controls=[
                        self.language_switch_button,
                        self.page_logo,
                        self.register_text,
                        self.social_buttons,
                        self.line_separator,
                        self.first_name_value,
                        self.last_name_value,
                        self.email_value,
                        self.password_value,
                        self.repeat_password_value,
                        self.registration,
                        self.cancel_button,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20
                )
            )
        ]
    
    
    def validate_fields(self, e=None):
        # Získame hodnoty z polí
        first_name = self.first_name_value.content.value
        last_name = self.last_name_value.content.value
        email = self.email_value.content.value
        password = self.password_value.content.value
        repeat_password = self.repeat_password_value.content.value
        
        # Aktivujeme tlačidlo len ak sú obe polia vyplnené
        if first_name and last_name and email and password and repeat_password:
            self.registration.content.disabled = False
        else:
            self.registration.content.disabled = True
            
        # Aktualizujeme UI
        self.registration.update()
    
    
    def update_language(self):
        # Update the view's language
        self.current_language = LanguageManager.get_current_language()
        self.translation = get_translation(self.current_language)
        self.update_ui()

    
    def update_ui(self):
        # Update all UI components with new translation
        self.controls.clear()
        self.init_components()
        self.page.update()
    
    
    def language_switch(self):
        return ft.Container(
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
        # Subscribe when the view is mounted
        LanguageManager.subscribe(self.update_language)


    def will_unmount(self):
        # Unsubscribe when the view is unmounted to prevent memory leaks
        LanguageManager.unsubscribe(self.update_language)
        
        
    def handle_register(self, e):
        try:
            first_name = self.first_name_value.content.value
            last_name = self.last_name_value.content.value
            email = self.email_value.content.value
            password = self.password_value.content.value
            
            response = self.supabase.auth.sign_up(
                credentials={
                    "email": f"{email}",
                    "password": f"{password}",
                    "options": {
                        "data": {
                            "first_name": f"{first_name}", 
                            "last_name": f"{last_name}"
                        }
                    }
                }
            )
            
            if response:
                self.snack_bar.content.value = self.translation["msg_cadastrar_usuario"]
                self.snack_bar.open = True
                self.page.update()
                
                self.page.go("/login")
                
        except Exception as e:
            self.snack_bar.content.value = str(e)
            self.snack_bar.open = True
            self.page.update()
            return
            
        
        
        