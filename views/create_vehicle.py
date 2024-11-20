import os
import json
import flet as ft

from core.supa_base import SupabaseVehicle
from locales.localization import (
    LocalizedTextButton,
    LocalizedText,
    LocalizedElevatedButton,
    LocalizedTextField,
    LocalizedDropdown
)
from views.base_page import BaseView


class CreateVehicles(BaseView):
    def __init__(self, page: ft.Page, loc):
        super().__init__(page, loc)
        self.page = page
        self.setup_app_bar()

        self.supabase_vehicle = SupabaseVehicle(self.page)

        # self.navigation_header_bar = self.build_navigation_header_bar()
        self.control_panel = self.build_control_panel()

        self.vehicle_name_field = LocalizedTextField(
            localization=self.loc,
            text_key="nome",
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            on_change=lambda _: self.validate_fields()
        )

        options_vehicle_type = [
            {"key": "tipo_veiculo_01"},
            {"key": "tipo_veiculo_02"},
            {"key": "tipo_veiculo_03"},
            {"key": "tipo_veiculo_04"}
        ]

        self.vehicle_type_field = LocalizedDropdown(
            localization=self.loc,
            label_key="tipo_veiculo",
            options_keys=options_vehicle_type,
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            border_color=ft.colors.GREY,
            width=300,
            height=50,
            # on_change=self.validate_field,
        )

        self.manufacturer_field = self.vehicle_manufacturer_field()

        self.vehicle_model_field = LocalizedTextField(
            localization=self.loc,
            text_key="modelo",
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            on_change=lambda _: self.validate_fields()
        )

        self.vehicle_year_field = LocalizedTextField(
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
        self.vehicle_fuel_type_field = LocalizedDropdown(
            localization=self.loc,
            label_key="tipo_combustivel",
            options_keys=options_fuel_type,
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            border_color=ft.colors.GREY,
            width=300,
            height=50,
            # on_change=self.validate_field,
        )
        self.vehicle_fuel_capacity_field = LocalizedTextField(
            localization=self.loc,
            text_key="volume_tanque_litros",
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            on_change=lambda _: self.validate_fields()
        )

        options_unit_measurement = [
            {"key": "distancia_01"},
            {"key": "distancia_02"},
        ]
        self.vehicle_unit_measurement_field = LocalizedDropdown(
            localization=self.loc,
            label_key="unit_of_measure",
            options_keys=options_unit_measurement,
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            border_color=ft.colors.GREY,
            width=300,
            height=50,
            # on_change=self.validate_field,
        )

        self.vehicle_license_plate_field = LocalizedTextField(
            localization=self.loc,
            text_key="placa",
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            # on_change=self.validate_field
        )

        self.vehicle_chassis_number_field = LocalizedTextField(
            localization=self.loc,
            text_key="chassi",
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            # on_change=self.validate_field
        )

        self.vehicle_vin_field = LocalizedTextField(
            localization=self.loc,
            text_key="renavam",
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            # on_change=self.validate_field
        )

        self.vehicle_notes_field = LocalizedTextField(
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
        self.active_status_field = LocalizedDropdown(
            localization=self.loc,
            label_key="status",
            options_keys=options_active_status,
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            on_change=lambda _: self.validate_fields()
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
            on_click=self.handle_add_vehicle_data
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
                                    ft.Container(content=self.vehicle_name_field, alignment=ft.alignment.center),
                                    ft.Container(content=self.vehicle_type_field, alignment=ft.alignment.center),
                                    self.manufacturer_field,
                                    ft.Container(content=self.vehicle_model_field, alignment=ft.alignment.center),
                                    ft.Container(content=self.vehicle_year_field, alignment=ft.alignment.center),
                                    ft.Container(content=self.vehicle_fuel_type_field, alignment=ft.alignment.center),
                                    ft.Container(content=self.vehicle_fuel_capacity_field, alignment=ft.alignment.center),
                                    ft.Container(content=self.vehicle_unit_measurement_field, alignment=ft.alignment.center),
                                    ft.Container(content=self.vehicle_license_plate_field, alignment=ft.alignment.center),
                                    ft.Container(content=self.vehicle_chassis_number_field, alignment=ft.alignment.center),
                                    ft.Container(content=self.vehicle_vin_field, alignment=ft.alignment.center),
                                    ft.Container(content=self.vehicle_notes_field, alignment=ft.alignment.center),
                                    ft.Container(content=self.active_status_field, alignment=ft.alignment.center),
                                    ft.Container(content=self.register_button, alignment=ft.alignment.center, padding=ft.padding.only(bottom=10))
                                ]
                            )
                        )
                    ]
                )
            )
        ]

    def setup_app_bar(self):
        self.appbar.leading = ft.IconButton(
            icon=ft.icons.ARROW_BACK_OUTLINED,
            on_click=lambda _: self.page.go("/vehicles")
        )

    def validate_fields(self):
        # Získame hodnoty z polí
        vehicle_nickname = self.vehicle_name_field.value
        vehicle_manufacterer = self.manufacturer_field.content.controls[0].value
        vehicle_model = self.vehicle_model_field.value
        fuel_capacity = self.vehicle_fuel_capacity_field.value
        active_status = self.active_status_field.value

        # Aktivujeme tlačidlo len ak sú polia vyplnené
        if vehicle_nickname and vehicle_manufacterer and vehicle_model and fuel_capacity and active_status:
        # if vehicle_nickname:
            self.register_button.disabled = False
        else:
            self.register_button.disabled = True

        # Aktualizujeme UI
        self.register_button.update()

    def vehicle_manufacturer_field(self):
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
            icon=ft.icons.SHIELD,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            localization=self.loc,
            text_key="marca",
            on_change=filter_manufacturers,
            on_submit=lambda _: self.validate_fields()
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
                        content=LocalizedText(self.loc, "veiculo")
                    ),
                ]
            )
        )
        return table_header

    def handle_add_vehicle_data(self, e):
        vehicle_type = self.vehicle_type_field.value
        manufacturer = self.manufacturer_field.content.controls[0].value
        vehicle_model = self.vehicle_model_field.value
        year = self.vehicle_year_field.value
        vehicle_name = self.vehicle_name_field.value

        fuel_type = self.vehicle_fuel_type_field.value
        fuel_capacity = self.vehicle_fuel_capacity_field.value
        unit_measure = self.vehicle_unit_measurement_field.value
        license_plate = self.vehicle_license_plate_field.value
        chassis_number = self.vehicle_chassis_number_field.value
        vin = self.vehicle_vin_field.value
        notes = self.vehicle_notes_field.value
        active_status = self.active_status_field.value

        vehicle_data: dict = {
                "vehicle": vehicle_type, # Vehicle type
                "manufacturer": manufacturer, # Manufacturer
                "model": vehicle_model, # Model
                "year": year, # Year
                "name": vehicle_name, # Name
                "fuel_type": fuel_type, # Fuel type
                "fuel_capacity": fuel_capacity, # Fuel capacity
                "unit_measure": unit_measure, # Unit measure
                "license_plate": license_plate, # License plate
                "chassis_number": chassis_number, # Chassis number
                "vin": vin, # VIN
                "notes": notes, # Notes
                "is_active": active_status, # Active
            }
        try:
            self.supabase_vehicle.create_vehicle_in_table_vehicles(self.page, vehicle_data)

            self.page.go("/vehicles")
            self.page.open(ft.SnackBar(content=LocalizedText(self.loc, "msg_cadastra_veiculo")))
            self.page.update()
            # return response.data
        except Exception as ex:
            print(f"Error adding user data: {ex}")
            return None


