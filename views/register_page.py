import flet as ft
from components.logo import page_logo
from components.buttons import (
    RegisterButtons,
)
from components.links_separator_text import (
    LinkSeparatorText,
)
from supabase import Client
from core.auth_google import handle_google_login
from core.supa_base import get_supabese_client
from locales.localization import LocalizedElevatedButton, LocalizedOutlinedButton, LocalizedText, LocalizedTextButton, LocalizedTextField
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

        self.page_logo = page_logo()
        
        self.register_text = ft.Container(
            alignment=ft.alignment.center,
            content=LocalizedText(
                localization=self.loc,
                text_key="criar_conta_tankify",
                size=24,
                weight=ft.FontWeight.NORMAL,
                font_family="Roboto_Slap",
            )
        )
        
        self.sub_register_text = ft.Container(
            alignment=ft.alignment.center,
            padding=ft.padding.only(bottom=20),
            content=LocalizedText(
                localization=self.loc,
                text_key="comece_gerenciamento_gratuito",
                size=15,
                weight=ft.FontWeight.NORMAL,
                color=ft.colors.GREY_600,
            )
        )
        
        # Create social buttons
        self.social_buttons = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    content=LocalizedOutlinedButton(
                        localization=self.loc, 
                        text_key="criar_conta_com_facebook", 
                        icon=ft.icons.FACEBOOK,
                        width=300,
                        height=60,
                        expand=True,
                        on_click=lambda e: self.page.go("/login"),
                        style=ft.ButtonStyle(
                            bgcolor=ft.colors.WHITE,
                            overlay_color=ft.colors.WHITE,
                            side={
                                "": ft.BorderSide(width=0.5, color=ft.colors.GREY),
                                "hovered": ft.BorderSide(width=0.5, color=ft.colors.BLACK),
                            },
                        ),
                    ),
                ),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=LocalizedOutlinedButton(
                        localization=self.loc,
                        text_key="criar_conta_com_google",
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Image(
                                    src="https://cdn-icons-png.flaticon.com/512/300/300221.png",
                                    width=18,
                                    height=18,
                                    fit=ft.ImageFit.CONTAIN,
                                    repeat=ft.ImageRepeat.NO_REPEAT,
                                ),
                                LocalizedText(
                                    localization=self.loc,
                                    text_key="criar_conta_com_google"
                                ),
                            ]
                        ),
                        width=300,
                        height=60,
                        expand=True,
                        style=ft.ButtonStyle(
                            bgcolor=ft.colors.WHITE,
                            overlay_color=ft.colors.WHITE,
                            side={
                                "": ft.BorderSide(width=0.5, color=ft.colors.GREY),
                                "hovered": ft.BorderSide(width=0.5, color=ft.colors.BLACK),
                            },
                        ),
                        on_click=lambda e: handle_google_login(e, self.page),
                    )
                )
            ]
        )
        
        self.line_separator = ft.Container(
            padding=ft.padding.only(top=10, bottom=20),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        bgcolor=ft.colors.GREY,
                        height=0.5,
                        width=130,
                        # expand=True
                    ),
                    LocalizedText(
                        localization=self.loc, text_key="ou"
                    ),
                    ft.Container(
                        bgcolor=ft.colors.GREY,
                        height=0.5,
                        width=130,
                        # expand=True
                    ),
                ]
            )
        )
        
        self.first_name_value = ft.Container(
            alignment=ft.alignment.center,
            content=LocalizedTextField(
                localization=self.loc,
                text_key="primeiro_nome",
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                on_change=lambda e: self.validate_fields(e)
            )
        )
        
        self.last_name_value = ft.Container(
            padding=ft.padding.only(top=10, bottom=10),
            alignment=ft.alignment.center,
            content=LocalizedTextField(
                localization=self.loc,
                text_key="segundo_nome",
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                on_change=lambda e: self.validate_fields(e)
            )
        )
        
        self.email_value = ft.Container(
            alignment=ft.alignment.center,
            content=LocalizedTextField(
                localization=self.loc,
                text_key="email",
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                on_change=lambda e: self.validate_fields(e)
            )
        )
        
        self.password_value = ft.Container(
            padding=ft.padding.only(top=10, bottom=10),
            alignment=ft.alignment.center,
            content=LocalizedTextField(
                localization=self.loc,
                text_key="senha",
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                password=True,
                can_reveal_password=True,
                on_change=lambda e: self.validate_fields(e)
            )
        )
        
        self.repeat_password_value = ft.Container(
            alignment=ft.alignment.center,
            content=LocalizedTextField(
                localization=self.loc,
                text_key="senha_repetir",
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                password=True,
                can_reveal_password=True,
                on_change=lambda e: self.validate_fields(e)
            )
        )
        
        # Registration button and cancel button
        self.registration = ft.Container(
            alignment=ft.alignment.center,
            padding=ft.padding.only(top=10),
            content=LocalizedElevatedButton(
                localization=self.loc,
                text_key="criar_conta",
                disabled=True,
                bgcolor=ft.colors.BLUE_700,
                style=ft.ButtonStyle(
                    overlay_color=ft.colors.BLUE_900,
                ),
                width=300,
                height=50,
                color=ft.colors.WHITE,
                on_click=lambda e: self.handle_register(e)
            )
        )
        
        self.cancel_button = ft.Container(
            alignment=ft.alignment.center,
            content=LocalizedTextButton(
                localization=self.loc,
                text_key="btn_cancelar",
                style=ft.ButtonStyle(
                    overlay_color=ft.colors.TRANSPARENT,
                ),
                on_click=lambda e: self.page.go("/login"),
            )
        )
        
        self.terms_of_use = ft.Container(
            alignment=ft.alignment.center,
            # bgcolor=ft.colors.SURFACE_VARIANT,
            expand=True,
            content=LocalizedTextButton(
                localization=self.loc,
                text_key="politica_privacidade_termos_uso",
                style=ft.ButtonStyle(
                    overlay_color=ft.colors.TRANSPARENT,
                )
            )
        )
        
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
                        self.sub_register_text,
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
            ),
            ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                # bgcolor=ft.colors.SURFACE_VARIANT,
                content=self.terms_of_use
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
                self.snack_bar.content.value = self.loc.get_text("msg_cadastrar_usuario")
                self.snack_bar.open = True
                self.page.update()
                
                self.page.go("/login")
                
        except Exception as e:
            self.snack_bar.content.value = str(e)
            self.snack_bar.open = True
            self.page.update()
            return
            
        
        
        