import os
import json

import flet as ft
from core.supa_base import get_supabese_client, get_current_user, SupabaseVehicle

from locales.localization import LocalizedText, LocalizedTextButton, LocalizedOutlinedButton, LocalizedDataTable, \
    LocalizedTextField, LocalizedDropdown, LocalizedElevatedButton
from views.base_page import BaseView

from typing import Optional


class EditVehiclesViews(BaseView):
    def __init__(self, page: ft.Page, loc):
        super().__init__(page=page, loc=loc)
        self.supabase_vehicle = SupabaseVehicle(self.page)
        self.page = page
        self.loc = loc
        self.id = self.get_id_from_route()

        self.vehicle_type_field = None
        self.manufacturer_field = None
        self.vehicle_model_field = None
        self.vehicle_name_field = None
        self.vehicle_year_field = None
        self.vehicle_fuel_type_field = None
        self.vehicle_fuel_capacity_field = None
        self.vehicle_unit_measurement_field = None
        self.vehicle_license_plate_field = None
        self.vehicle_chassis_number_field = None
        self.vehicle_vin_field = None
        self.vehicle_notes_field = None
        self.active_status_field = None

        self.setup_app_bar()

        self.control_panel = self.build_control_panel()
        self.edit_vehicle = self.handle_edit_vehicle()

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
                                    self.edit_vehicle
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
                    ft.Icon(ft.icons.DIRECTIONS_CAR_OUTLINED),
                    ft.Text("|"),
                    LocalizedText(localization=self.loc, text_key="btn_editar"),

                    # ft.Container(
                    #     expand=True,
                    #     alignment=ft.alignment.center_left,
                    #     content=LocalizedOutlinedButton(
                    #         localization=self.loc,
                    #         text_key="btn_salvar",
                    #         icon=ft.icons.SAVE,
                    #         on_click=lambda e: self.save_vehicle(e),
                    #         style=ft.ButtonStyle(
                    #             bgcolor=ft.colors.TRANSPARENT,
                    #             shape={
                    #                 ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=50),
                    #             }
                    #         )
                    #     ),
                    # ),
                ]
            ),
        )
        return panel

    def save_vehicle(self, e):
        e.page.go("/vehicles")

    def setup_app_bar(self):
        self.appbar.leading = ft.IconButton(
            icon=ft.icons.ARROW_BACK_OUTLINED,
            on_click=lambda _: self.page.go("/vehicles")
        )

    def get_id_from_route(self) -> Optional[str]:
        # Získanie ID vozidla z URL
        parts = self.page.route.split('/')
        # print(f"Parts: {parts[-1]}")
        return parts[-1]

    def load_vehicle_data(self):
        try:
            # Get current user id
            supabase = get_supabese_client()
            response = supabase.table("vehicles").select("*").eq("id", self.id).execute()
            vehicles_data = response.data
            return vehicles_data
        except Exception as ex:
            print(f"Error getting all vehicle data: {ex}")
            return None

    def handle_edit_vehicle(self):
        vehicles_data = self.load_vehicle_data()
        if vehicles_data is None:
            self.page.open(ft.SnackBar(content=LocalizedText("msg_no_vehdata")))
            self.page.update()
            return None

        data_container = ft.Column()

        name_valeu = vehicles_data[0]["name"]
        vehicle_name_field = LocalizedTextField(
            value=name_valeu,
            localization=self.loc,
            text_key="nome",
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            # on_change=self.validate_fields
        )

        options_vehicle_type = [
            {"key": "tipo_veiculo_01"},
            {"key": "tipo_veiculo_02"},
            {"key": "tipo_veiculo_03"},
            {"key": "tipo_veiculo_04"}
        ]
        type_value = vehicles_data[0]["vehicle"]
        vehicle_type_field = LocalizedDropdown(
            value=type_value,
            localization=self.loc,
            label_key="tipo_veiculo",
            options_keys=options_vehicle_type,
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            border_color=ft.colors.GREY,
            width=300,
            height=50,
            # on_change=self.validate_field,
        )
        manufacturer_value = vehicles_data[0]["manufacturer"]
        manufacturer_field = self.vehicle_manufacturer_field(manufacturer_value)

        model_value = vehicles_data[0]["model"]
        vehicle_model_field = LocalizedTextField(
            value=model_value,
            localization=self.loc,
            text_key="modelo",
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            # on_change=self.validate_fields
        )

        year_value = vehicles_data[0]["year"]
        vehicle_year_field = LocalizedTextField(
            value=year_value,
            localization=self.loc,
            text_key="ano",
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            # on_change=self.validate_field
        )

        options_fuel_type = [
            {"key": "tipo_combustivel_01"},
            {"key": "tipo_combustivel_02"},
            {"key": "tipo_combustivel_03"},
            {"key": "tipo_combustivel_04"}
        ]
        fuel_type_value = vehicles_data[0]["fuel_type"]
        vehicle_fuel_type_field = LocalizedDropdown(
            value=fuel_type_value,
            localization=self.loc,
            label_key="tipo_combustivel",
            options_keys=options_fuel_type,
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            border_color=ft.colors.GREY,
            width=300,
            height=50,
            # on_change=self.validate_field,
        )

        fuel_capacity = vehicles_data[0]["fuel_capacity"]
        vehicle_fuel_capacity_field = LocalizedTextField(
            value=fuel_capacity,
            localization=self.loc,
            text_key="volume_tanque_litros",
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            # on_change=self.validate_fields
        )

        options_unit_measurement = [
            {"key": "distancia_01"},
            {"key": "distancia_02"},
        ]
        unit_measurement_value = vehicles_data[0]["unit_measure"]
        vehicle_unit_measurement_field = LocalizedDropdown(
            value=unit_measurement_value,
            localization=self.loc,
            label_key="unit_of_measure",
            options_keys=options_unit_measurement,
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            border_color=ft.colors.GREY,
            width=300,
            height=50,
            # on_change=self.validate_field,
        )

        license_plate_value = vehicles_data[0]["license_plate"]
        vehicle_license_plate_field = LocalizedTextField(
            value=license_plate_value,
            localization=self.loc,
            text_key="placa",
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            # on_change=self.validate_field
        )

        chassis_number_value = vehicles_data[0]["chassis_number"]
        vehicle_chassis_number_field = LocalizedTextField(
            value=chassis_number_value,
            localization=self.loc,
            text_key="chassi",
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            # on_change=self.validate_field
        )

        vin_value = vehicles_data[0]["vin"]
        vehicle_vin_field = LocalizedTextField(
            value=vin_value,
            localization=self.loc,
            text_key="renavam",
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            # on_change=self.validate_field
        )

        notes_value = vehicles_data[0]["notes"]
        vehicle_notes_field = LocalizedTextField(
            value=notes_value,
            localization=self.loc,
            text_key="observacao",
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
        )

        options_active_status = [
            {"key": "ativo"},
            {"key": "inativo"},
        ]
        active_status_value = vehicles_data[0]["is_active"]
        active_status_field = LocalizedDropdown(
            value=active_status_value,
            localization=self.loc,
            label_key="status",
            options_keys=options_active_status,
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            # on_change=self.validate_fields,
        )

        self.vehicle_type_field = vehicle_type_field
        self.manufacturer_field = manufacturer_field
        self.vehicle_model_field = vehicle_model_field
        self.vehicle_name_field = vehicle_name_field
        self.vehicle_year_field = vehicle_year_field
        self.vehicle_fuel_type_field = vehicle_fuel_type_field
        self.vehicle_fuel_capacity_field = vehicle_fuel_capacity_field
        self.vehicle_unit_measurement_field = vehicle_unit_measurement_field
        self.vehicle_license_plate_field = vehicle_license_plate_field
        self.vehicle_chassis_number_field = vehicle_chassis_number_field
        self.vehicle_vin_field = vehicle_vin_field
        self.vehicle_notes_field = vehicle_notes_field
        self.active_status_field = active_status_field

        save_button = LocalizedElevatedButton(
            localization=self.loc,
            text_key="btn_salvar",
            # disabled=False,
            bgcolor=ft.colors.BLUE_700,
            width=200,
            height=50,
            style=ft.ButtonStyle(
                overlay_color=ft.colors.BLUE_900,
            ),
            color=ft.colors.WHITE,
            on_click=lambda e: self.save_vehicle_data(e, self.id)
        )

        data_container.controls.extend(
            [
                ft.Container(content=vehicle_name_field, alignment=ft.alignment.center),
                ft.Container(content=vehicle_type_field, alignment=ft.alignment.center),
                ft.Container(content=manufacturer_field, alignment=ft.alignment.center),
                ft.Container(content=vehicle_model_field, alignment=ft.alignment.center),
                ft.Container(content=vehicle_year_field, alignment=ft.alignment.center),
                ft.Container(content=vehicle_fuel_type_field, alignment=ft.alignment.center),
                ft.Container(content=vehicle_fuel_capacity_field, alignment=ft.alignment.center),
                ft.Container(content=vehicle_unit_measurement_field, alignment=ft.alignment.center),
                ft.Container(content=vehicle_license_plate_field, alignment=ft.alignment.center),
                ft.Container(content=vehicle_chassis_number_field, alignment=ft.alignment.center),
                ft.Container(content=vehicle_vin_field, alignment=ft.alignment.center),
                ft.Container(content=vehicle_notes_field, alignment=ft.alignment.center),
                ft.Container(content=active_status_field, alignment=ft.alignment.center),
                ft.Container(content=save_button, alignment=ft.alignment.center, padding=ft.padding.only(bottom=10)),
            ]
        )
        return data_container

    def vehicle_manufacturer_field(self, manufacturer_value):
        def _load_manufacturers(manufacturer):
            # Načíta JSON súbor podľa jazykového kódu
            file_path = os.path.join("assets/manufacturers", f"{manufacturer}.json")
            with open(file_path, "r", encoding="utf-8") as file:
                all_manufacturers = json.load(file)
            return [item['nome'] for item in all_manufacturers]

        manufacturers: list = _load_manufacturers("manufacturers")

        search_results = ft.ListView(
            spacing=5,
            height=200,  # pridáme výšku pre zobrazenie výsledkov
            visible=False,  # na začiatku skryjeme zoznam
        )

        # Funkcia na filtrovanie výrobcov podľa vstupu
        def filter_manufacturers(e):
            search_text = e.control.value.lower()
            filtered = [m for m in manufacturers if search_text in m.lower()]

            search_results.controls.clear()
            if search_text:  # zobrazíme výsledky len ak je nejaký text
                search_results.visible = True
                for manufacturer in filtered:
                    search_results.controls.append(
                        ft.Container(
                            border=ft.border.all(0.5, ft.colors.GREY),
                            border_radius=5,
                            content=ft.TextButton(
                                text=manufacturer,
                                on_click=select_manufacturer,
                                style=ft.ButtonStyle(
                                    # bgcolor=ft.colors.BLUE_GREY_100,
                                    shape=ft.RoundedRectangleBorder(radius=5),
                                )
                            )
                        ))
            else:
                search_results.visible = False
            self.page.update()

        # Funkcia na nastavenie vybraného výrobcu ako hodnoty vo `TextField`
        def select_manufacturer(e):
            search_input.value = e.control.text
            search_results.visible = False
            search_results.controls.clear()
            self.page.update()

        search_input = LocalizedTextField(
            value=manufacturer_value,
            icon=ft.icons.SHIELD,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            localization=self.loc,
            text_key="marca",
            on_change=filter_manufacturers,
            # on_submit=self.validate_fields
        )

        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column(
                controls=[
                    search_input,
                    search_results
                ]
            )
        )

    def save_vehicle_data(self, e, vehicle_id):
        try:
            # Získanie aktuálnych hodnôt z formulára
            current_data = {
                "vehicle": self.vehicle_type_field.value,
                "manufacturer": self.manufacturer_field.content.controls[0].value,
                "model": self.vehicle_model_field.value,
                "year": self.vehicle_year_field.value,
                "name": self.vehicle_name_field.value,
                "fuel_type": self.vehicle_fuel_type_field.value,
                "fuel_capacity": self.vehicle_fuel_capacity_field.value,
                "unit_measure": self.vehicle_unit_measurement_field.value,
                "license_plate": self.vehicle_license_plate_field.value,
                "chassis_number": self.vehicle_chassis_number_field.value,
                "vin": self.vehicle_vin_field.value,
                "notes": self.vehicle_notes_field.value,
                "is_active": self.active_status_field.value,
            }

            result = self.supabase_vehicle.update_vehicle_in_table_vehicles(vehicle_id, current_data)

            if result:
                self.page.open(ft.SnackBar(content=LocalizedText(localization=self.loc, text_key="msg_editar_conta")))
                self.page.go("/vehicles")
                self.page.update()
            else:
                self.page.open(ft.SnackBar(content=LocalizedText(localization=self.loc, text_key="erro_editar_vehic")))
                self.page.update()
        except Exception as ex:
            # print(f"Error saving vehicle data: {ex}")
            self.page.open(ft.SnackBar(content=LocalizedText(localization=self.loc, text_key="erro_editar_vehic")))
            self.page.update()

