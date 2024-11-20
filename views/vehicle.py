import flet as ft
from core.supa_base import get_supabese_client, get_current_user, SupabaseVehicle

from locales.localization import LocalizedText, LocalizedTextButton, LocalizedOutlinedButton, LocalizedDataTable
from views.base_page import BaseView
from views.edit_vehicle import EditVehiclesViews


class VehiclesViews(BaseView):
    def __init__(self, page: ft.Page, loc):
        super().__init__(page=page, loc=loc)
        self.page = page
        self.loc = loc
        self.supabase_vehicle = SupabaseVehicle(self.page)

        # self.header_bar = self.build_header_bar()
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
                                    # self.header_bar,
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

    def build_header_bar(self):
        return ft.Container(
            # border=ft.border.all(0.5, ft.colors.GREY_400),
            border_radius=10,
            # padding=ft.padding.only(20, 20, 20, 20),
            content=ft.ResponsiveRow(
                controls=[
                    # LocalizedTextButton(
                    #     localization=self.loc,
                    #     text_key="configuracoes",
                    #     on_click=lambda e: self.go_to_settings(e),
                    #     style=ft.ButtonStyle(
                    #         overlay_color=ft.colors.TRANSPARENT,
                    #         shadow_color=ft.colors.TRANSPARENT,
                    #         bgcolor=ft.colors.TRANSPARENT,
                    #     )
                    # ),
                    # ft.Icon(
                    #     name=ft.icons.KEYBOARD_ARROW_RIGHT_OUTLINED,
                    #     color=ft.colors.BLUE_700,
                    #     size=20,
                    # ),
                    LocalizedText(self.loc, "veiculo_usuario_descricao"),
                ]
            ),
        )

    def go_to_settings(self, e):
        e.page.go("/settings/general")

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
                            on_click=lambda e: self.go_to_add_vehicle(e),
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

    def go_to_add_vehicle(self, e):
        e.page.go("/vehicle/create")
        # print(f"Aktuálna URL trasa je: {e.page.route}")
        # self.page.update()

    def load_vehicle_data(self):
        try:
            # Get current user id
            supabase = get_supabese_client()
            current_user_id = get_current_user(self.page).id
            response = supabase.table("vehicles").select("*").eq("vehicle_id", current_user_id).execute()
            vehicles_data = response.data
            return vehicles_data
        except Exception as ex:
            print(f"Error getting all vehicle data: {ex}")
            return None

    def build_list_tile(self):
        vehicles_data = self.load_vehicle_data()
        if vehicles_data is None:
            self.page.open(ft.SnackBar(
                content=LocalizedText(
                    localization=self.loc, 
                    text_key="msg_no_vehdata"
                    )
                )
            )
            self.page.update()
            return None

        tiles_container = ft.Column()

        for idx, vehicle in enumerate(vehicles_data):
            # print(vehicle["is_active"])
            if vehicle["is_active"] == "Active" or vehicle["is_active"] == "Aktivní" or vehicle["is_active"] == "Aktívny":
                status = ft.Icon(name=ft.cupertino_icons.CHECK_MARK_CIRCLED, color=ft.colors.GREEN)
            else:
                status = ft.Icon(name=ft.cupertino_icons.XMARK_CIRCLE, color=ft.colors.RED)

            text_manufacturer = vehicle["manufacturer"]
            text_model = vehicle["model"]
            connect_text = f"{text_manufacturer} {text_model}"

            tile = ft.CupertinoListTile(
                notched=True,
                additional_info=ft.Text(vehicle["is_active"]),
                leading=ft.Icon(name=ft.cupertino_icons.CAR),
                title=ft.Text(vehicle["name"]),
                subtitle=ft.Text(connect_text),
                trailing=status,
                on_click=lambda e, v=vehicle, i=idx: self.show_detail_vehicle(e, v, i)
            )
            divider = ft.Divider(thickness=1)
            tiles_container.controls.append(tile)
            tiles_container.controls.append(divider)

        return tiles_container

    def show_detail_vehicle(self, e, v, i):
        vehicle_id = v.get("id")

        def handle_close(e):
            self.page.close(dialog)
            self.page.update()

        def edit_vehicle(e, vehicle_id):
            self.page.go(f"/vehicle/edit/{vehicle_id}")
            self.page.update()

        dialog = ft.AlertDialog(
            modal=True,
            title=LocalizedText(localization=self.loc, text_key="tile_heames"),
            content=ft.Column(
                height=400,
                controls=[
                    ft.Text(v.get("vehicle")),
                    ft.Text(v.get("manufacturer")),
                    ft.Text(v.get("model")),
                    ft.Text(v.get("year")),
                    ft.Text(v.get("name")),
                    ft.Text(v.get("fuel_type")),
                    ft.Text(v.get("fuel_capacity")),
                    ft.Text(v.get("unit_measure")),
                    ft.Text(v.get("license_plate")),
                    ft.Text(v.get("chassis_number")),
                    ft.Text(v.get("vin")),
                    ft.Text(v.get("notes")),
                    ft.Text(v.get("is_active")),
                ]
            ),

            actions=[
                ft.IconButton(ft.icons.DELETE, on_click=lambda _: self.supabase_vehicle.delete_vehicle_from_table_vehicles(page=self.page, vehicle_id=vehicle_id, loc=self.loc, dialog=dialog)),
                ft.IconButton(ft.icons.EDIT, on_click=lambda e: edit_vehicle(e, vehicle_id)),
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
        vehicles_data = self.load_vehicle_data()
        if vehicles_data is None:
            self.page.show_snack_bar(ft.SnackBar(content=LocalizedText(self.loc, "msg_no_vehdata")))
            self.page.update()
            return

        # Vyčisti existujúce riadky
        self.build_list_tile.controls.clear()

        for idx, vehicle in enumerate(vehicles_data):
            if vehicle["is_active"] == "Active" or vehicle["is_active"] == "Aktivní" or vehicle["is_active"] == "Aktívny":
                status = ft.Icon(name=ft.cupertino_icons.CHECK_MARK_CIRCLED, color=ft.colors.GREEN)
            else:
                status = ft.Icon(name=ft.cupertino_icons.XMARK_CIRCLE, color=ft.colors.RED)

            text_manufacturer = vehicle["manufacturer"]
            text_model = vehicle["model"]
            connect_text = f"{text_manufacturer} {text_model}"

            self.build_list_tile.controls.append(
                ft.CupertinoListTile(
                    notched=True,
                    additional_info=ft.Text(vehicle["is_active"]),
                    leading=ft.Icon(name=ft.cupertino_icons.CAR),
                    title=ft.Text(vehicle["name"]),
                    subtitle=ft.Text(connect_text),
                    trailing=status,
                    on_click=lambda e, v=vehicle, i=idx: self.show_detail_vehicle(e, v, i)
                )
            )
            self.build_list_tile.controls.append(ft.Divider(thickness=1))
        self.build_list_tile.update()
        self.page.update()

