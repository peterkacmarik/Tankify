import flet as ft
from core.page_classes import BgColor, LanguageSwitcher
from locales.open_files import get_translation
from components.fields import (
    email_field,
    login_email_field,
    login_password_field, 
    password_field
)
from components.buttons import (
    google_login_button, 
    facebook_login_button,
    login_button
)
from components.logo import (
    page_logo
)
from components.links_separator_text import (
    line_separator,
    main_login_text,
    forgot_password_link,
    create_account_link
)
from locales.language_manager import LanguageManager
from supabase import Client
from core.supa_base import get_supabese_client
from views.base_page import BaseView


class LoginView(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__(route="/login", page=page)
        self.page = page
        self.lang_manager = LanguageManager()
        
        # self.bgcolor = ft.colors.WHITE
        self.bgcolor = BgColor(self.page).get_background_color()
        self.supabase: Client = get_supabese_client()
        
        self.scroll = ft.ScrollMode.HIDDEN
        self.fullscreen_dialog = True
        
        # Snack bar
        self.snack_bar = ft.SnackBar(
            content=ft.Text(""),
            show_close_icon=True
        )
        self.page.overlay.append(self.snack_bar)

        self.language_switch_button = LanguageSwitcher(self.page).language_switch_button
        self.page_logo = page_logo()
        self.login_text = ft.Container(
            alignment=ft.alignment.center,
            content=main_login_text()
        )
        self.social_buttons = ft.Container(
            alignment=ft.alignment.center,
            padding=ft.padding.only(top=20, bottom=10),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    facebook_login_button(self.page),
                    google_login_button(self.page)
                ],
            ),
        )

        self.line_separator = line_separator()
        
        self.login_fields = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    login_email_field(self.validate_fields),
                    login_password_field(self.validate_fields)
                ]
            )
        )
        
        self.forgot_password_link = forgot_password_link(self.page)
        self.login_button = login_button(self.handle_login)
        self.create_account_link = create_account_link(self.page)
        
        # Pridanie komponentov do hlavnej časti stránky
        self.controls = [
            ft.Container(
                alignment=ft.alignment.center,
                padding=ft.padding.only(20, 30, 20, 0),
                content=ft.Column(
                    controls=[
                        self.language_switch_button,
                        self.page_logo,
                        self.login_text,
                        self.social_buttons,
                        self.line_separator,
                        self.login_fields,
                        # self.email_field,
                        # self.password_field,
                        self.forgot_password_link,
                        self.login_button,
                        self.create_account_link
                    ]
                )
            )
        ]
    
    def update_texts(self) -> None:
        # Aktualizácia textov v settings view
        self.login_text.content.value = LanguageManager.get_text("login")
        self.line_separator.controls[1].value = LanguageManager.get_text("ou")
        self.login_fields.content.controls[0].label = LanguageManager.get_text("email")
        self.login_fields.content.controls[1].label = LanguageManager.get_text("senha")
        self.forgot_password_link.content.content.value = LanguageManager.get_text("esqueceu_sua_senha")
        self.login_button.content.text = LanguageManager.get_text("login")
        self.create_account_link.content.text = LanguageManager.get_text("criar_conta")
        self.update()
    
    def validate_fields(self, e=None):
        # Získame hodnoty z polí
        email = self.login_fields.content.controls[0].value
        password = self.login_fields.content.controls[1].value
    
        # Aktivujeme tlačidlo len ak sú obe polia vyplnené
        if email and password:
            self.login_button.content.disabled = False
        else:
            self.login_button.content.disabled = True
            
        # Aktualizujeme UI
        self.login_button.update()

        
    def handle_login(self, e=None):
        try:
            email = self.login_fields.content.controls[0].value
            password = self.login_fields.content.controls[1].value
            
            response = self.supabase.auth.sign_in_with_password(
                credentials={
                    "email": email, 
                    "password": password
                }
            )
            
            if response:
                self.snack_bar.content.value = self.lang_manager.get_text('msg_login')
                self.snack_bar.open = True
                self.page.update()
                
                self.page.go("/history")
                
        except Exception as ex:
            self.snack_bar.content.value = str(ex)
            self.snack_bar.open = True
            self.page.update()
            return
        
        # if user is None:
        #     self.snack_bar.content.value = self.translation["erro_login"]
        #     self.snack_bar.open = True
        #     self.page.update()
        #     return
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #     # # Overenie e-mailu v database
    #     # user = self.user_crud.verify_user_by_email(email)
    #     # if user is None:
    #     #     self.snack_bar.content.value = self.translation["erro_email_invalido"]
    #     #     self.snack_bar.open = True
    #     #     self.page.update()
    #     #     return
        
    #     # # Overenie hesla v database
    #     # verify_user = self.user_crud.verify_user_password(email, password)
    #     # if verify_user is None:
    #     #     self.snack_bar.content.value = self.translation["erro_usuario_senha"]
    #     #     self.snack_bar.open = True
    #     #     self.page.update()
    #     #     return
        
    #     # # Overenie hesla na základe jeho dlzky
    #     # if len(password) < 6:
    #     #     self.snack_bar.content.value = self.translation["erro_quantidade_caracteres_senha"]
    #     #     self.snack_bar.open = True
    #     #     self.page.update()
    #     #     return

    #     # # Ak všetko prejde, zobrazenie správy o úspešnom prihlásení
    #     # self.snack_bar.content.value = self.translation["msg_login"]
    #     # self.snack_bar.open = True
    #     # self.page.update()

    #     # # Presmerovanie na domovskú stránku (príklad)
    #     # self.page.go("/")
