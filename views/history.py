import flet as ft
from core.supa_base import get_supabese_client, get_current_user
from locales.localization import LocalizedText
from views.base_page import BaseView


class HistoryView(BaseView):
    def __init__(self, page: ft.Page, loc):
        super().__init__(page, loc)
        self.page = page

        # Nastavíme build_list_tile ako metódu (bez jej okamžitého vykonania)
        self.build_list_tile = self.build_list_tile

        self.controls.append(
            ft.Container(
                alignment=ft.alignment.center,
                padding=ft.padding.only(20, 30, 20, 0),
                content=ft.Column(
                    controls=[
                        LocalizedText(self.loc, "History Page"),
                        self.build_list_tile()
                    ]
                )
            )
        )

    def build_list_tile(self):
        # Kontajner pre všetky tiles
        tiles_container = ft.Column()

        # Ukážkové dáta pre vozidlá
        vehicles_data = [
            {'id': 38, 'name': 'Car Fast', 'manufacturer': 'Renault', 'model': 'Clio', 'is_active': 'Active'}
        ]

        for vehicle in vehicles_data:
            # Vytvorenie jednotlivého tile
            tile = ft.CupertinoListTile(
                notched=True,
                additional_info=ft.Text(vehicle["is_active"]),
                leading=ft.Icon(name=ft.cupertino_icons.CAR),
                title=ft.Text(vehicle["name"]),
                subtitle=ft.Text(vehicle["manufacturer"] + " " + vehicle["model"]),
                trailing=ft.Icon(name=ft.cupertino_icons.CHECK_MARK_CIRCLED),
                on_click=self.tile_clicked,  # Použitie funkcie tile_clicked
            )
            tiles_container.controls.append(tile)

        return tiles_container

    def tile_clicked(self, e):
        print("Tile clicked")
