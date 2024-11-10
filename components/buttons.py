import flet as ft
from core.auth_google import handle_google_login
from core.lang_manager import LanguageManager


class LoginButtons:
    def __init__(self, page: ft.Page):
        self.page = page
        self.lang_manager = LanguageManager(self.page)
        
    def facebook_login_button(self):
        return ft.OutlinedButton(
            width=150,
            height=60,
            text=self.lang_manager.get_translation("facebook"),
            icon=ft.icons.FACEBOOK,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.WHITE,
                overlay_color=ft.colors.WHITE,
                side={
                    "": ft.BorderSide(width=0.5, color=ft.colors.GREY),
                    "hovered": ft.BorderSide(width=0.5, color=ft.colors.BLACK),
                },
            ),
            on_click=lambda _: self.page.go("/login"),
        )
        
    def google_login_button(self):
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
                    ft.Text(self.lang_manager.get_translation("google")),
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
            on_click=lambda e: handle_google_login(e, self.page),
        )
        
    def login_button(self, handle_login):
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
                text=self.lang_manager.get_translation("login").upper(), 
                color=ft.colors.WHITE,
                on_click=handle_login,
            ),
        )

    def logout_button(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.ElevatedButton(
                bgcolor=ft.colors.BLUE_700,
                style=ft.ButtonStyle(
                    overlay_color=ft.colors.BLUE_900,
                ),
                width=200,
                height=50,
                text=self.lang_manager.get_translation("logoff"), 
                color=ft.colors.WHITE,
                on_click=lambda _: self.page.go("/login"),
            ),
        )
    
    
    
class RegisterButtons:
    def __init__(self, page: ft.Page):
        self.page = page
        self.lang_manager = LanguageManager(self.page)
    
    def register_button_facebook(self):
        return ft.Container(
            # padding=ft.padding.only(20, 0, 20, 0),
            alignment=ft.alignment.center,
            content=ft.OutlinedButton(
                width=300,
                height=60,
                expand=True,
                text=self.lang_manager.get_translation("criar_conta_com_facebook"),
                icon=ft.icons.FACEBOOK,
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.WHITE,
                    overlay_color=ft.colors.WHITE,
                    side={
                        "": ft.BorderSide(width=0.5, color=ft.colors.GREY),
                        "hovered": ft.BorderSide(width=0.5, color=ft.colors.BLACK),
                    },
                ),
                on_click=lambda e: self.page.go("/login")
            )
        )

        
    def register_button_google(self):
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
                        ft.Text(self.lang_manager.get_translation("criar_conta_com_google")),
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
                on_click=lambda e: handle_google_login(e, self.page),
            )
        )
        
        
    def register_button(self, handle_register):
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
                text=self.lang_manager.get_translation("criar_conta").upper(),
                color=ft.colors.WHITE,
                on_click=handle_register
            )
        )
        
        
    def cancel_button(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextButton(
                text=self.lang_manager.get_translation("btn_cancelar").upper(),
                style=ft.ButtonStyle(
                    overlay_color=ft.colors.TRANSPARENT,
                ),
                on_click=lambda e: self.page.go("/login")
            )
        )
        
    
    def button_on_register(self, handle_data):
        return ft.Container(
            # padding=ft.padding.only(left=20, top=10, right=20, bottom=0),
            alignment=ft.alignment.center,
            content=ft.ElevatedButton(
                disabled=True,
                bgcolor=ft.colors.BLUE_700,
                text=self.lang_manager.get_translation("btn_cadastrar").upper(),
                width=200,
                height=50,
                style=ft.ButtonStyle(
                    overlay_color=ft.colors.BLUE_900,
                ),
                color=ft.colors.WHITE,
                on_click=handle_data
            )
        )
    
    
    
class ForgotPasswordButtons:
    def __init__(self, page: ft.Page):
        self.page = page
        self.lang_manager = LanguageManager(self.page)

    def send_button(self, handle_forgot_password):
        return ft.Container(
            padding=ft.padding.only(left=20, top=10, right=20, bottom=0),
            alignment=ft.alignment.center,
            content=ft.ElevatedButton(
                disabled=True,
                bgcolor=ft.colors.BLUE_700,
                text=self.lang_manager.get_translation("btn_enviar").upper(),
                width=300,
                height=50,
                style=ft.ButtonStyle(
                    overlay_color=ft.colors.BLUE_900,
                ),
                color=ft.colors.WHITE,
                on_click=handle_forgot_password
            )
        )
        
    
    
    
def floating_action_button(dialog_window):
    return ft.FloatingActionButton(
            icon=ft.icons.ADD, 
            shape=ft.CircleBorder(type="circle"), 
            on_click=dialog_window,
        )
    
    

    

