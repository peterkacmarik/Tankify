import flet as ft

from core.page_classes import BgColor, LanguageSwitcher
from locales.open_files import get_translation
from components.logo import page_logo
from components.links_separator_text import (
    main_forgot_password_text,
    sub_forgot_password_text,
    cancel_link
)
from components.fields import email_field
from components.buttons import send_button
from locales.language_manager import LanguageManager

from supabase import Client
from core.supa_base import get_supabese_client
from views.base_page import BaseView


class ForgotPasswordView(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__("/forgot-password", page)
        self.page = page
        self.lang_manager = LanguageManager()
        
        # self.bgcolor = ft.colors.WHITE
        self.bgcolor = BgColor(self.page).get_background_color()
        self.supabase: Client = get_supabese_client()
        
        self.scroll = ft.ScrollMode.AUTO
        self.fullscreen_dialog = True
        
        self.snack_bar = ft.SnackBar(
            content=ft.Text(""),
            show_close_icon=True
        )
        self.page.overlay.append(self.snack_bar)
    
        self.language_switch_button = LanguageSwitcher(self.page).language_switch_button
        self.page_logo = page_logo()
        self.main_forgot_text = main_forgot_password_text()
        self.sub_forgot_text = sub_forgot_password_text()
        self.email_field = email_field(self.validate_fields)
        self.send_button = send_button(self.handle_forgot_password)
        self.cancel_button = cancel_link(self.page)
        
        self.controls = [
            ft.Container(
                alignment=ft.alignment.center,
                padding=ft.padding.only(20, 30, 20, 0),
                content=ft.Column(
                    controls=[
                        self.language_switch_button,
                        self.page_logo,
                        self.main_forgot_text,
                        self.sub_forgot_text,
                        self.email_field,
                        self.send_button,
                        self.cancel_button
                    ]
                )
            )
        ]
        
    def update_texts(self) -> None:
        # Aktualizácia textov v settings view
        self.main_forgot_text.content.value = LanguageManager.get_text("esqueceu_sua_senha")
        self.sub_forgot_text.content.value = LanguageManager.get_text("ajudaremos_redefinir")
        self.email_field.content.label = LanguageManager.get_text("email")
        self.send_button.content.text = LanguageManager.get_text("btn_enviar")
        self.cancel_button.content.text = LanguageManager.get_text("btn_cancelar")
        self.update()
    
    
    def validate_fields(self, e=None):
        # Získame hodnoty z polí
        email = self.email_field.value
    
        # Aktivujeme tlačidlo len ak sú obe polia vyplnené
        if email:
            self.send_button.content.disabled = False
        else:
            self.send_button.content.disabled = True
            
        # Aktualizujeme UI
        self.send_button.update()
        
        
    def handle_forgot_password(self, e):
        try:
            email = self.email_field.value
            
            response = self.supabase.auth.reset_password_for_email(
                email
            )
            
            self.snack_bar.content.value = f"Email na reset hesla bol odoslaný!\nResponse:{response}\n{email}"
            self.snack_bar.open = True
            self.page.update()
            
            self.page.go("/update-password")
                
        except Exception as ex:
            self.snack_bar.content.value = str(ex)
            self.snack_bar.open = True
            self.page.update()
            return
    
    