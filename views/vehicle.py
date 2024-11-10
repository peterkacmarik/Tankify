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
                            on_click=lambda e: self.load_data(e)
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
            self.page.open(ft.SnackBar(content=LocalizedText("msg_no_vehdata")))
            self.page.update()
            return None

        tiles_container = ft.Column()

        for idx, vehicle in enumerate(vehicles_data):
            if vehicle["is_active"] == "Active" or "Aktivní" or "Aktívny":
                status = ft.Icon(name=ft.cupertino_icons.CHECK_MARK_CIRCLED)
            else:
                status = ft.Icon(name=ft.cupertino_icons.XMARK_CIRCLE)

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

    def load_data(self, e):
        vehicles_data = self.load_vehicle_data()
        if vehicles_data is None:
            self.page.show_snack_bar(ft.SnackBar(content=LocalizedText(self.loc, "msg_no_vehdata")))
            self.page.update()
            return

        # Vyčisti existujúce riadky
        self.build_list_tile.controls.clear()

        for idx, vehicle in enumerate(vehicles_data):
            if vehicle["is_active"] == "Active" or "Aktivní" or "Aktívny":
                status = ft.Icon(name=ft.cupertino_icons.CHECK_MARK_CIRCLED)
            else:
                status = ft.Icon(name=ft.cupertino_icons.XMARK_CIRCLE)

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



    # def get_value_from_fields(self, vehicle):
    #     # from views.create_vehicle import CreateVehicles
    #     # create_vehicles = CreateVehicles(self.page, self.loc)
    #
    #     # name_field = create_vehicles.vehicle_name_field()
    #     name_field = vehicle["name"]
    #
    #     # vehicle_type_field = create_vehicles.vehicle_type_field()
    #     vehicle_type_field = vehicle["vehicle"]
    #
    #     # vehicle_manufacturer_field = create_vehicles.vehicle_manufacturer_field()
    #     vehicle_manufacturer_field = vehicle["manufacturer"]
    #
    #     # vehicle_model_field = create_vehicles.vehicle_model_field()
    #     vehicle_model_field = vehicle["model"]
    #
    #     # vehicle_active_status_field = create_vehicles.active_status_field()
    #     vehicle_active_status_field = vehicle["is_active"]
    #
    #     # vehicle_year_field = create_vehicles.vehicle_year_field()
    #     vehicle_year_field = vehicle["year"]
    #
    #     # vehicle_fuel_type_field = create_vehicles.vehicle_fuel_type_field()
    #     vehicle_fuel_type_field = vehicle["fuel_type"]
    #
    #     # vehicle_fuel_capacity_field = create_vehicles.vehicle_fuel_capacity_field()
    #     vehicle_fuel_capacity_field = vehicle["fuel_capacity"]
    #
    #     # vehicle_unit_measurement_field = create_vehicles.vehicle_unit_measurement_field()
    #     vehicle_unit_measurement_field = vehicle["unit_measure"]
    #
    #     # vehicle_license_plate_field = create_vehicles.vehicle_license_plate_field()
    #     vehicle_license_plate_field = vehicle["license_plate"]
    #
    #     # vehicle_chassis_number_field = create_vehicles.vehicle_chassis_number_field()
    #     vehicle_chassis_number_field = vehicle["chassis_number"]
    #
    #     # vehicle_vin_field = create_vehicles.vehicle_vin_field()
    #     vehicle_vin_field = vehicle["vin"]
    #
    #     # vehicle_notes_field = create_vehicles.vehicle_notes_field()
    #     vehicle_notes_field = vehicle["notes"]
    #     return {
    #         "vehicle": vehicle_type_field,
    #         "manufacturer": vehicle_manufacturer_field,
    #         "model": vehicle_model_field,
    #         "year": vehicle_year_field,
    #         "name": name_field,
    #         "fuel_type": vehicle_fuel_type_field,
    #         "fuel_capacity": vehicle_fuel_capacity_field,
    #         "unit_measure": vehicle_unit_measurement_field,
    #         "license_plate": vehicle_license_plate_field,
    #         "chassis_number": vehicle_chassis_number_field,
    #         "vin": vehicle_vin_field,
    #         "notes": vehicle_notes_field,
    #         "is_active": vehicle_active_status_field,
    #     }
    #
    # def handle_edit_vehicle(self, e, vehicle, idx):
    #     vehicle_data: dict[str, str] = self.get_value_from_fields(vehicle)
    #
    #     def close_dialog(e):
    #         # Zatvorenie dialógu v overlay
    #         for dialog in self.page.overlay:
    #             if isinstance(dialog, ft.AlertDialog):
    #                 dialog.open = False
    #         self.page.update()
    #
    #     def handle_edit(e):
    #         vehicle_id = vehicle["id"]
    #         self.update_vehicle_in_table_vehicles(vehicle_id, vehicle_data)
    #         self.page.open(ft.SnackBar(content=LocalizedText(self.loc, "msg_atualiza_veiculo")))
    #         self.page.close(dialog)
    #         self.page.update()
    #
    #     dialog = ft.AlertDialog(
    #         modal=True,
    #         title=LocalizedText(self.loc, "atualizar"),
    #         content=ft.Container(
    #             content=ft.Column(
    #                 controls=[
    #                     vehicle_data["name"],
    #                     vehicle_data["vehicle"],
    #                     vehicle_data["manufacturer"],
    #                     vehicle_data["model"],
    #                     vehicle_data["is_active"],
    #                     vehicle_data["year"],
    #                     vehicle_data["fuel_type"],
    #                     vehicle_data["fuel_capacity"],
    #                     vehicle_data["unit_measure"],
    #                     vehicle_data["license_plate"],
    #                     vehicle_data["chassis_number"],
    #                     vehicle_data["vin"],
    #                     vehicle_data["notes"],
    #                 ]
    #             )
    #         ),
    #         actions=[
    #             LocalizedTextButton(localization=self.loc, text_key="btn_salvar", on_click=handle_edit),
    #             LocalizedTextButton(localization=self.loc, text_key="btn_cancelar", on_click=close_dialog),
    #             # ft.TextButton(self.lang_manager.get_translation("btn_salvar"), on_click=handle_edit),
    #             # ft.TextButton(self.lang_manager.get_translation("btn_cancelar"), on_click=close_dialog),
    #         ],
    #         actions_alignment=ft.MainAxisAlignment.END,
    #     )
    #     if dialog not in self.page.overlay:
    #         self.page.overlay.append(dialog)
    #     dialog.open = True
    #     self.page.update()
    #
    # def update_vehicle_in_table_vehicles(self, vehicle_id, vehicle_data: dict):
    #     try:
    #         update_data = {
    #             "name": vehicle_data["name"].content.value,
    #             "email": vehicle_data["email"].content.value,
    #             "user_type": vehicle_data["user_type"].content.value,
    #             "driver_license_category": vehicle_data["driver_license_category"].content.value,
    #             "driver_license_expiry": vehicle_data["driver_license_expiry"].content.controls[1].value,
    #             "is_active": vehicle_data["is_active"].content.value,
    #             "vehicle_user": vehicle_data["vehicle_user"].content.value,
    #         }
    #
    #         # Vloženie údajov do tabuľky users
    #         supabase = get_supabese_client()
    #         response = (
    #             supabase.table("vehicles")
    #             .update(update_data)
    #             .eq("id", vehicle_id)
    #             .execute()
    #         )
    #         # return response.data
    #     except Exception as ex:
    #         print(f"Error updating user: {ex}")
    #         return None
    #



