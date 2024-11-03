import flet as ft
from components.buttons import floating_action_button
from components.navigations import app_bar, navigation_bottom_bar, left_drawer
from core.page_classes import ManageDialogWindow
from locales.language_manager import LanguageManager

from core.supa_base import get_supabese_client
from views.base_page import BaseView


class UsersView(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__("/users", page)
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
    
# ---------------------------------------------------


    
    
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
                    )
                ]
            )
        )
        return table_header
    
    def go_to_add_user(self, e):
        e.page.go("/users/add")
    
    
    def build_user_table(self):
        # Získanie údajov o používateľoch
        users_data = self.get_all_data()

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
                    ft.Text(self.lang_manager.get_text("nome")),
                ),
                ft.DataColumn(
                    ft.Text(self.lang_manager.get_text("email"))
                ),
                ft.DataColumn(
                    ft.Text(self.lang_manager.get_text("tipo_usuario"))
                ),
                ft.DataColumn(
                    ft.Text(self.lang_manager.get_text("cnh_validade")),
                ),
                ft.DataColumn(
                    ft.Text(self.lang_manager.get_text("veiculo_usuario"))
                ),
                ft.DataColumn(
                    ft.Text(self.lang_manager.get_text("ativo"))
                ),
                ft.DataColumn(
                    ft.Text(self.lang_manager.get_text("Actions"))
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
                            ft.Text(user["driver_license_category"])
                        ),
                        ft.DataCell(
                            ft.Text(user["active"])
                        ),
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.EDIT,
                                            on_click=lambda e: print("Edit"),
                                        ),
                                        ft.IconButton(
                                            icon=ft.icons.DELETE,
                                            on_click=lambda e: print("Delete"),
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


    def get_current_user(self):
        try:
            # Skontroluj, či máme uloženú session v page client storage
            access_token = self.page.client_storage.get("access_token")
            refresh_token = self.page.client_storage.get("refresh_token")

            # Skontroluj, či oba tokeny existujú
            if access_token and refresh_token:
                # Nastav session pre supabase klienta
                self.supabase.auth.set_session(access_token, refresh_token)
                return self.supabase.auth.get_session().user
            return None
        except Exception as ex:
            print(f"Error getting current user: {ex}")
            return None


    def get_all_data(self):
        try:
            # Get current user id
            current_user_id = self.get_current_user().id
            
            # Get all data from current user
            response = self.supabase.table("users").select("*").eq("user_id", current_user_id).execute()

            return response.data
        except Exception as ex:
            print(f"Error getting all data: {ex}")
            return None
        
        
        
        
