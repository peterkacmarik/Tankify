import os
import flet as ft
from flet_core import ViewPopEvent

from locales.localization import LocalizationService

# from views.home_page import HomeView
from views.history import HistoryView

from views.login_page import LoginView
from views.register_page import RegisterView
from views.forgot_password import ForgotPasswordView
from views.update_password import UpdatePasswordView

from views.users import UsersView
from views.create_user import CreateUsers
from views.edit_user import EditUsersViews

from views.vehicle import VehiclesViews
from views.create_vehicle import CreateVehicles
from views.edit_vehicle import EditVehiclesViews

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
port = int(os.getenv("PORT", 8000))


def main(page: ft.Page):
    page.title = "TankiFy"
    page.fonts = {
        "PoiretOne": "/fonts/Poiret_One/PoiretOne-Regular.ttf",
        "Roboto": "/fonts/Roboto/Roboto-Regular.ttf",
        "Roboto_Slap": "/fonts/Roboto_Slab/RobotoSlab-VariableFont_wght.ttf",
        "Audiowide": "/fonts/Audiowide/Audiowide-Regular.ttf"
    }
    page.theme = ft.Theme(font_family="Roboto")
    page.theme_mode = ft.ThemeMode.LIGHT
    # page.splash = ft.ProgressBar(visible=False)
    page.adaptive = True
    page.window.width = 400
    page.window.height = 800
    loc = LocalizationService()

    def route_change(route):
        page.views.clear()

        # if page.route == "/":
        #     page.views.append(HomeView(page))
        if page.route == "/login":
            page.views.append(LoginView(page, loc))
        elif page.route == "/register":
            page.views.append(RegisterView(page, loc))
        elif page.route == "/forgot-password":
            page.views.append(ForgotPasswordView(page, loc))
        elif page.route == "/update-password":
            page.views.append(UpdatePasswordView(page, loc))
        elif page.route == "/history":
            page.views.append(HistoryView(page, loc))
        # elif page.route == "/settings/general":
        #     page.views.append(SettingsView(page))
        
        elif page.route == "/users":
            page.views.append(UsersView(page, loc))
        elif page.route == "/user/create":
            page.views.append(CreateUsers(page, loc))
        elif page.route.startswith("/user/edit/"):
            page.views.append(EditUsersViews(page, loc))
            
        elif page.route == "/vehicles":
            page.views.append(VehiclesViews(page, loc))
        elif page.route == "/vehicle/create":
            page.views.append(CreateVehicles(page, loc))
        elif page.route.startswith("/vehicle/edit/"):
            page.views.append(EditVehiclesViews(page, loc))
        page.update()

    def view_pop(e: ViewPopEvent):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/user/edit")
    # page.go(page.route) # pri spusteni apk zobrazuje home page stranku


if __name__ == '__main__':
    ft.app(
        target=main,
        view=ft.AppView.FLET_APP,
        web_renderer=ft.WebRenderer.CANVAS_KIT,
        assets_dir="assets",
        port=port
        # export_asgi_app=True
    )
