import flet as ft



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