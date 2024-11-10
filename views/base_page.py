import flet as ft
from abc import ABC

from components.buttons import floating_action_button
from core.supa_base import get_supabese_client
from locales.localization import LocalizedNavigationDrawer, LocalizedPopupMenuButton, LocalizedNavigationBar, \
    LocalizedText


class BaseView(ft.View, ABC):
    def __init__(self, page: ft.Page, loc):
        super().__init__()
        self.page = page
        self.loc = loc

        self.scroll = ft.ScrollMode.HIDDEN
        self.fullscreen_dialog = True
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.horizontal_alignment = ft.MainAxisAlignment.CENTER
        self.language_selector = self.loc.create_language_selector()

        self.snack_bar = ft.SnackBar(
            content=ft.Text(""),
            show_close_icon=True
        )
        self.page.overlay.append(self.snack_bar)

        self.setup_appbar()
        self.page.drawer = self.left_drawer()
        self.drawer = self.page.drawer
        self.navigation_bar = self.navigation_bottom_bar()
        self.floating_action_button = floating_action_button(self.dialog_window)
        self.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED


    def setup_appbar(self):
        popup_items = [
            {"key": "minha_conta", "icon": ft.icons.ACCOUNT_CIRCLE, "on_click": lambda e: self.page.go("/settings/account")},
            {"key": "logoff", "icon": ft.icons.LOGOUT, "on_click": lambda e: self.logout_user(e)},
        ]
        self.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.PALETTE, color=ft.colors.TRANSPARENT),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                self.language_selector,
                ft.Container(
                    padding=ft.padding.only(left=0, top=0, right=10, bottom=0),
                    content=ft.Row(
                        spacing=10,
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.LIGHT_MODE_OUTLINED,
                                selected_icon=ft.icons.DARK_MODE_OUTLINED,
                                # on_click=lambda e: switch_theme(self.page, e),
                            ),
                            LocalizedPopupMenuButton(
                                self.loc,
                                item_keys=popup_items,
                                page=self.page
                                # item_keys=["minha_conta", "logoff"]
                            )
                        ]
                    )
                )
            ],
        )

    def logout_user(self, e):
        try:
            # Odstránenie session údajov z Flet session storage
            self.page.client_storage.remove("access_token")
            self.page.client_storage.remove("refresh_token")

            supabase = get_supabese_client()
            response = supabase.auth.sign_out()

            self.page.go("/login")
            self.page.open(ft.SnackBar(
                content=LocalizedText(self.loc, "logoff_sucesso")
            ))
            self.page.update()
        except Exception as exception:
            # print("Error:", exception)
            self.page.open(ft.SnackBar(
                content=LocalizedText(self.loc, "logoff_erro")
            ))
            self.page.update()

    def left_drawer(self):
        drawer_items = [
            {"key": "veiculos", "icon": ft.icons.DIRECTIONS_CAR_OUTLINED}, # Vehicles
            {"key": "usuarios", "icon": ft.icons.SUPERVISED_USER_CIRCLE_OUTLINED}, # Users
            {"key": "veiculo_usuario", "icon": ft.icons.OTHER_HOUSES_OUTLINED}, # Vehicles / Users
            {"key": "", "icon": ""}, # Divider
            {"key": "combustivel", "icon": ft.icons.GAS_METER_OUTLINED}, # Fuel
            {"key": "postos_combustiveis", "icon": ft.icons.LOCAL_GAS_STATION_OUTLINED}, # Gas station
            {"key": "locais", "icon": ft.icons.PLACE_OUTLINED}, # Place

            {"key": "tipo_servico", "icon": ft.icons.DIRECTIONS_CAR_OUTLINED}, # Type of service
            {"key": "tipo_despesa", "icon": ft.icons.SUPERVISED_USER_CIRCLE_OUTLINED}, # Type of expense
            {"key": "tipo_receitas", "icon": ft.icons.OTHER_HOUSES_OUTLINED}, # Type of income

            {"key": "formas_pagamento", "icon": ft.icons.SETTINGS_OUTLINED}, #Payment methods
            {"key": "motivos", "icon": ft.icons.EMAIL_OUTLINED}, # Reasons
            {"key": "", "icon": ""}, # Divider
            {"key": "configuracoes", "icon": ft.icons.SETTINGS_OUTLINED}, # Settings
            {"key": "contato", "icon": ft.icons.EMAIL_OUTLINED}, # Contact
        ]
        return LocalizedNavigationDrawer(
            localization=self.loc,
            item_keys=drawer_items,
            position=ft.NavigationDrawerPosition.START,
            on_change=lambda e: self.handle_change_drawer(e),
            selected_index=0,
            indicator_color=ft.colors.TRANSPARENT,
            indicator_shape=ft.ContinuousRectangleBorder(radius=50),
        )

    def handle_change_drawer(self, e):
        selected_index = e.control.selected_index
        if selected_index == 0:  # Vehicles
            e.page.go("/vehicles")
        elif selected_index == 1:  # Users
            e.page.go("/users")
        elif selected_index == 2:  # Vehicle / User
            e.page.go("/vehicle-user")
        elif selected_index == 3:  # Fuel
            e.page.go("/fuel")
        elif selected_index == 4:  # Gas station
            e.page.go("/gas-station")
        elif selected_index == 5:  # Places
            e.page.go("/places")
        elif selected_index == 6:  # Type of service
            e.page.go("/type-service")
        elif selected_index == 7:  # Type of expense
            e.page.go("/type-expense")
        elif selected_index == 8:  # Type of income
            e.page.go("/type-income")
        elif selected_index == 9:  # Payment methods
            e.page.go("/payment-methods")
        elif selected_index == 10:  # Reasons
            e.page.go("/reason")
        elif selected_index == 11:  # Settings
            e.page.go("/settings/general")
        elif selected_index == 12:  # Contact
            e.page.go("/contact")
        e.page.update()

    def navigation_bottom_bar(self):
        navigation_items = [
            {"key": "historico", "icon": f"{ft.icons.HISTORY_OUTLINED}"},
            {"key": "relatorios", "icon": f"{ft.icons.REPORT_GMAILERRORRED_OUTLINED}"},
            {"key": "lembretes", "icon": f"{ft.icons.NOTIFICATIONS_OUTLINED}"},
            {"key": "mais", "icon": f"{ft.icons.KEYBOARD_CONTROL_OUTLINED}"}
        ]

        nav_bar = LocalizedNavigationBar(
            selected_index=0,
            indicator_color=ft.colors.TRANSPARENT,
            indicator_shape=ft.CircleBorder(type="circle"),
            localization=self.loc,
            navigation_items=navigation_items,
            on_change=lambda e: self.handle_change_bottom_nav(e),
        )
        return nav_bar

    def handle_change_bottom_nav(self, e):
        selected_index = e.control.selected_index
        if selected_index == 0:  # History
            e.page.go("/history")
        elif selected_index == 1:  # Report
            e.page.go("/reports/general")
        elif selected_index == 2:  # Reminders
            e.page.go("/reminders")
        elif selected_index == 3:  # More
            self.open_drawer()
        e.page.update()

    def open_drawer(self):
        self.page.drawer.open = True
        self.page.update()

    def dialog_window(self, e):  # Parameter e je pridaný pre podporu on_click
        # Vytvorenie dialógového okna
        dialog = ft.AlertDialog(
            bgcolor=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=10),
            open=False,
            # actions=[ft.TextButton(self.lang_manager.get_translation["btn_cancelar"], on_click=self.close_dialog)],
            # actions_alignment=ft.MainAxisAlignment.END,
            # title=ft.Text("Add new item"),
            content=ft.Container(
                # border=ft.border.all(0),
                # padding=ft.padding.only(left=10, right=10, top=0, bottom=0),
                # margin=ft.margin.only(left=10, right=10, top=0, bottom=0),
                alignment=ft.alignment.center,
                # width=50,
                height=340,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.ElevatedButton(
                            text=self.loc.get_text("abastecimento"),
                            icon=ft.icons.LOCAL_GAS_STATION_OUTLINED,
                            color="#5d93b5",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                shadow_color=ft.colors.TRANSPARENT,
                                bgcolor=ft.colors.TRANSPARENT,
                                text_style=ft.TextStyle(
                                    size=16,
                                ),
                                icon_size=28,
                                icon_color=ft.colors.ORANGE,
                            ),
                            width=220,
                            on_click=self.close_dialog
                        ),
                        ft.ElevatedButton(
                            text=self.loc.get_text("servico"),
                            icon=ft.icons.MISCELLANEOUS_SERVICES_OUTLINED,
                            color="#5d93b5",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                shadow_color=ft.colors.TRANSPARENT,
                                bgcolor=ft.colors.TRANSPARENT,
                                text_style=ft.TextStyle(
                                    size=16,
                                ),
                                icon_size=28,
                                icon_color=ft.colors.BROWN,
                            ),
                            width=220,
                            on_click=self.close_dialog
                        ),
                        ft.ElevatedButton(
                            text=self.loc.get_text("despesa"),
                            icon=ft.icons.CREDIT_CARD_OFF_OUTLINED,
                            color="#5d93b5",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                shadow_color=ft.colors.TRANSPARENT,
                                bgcolor=ft.colors.TRANSPARENT,
                                text_style=ft.TextStyle(
                                    size=16,
                                ),
                                icon_size=28,
                                icon_color=ft.colors.BLUE,
                            ),
                            width=220,
                            on_click=self.close_dialog
                        ),
                        ft.ElevatedButton(
                            text=self.loc.get_text("receita"),
                            icon=ft.icons.ADD_CARD_OUTLINED,
                            color="#5d93b5",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                shadow_color=ft.colors.TRANSPARENT,
                                bgcolor=ft.colors.TRANSPARENT,
                                text_style=ft.TextStyle(
                                    size=16,
                                ),
                                icon_size=28,
                                icon_color=ft.colors.GREEN,
                            ),
                            width=220,
                            on_click=self.close_dialog
                        ),
                        ft.ElevatedButton(
                            text=self.loc.get_text("percurso"),
                            icon=ft.icons.ROUTE_OUTLINED,
                            color="#5d93b5",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                shadow_color=ft.colors.TRANSPARENT,
                                bgcolor=ft.colors.TRANSPARENT,
                                text_style=ft.TextStyle(
                                    size=16,
                                ),
                                icon_size=28,
                                icon_color=ft.colors.RED,
                            ),
                            width=220,
                            on_click=self.close_dialog
                        ),
                        ft.ElevatedButton(
                            text=self.loc.get_text("checklist"),
                            icon=ft.icons.CHECKLIST_OUTLINED,
                            color="#5d93b5",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                shadow_color=ft.colors.TRANSPARENT,
                                bgcolor=ft.colors.TRANSPARENT,
                                text_style=ft.TextStyle(
                                    size=16,
                                ),
                                icon_size=28,
                                icon_color=ft.colors.PURPLE,
                            ),
                            width=220,
                            on_click=self.close_dialog
                        ),
                        ft.ElevatedButton(
                            text=self.loc.get_text("lembrete"),
                            icon=ft.icons.NOTIFICATIONS_OUTLINED,
                            color="#5d93b5",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                                shadow_color=ft.colors.TRANSPARENT,
                                bgcolor=ft.colors.TRANSPARENT,
                                text_style=ft.TextStyle(
                                    size=16,
                                ),
                                icon_size=28,
                                icon_color=ft.colors.YELLOW_700,
                            ),
                            width=220,
                            on_click=self.close_dialog
                        )
                    ],
                ),
            ),
        )

        # Pridanie dialógu do overlay a jeho otvorenie
        if dialog not in self.page.overlay:
            self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()

    def close_dialog(self, e):
        # Zatvorenie dialógu v overlay
        for dialog in self.page.overlay:
            if isinstance(dialog, ft.AlertDialog):
                dialog.open = False
        self.page.update()


