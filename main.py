import os
import flet as ft

# from views.history_old import HistoryView
from views.create_user import CreateUsers
from views.create_vehicle import CreateVehicles
from views.history import HistoryView
from views.login_page import LoginView
from views.home_page import HomeView
from views.register_page import RegisterView
from views.forgot_password import ForgotPasswordView
from locales.language_manager import LanguageManager
from views.settings import SettingsView

import warnings

from views.users import UsersView
from views.vehicle import VehiclesViews
warnings.filterwarnings("ignore", category=DeprecationWarning)

port = int(os.getenv("PORT", 8000))


def main(page: ft.Page):
    # Inicializácia language managera
    LanguageManager.initialize(page)
    
    # Nastavenie predvoleného jazyka
    LanguageManager.set_language("en", page)
    
    page.title = "TankiFy"
    page.fonts = {
        "PoiretOne": "/fonts/Poiret_One/PoiretOne-Regular.ttf",
        "Roboto": "/fonts/Roboto/Roboto-Regular.ttf",
        "OpenSans": "/fonts/Open_Sans/OpenSans-VariableFont_wdth,wght.ttf",
        "ABeeZee": "/fonts/ABeeZee/ABeeZee-Regular.ttf",
        "Roboto_Slap": "/fonts/Roboto_Slab/RobotoSlab-VariableFont_wght.ttf",
    }
    page.theme = ft.Theme(font_family="Roboto")
    page.theme_mode = ft.ThemeMode.LIGHT
    page.splash = ft.ProgressBar(visible=False)
    # page.adaptive = True
    # page.window.width = 400
    # page.window.height = 800
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
        elif page.route == "/history":
            page.views.append(HistoryView(page))
        elif page.route == "/settings/general":
            page.views.append(SettingsView(page))
        
        elif page.route == "/users":
            page.views.append(UsersView(page))
        elif page.route == "/user/create":
            page.views.append(CreateUsers(page))
        
        elif page.route == "/vehicles":
            page.views.append(VehiclesViews(page))
        elif page.route == "/vehicle/create":
            page.views.append(CreateVehicles(page))
        page.update()

    page.on_route_change = route_change
    page.go("/vehicle/create")
    # page.go(page.route) # pri spusteni apk zobrazuje home page stranku

ft.app(
    target=main,
    view=ft.AppView.WEB_BROWSER,
    web_renderer=ft.WebRenderer.CANVAS_KIT,
    assets_dir="assets",
    port=port
    # export_asgi_app=True
)
