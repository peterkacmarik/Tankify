import datetime
import flet as ft
from locales.open_files import get_manufacturers
from locales.language_manager import LanguageManager


lang_manager = LanguageManager()

def login_email_field(validate_field):
    return ft.TextField(
        width=300,
        height=50,
        border_color=ft.colors.GREY,
        label=lang_manager.get_text("email"),
        on_change=validate_field,
    )
    

def login_password_field(validate_field):
    return ft.TextField(
        width=300,
        height=50,
        border_color=ft.colors.GREY,
        label=lang_manager.get_text("senha"),
        password=True,
        can_reveal_password=True,
        on_change=validate_field
    )


def first_name_field(validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            label=lang_manager.get_text("primeiro_nome"),
            on_change=validate_field
        )
    )
                                                    
                                                    
def last_name_field(validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            label=lang_manager.get_text("segundo_nome"),
            on_change=validate_field
        )
    )


def email_field(validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            label=lang_manager.get_text("email"),
            on_change=validate_field,
        )
    )
    
    
def password_field(validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            label=lang_manager.get_text("senha"),
            password=True,
            can_reveal_password=True,
            on_change=validate_field
        )
    )
    
    
def repeat_password_field(validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            label=lang_manager.get_text("senha_repetir"),
            password=True,
            can_reveal_password=True,
            on_change=validate_field
        )
    )
    
    
def confirm_password_field(validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            label=lang_manager.get_text("senha"),
            password=True,
            can_reveal_password=True,
            on_change=validate_field
        )
    )    

    
def model_field():
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            label=lang_manager.get_text("modelo"),
        )
    )
    
    
def name_field(validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            label=lang_manager.get_text("nome"),
            on_change=validate_field,
        )
    )
    
    
def user_type_field(validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.Dropdown(
            label=lang_manager.get_text("tipo_usuario"),
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            on_change=validate_field,
            options=[
                ft.dropdown.Option(lang_manager.get_text("tipo_usuario_02")),
                ft.dropdown.Option(lang_manager.get_text("tipo_usuario_03")),
            ]
        )
    )
    
    
def driver_license_category_field(validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            label=lang_manager.get_text("cnh_categoria"),
            on_change=validate_field,
        )
    )
    

def driver_license_expiry_field(page: ft.Page, validate_field):
    # Funkcia na otvorenie DatePicker a spracovanie dátumu
    def on_button_click(e):
        # Nastavíme dialógové okno s DatePicker
        page.dialog = ft.DatePicker(
            first_date=datetime.datetime(year=2023, month=10, day=1),
            last_date=datetime.datetime(year=2024, month=10, day=1),
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
        label=lang_manager.get_text("cnh_validade"),
        on_change=validate_field,
    )
    
    # Tlačidlo na otvorenie DatePicker
    date_picker_button = ft.ElevatedButton(
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        icon=ft.icons.CALENDAR_MONTH_OUTLINED,
        width=140,
        text=lang_manager.get_text("data"),
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

    
def active_status_field(validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.Dropdown(
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            label=lang_manager.get_text("status"),
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            on_change=validate_field,
            options=[
                ft.dropdown.Option(lang_manager.get_text("ativo")),
                ft.dropdown.Option(lang_manager.get_text("inativo")),
            ]
        )
    )
    
#-------------------------------------------------------------------------------
    
    
def vehicle_name_field(validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            label=lang_manager.get_text("nome_carro"),
            on_change=validate_field
        )
    )
    
    
def vehicle_type_field(validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.Dropdown(
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            border_color=ft.colors.GREY,
            width=300,
            height=50,
            # border=ft.border.all(0.5, ft.colors.GREY),
            label=lang_manager.get_text("tipo_veiculo"),
            on_change=validate_field,
            options=[
                ft.dropdown.Option(lang_manager.get_text("tipo_veiculo_03")),
                ft.dropdown.Option(lang_manager.get_text("tipo_veiculo_01")),
                ft.dropdown.Option(lang_manager.get_text("tipo_veiculo_02")),
                ft.dropdown.Option(lang_manager.get_text("tipo_veiculo_04")),
            ]
        )
    )
    
    
def manufacturer_field(page: ft.Page):
    manufacturers: list = get_manufacturers()
    
    search_results = ft.ListView(
        spacing=5,
        height=200,  # pridáme výšku pre zobrazenie výsledkov
        visible=False  # na začiatku skryjeme zoznam
    )
    
    # Funkcia na filtrovanie výrobcov podľa vstupu
    def filter_manufacturers(e):
        search_text = e.control.value.lower()
        filtered = [m for m in manufacturers if search_text in m.lower()]
        
        search_results.controls.clear()
        if search_text:  # zobrazíme výsledky len ak je nejaký text
            search_results.visible = True
            for manufacturer in filtered:
                search_results.controls.append(ft.TextButton(
                    text=manufacturer, 
                    on_click=select_manufacturer
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
        hint_text=lang_manager.get_text("marca"),
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
    
    
def vehicle_model_field(validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            height=50,
            border_color=ft.colors.GREY,
            label=lang_manager.get_text("modelo"),
            on_change=validate_field
        )
    )
    