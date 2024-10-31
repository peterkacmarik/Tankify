import flet as ft
from components.logo import home_page_logo, page_logo
from components.buttons import log_in_button_home_page

def line_separator(translation):
    return ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Container(
                bgcolor=ft.colors.GREY,
                height=0.5,
                width=130,
                # expand=True
            ),
            ft.Text(
                value=translation["ou"].lower(),
            ),
            ft.Container(
                bgcolor=ft.colors.GREY,
                height=0.5,
                width=130,
                # expand=True
            ),
        ]
    )
    
    
def main_login_text(translation):
    return ft.Text(
        translation["login"],
        size=24,
        weight=ft.FontWeight.NORMAL,
        font_family="Roboto_Slap",
    )
    
    
def forgot_password_link(translation, page: ft.Page):
    return ft.Container(
        # border=ft.border.all(0),
        alignment=ft.alignment.center,
        content=ft.TextButton(
            content=ft.Text(
                value=translation["esqueceu_sua_senha"],
                style=ft.TextStyle(
                    size=13,
                    decoration=ft.TextDecoration.UNDERLINE
                )
            ),
            style=ft.ButtonStyle(
                overlay_color=ft.colors.TRANSPARENT,
            ),
            on_click=lambda _: page.go("/forgot-password"),
        )
    )
    
    
def create_account_link(translation, page: ft.Page):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextButton(
            text=translation["criar_conta"].upper(),
            style=ft.ButtonStyle(
                overlay_color=ft.colors.TRANSPARENT,
            ),
            on_click=lambda _: page.go("/register"),
        )
    )
    
    
def main_register_text(translation):
    return ft.Container(
        # border=ft.border.all(0),
        alignment=ft.alignment.center,
        content=ft.Text(
            translation["criar_conta_drivvo"],
            size=24,
            weight=ft.FontWeight.NORMAL,
            font_family="Roboto_Slap",
        )        
    )
    
    
def sub_register_text(translation):
    return ft.Container(
        # border=ft.border.all(0),
        alignment=ft.alignment.center,
        content=ft.Text(
            translation["comece_gerenciamento_gratuito"],
            size=15,
            weight=ft.FontWeight.NORMAL,
            color=ft.colors.GREY_600,
        )
    )
    
    
def main_forgot_password_text(translation):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.Text(
            translation["esqueceu_sua_senha"],
            size=24,
            weight=ft.FontWeight.NORMAL,
            font_family="Roboto_Slap",
        )
    )
    
    
def sub_forgot_password_text(translation):
    return ft.Container(
        padding=ft.padding.only(bottom=20),
        alignment=ft.alignment.center,
        content=ft.Text(
            translation["ajudaremos_redefinir"],
            size=16,
            weight=ft.FontWeight.NORMAL,
            font_family="Roboto_Slab",
        )
    )
    
    
def cancel_link(translation, page: ft.Page):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextButton(
            text=translation["btn_cancelar"].upper(),
            style=ft.ButtonStyle(
                overlay_color=ft.colors.TRANSPARENT,
            ),
            on_click=lambda _: page.go("/login")
        )
    )
    
    

def home_page_box(translation, page: ft.Page):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.Column(
            alignment=ft.alignment.center,
            controls=[
                ft.Stack(
                    alignment=ft.alignment.center,
                    controls=[
                        # Spodný rámček
                        ft.Container(
                            alignment=ft.alignment.center,
                            width=400,
                            height=300,
                            top=100,  # posunie rámček nižšie
                            border_radius=20,
                            border=ft.border.all(1, ft.colors.GREY_500),
                            bgcolor=ft.colors.WHITE,
                            padding=ft.padding.only(left=20, top=70, right=20, bottom=20),
                            content=ft.Column(
                                spacing=10,
                                alignment=ft.alignment.center,
                                controls=[
                                    ft.Text(
                                        value=translation["home_personal_use_desc"],
                                        size=16,
                                        weight=ft.FontWeight.NORMAL,
                                        font_family="Roboto_Slap",
                                    ),
                                    log_in_button_home_page(translation=translation, page=page),
                                ]
                            )
                        ),
                        
                        # Logo prekrývajúce rámček
                        ft.Column(
                            alignment=ft.alignment.center,
                            top=40,
                            controls=[
                                ft.Container(
                                    content=ft.Image(
                                        src="/logo/logo_147.png",
                                        width=128,
                                        height=128,
                                    ),
                                    width=128,
                                    height=128,
                                    # bgcolor=ft.colors.WHITE,
                                    # border=ft.border.all(1, ft.colors.GREY_500),
                                    border_radius=100,
                                )
                            ]
                        )
                    ],
                    width=600,
                    height=800,
                )
            ]
        )
    )
    
    
    
    