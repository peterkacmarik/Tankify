import flet as ft
from core.auth_google import handle_google_login
from components.logo import (
    page_logo
)
from supabase import Client
from core.supa_base import get_supabese_client
from locales.localization import (
    LocalizedText,
    LocalizedOutlinedButton,
    LocalizedTextField,
    LocalizedTextButton,
    LocalizedElevatedButton
)
from views.base_page import BaseView


class LoginView(BaseView):
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
        
        self.login_text = ft.Container(
            alignment=ft.alignment.center,
            content=LocalizedText(
                localization=self.loc,
                text_key="login",
                size=24,
                weight=ft.FontWeight.NORMAL,
                font_family="Roboto_Slap",
            )
        )
        
        self.social_buttons = ft.Container(
            # alignment=ft.alignment.center,
            # padding=ft.padding.only(top=10, bottom=20),
            content=ft.Row(
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
                controls=[
                    LocalizedOutlinedButton(
                        localization=self.loc,
                        text_key="facebook",
                        width=150,
                        height=60,
                        icon=ft.icons.FACEBOOK,
                        style=ft.ButtonStyle(
                            bgcolor=ft.colors.WHITE,
                            overlay_color=ft.colors.WHITE,
                            side={
                                "": ft.BorderSide(width=0.5, color=ft.colors.GREY),
                                "hovered": ft.BorderSide(width=0.5, color=ft.colors.BLACK),
                            },
                        ),
                        on_click=lambda _: self.page.go("/login"),
                    ),
                    LocalizedOutlinedButton(
                        localization=self.loc,
                        text_key="google",
                        width=150,
                        height=60,
                        content=ft.Row(
                            controls=[
                                ft.Image(
                                    src="https://cdn-icons-png.flaticon.com/512/300/300221.png",
                                    width=18,
                                    height=18,
                                    fit=ft.ImageFit.CONTAIN,
                                    repeat=ft.ImageRepeat.NO_REPEAT,
                                ),
                                LocalizedText(self.loc, "google")
                            ]
                        ),
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
                ],
            ),
        )

        self.line_separator = ft.Row(
            # spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    bgcolor=ft.colors.GREY,
                    height=0.5,
                    width=130,
                    # expand=True
                ),
                LocalizedText(self.loc, "ou"),
                ft.Container(
                    bgcolor=ft.colors.GREY,
                    height=0.5,
                    width=130,
                    # expand=True
                ),
            ]
        )
        
        self.email_field = LocalizedTextField(
            localization=self.loc,
            text_key="email",
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            on_change=lambda _: self.validate_fields(),
        )

        self.password_field = LocalizedTextField(
            localization=self.loc,
            text_key="senha",
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            password=True,
            can_reveal_password=True,
            on_change=lambda _: self.validate_fields()
        )

        self.forgot_password_link = LocalizedTextButton(
            localization=self.loc,
            text_key="esqueceu_sua_senha",
            on_click=lambda _: self.page.go("/forgot-password"),
        )

        self.login_button = LocalizedElevatedButton(
            localization=self.loc,
            text_key="login",
            disabled=True,
            bgcolor=ft.colors.BLUE_700,
            style=ft.ButtonStyle(
                overlay_color=ft.colors.BLUE_900,
            ),
            width=300,
            height=50,
            color=ft.colors.WHITE,
            on_click=lambda  e: self.handle_login(e),
        )

        self.create_account_link = LocalizedTextButton(
            localization=self.loc,
            text_key="criar_conta",
            on_click=lambda _: self.page.go("/register"),
        )

        # Pridanie komponentov do hlavnej časti stránky
        self.controls = [
            ft.Container(
                alignment=ft.alignment.center,
                padding=ft.padding.only(20, 30, 20, 0),
                content=ft.Column(
                    controls=[
                        self.language_selector,
                        self.page_logo,
                        self.login_text,
                        ft.Container(alignment=ft.alignment.center, content=self.social_buttons, padding=ft.padding.only(top=20)),
                        ft.Container(alignment=ft.alignment.center, content=self.line_separator, padding=ft.padding.only(top=20, bottom=20)),
                        ft.Container(alignment=ft.alignment.center,content=self.email_field),
                        ft.Container(alignment=ft.alignment.center,content=self.password_field, padding=ft.padding.only(top=10)),
                        ft.Container(alignment=ft.alignment.center, content=self.forgot_password_link),
                        ft.Container(alignment=ft.alignment.center, content=self.login_button),
                        ft.Container(alignment=ft.alignment.center, content=self.create_account_link),
                    ]
                )
            )
        ]

    def validate_fields(self):
        # Získame hodnoty z polí
        email = self.email_field.value
        password = self.password_field.value
    
        # Aktivujeme tlačidlo len ak sú obe polia vyplnené
        if email and password:
            self.login_button.disabled = False
        else:
            self.login_button.disabled = True
            
        # Aktualizujeme UI
        self.login_button.update()

    def save_session(self, response):
        """Uloží session údaje do Flet session storage"""
        self.page.client_storage.set("access_token", response.session.access_token)
        self.page.client_storage.set("refresh_token", response.session.refresh_token)
        
    def handle_login(self, e=None):
        try:
            email = self.email_field.value
            password = self.password_field.value
            
            response = self.supabase.auth.sign_in_with_password(
                credentials={
                    "email": email, 
                    "password": password
                }
            )
            self.save_session(response)
            
            if response:
                self.snack_bar.content.value = self.loc.get_text('msg_login')
                self.snack_bar.open = True
                self.page.update()
                
                self.page.go("/history")
            # return response.user
        except Exception as ex:
            self.snack_bar.content.value = str(ex)
            self.snack_bar.open = True
            self.page.update()
            return
        
        
        