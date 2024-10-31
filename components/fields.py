import flet as ft



def first_name_field(translation, validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            width=300,
            border_color=ft.colors.GREY,
            label=translation["primeiro_nome"],
            on_change=validate_field
        )
    )
                                                    
                                                    
def last_name_field(translation, validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            width=300,
            border_color=ft.colors.GREY,
            label=translation["segundo_nome"],
            on_change=validate_field
        )
    )


def email_field(translation, validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            width=300,
            border_color=ft.colors.GREY,
            label=translation["email"],
            on_change=validate_field,
        )
    )
    

def password_field(translation, validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            width=300,
            border_color=ft.colors.GREY,
            label=translation["senha"],
            password=True,
            can_reveal_password=True,
            on_change=validate_field
        )
    )
    
def repeat_password_field(translation, validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            width=300,
            border_color=ft.colors.GREY,
            label=translation["senha_repetir"],
            password=True,
            can_reveal_password=True,
            on_change=validate_field
        )
    )
    
    
def confirm_password_field(translation, validate_field):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            width=300,
            border_color=ft.colors.GREY,
            label=translation["senha"],
            password=True,
            can_reveal_password=True,
            on_change=validate_field
        )
    )