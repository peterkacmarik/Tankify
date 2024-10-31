import flet as ft
from locales.translations import get_translation
from components.fields import (
    email_field, 
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


class LoginView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/login")
        self.page = page
        
        self.bgcolor = ft.colors.WHITE
        self.supabase: Client = get_supabese_client()
        
        self.scroll = ft.ScrollMode.HIDDEN
        self.fullscreen_dialog = True
        
        LanguageManager.subscribe(self.update_language)
        self.current_language = LanguageManager.get_current_language()
        self.translation = get_translation(self.current_language)
        self.init_components()
        
        # Snack bar
        self.snack_bar = ft.SnackBar(
            content=ft.Text(""),
            show_close_icon=True
        )
        self.page.overlay.append(self.snack_bar)

    
    def init_components(self):
        # Tvorba prepínača jazyka a prihlasovacieho formulára
        self.language_switch_button = self.language_switch()
        self.page_logo = page_logo()
        self.login_text = ft.Container(
            alignment=ft.alignment.center,
            content=main_login_text(self.translation)
        )
        self.social_buttons = ft.Container(
            alignment=ft.alignment.center,
            padding=ft.padding.only(top=20, bottom=10),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    facebook_login_button(self.translation, self.page),
                    google_login_button(self.translation, self.page)
                ],
            ),
        )

        self.line_separator = line_separator(self.translation)
        
        self.login_fields = ft.Container(
            padding=ft.padding.only(top=10),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    email_field(self.translation, self.validate_fields),
                    password_field(self.translation, self.validate_fields)
                ]
            )
        )
        
        self.forgot_password_link = forgot_password_link(self.translation, self.page)
        self.login_button = login_button(self.translation, self.page, self.handle_login)
        self.create_account_link = create_account_link(self.translation, self.page)
        
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
                        self.forgot_password_link,
                        self.login_button,
                        self.create_account_link
                    ]
                )
            )
        ]
    
    
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
    
    
    def language_switch(self):
        return ft.Container(
            # padding=ft.padding.only(left=20),
            alignment=ft.Alignment(x=-1.0, y=0.0),
            content=ft.Dropdown(
                options=[
                    ft.dropdown.Option(
                        key="en", 
                        # text="English",
                        content=ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Image(
                                        src="/icons/us.svg",
                                        width=24,
                                        height=24,
                                        fit=ft.ImageFit.CONTAIN,
                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                    ),
                                    ft.Text("English"),
                                ]
                            )
                        ),
                    ),
                    ft.dropdown.Option(
                        key="sk", 
                        # text="Slovenčina"
                        content=ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Image(
                                        src="/icons/sk.svg",
                                        width=24,
                                        height=24,
                                        fit=ft.ImageFit.CONTAIN,
                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                    ),
                                    ft.Text("Slovenčina"),
                                ]
                            )
                        ),
                    ),
                    ft.dropdown.Option(
                        key="cs", 
                        # text="Čeština"
                        content=ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Image(
                                        src="/icons/cz.svg",
                                        width=24,
                                        height=24,
                                        fit=ft.ImageFit.CONTAIN,
                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                    ),
                                    ft.Text("Čeština"),
                                ]
                            )
                        ),
                    ),
                ],
                width=150,
                # padding=ft.padding.only(left=0),
                border=ft.InputBorder.NONE,
                value=self.current_language,
                border_radius=10,
                on_change=self.change_language
            )
        )
        
        
    def change_language(self, e):
        # Update the global language through the manager
        LanguageManager.set_language(e.control.value)
        # The update_language method will be called automatically through the subscription
    

    def did_mount(self):
        LanguageManager.subscribe(self.update_language)
        
        
    def will_unmount(self):
        LanguageManager.unsubscribe(self.update_language)
        
        
    def update_language(self):
        self.current_language = LanguageManager.get_current_language()
        self.translation = get_translation(self.current_language)
        self.update_ui()
        
        
    def update_ui(self):
        # Update all UI components with new translation
        self.controls.clear()
        self.init_components()
        self.page.update()
        
        
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
                self.snack_bar.content.value = self.translation['msg_login']
                self.snack_bar.open = True
                self.page.update()
                
                self.page.go("/")
                
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
