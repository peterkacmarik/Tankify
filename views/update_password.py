import flet as ft

from components.logo import page_logo
from supabase import Client
from core.supa_base import get_supabese_client
from locales.localization import LocalizedText, LocalizedTextField, LocalizedElevatedButton, LocalizedTextButton
from views.base_page import BaseView


class UpdatePasswordView(BaseView):
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
        self.main_updated_text = LocalizedText(self.loc, "updata_senha", size=24, weight=ft.FontWeight.NORMAL,
                                              font_family="Roboto_Slap", )
        self.sub_updated_text = LocalizedText(self.loc, "secura_acaunta", size=16, weight=ft.FontWeight.NORMAL,
                                             font_family="Roboto_Slab", )

        self.update_password_field = LocalizedTextField(
            localization=self.loc,
            text_key="nova_senha",
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            on_change=lambda _: self.validate_fields(),
        )

        self.send_button = LocalizedElevatedButton(
            localization=self.loc,
            text_key="alterar_senha",
            disabled=True,
            bgcolor=ft.colors.BLUE_700,
            width=300,
            height=50,
            style=ft.ButtonStyle(
                overlay_color=ft.colors.BLUE_900,
            ),
            color=ft.colors.WHITE,
            on_click=lambda _: self.handle_forgot_password(),
        )
        self.cancel_button = LocalizedTextButton(
            localization=self.loc,
            text_key="btn_cancelar",
            on_click=lambda _: self.page.go("/login"),
        )

        self.controls = [
            ft.Container(
                alignment=ft.alignment.center,
                padding=ft.padding.only(20, 30, 20, 0),
                content=ft.Column(
                    controls=[
                        self.language_selector,
                        self.page_logo,
                        ft.Container(content=self.main_updated_text, alignment=ft.alignment.center,
                                     padding=ft.padding.only(top=10)),
                        ft.Container(content=self.sub_updated_text, alignment=ft.alignment.center),
                        ft.Container(content=self.update_password_field, alignment=ft.alignment.center,
                                     padding=ft.padding.only(top=20)),
                        ft.Container(content=self.send_button, alignment=ft.alignment.center,
                                     padding=ft.padding.only(top=10)),
                        ft.Container(content=self.cancel_button, alignment=ft.alignment.center),
                    ]
                )
            )
        ]

    def validate_fields(self, e=None):
        # Získame hodnoty z polí
        new_password = self.update_password_field.value

        # Aktivujeme tlačidlo len ak sú obe polia vyplnené
        if new_password:
            self.send_button.disabled = False
        else:
            self.send_button.disabled = True

        # Aktualizujeme UI
        self.send_button.update()

    def handle_forgot_password(self):
        try:
            new_password = self.update_password_field.value

            response = self.supabase.auth.update_user({
                "password": new_password
            })

            if response:
                self.snack_bar.content.value = self.loc.get_text("msg_alterar_senha")
                self.snack_bar.open = True
                self.page.update()

                self.page.go("/login")

        except Exception as ex:
            self.snack_bar.content.value = str(ex)
            self.snack_bar.open = True
            self.page.update()
            return

