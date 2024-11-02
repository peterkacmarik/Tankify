import flet as ft

from core.page_classes import BgColor, LanguageSwitcher
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
from views.base_page import BaseView


class RegisterView(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__(route="/register", page=page)
        self.page = page
        self.lang_manager = LanguageManager()
        
        self.bgcolor = BgColor(self.page).get_background_color()
        self.supabase: Client = get_supabese_client()
        
        self.scroll = ft.ScrollMode.HIDDEN
        self.fullscreen_dialog = True
        
        self.snack_bar = ft.SnackBar(
            content=ft.Text(""),
            show_close_icon=True
        )
        self.page.overlay.append(self.snack_bar)
        
        self.language_switch_button = LanguageSwitcher(self.page).language_switch_button
        self.page_logo = page_logo()
        self.register_text = ft.Container(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    main_register_text(),
                    sub_register_text()
                ]
            )
        )
        
        # Create social buttons
        self.social_buttons = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                register_button_facebook(self.page),
                register_button_google(self.page)
            ]
        )
        
        self.line_separator = line_separator()
        
        # Create account form fields
        self.first_name_value = first_name_field(self.validate_fields)
        self.last_name_value = last_name_field(self.validate_fields)
        
        self.email_value = email_field(self.validate_fields)
        self.password_value = password_field(self.validate_fields)
        self.repeat_password_value = repeat_password_field(self.validate_fields)
        
        # Registration button and cancel button
        self.registration = register_button(self.handle_register)
        self.cancel_button = cancel_button(self.page)
        
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
    
    def update_texts(self) -> None:
        # Aktualizácia textov v settings view
        self.register_text.content.controls[0].content.value = LanguageManager.get_text("criar_conta_tankify")
        self.register_text.content.controls[1].content.value = LanguageManager.get_text("comece_gerenciamento_gratuito")
        
        self.social_buttons.controls[0].content.text = LanguageManager.get_text("criar_conta_com_facebook")
        self.social_buttons.controls[1].content.content.controls[1].value = LanguageManager.get_text("criar_conta_com_google")
        
        self.line_separator.controls[1].value = LanguageManager.get_text("ou")
        self.first_name_value.content.label = LanguageManager.get_text("primeiro_nome")
        self.last_name_value.content.label = LanguageManager.get_text("segundo_nome")
        self.email_value.content.label = LanguageManager.get_text("email")
        self.password_value.content.label = LanguageManager.get_text("senha")
        self.repeat_password_value.content.label = LanguageManager.get_text("senha_repetir")
        self.registration.content.text = LanguageManager.get_text("criar_conta")
        self.cancel_button.content.text = LanguageManager.get_text("btn_cancelar")
        self.update()
    
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
                self.snack_bar.content.value = self.lang_manager.get_text("msg_cadastrar_usuario")
                self.snack_bar.open = True
                self.page.update()
                
                self.page.go("/login")
                
        except Exception as e:
            self.snack_bar.content.value = str(e)
            self.snack_bar.open = True
            self.page.update()
            return
            
        
        
        