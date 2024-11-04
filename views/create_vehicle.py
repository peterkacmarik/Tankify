import flet as ft
from components.buttons import floating_action_button, button_on_register
from components.fields import (
    CustomVehicleField,
)
from components.navigations import app_bar, navigation_bottom_bar, left_drawer
from core.page_classes import ManageDialogWindow
from locales.language_manager import LanguageManager

from core.supa_base import get_supabese_client, SupabaseVehicle
from views.base_page import BaseView


class CreateVehicles(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__("/vehicle/create", page)
        self.page = page
        self.lang_manager = LanguageManager()
        self.supabase_vehicle = SupabaseVehicle()
        
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
        
        self.custom_vehicle_field = CustomVehicleField(self.validate_fields)
        
        self.vehicle_type_field = self.custom_vehicle_field.vehicle_type_field()
        self.manufacturer_field = self.custom_vehicle_field.vehicle_manufacturer_field(self.page)
        self.vehicle_model_field = self.custom_vehicle_field.vehicle_model_field()
        self.vehicle_year_field = self.custom_vehicle_field.vehicle_year_field()
        self.vehicle_name_field = self.custom_vehicle_field.vehicle_name_field()
        self.vehicle_fuel_type_field = self.custom_vehicle_field.vehicle_fuel_type_field()
        self.vehicle_fuel_capacity_field = self.custom_vehicle_field.vehicle_fuel_capacity_field()
        self.vehicle_unit_measurement_field = self.custom_vehicle_field.vehicle_unit_measurement_field()
        self.vehicle_license_plate_field = self.custom_vehicle_field.vehicle_license_plate_field()
        self.vehicle_chassis_number_field = self.custom_vehicle_field.vehicle_chassis_number_field()
        self.vehicle_vin_field = self.custom_vehicle_field.vehicle_vin_field()
        self.vehicle_notes_field = self.custom_vehicle_field.vehicle_notes_field()
        
        self.active_status_field = self.custom_vehicle_field.vehicle_active_status_field()
        
        # self.form_fields = self.build_form_fields()
        self.register_button = button_on_register(self.handle_add_vehicle_data)
        
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
                                    self.vehicle_name_field,
                                    self.vehicle_type_field,
                                    self.manufacturer_field,
                                    self.vehicle_model_field,
                                    self.vehicle_year_field,
                                    self.vehicle_fuel_type_field,
                                    self.vehicle_fuel_capacity_field,
                                    self.vehicle_unit_measurement_field,
                                    self.vehicle_license_plate_field,
                                    self.vehicle_chassis_number_field,
                                    self.vehicle_vin_field,
                                    self.vehicle_notes_field,
                                    self.active_status_field,
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
        vehicle_model = self.vehicle_model_field.content.value
        vehicle_type = self.vehicle_type_field.content.value
        active_status = self.active_status_field.content.value
        
        # Aktivujeme tlačidlo len ak sú polia vyplnené
        if vehicle_model and active_status and vehicle_type:
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
                        text=self.lang_manager.get_text("veiculos"),
                        on_click=lambda e: self.go_to_vehicles(e),
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
    
    
    def go_to_vehicles(self, e):
        e.page.go("/vehicles")
        
        
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
    
        
    def handle_add_vehicle_data(self, e):
        vehicle_model = self.vehicle_model_field.content.value
        vehicle_name = self.vehicle_name_field.content.value
        vehicle_type = self.vehicle_type_field.content.value
        active_status = self.active_status_field.content.value
        manufacturer = self.manufacturer_field.content.controls[0].value
        year = self.vehicle_year_field.content.value
        fuel_type = self.vehicle_fuel_type_field.content.value
        fuel_capacity = self.vehicle_fuel_capacity_field.content.value
        unit_measure = self.vehicle_unit_measurement_field.content.value
        license_plate = self.vehicle_license_plate_field.content.value
        chassis_number = self.vehicle_chassis_number_field.content.value
        vin = self.vehicle_vin_field.content.value
        notes = self.vehicle_notes_field.content.value
            
        vehicle_data: dict = {
                "vehicle": vehicle_type,
                "manufacturer": manufacturer,
                "model": vehicle_model,
                "year": year,
                "name": vehicle_name,
                "fuel_type": fuel_type,
                "fuel_capacity": fuel_capacity,
                "unit_measure": unit_measure,
                "license_plate": license_plate,
                "chassis_number": chassis_number,
                "vin": vin,
                "notes": notes,
                "is_active": active_status,
            }
        try:
            self.supabase_vehicle.create_vehicle_in_table_vehicles(self.page, vehicle_data)

            self.page.go("/vehicles")
            self.page.open(ft.SnackBar(content=ft.Text(self.lang_manager.get_text("msg_cadastra_veiculo"))))
            
            # return response.data
        except Exception as ex:
            print(f"Error adding user data: {ex}")
            return None

        
    
    
    # def build_form_fields(self):
    #     form_fields = ft.Container(
    #         # alignment=ft.alignment.center,
    #         # border=ft.border.all(0.5, ft.colors.GREY_400),
    #         # border_radius=10,
    #         padding=ft.padding.only(20, 20, 20, 20),
    #         content=ft.Column(
    #             alignment=ft.MainAxisAlignment.START,
    #             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    #             controls=[
    #                 self.vehicle_name_field,
    #                 self.vehicle_type_field,
    #                 self.active_status_field,
                    
    #             ]
    #         )
    #     )
    #     return form_fields
    
    
    
    