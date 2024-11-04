import flet as ft
from components.buttons import floating_action_button
from components.fields import (
    CustomUserField,
    # active_status_field, 
    # driver_license_category_field, 
    # driver_license_expiry_field, 
    # email_field, 
    # name_field, 
    # user_type_field
)
from components.navigations import app_bar, navigation_bottom_bar, left_drawer
from core.page_classes import ManageDialogWindow
from locales.language_manager import LanguageManager

from core.supa_base import get_supabese_client, get_current_user
from views.base_page import BaseView
from components.buttons import button_on_register


class CreateUsers(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__("/user/create", page)
        self.page = page
        self.lang_manager = LanguageManager()
        
        self.supabase = get_supabese_client()
        
        self.appbar = app_bar(self.page)
        
        self.page.drawer = left_drawer(self.page)
        self.drawer = self.page.drawer
        
        self.navigation_bar = navigation_bottom_bar(self.page)
        
        self.dialog_window = ManageDialogWindow(self.page).dialog_window
        self.floating_action_button = floating_action_button(self.dialog_window)
        self.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
                
        self.navigation_header_bar = self.build_navigation_header_bar()
        self.table_header = self.build_table_header()
        
        self.custom_user_field = CustomUserField(self.validate_fields)
        self.name_field = self.custom_user_field.name_field()
        self.email_field = self.custom_user_field.user_email_field()
        self.user_type_field = self.custom_user_field.user_type_field()
        self.driver_license_category_field = self.custom_user_field.driver_license_category_field()
        self.driver_license_expiry_field = self.custom_user_field.driver_license_expiry_field(self.page)
        self.active_status_field = self.custom_user_field.active_status_field()
        self.vehicle_user_field = self.custom_user_field.vehicle_user_field(self.page)
        
        self.form_fields = self.build_form_fields()
        self.register_button = button_on_register(self.handle_add_user_data)
        
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
                                    self.navigation_header_bar,
                                    self.table_header,
                                    ft.Divider(),
                                    self.form_fields,
                                    self.register_button
                                ]
                            )
                        )
                    ]
                )
            )
        ]
        
    def update_texts(self) -> None:
        # Aktualizácia textov v settings view
        # self.title_text.value = LanguageManager.get_text("intro_texto_05")
        self.update()
    
    
    def validate_fields(self, e=None):
        # Získame hodnoty z polí
        name = self.name_field.content.value
        email = self.email_field.content.value
        user_type = self.user_type_field.content.value
        driver_license_category = self.driver_license_category_field.content.value
        driver_license_expiry = self.driver_license_expiry_field.content.controls[1].value
        active_status = self.active_status_field.content.value
        vehicle_user = self.vehicle_user_field.content.value
        
        # Aktivujeme tlačidlo len ak sú obe polia vyplnené
        if name and email and user_type and driver_license_category and driver_license_expiry and active_status and vehicle_user:
            self.register_button.content.disabled = False
        else:
            self.register_button.content.disabled = True
            
        # Aktualizujeme UI
        self.register_button.update()
    
    
    def build_navigation_header_bar(self):
        return ft.Container(
            border=ft.border.all(0.5, ft.colors.GREY_400),
            border_radius=10,
            # padding=ft.padding.only(20, 20, 20, 20),
            content=ft.Row(
                controls=[
                    ft.TextButton(
                        style=ft.ButtonStyle(
                            overlay_color=ft.colors.TRANSPARENT,
                            shadow_color=ft.colors.TRANSPARENT,
                            bgcolor=ft.colors.TRANSPARENT,
                        ),
                        text=self.lang_manager.get_text("configuracoes"),
                        on_click=lambda e: self.go_to_settings(e),
                        
                    ),
                    ft.Icon(
                        name=ft.icons.KEYBOARD_ARROW_RIGHT_OUTLINED,
                        color=ft.colors.BLUE_700,
                        size=20,
                    ),
                    ft.TextButton(
                        style=ft.ButtonStyle(
                            overlay_color=ft.colors.TRANSPARENT,
                            shadow_color=ft.colors.TRANSPARENT,
                            bgcolor=ft.colors.TRANSPARENT,
                        ),
                        text=self.lang_manager.get_text("usuarios"),
                        on_click=lambda e: self.go_to_users(e),
                    ),
                    ft.Icon(
                        name=ft.icons.KEYBOARD_ARROW_RIGHT_OUTLINED,
                        color=ft.colors.BLUE_700,
                        size=20,
                    )
                    ,
                    ft.Text(
                        self.lang_manager.get_text("adicionar_novo"),
                    )
                ]
            )
        )
    
    
    def go_to_users(self, e):
        e.page.go("/users")
        
    def go_to_settings(self, e):
        e.page.go("/settings/general")
        
        
    def handle_add_user_data(self, e):
        name = self.name_field.content.value
        email = self.email_field.content.value
        user_type = self.user_type_field.content.value
        driver_license_category = self.driver_license_category_field.content.value
        driver_license_expiry = self.driver_license_expiry_field.content.controls[1].value
        active_status = self.active_status_field.content.value
        vehicle_user = self.vehicle_user_field.content.value
            
        user_data: dict = {
                "name": name,
                "email": email,
                "user_type": user_type,
                "driver_license_category": driver_license_category,
                "driver_license_expiry": driver_license_expiry,
                "is_active": active_status,
                "vehicle_user": vehicle_user
            }
        try:
            # Získanie ID prihláseného používateľa
            current_user: dict = get_current_user(self.page)
            if not current_user:
                raise Exception("No user is currently logged in")
                            
            # Pridanie user_id do údajov
            user_data["user_id"] = current_user.id
            
            # Vloženie údajov do tabuľky users
            response = self.supabase.table("users").insert(user_data).execute()
           
            self.page.go("/users")
            self.page.open(ft.SnackBar(content=ft.Text(self.lang_manager.get_text("msg_cadastrar_usuario"))))
            
            # return response.data
        except Exception as ex:
            print(f"Error adding user data: {ex}")
            return None

        
    def build_table_header(self):
        table_header = ft.Container(
            border=ft.border.all(0.5, ft.colors.GREY_400),
            border_radius=10,
            padding=ft.padding.only(20, 10, 20, 10),
            alignment=ft.alignment.center,
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            self.lang_manager.get_text("adicionar_novo"),
                            size=20,
                        ),
                        # alignment=ft.alignment.center_left,
                    ),
                    # ft.Container(
                    #     content=ft.SearchBar(
                    #         bar_bgcolor=ft.colors.GREY_100,
                    #         bar_overlay_color=ft.colors.GREY_100,
                    #         value="Search...",
                    #         width=200,
                    #         height=40,
                    #         on_change=lambda e: print("Search"),
                    #         on_submit=lambda e: print("Search"),
                    #     ),
                    #     # alignment=ft.alignment.center_left,
                    # ),
                    
                ]
            )
        )
        return table_header
    
    
    def build_form_fields(self):
        form_fields = ft.Container(
            # alignment=ft.alignment.center,
            # border=ft.border.all(0.5, ft.colors.GREY_400),
            # border_radius=10,
            padding=ft.padding.only(20, 20, 20, 20),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    self.name_field,
                    self.email_field,
                    self.user_type_field,
                    self.driver_license_category_field,
                    self.driver_license_expiry_field,
                    self.active_status_field,
                    self.vehicle_user_field
                ]
            )
        )
        return form_fields
    
    
    
    