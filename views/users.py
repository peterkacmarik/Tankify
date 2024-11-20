from datetime import datetime, date
# import datetime
import flet as ft

from core.supa_base import SupabaseUser, get_supabese_client, get_current_user
from locales.localization import LocalizedOutlinedButton, LocalizedText
from views.base_page import BaseView


class UsersView(BaseView):
    def __init__(self, page: ft.Page, loc):
        super().__init__(page=page, loc=loc)
        self.page = page
        self.loc = loc
        self.supabase_user = SupabaseUser(self.page)
        
        self.control_panel = self.build_control_panel()
        self.build_list_tile = self.build_list_tile()

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
                                    self.control_panel,
                                    ft.Divider(),
                                    self.build_list_tile,
                                ]
                            )
                        )
                    ]
                )
            )
        ]
        
    def build_control_panel(self):
        panel = ft.Container(
            border=ft.border.all(0.5, ft.colors.GREY_400),
            border_radius=10,
            padding=ft.padding.only(20, 10, 20, 10),
            alignment=ft.alignment.center,
            content=ft.Row(
                controls=[
                    # ft.Icon(ft.icons.DIRECTIONS_CAR_OUTLINED),
                    # LocalizedText(self.loc, "veiculo_usuario_descricao"),
                    ft.Container(
                        expand=True,
                        alignment=ft.alignment.center_left,
                        content=LocalizedOutlinedButton(
                            localization=self.loc,
                            text_key="adicionar_novo",
                            icon=ft.icons.ADD,
                            on_click=lambda e: self.go_to_add_user(e),
                            style=ft.ButtonStyle(
                                bgcolor=ft.colors.TRANSPARENT,
                                shape={
                                    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=50),
                                }
                            )
                        ),
                    ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.IconButton(
                            icon=ft.icons.REFRESH,
                            on_click=lambda e: self.update_data(e)
                        ),
                    ),
                ]
            ),
        )
        return panel

    def go_to_add_user(self, e):
        e.page.go("/user/create")
        # print(f"Aktuálna URL trasa je: {e.page.route}")
        # self.page.update()
        
    def load_user_data(self):
        try:
            # Get current user id
            supabase = get_supabese_client()
            current_user_id = get_current_user(self.page).id
            response = supabase.table("users").select("*").eq("user_id", current_user_id).execute()
            # print(response.data)
            vehicles_data = response.data
            return vehicles_data
        except Exception as ex:
            print(f"Error getting all vehicle data: {ex}")
            return None
    
    def build_list_tile(self):
        user_data = self.load_user_data()
        # print(user_data)
        if user_data is None:
            self.page.open(
                ft.SnackBar(
                    content=LocalizedText(
                        localization=self.loc, 
                        text_key="msg_no_usrdata"
                    )
                )
            )
            self.page.update()
            return 
    
        tiles_container = ft.Column()

        for idx, user in enumerate(user_data):
            driver_license_expiry: datetime = datetime.strptime(user["driver_license_expiry"], "%Y-%m-%d").date()
            if driver_license_expiry < date.today(): # if driver license is expired
                status = ft.Icon(name=ft.cupertino_icons.XMARK_CIRCLE, color=ft.colors.RED)
            else:
                status = ft.Icon(name=ft.cupertino_icons.CHECK_MARK_CIRCLED, color=ft.colors.GREEN)

            user_type = f"{user['user_type']}"
            tile = ft.CupertinoListTile(
                notched=True,
                additional_info=ft.Text(user["driver_license_expiry"]),
                leading=ft.Icon(name=ft.cupertino_icons.CAR),
                title=ft.Text(user["name"]),
                subtitle=ft.Text(user_type),
                trailing=status,
                on_click=lambda e, u=user, i=idx: self.show_detail_user(e, u, i)
            )
            divider = ft.Divider(thickness=1)
            tiles_container.controls.append(tile)
            tiles_container.controls.append(divider)

        return tiles_container
        
    def show_detail_user(self, e, u, i):
        user_id = u.get("id")

        def handle_close(e):
            self.page.close(dialog)
            self.page.update()

        def edit_user(e, user_id):
            self.page.go(f"/user/edit/{user_id}")
            self.page.update()

        dialog = ft.AlertDialog(
            modal=True,
            title=LocalizedText(localization=self.loc, text_key="tile_heames_user"),
            content=ft.Column(
                height=400,
                controls=[
                    ft.Text(u.get("email")),
                    ft.Text(u.get("name")),
                    ft.Text(u.get("user_type")),
                    ft.Text(u.get("driver_license_category")),
                    ft.Text(u.get("driver_license_expiry")),
                    ft.Text(u.get("is_active")),
                ]
            ),

            actions=[
                ft.IconButton(ft.icons.DELETE, on_click=lambda _: self.supabase_user.delete_user_from_table_users(page=self.page, user_id=user_id, loc=self.loc, dialog=dialog)),
                ft.IconButton(ft.icons.EDIT, on_click=lambda e: edit_user(e, user_id)),
                ft.IconButton(ft.icons.CLOSE, on_click=handle_close),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            # on_dismiss=lambda e: self.page.add(ft.Text("Modal dialog dismissed")),
        )

        # Pridanie dialógu do overlay a jeho otvorenie
        if dialog not in self.page.overlay:
            self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()

    def update_data(self, e):
        users_data = self.load_user_data()
        if users_data is None:
            self.page.show_snack_bar(ft.SnackBar(content=LocalizedText(self.loc, "msg_no_usrdata")))
            self.page.update()
            return

        # Vyčisti existujúce riadky
        self.build_list_tile.controls.clear()

        for idx, user in enumerate(users_data):
            driver_license_expiry = datetime.strptime(user["driver_license_expiry"], "%Y-%m-%d").date()
            if driver_license_expiry <= date.today(): # if driver license is expired
                status = ft.Icon(name=ft.cupertino_icons.XMARK_CIRCLE, color=ft.colors.RED)
            else:
                status = ft.Icon(name=ft.cupertino_icons.CHECK_MARK_CIRCLED, color=ft.colors.GREEN)

            user_type = f"{user['user_type']}"
            self.build_list_tile.controls.append(
                ft.CupertinoListTile(
                    notched=True,
                additional_info=ft.Text(user["driver_license_expiry"]),
                leading=ft.Icon(name=ft.cupertino_icons.CAR),
                title=ft.Text(user["name"]),
                subtitle=ft.Text(user_type),
                trailing=status,
                on_click=lambda e, u=user, i=idx: self.show_detail_user(e, u, i)
            )
            )
            self.build_list_tile.controls.append(ft.Divider(thickness=1))
        self.build_list_tile.update()
        self.page.update()

    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        