import os
import flet as ft

from views.login_page import LoginView
from views.home_page import HomeView
from views.register_page import RegisterView
from views.forgot_password import ForgotPasswordView
from views.service_terms import ServiceTermsView
from locales.language_manager import LanguageManager

port = int(os.getenv("PORT", 8000))


def main(page: ft.Page):
    LanguageManager.set_language("en")  # Predvolený jazyk je angličtina
    page.title = "TankiFy"
    page.fonts = {
        "Roboto": "/fonts/Roboto/Roboto-Regular.ttf",
        "OpenSans": "/fonts/Open_Sans/OpenSans-VariableFont_wdth,wght.ttf",
        "ABeeZee": "/fonts/ABeeZee/ABeeZee-Regular.ttf",
        "Roboto_Slap": "/fonts/Roboto_Slab/RobotoSlab-VariableFont_wght.ttf",
    }
    page.theme = ft.Theme(font_family="Roboto")
    page.theme_mode = ft.ThemeMode.LIGHT
    page.adaptive = True
    page.window.width = 400
    page.window.height = 800
    page.update()

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(HomeView(page))
        if page.route == "/login":
            page.views.append(LoginView(page))
        elif page.route == "/register":
            page.views.append(RegisterView(page))
        elif page.route == "/forgot-password":
            page.views.append(ForgotPasswordView(page))
        elif page.route == "/service-terms":
            page.views.append(ServiceTermsView(page))

        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(
    target=main,
    view=ft.AppView.FLET_APP,
    web_renderer=ft.WebRenderer.CANVAS_KIT,
    assets_dir="assets",
    port=port
    # export_asgi_app=True
)
