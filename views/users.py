import flet as ft
from components.buttons import floating_action_button
from components.navigations import app_bar, navigation_bottom_bar, left_drawer
from core.page_classes import ManageDialogWindow
from locales.language_manager import LanguageManager
from components.fields import CustomUserField

from core.supa_base import get_supabese_client, SupabaseUser
from views.base_page import BaseView


class UsersView(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__("/users", page)
        self.page = page
        self.lang_manager = LanguageManager()
        self.supabase_user = SupabaseUser()
        self.user_field = CustomUserField(validate_field=self.validate_user_field())
        
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
        self.user_table = self.build_user_table() 
        
        self.controls = [
            ft.Container(
                alignment=ft.alignment.center,
                padding=ft.padding.only(20, 30, 20, 0),
                content=ft.Column(
                    controls=[
                        ft.Container(
                            bgcolor=ft.colors.TRANSPARENT,
                            border=ft.border.all(0.5, ft.colors.GREY_400),
                            border_radius=10,
                            padding=ft.padding.only(20, 20, 20, 20),
                            alignment=ft.alignment.center,
                            content=ft.Column(
                                controls=[
                                    self.navigation_header_bar,
                                    self.table_header,
                                    ft.Divider(),
                                    self.user_table
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
        
    def validate_user_field(self):
        pass
    
    
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
                    )
                    ,
                    ft.Text(
                        self.lang_manager.get_text("usuarios"),
                    )
                ]
            )
        )
    
    
    def go_to_settings(self, e):
        e.page.go("/settings/general")
        

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
                            self.lang_manager.get_text("usuarios"),
                            size=20,
                        ),
                        # alignment=ft.alignment.center_left,
                    ),
                    ft.Container(
                        content=ft.SearchBar(
                            bar_bgcolor=ft.colors.GREY_100,
                            bar_overlay_color=ft.colors.GREY_100,
                            value="Search...",
                            width=200,
                            height=40,
                            on_change=lambda e: print("Search"),
                            on_submit=lambda e: print("Search"),
                        ),
                        # alignment=ft.alignment.center_left,
                    ),
                    ft.Container(
                        # alignment=ft.alignment.center_right,
                        content=ft.OutlinedButton(
                            text=self.lang_manager.get_text("adicionar_novo").upper(),
                            icon=ft.icons.ADD,
                            on_click=lambda e: self.go_to_add_user(e),
                            style=ft.ButtonStyle(
                                bgcolor=ft.colors.TRANSPARENT,
                                shape={
                                    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=50),
                                    
                                }
                            ),
                        )
                    ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.IconButton(
                            icon=ft.icons.REFRESH, on_click=lambda e: self.load_data(e)
                        ),
                    ),
                ]
            )
        )
        return table_header
    
    def load_data(self, e):
        response_data = self.supabase_user.get_all_data_from_table_users(
            self.page
        )

        if response_data is None:
            self.page.show_snack_bar(ft.SnackBar(content=ft.Text("No data available")))
            return

        # Vyčisti existujúce riadky
        self.user_table.rows.clear()

        # Pridaj nové riadky
        for idx, user in enumerate(response_data):
            self.user_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(idx+1),
                        ),
                        ft.DataCell(
                            ft.Text(user["name"])
                        ),
                        ft.DataCell(
                            ft.Text(user["email"])
                        ),
                        ft.DataCell(
                            ft.Text(user["user_type"])
                        ),
                        ft.DataCell(
                            ft.Text(user["driver_license_expiry"])
                        ),
                        ft.DataCell(
                            ft.Text(user["vehicle_user"])
                        ),
                        ft.DataCell(
                            ft.Text(user["is_active"])
                        ),
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.EDIT,
                                            on_click=lambda e, u=user: self.handle_edit_user(e, user),
                                        ),
                                        ft.IconButton(
                                            icon=ft.icons.DELETE,
                                            on_click=lambda _, u=user: self.supabase_user.delete_user_from_table_users(self.page, user["id"]),
                                        ),
                                    ]
                                )
                            )
                        ),
                    ]
                )
            )

        # Aktualizuj UI
        self.user_table.update()
        self.page.update()

    
    def go_to_add_user(self, e):
        e.page.go("/user/create")
    
    
    def build_user_table(self):
        # Získanie údajov o používateľoch
        users_data = self.supabase_user.get_all_data_from_table_users(self.page)

        if users_data is None:
            print("No data available")
            return ft.Text("No data available")
        
        # Vytvorenie tabuľky používateľov
        user_table = ft.DataTable(
            columns=[
                ft.DataColumn(
                    ft.Text("#"),
                ),
                ft.DataColumn(
                    ft.Text(self.lang_manager.get_text("nome")), # Name
                ),
                ft.DataColumn(
                    ft.Text(self.lang_manager.get_text("email")) # Email
                ),
                ft.DataColumn(
                    ft.Text(self.lang_manager.get_text("tipo_usuario")) # User type
                ),
                ft.DataColumn(
                    ft.Text(self.lang_manager.get_text("cnh_validade")), # Driver license expiry
                ),
                ft.DataColumn(
                    ft.Text(self.lang_manager.get_text("veiculo_usuario")) # Vehicle \/ User
                ),
                ft.DataColumn(
                    ft.Text(self.lang_manager.get_text("status")) # Active
                ),
                ft.DataColumn(
                    ft.Text(self.lang_manager.get_text("actions")) # Actions
                ),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(idx+1),
                        ),
                        ft.DataCell(
                            ft.Text(user["name"])
                        ),
                        ft.DataCell(
                            ft.Text(user["email"])
                        ),
                        ft.DataCell(
                            ft.Text(user["user_type"])
                        ),
                        ft.DataCell(
                            ft.Text(user["driver_license_expiry"])
                        ),
                        ft.DataCell(
                            ft.Text(user["vehicle_user"])
                        ),
                        ft.DataCell(
                            ft.Text(user["is_active"])
                        ),
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.EDIT,
                                            on_click=lambda e, user=user: self.handle_edit_user(e, user),
                                        ),
                                        ft.IconButton(
                                            icon=ft.icons.DELETE,
                                            on_click=lambda _: self.supabase_user.delete_user_from_table_users(self.page, users_data[0]["id"]),
                                        ),
                                    ]
                                )
                            )
                        )
                    ]
                )
                for idx, user in enumerate(users_data)
            ]
        )
        return user_table

    def get_value_from_fields(self, user):
        name_field = self.user_field.name_field()
        name_field.content.value = user["name"]
        
        user_type_field = self.user_field.user_type_field()
        user_type_field.content.value = user["user_type"]
        
        driver_license_category_field = self.user_field.driver_license_category_field()
        driver_license_category_field.content.value = user["driver_license_category"]
        
        driver_license_expiry_field = self.user_field.driver_license_expiry_field(self.page)
        driver_license_expiry_field.content.controls[1].value = user["driver_license_expiry"]
        
        active_status_field = self.user_field.active_status_field()
        active_status_field.content.value = user["is_active"]
        
        user_email_field = self.user_field.user_email_field()
        user_email_field.content.value = user["email"]
        
        vehicle_user_field = self.user_field.vehicle_user_field(self.page)
        vehicle_user_field.content.value = user["vehicle_user"]
        return {
            "name": name_field,
            "email": user_email_field,
            "user_type": user_type_field,
            "driver_license_category": driver_license_category_field,
            "driver_license_expiry": driver_license_expiry_field,
            "is_active": active_status_field,
            "vehicle_user": vehicle_user_field
        }

    def handle_edit_user(self, e, user):
        user_data: dict = self.get_value_from_fields(user)
        
        def close_dialog(e):  
            # Zatvorenie dialógu v overlay
            for dialog in self.page.overlay:
                if isinstance(dialog, ft.AlertDialog):
                    dialog.open = False
            self.page.update()
        
        def handle_edit(e):
            user_id = user["id"]
            self.supabase_user.update_user_in_table_users(user_id, user_data)
            self.page.open(ft.SnackBar(content=ft.Text(self.lang_manager.get_text(self.lang_manager.get_text("msg_atualiza_usuario")))))
            self.page.close(dialog)
            self.page.update()
        
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(self.lang_manager.get_text("atualizar")),
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        user_data["name"],
                        user_data["email"],
                        user_data["user_type"],
                        user_data["driver_license_category"],
                        user_data["driver_license_expiry"],
                        user_data["is_active"],
                        user_data["vehicle_user"],
                    ]
                )
            ),
            actions=[
                ft.TextButton(self.lang_manager.get_text("btn_salvar"), on_click=handle_edit),
                ft.TextButton(self.lang_manager.get_text("btn_cancelar"), on_click=close_dialog),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        if dialog not in self.page.overlay:
            self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()
        
    
    