import flet as ft
from components.buttons import floating_action_button, refresh_button
from components.navigations import app_bar, navigation_bottom_bar, left_drawer
from core.page_classes import ManageDialogWindow
from locales.language_manager import LanguageManager

from core.supa_base import get_supabese_client, SupabaseVehicle
from views.base_page import BaseView


class VehiclesViews(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__("/vehicle", page)
        self.page = page
        self.lang_manager = LanguageManager()
        self.supabase_vehicle = SupabaseVehicle()

        self.supabase = get_supabese_client()

        self.appbar = app_bar(self.page)

        self.page.drawer = left_drawer(self.page)
        self.drawer = self.page.drawer

        self.navigation_bar = navigation_bottom_bar(self.page)

        self.dialog_window = ManageDialogWindow(self.page).dialog_window
        self.floating_action_button = floating_action_button(self.dialog_window)
        self.floating_action_button_location = (
            ft.FloatingActionButtonLocation.CENTER_DOCKED
        )

        self.navigation_header_bar = self.build_navigation_header_bar()
        self.table_header = self.build_table_header()
        self.vehicle_table = self.build_vehicle_table()

        self.controls = [
            ft.Container(
                alignment=ft.alignment.center,
                padding=ft.padding.only(20, 30, 20, 0),
                content=ft.Column(
                    controls=[
                        ft.Container(
                            bgcolor=ft.colors.TRANSPARENT,
                            border=ft.border.all(0.5, ft.colors.GREY_400),
                            border_radius=10,
                            padding=ft.padding.only(20, 20, 20, 20),
                            alignment=ft.alignment.center,
                            content=ft.Column(
                                controls=[
                                    self.navigation_header_bar,
                                    self.table_header,
                                    ft.Divider(),
                                    self.vehicle_table,
                                ]
                            ),
                        )
                    ]
                ),
            )
        ]

    def update_texts(self) -> None:
        # Aktualizácia textov v settings view
        # self.title_text.value = LanguageManager.get_text("intro_texto_05")
        self.update()

    def build_navigation_header_bar(self):
        return ft.Container(
            border=ft.border.all(0.5, ft.colors.GREY_400),
            border_radius=10,
            # padding=ft.padding.only(20, 20, 20, 20),
            content=ft.Row(
                controls=[
                    ft.TextButton(
                        style=ft.ButtonStyle(
                            overlay_color=ft.colors.TRANSPARENT,
                            shadow_color=ft.colors.TRANSPARENT,
                            bgcolor=ft.colors.TRANSPARENT,
                        ),
                        text=self.lang_manager.get_text("configuracoes"),
                        on_click=lambda e: self.go_to_settings(e),
                    ),
                    ft.Icon(
                        name=ft.icons.KEYBOARD_ARROW_RIGHT_OUTLINED,
                        color=ft.colors.BLUE_700,
                        size=20,
                    ),
                    ft.Text(
                        self.lang_manager.get_text("veiculos"),
                    ),
                ]
            ),
        )

    def go_to_settings(self, e):
        e.page.go("/settings/general")

    def build_table_header(self):
        table_header = ft.Container(
            border=ft.border.all(0.5, ft.colors.GREY_400),
            border_radius=10,
            padding=ft.padding.only(20, 10, 20, 10),
            alignment=ft.alignment.center,
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            self.lang_manager.get_text("veiculos"),
                            size=20,
                        ),
                        # alignment=ft.alignment.center_left,
                    ),
                    ft.Container(
                        content=ft.SearchBar(
                            bar_bgcolor=ft.colors.GREY_100,
                            bar_overlay_color=ft.colors.GREY_100,
                            value="Search...",
                            width=200,
                            height=40,
                            on_change=lambda e: print("Search"),
                            on_submit=lambda e: print("Search"),
                        ),
                        # alignment=ft.alignment.center_left,
                    ),
                    ft.Container(
                        # alignment=ft.alignment.center_right,
                        content=ft.OutlinedButton(
                            text=self.lang_manager.get_text("adicionar_novo").upper(),
                            icon=ft.icons.ADD,
                            on_click=lambda e: self.go_to_add_vehicle(e),
                            style=ft.ButtonStyle(
                                bgcolor=ft.colors.TRANSPARENT,
                                shape={
                                    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(
                                        radius=50
                                    ),
                                },
                            ),
                        )
                    ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.IconButton(
                            icon=ft.icons.REFRESH, on_click=lambda e: self.load_data(e)
                        ),
                    ),
                ]
            ),
        )
        return table_header

    def load_data(self, e):
        response_data = self.supabase_vehicle.get_all_data_from_table_vehicles(
            self.page
        )

        if response_data is None:
            self.page.show_snack_bar(ft.SnackBar(content=ft.Text("No data available")))
            return

        # Vyčisti existujúce riadky
        self.vehicle_table.rows.clear()

        # Pridaj nové riadky
        for idx, vehicle in enumerate(response_data):
            self.vehicle_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(idx + 1)),
                        ft.DataCell(ft.Text(vehicle["vehicle"])),
                        ft.DataCell(ft.Text(vehicle["name"])),
                        ft.DataCell(ft.Text(vehicle["manufacturer"])),
                        ft.DataCell(ft.Text(vehicle["model"])),
                        ft.DataCell(ft.Text(vehicle["is_active"])),
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.EDIT,
                                            on_click=lambda e, v=vehicle: self.handle_edit_vehicle(e, v),
                                        ),
                                        ft.IconButton(
                                            icon=ft.icons.DELETE,
                                            on_click=lambda _, v=vehicle: self.supabase_vehicle.delete_vehicle_from_table_vehicles(self.page, v["id"]),
                                        ),
                                    ]
                                )
                            )
                        ),
                    ]
                )
            )

        # Aktualizuj UI
        self.vehicle_table.update()
        self.page.update()

    def go_to_add_vehicle(self, e):
        e.page.go("/vehicle/create")

    def build_vehicle_table(self):
        # Získanie údajov o používateľoch
        vehicles_data = self.supabase_vehicle.get_all_data_from_table_vehicles(
            self.page
        )

        if vehicles_data is None:
            self.page.open(ft.SnackBar(content=ft.Text("No data available")))
            # print("No data available")
            return None

        # Vytvorenie tabuľky používateľov
        vehicle_table = ft.DataTable(
            columns=[
                ft.DataColumn(
                    ft.Text("#"),
                ),
                ft.DataColumn(
                    ft.Text(self.lang_manager.get_text("tipo")),  # Type
                ),
                ft.DataColumn(
                    ft.Text(self.lang_manager.get_text("apelido"))  # Nickname
                ),
                ft.DataColumn(
                    ft.Text(self.lang_manager.get_text("marca"))  # Manufacturer
                ),
                ft.DataColumn(ft.Text(self.lang_manager.get_text("modelo"))),  # Model
                ft.DataColumn(ft.Text(self.lang_manager.get_text("status"))),  # Active
                ft.DataColumn(
                    ft.Text(self.lang_manager.get_text("actions"))  # Actions
                ),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(idx + 1),),
                        ft.DataCell(ft.Text(vehicle["vehicle"])),
                        ft.DataCell(ft.Text(vehicle["name"])),
                        ft.DataCell(ft.Text(vehicle["manufacturer"])),
                        ft.DataCell(ft.Text(vehicle["model"])),
                        ft.DataCell(ft.Text(vehicle["is_active"])),  # Active
                        ft.DataCell(
                            content=ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.EDIT,
                                            on_click=lambda e, vehicle=vehicle: self.handle_edit_vehicle(e, vehicle),
                                        ),
                                        ft.IconButton(
                                            icon=ft.icons.DELETE,
                                            on_click=lambda _: self.supabase_vehicle.delete_vehicle_from_table_vehicles(self.page, vehicles_data[0]["id"]),
                                        ),
                                    ]
                                )
                            )
                        ),
                    ]
                )
                for idx, vehicle in enumerate(vehicles_data)
            ],
        )
        return vehicle_table

    def get_value_from_fields(self, vehicle):
        pass

    def handle_edit_vehicle(self, e, vehicle):
        vehicle_data = self.get_value_from_fields(vehicle)
