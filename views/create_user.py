import datetime
import os
import json
import flet as ft

from core.supa_base import SupabaseUser
from locales.localization import (
    LocalizedTextButton,
    LocalizedText,
    LocalizedElevatedButton,
    LocalizedTextField,
    LocalizedDropdown
)
from views.base_page import BaseView


class CreateUsers(BaseView):
    def __init__(self, page: ft.Page, loc):
        super().__init__(page, loc)
        self.page = page
        self.setup_app_bar()

        self.supabase_vehicle = SupabaseUser(self.page)
        
        self.control_panel = self.build_control_panel()

        self.user_name_field = LocalizedTextField(
            localization=self.loc,
            text_key="nome",
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            on_change=lambda _: self.validate_fields()
        )
        
        self.user_email_field = LocalizedTextField(
            localization=self.loc,
            text_key="email",
            icon=ft.icons.EMAIL_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            on_change=lambda _: self.validate_fields()
        )
        
        self.user_type_field = LocalizedDropdown(
            localization=self.loc,
            label_key="tipo_usuario",
            options_keys=[
                {"key": "tipo_usuario_02"},
                {"key": "tipo_usuario_03"},
            ],
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            border_color=ft.colors.GREY,
            width=300,
            height=50,
            on_change=lambda _: self.validate_fields()
        )
        
        self.user_driver_license_category_field = LocalizedTextField(
            localization=self.loc,
            text_key="cnh_categoria",
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
        )
                
        self.user_driver_license_expiry_field = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    LocalizedElevatedButton(
                        localization=self.loc,
                        text_key="data",
                        width=90,
                        height=50,
                        on_click=lambda e: page.open(
                            ft.DatePicker(
                                first_date=datetime.datetime(year=1960, month=1, day=1),
                                last_date=datetime.datetime(year=2050, month=12, day=31),
                                on_change=lambda e: self.handle_change(e),
                                # on_dismiss=handle_dismissal,
                            )
                        )
                    ),
                    LocalizedTextField(
                        localization=self.loc,
                        text_key="cnh_validade",                        
                        width=180,
                        height=50,
                        border_color=ft.colors.GREY,
                        on_change=lambda _: self.validate_fields()
                    )
                ]
            )
        )
        
        self.active_status_field = LocalizedDropdown(
            localization=self.loc,
            label_key="status",
            options_keys=[
                {"key": "ativo"},
                {"key": "inativo"},
            ],
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            border_color=ft.colors.GREY,
            width=300,
            height=50,
            # on_change=self.validate_fields
        )
        
        self.register_button = LocalizedElevatedButton(
            localization=self.loc,
            text_key="btn_cadastrar",
            disabled=True,
            bgcolor=ft.colors.BLUE_700,
            width=200,
            height=50,
            style=ft.ButtonStyle(
                overlay_color=ft.colors.BLUE_900,
            ),
            color=ft.colors.WHITE,
            on_click=lambda e: self.handle_add_user_data(e)
        )
    
        self.controls = [
                ft.Container(
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(20, 30, 20, 0),
                    content=ft.Column(
                        width=400,
                        controls=[
                            ft.Container(
                                bgcolor=ft.colors.TRANSPARENT,
                                border=ft.border.all(0.5, ft.colors.GREY_400),
                                border_radius=10,
                                padding=ft.padding.only(20, 20, 20, 20),
                                alignment=ft.alignment.center,
                                content=ft.Column(
                                    spacing=10,
                                    controls=[
                                        # self.navigation_header_bar,
                                        self.control_panel,
                                        ft.Divider(),
                                        ft.Container(content=self.user_name_field, alignment=ft.alignment.center),
                                        ft.Container(content=self.user_email_field, alignment=ft.alignment.center),
                                        ft.Container(content=self.user_type_field, alignment=ft.alignment.center),
                                        ft.Container(content=self.user_driver_license_category_field, alignment=ft.alignment.center),
                                        ft.Container(content=self.user_driver_license_expiry_field, alignment=ft.alignment.center),
                                        # ft.Container(content=self.active_status_field, alignment=ft.alignment.center),
                                        ft.Container(content=self.register_button, alignment=ft.alignment.center, padding=ft.padding.only(bottom=10))
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        
    
    def handle_change(self, e):
        value = e.control.value.strftime("%Y-%m-%d")
        self.user_driver_license_expiry_field.content.controls[1].value = value
        self.page.update()
    
    def setup_app_bar(self):
        self.appbar.leading = ft.IconButton(
            icon=ft.icons.ARROW_BACK_OUTLINED,
            on_click=lambda _: self.page.go("/users")
        )
    
    def validate_fields(self):
        # Získame hodnoty z polí
        user_nickname = self.user_name_field.value
        user_email = self.user_email_field.value
        user_type = self.user_type_field.value
        # driver_license_expiry = self.user_driver_license_expiry_field.content.controls[1].value

        # Aktivujeme tlačidlo len ak sú polia vyplnené
        if user_nickname and user_email and user_type:
            self.register_button.disabled = False
        else:
            self.register_button.disabled = True

        # Aktualizujeme UI
        self.register_button.update()
    
    def build_control_panel(self):
        table_header = ft.Container(
            border=ft.border.all(0.5, ft.colors.GREY_400),
            border_radius=10,
            padding=ft.padding.only(20, 10, 20, 10),
            alignment=ft.alignment.center,
            content=ft.Row(
                controls=[
                    ft.Icon(ft.icons.DIRECTIONS_CAR_OUTLINED),
                    ft.Text("|"),
                    ft.Container(
                        content=LocalizedText(self.loc, "usuario")
                    ),
                ]
            )
        )
        return table_header
    
    def handle_add_user_data(self, e):
        user_name = self.user_name_field.value
        user_email = self.user_email_field.value
        user_type = self.user_type_field.value
        user_driver_license_category = self.user_driver_license_category_field.value
        user_driver_license_expiry = self.user_driver_license_expiry_field.content.controls[1].value

        user_data: dict = {
                "name": user_name,
                "email": user_email,
                "user_type": user_type,
                "driver_license_category": user_driver_license_category,
                "driver_license_expiry": user_driver_license_expiry,
            }
        try:
            self.supabase_vehicle.create_user_in_table_users(self.page, user_data)

            self.page.go("/users")
            self.page.open(ft.SnackBar(content=LocalizedText(self.loc, "msg_cadastra_usuiculo")))
            self.page.update()
            # return response.data
        except Exception as ex:
            print(f"Error adding user data: {ex}")
            return None
