import flet as ft
from components.logo import page_logo
from components.buttons import (
    RegisterButtons,
)
from components.links_separator_text import (
    LinkSeparatorText,
)
from supabase import Client
from core.supa_base import get_supabese_client
from views.base_page import BaseView



class RegisterView(BaseView):
    def __init__(self, page: ft.Page, loc):
        super().__init__(page, loc)
        self.page = page
        self.supabase: Client = get_supabese_client()
        self.initialize_view()

    def initialize_view(self):
        self.appbar.visible = False
        self.navigation_bar.visible = False
        self.floating_action_button.visible = False
        # self.language_selector = self.loc.create_language_selector()

        self.page_logo = page_logo()
        self.register_text = ft.Container(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    LinkSeparatorText(self.page).main_register_text(),
                    LinkSeparatorText(self.page).sub_register_text()
                ]
            )
        )
        
        # Create social buttons
        self.social_buttons = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                RegisterButtons(self.page).register_button_facebook(),
                RegisterButtons(self.page).register_button_google()
            ]
        )
        
        self.line_separator = LinkSeparatorText(self.page).line_separator()
        
        # self.log_reg_forgot_fields = LoginRegisterForgotFields(self.validate_fields)
        self.first_name_value = ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=self.translate("primeiro_nome"),
                on_change=lambda e: self.validate_fields(e)
            )
        )
        self.last_name_value = ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=self.translate("segundo_nome"),
                on_change=lambda e: self.validate_fields(e)
            )
        )
        self.email_value = ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=self.translate("email"),
                on_change=lambda e: self.validate_fields(e)
            )
        )
        self.password_value = ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=self.translate("senha"),
                password=True,
                can_reveal_password=True,
                on_change=lambda e: self.validate_fields(e)
            )
        )
        self.repeat_password_value = ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=self.translate("senha_repetir"),
                password=True,
                can_reveal_password=True,
                on_change=lambda e: self.validate_fields(e)
            )
        )
        
        # Registration button and cancel button
        self.registration = RegisterButtons(self.page).register_button(self.handle_register)
        self.cancel_button = RegisterButtons(self.page).cancel_button()
        
        # Setup controls
        self.controls = [
            ft.Container(
                # border=ft.border.all(5),
                alignment=ft.alignment.center,
                padding=ft.padding.only(20, 30, 20, 0),
                content=ft.Column(
                    controls=[
                        self.language_selector,
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
                self.snack_bar.content.value = self.translate("msg_cadastrar_usuario")
                self.snack_bar.open = True
                self.page.update()
                
                self.page.go("/login")
                
        except Exception as e:
            self.snack_bar.content.value = str(e)
            self.snack_bar.open = True
            self.page.update()
            return
            
        
        
        