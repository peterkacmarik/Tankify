import datetime
import json
import os
import flet as ft
from core.supa_base import SupabaseUser
from core.lang_manager import LanguageManager
from typing import Callable, Dict, Optional, Union, List, Any



class LoginRegisterForgotFields(ft.TextField):
    def __init__(self, validate_field, **kwargs):
        super().__init__(**kwargs)
        self.validate_field = validate_field
        self.lang_manager = LanguageManager(self.page)


    def forgot_email_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=self.lang_manager.get_translation("email"),
                on_change=self.validate_field,
            )
        )
    
    
    def login_email_field(self):
        return ft.TextField(
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            label=self.lang_manager.get_translation("email"),
            on_change=self.validate_field,
        )
        

    def login_password_field(self):
        return ft.TextField(
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            label=self.lang_manager.get_translation("senha"),
            password=True,
            can_reveal_password=True,
            on_change=self.validate_field
        )


    def first_name_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=self.lang_manager.get_translation("primeiro_nome"),
                on_change=self.validate_field
            )
        )
                                                        
                                                        
    def last_name_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=self.lang_manager.get_translation("segundo_nome"),
                on_change=self.validate_field
            )
        )


    def email_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=self.lang_manager.get_translation("email"),
                on_change=self.validate_field,
            )
        )
        
        
    def password_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=self.lang_manager.get_translation("senha"),
                password=True,
                can_reveal_password=True,
                on_change=self.validate_field
            )
        )
        
        
    def repeat_password_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=self.lang_manager.get_translation("senha_repetir"),
                password=True,
                can_reveal_password=True,
                on_change=self.validate_field
            )
        )
        

class CustomUserField(ft.TextField):
    def __init__(self, validate_field):
        super().__init__()
        self.lang_manager = LanguageManager(self.page)  
        self.validate_field = validate_field
        self.supabase_user = SupabaseUser(self.page)
        
         
    def name_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=self.lang_manager.get_translation("nome"),
                on_change=self.validate_field,
            )
        )
    
    
    def user_type_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.Dropdown(
                label=self.lang_manager.get_translation("tipo_usuario"),
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                on_change=self.validate_field,
                options=[
                    ft.dropdown.Option(self.lang_manager.get_translation("tipo_usuario_02")),
                    ft.dropdown.Option(self.lang_manager.get_translation("tipo_usuario_03")),
                ]
            )
        )
        
        
    def driver_license_category_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=self.lang_manager.get_translation("cnh_categoria"),
                on_change=self.validate_field,
            )
        )
        

    def driver_license_expiry_field(self, page: ft.Page):
        # Funkcia na otvorenie DatePicker a spracovanie dátumu
        def on_button_click(e):
            # Nastavíme dialógové okno s DatePicker
            page.dialog = ft.DatePicker(
                first_date=datetime.datetime(year=1960, month=1, day=1),
                last_date=datetime.datetime(year=2050, month=12, day=31),
                on_change=on_date_change,
            )
            page.dialog.open = True  # Otvoríme dialóg
            page.update()  # Aktualizácia stránky pre zobrazenie dialógu

        # Funkcia na aktualizáciu textového poľa po výbere dátumu
        def on_date_change(e):
            date_display.value = e.control.value.strftime('%Y-%m-%d')
            date_display.update()  # Aktualizujeme textové pole
        
        # Textové pole na zobrazenie vybraného dátumu
        date_display = ft.TextField(
            border_color=ft.colors.GREY,
            width=150,
            height=50,
            read_only=True,
            # hint_text="Vybraný dátum",
            label=self.lang_manager.get_translation("cnh_validade"),
            on_change=self.validate_field,
        )
        
        # Tlačidlo na otvorenie DatePicker
        date_picker_button = ft.ElevatedButton(
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
            icon=ft.icons.CALENDAR_MONTH_OUTLINED,
            width=140,
            text=self.lang_manager.get_translation("data"),
            on_click=on_button_click,  # Pri kliknutí spustíme DatePicker
        )
        
        # Návrat rozloženia s tlačidlom a textovým poľom
        return ft.Container(
            width=300,  
            height=50,
            # border=ft.border.all(0.5, ft.colors.GREY),
            # border_radius=10,
            # alignment=ft.alignment.center,
            content=ft.Row(
                controls=[
                    date_picker_button,  # Tlačidlo na výber dátumu
                    date_display,  # Textové pole na zobrazenie vybraného dátumu
                ],
                # alignment=ft.MainAxisAlignment.START,
                # vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

        
    def active_status_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.Dropdown(
                icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
                label=self.lang_manager.get_translation("status"),
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                on_change=self.validate_field,
                options=[
                    ft.dropdown.Option(self.lang_manager.get_translation("ativo")),
                    ft.dropdown.Option(self.lang_manager.get_translation("inativo")),
                ]
            )
        )
        
        
    def user_email_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=self.lang_manager.get_translation("email"),
                on_change=self.validate_field,
            )
        )
    
    
    def vehicle_user_field(self, page: ft.Page):
        vehicle_names = self.supabase_user.get_vehicle_names(page)
        dropdown = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Dropdown(
                icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
                border_color=ft.colors.GREY,
                width=300,
                height=50,
                label=self.lang_manager.get_translation("veiculo_usuario"),
                on_change=self.validate_field,
                options=[ft.dropdown.Option(name) for name in vehicle_names],
            )
        )
        return dropdown
    
    
    
class CustomVehicleField(ft.TextField):
    def __init__(self, validate_field):
        super().__init__()
        self.lang_manager = LanguageManager(self.page)
        self.validate_field = validate_field
        
    def vehicle_name_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=f"{self.lang_manager.get_translation('nome')} ({self.lang_manager.get_translation('opcional')})",
                # on_change=self.validate_field
            )
        )
    
    
    def vehicle_type_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.Dropdown(
                icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
                border_color=ft.colors.GREY,
                width=300,
                height=50,
                label=self.lang_manager.get_translation("tipo_veiculo"),
                on_change=self.validate_field,
                options=[
                    ft.dropdown.Option(self.lang_manager.get_translation("tipo_veiculo_03")),
                    ft.dropdown.Option(self.lang_manager.get_translation("tipo_veiculo_01")),
                    ft.dropdown.Option(self.lang_manager.get_translation("tipo_veiculo_02")),
                    ft.dropdown.Option(self.lang_manager.get_translation("tipo_veiculo_04")),
                ]
            )
        )
        
        
    def vehicle_manufacturer_field(self, page: ft.Page):
        def _load_manufacturers(manufacturer):
            # Načíta JSON súbor podľa jazykového kódu
            file_path = os.path.join("manufacturers", f"{manufacturer}.json")
            with open(file_path, "r", encoding="utf-8") as file:
                manufacturers = json.load(file)
            return [item['nome'] for item in manufacturers]
        
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
                                ))
                        ))
            else:
                search_results.visible = False
            page.update()

        # Funkcia na nastavenie vybraného výrobcu ako hodnoty vo `TextField`
        def select_manufacturer(e):
            search_input.value = e.control.text
            search_results.visible = False
            search_results.controls.clear()
            page.update()
        
        search_input = ft.TextField(
            icon=ft.icons.SHIELD,
            width=300,
            border_color=ft.colors.GREY,
            hint_text=self.lang_manager.get_translation("marca"),
            on_change=filter_manufacturers,
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
        
        
    def vehicle_model_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=self.lang_manager.get_translation("modelo"),
                on_change=self.validate_field
            )
        )
        
        
    def vehicle_active_status_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.Dropdown(
                icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
                label=self.lang_manager.get_translation("status"),
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                on_change=self.validate_field,
                options=[
                    ft.dropdown.Option(self.lang_manager.get_translation("ativo")),
                    ft.dropdown.Option(self.lang_manager.get_translation("inativo")),
                ]
            )
        )
    
    
    def vehicle_year_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=f"{self.lang_manager.get_translation('ano')} ({self.lang_manager.get_translation('opcional')})",
                # on_change=self.validate_field
            )
        )
        
        
    def vehicle_fuel_type_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.Dropdown(
                icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
                border_color=ft.colors.GREY,
                width=300,
                height=50,
                label=self.lang_manager.get_translation("tipo_combustivel"),
                # on_change=self.validate_field,
                options=[
                    ft.dropdown.Option(self.lang_manager.get_translation("tipo_combustivel_03")),
                    ft.dropdown.Option(self.lang_manager.get_translation("tipo_combustivel_04")),
                    ft.dropdown.Option(self.lang_manager.get_translation("tipo_combustivel_02")),
                    ft.dropdown.Option(self.lang_manager.get_translation("tipo_combustivel_01")),
                ]
            )
        )
        
        
        
    def vehicle_fuel_capacity_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=self.lang_manager.get_translation("volume_tanque_litros"),
                # on_change=self.validate_field
            )
        )
        
        
    def vehicle_unit_measurement_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.Dropdown(
                icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
                border_color=ft.colors.GREY,
                width=300,
                height=50,
                label=self.lang_manager.get_translation("unit_of_measure"),
                # on_change=self.validate_field,
                options=[
                    ft.dropdown.Option(self.lang_manager.get_translation("distancia_01")),
                    ft.dropdown.Option(self.lang_manager.get_translation("distancia_02")),
                ]
            )
        )
        
        
    def vehicle_license_plate_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=f"{self.lang_manager.get_translation('placa')} ({self.lang_manager.get_translation('opcional')})",
                # on_change=self.validate_field
            )
        )
        
    
    def vehicle_chassis_number_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=f"{self.lang_manager.get_translation('chassi')} ({self.lang_manager.get_translation('opcional')})",
                # on_change=self.validate_field
            )
        )
        
        
    def vehicle_vin_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=f"{self.lang_manager.get_translation('renavam')} ({self.lang_manager.get_translation('opcional')})",
                # on_change=self.validate_field
            )
        )
        
        
    def vehicle_notes_field(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(
                icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
                width=300,
                height=50,
                border_color=ft.colors.GREY,
                label=self.lang_manager.get_translation("observacao"),
                # on_change=self.validate_field
            )
        )