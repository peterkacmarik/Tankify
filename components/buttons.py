import flet as ft
from core.auth_google import handle_google_login
from locales.language_manager import LanguageManager


lang_manager = LanguageManager()

def facebook_login_button(page: ft.Page):
    return ft.OutlinedButton(
        width=150,
        height=60,
        text=lang_manager.get_text("facebook"),
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
    

def google_login_button(page: ft.Page):
    return ft.OutlinedButton(
        width=150,
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
                ft.Text(lang_manager.get_text("google")),
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
    
    
def login_button(handle_login):
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
            text=lang_manager.get_text("login").upper(), 
            color=ft.colors.WHITE,
            on_click=handle_login,
        ),
    )


def logout_button(page: ft.Page):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.ElevatedButton(
            bgcolor=ft.colors.BLUE_700,
            style=ft.ButtonStyle(
                overlay_color=ft.colors.BLUE_900,
            ),
            width=200,
            height=50,
            text=lang_manager.get_text("logoff"), 
            color=ft.colors.WHITE,
            on_click=lambda _: page.go("/login"),
        ),
    )
    
    
def register_button_facebook(page: ft.Page):
    return ft.Container(
        # padding=ft.padding.only(20, 0, 20, 0),
        alignment=ft.alignment.center,
        content=ft.OutlinedButton(
            width=300,
            height=60,
            expand=True,
            text=lang_manager.get_text("criar_conta_com_facebook"),
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

    
def register_button_google(page: ft.Page):
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
                    ft.Text(lang_manager.get_text("criar_conta_com_google")),
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
    
    
def register_button(handle_register):
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
            text=lang_manager.get_text("criar_conta").upper(),
            color=ft.colors.WHITE,
            on_click=handle_register
        )
    )
    
    
def cancel_button(page: ft.Page):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextButton(
            text=lang_manager.get_text("btn_cancelar").upper(),
            style=ft.ButtonStyle(
                overlay_color=ft.colors.TRANSPARENT,
            ),
            on_click=lambda e: page.go("/login")
        )
    )
    
    
def send_button(handle_forgot_password):
    return ft.Container(
        padding=ft.padding.only(left=20, top=10, right=20, bottom=0),
        alignment=ft.alignment.center,
        content=ft.ElevatedButton(
            disabled=True,
            bgcolor=ft.colors.BLUE_700,
            text=lang_manager.get_text("btn_enviar").upper(),
            width=300,
            height=50,
            style=ft.ButtonStyle(
                overlay_color=ft.colors.BLUE_900,
            ),
            color=ft.colors.WHITE,
            on_click=handle_forgot_password
        )
    )
    
    
def log_in_button_home_page(page: ft.Page):
    return ft.Container(
        padding=ft.padding.only(left=20, top=10, right=20, bottom=0),
        alignment=ft.alignment.center,
        content=ft.ElevatedButton(
            disabled=False,
            bgcolor=ft.colors.BLUE_700,
            text=lang_manager.get_text("login").upper(),
            width=150,
            height=50,
            style=ft.ButtonStyle(
                overlay_color=ft.colors.BLUE_900,
            ),
            color=ft.colors.WHITE,
            on_click=lambda _: page.go("/login")
        )
    )
    
    
def floating_action_button(dialog_window):
    return ft.FloatingActionButton(
            icon=ft.icons.ADD, 
            shape=ft.CircleBorder(type="circle"), 
            on_click=dialog_window,
        )
    
    
def add_new_user_button(handle_add_user_data):
    return ft.Container(
        # padding=ft.padding.only(left=20, top=10, right=20, bottom=0),
        alignment=ft.alignment.center,
        content=ft.ElevatedButton(
            disabled=True,
            bgcolor=ft.colors.BLUE_700,
            text=lang_manager.get_text("btn_cadastrar").upper(),
            width=200,
            height=50,
            style=ft.ButtonStyle(
                overlay_color=ft.colors.BLUE_900,
            ),
            color=ft.colors.WHITE,
            on_click=handle_add_user_data
        )
    )