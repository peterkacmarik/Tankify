import flet as ft
from locales.open_files import get_manufacturers
from locales.language_manager import LanguageManager


lang_manager = LanguageManager()

def login_email_field(validate_field):
    return ft.TextField(
        width=300,
        border_color=ft.colors.GREY,
        label=lang_manager.get_text("email"),
        on_change=validate_field,
    )
    

def login_password_field(validate_field):
    return ft.TextField(
        width=300,
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
            border_color=ft.colors.GREY,
            label=lang_manager.get_text("senha"),
            password=True,
            can_reveal_password=True,
            on_change=validate_field
        )
    )
    
    
def vehicle_type_field():
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.Dropdown(
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            border_color=ft.colors.GREY,
            bgcolor=ft.colors.WHITE,
            width=300,
            # border=ft.border.all(0.5, ft.colors.GREY),
            label=lang_manager.get_text("tipo_veiculo"),
            options=[
                ft.dropdown.Option(lang_manager.get_text("tipo_veiculo_03")),
                ft.dropdown.Option(lang_manager.get_text("tipo_veiculo_01")),
                ft.dropdown.Option(lang_manager.get_text("tipo_veiculo_02")),
                ft.dropdown.Option(lang_manager.get_text("tipo_veiculo_04")),
            ]
        )
    )
    


def manufacturer_field(page: ft.Page):
    manufacturers = get_manufacturers()
    search_results = ft.ListView(
            spacing=5
        )

    
    # Funkcia na filtrovanie výrobcov podľa vstupu
    def filter_manufacturers(e):
        search_text = e.control.value.lower()  # získa zadaný text
        filtered = [m for m in manufacturers if search_text in m.lower()]  # filtrovanie

        # Vymazanie starých výsledkov a pridanie nových
        search_results.controls.clear()
        for manufacturer in filtered:
            search_results.controls.append(ft.TextButton(manufacturer, on_click=select_manufacturer))
        page.update()

    # Funkcia na nastavenie vybraného výrobcu ako hodnoty vo `TextField`
    def select_manufacturer(e):
        search_input.value = e.control.text  # nastavenie textu vo `TextField`
        search_results.controls.clear()  # vyčistenie výsledkov po výbere
        page.update()
    
    # Vstupné pole na vyhľadávanie výrobcov
    search_input = ft.TextField(
            icon=ft.icons.SHIELD,
            width=300,
            border_color=ft.colors.GREY,
            hint_text=lang_manager.get_text("marca"),
            on_change=filter_manufacturers,  # Pripojenie funkcie na zmenu textu
        )
        
    return ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column(
                controls=[
                    search_input,
                    
                ]
            )
        ), search_results
    
    
def model_field():
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            border_color=ft.colors.GREY,
            label=lang_manager.get_text("modelo"),
        )
    )


def vehicle_name_field():
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
            width=300,
            border_color=ft.colors.GREY,
            label=lang_manager.get_text["nome_carro"],
        )
    )
    
    
    
    
    
    