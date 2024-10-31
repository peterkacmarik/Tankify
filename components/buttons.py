import flet as ft
from core.auth_google import handle_google_login


def facebook_login_button(translation, page: ft.Page):
    return ft.OutlinedButton(
        width=140,
        height=60,
        text=translation["facebook"],
        icon=ft.icons.FACEBOOK,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.WHITE,
            overlay_color=ft.colors.WHITE,
            side={
                "": ft.BorderSide(width=0.5, color=ft.colors.GREY),
                "hovered": ft.BorderSide(width=0.5, color=ft.colors.BLACK),
            },
        ),
        on_click=lambda _: page.go("/login"),
    )
    

def google_login_button(translation, page: ft.Page):
    return ft.OutlinedButton(
        width=140,
        height=60,
        content=ft.Row(
            controls=[
                ft.Image(
                    src="https://cdn-icons-png.flaticon.com/512/300/300221.png",
                    width=18,
                    height=18,
                    fit=ft.ImageFit.CONTAIN,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                ),
                ft.Text(translation["google"]),
            ]
        ),
        style=ft.ButtonStyle(
            bgcolor=ft.colors.WHITE,
            overlay_color=ft.colors.WHITE,
            side={
                "": ft.BorderSide(width=0.5, color=ft.colors.GREY),
                "hovered": ft.BorderSide(width=0.5, color=ft.colors.BLACK),
            },
        ),
        on_click=lambda e: handle_google_login(e, page),
    )
    
    
def login_button(translation, page: ft.Page, handle_login):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.ElevatedButton(
            disabled=True,
            bgcolor=ft.colors.BLUE_700,
            style=ft.ButtonStyle(
                overlay_color=ft.colors.BLUE_900,
            ),
            width=300,
            height=50,
            text=translation["login"].upper(), 
            color=ft.colors.WHITE,
            on_click=handle_login,
        ),
    )


def logout_button(translation, page: ft.Page):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.ElevatedButton(
            bgcolor=ft.colors.BLUE_700,
            style=ft.ButtonStyle(
                overlay_color=ft.colors.BLUE_900,
            ),
            width=200,
            height=50,
            text=translation["logoff"], 
            color=ft.colors.WHITE,
            on_click=lambda _: page.go("/login"),
        ),
    )
    
    
def register_button_facebook(translation, page: ft.Page):
    return ft.Container(
        # padding=ft.padding.only(20, 0, 20, 0),
        alignment=ft.alignment.center,
        content=ft.OutlinedButton(
            width=300,
            height=60,
            expand=True,
            text=translation["criar_conta_com_facebook"],
            icon=ft.icons.FACEBOOK,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.WHITE,
                overlay_color=ft.colors.WHITE,
                side={
                    "": ft.BorderSide(width=0.5, color=ft.colors.GREY),
                    "hovered": ft.BorderSide(width=0.5, color=ft.colors.BLACK),
                },
            ),
            on_click=lambda e: page.go("/login")
        )
    )

    
def register_button_google(translation, page: ft.Page):
    return ft.Container(
        # padding=ft.padding.only(20, 0, 20, 0),
        alignment=ft.alignment.center,
        content=ft.OutlinedButton(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Image(
                        src="https://cdn-icons-png.flaticon.com/512/300/300221.png",
                        width=18,
                        height=18,
                        fit=ft.ImageFit.CONTAIN,
                        repeat=ft.ImageRepeat.NO_REPEAT,
                    ),
                    ft.Text(translation["criar_conta_com_google"]),
                ]
            ),
            width=300,
            height=60,
            expand=True,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.WHITE,
                overlay_color=ft.colors.WHITE,
                side={
                    "": ft.BorderSide(width=0.5, color=ft.colors.GREY),
                    "hovered": ft.BorderSide(width=0.5, color=ft.colors.BLACK),
                },
            ),
            on_click=lambda e: handle_google_login(e, page),
        )
    )
    
    
def register_button(translation, handle_register):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.ElevatedButton(
            disabled=True,
            bgcolor=ft.colors.BLUE_700,
            style=ft.ButtonStyle(
                overlay_color=ft.colors.BLUE_900,
            ),
            width=300,
            height=50,
            text=translation["criar_conta"].upper(),
            color=ft.colors.WHITE,
            on_click=handle_register
        )
    )
    
    
def cancel_button(translation, page: ft.Page):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextButton(
            text=translation["btn_cancelar"].upper(),
            style=ft.ButtonStyle(
                overlay_color=ft.colors.TRANSPARENT,
            ),
            on_click=lambda e: page.go("/login")
        )
    )
    
    
def send_button(translation, page: ft.Page, handle_forgot_password):
    return ft.Container(
        padding=ft.padding.only(left=20, top=10, right=20, bottom=0),
        alignment=ft.alignment.center,
        content=ft.ElevatedButton(
            disabled=True,
            bgcolor=ft.colors.BLUE_700,
            text=translation["btn_enviar"].upper(),
            width=300,
            height=50,
            style=ft.ButtonStyle(
                overlay_color=ft.colors.BLUE_900,
            ),
            color=ft.colors.WHITE,
            on_click=handle_forgot_password
        )
    )
    
    
def log_in_button_home_page(translation, page: ft.Page):
    return ft.Container(
        padding=ft.padding.only(left=20, top=10, right=20, bottom=0),
        alignment=ft.alignment.center,
        content=ft.ElevatedButton(
            disabled=False,
            bgcolor=ft.colors.BLUE_700,
            text=translation["login"].upper(),
            width=150,
            height=50,
            style=ft.ButtonStyle(
                overlay_color=ft.colors.BLUE_900,
            ),
            color=ft.colors.WHITE,
            on_click=lambda _: page.go("/login")
        )
    )