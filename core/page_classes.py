
import flet as ft

from locales.language_manager import LanguageManager



class LanguageSwitcher(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.current_language = LanguageManager._current_language
        self.language_switch_button = self.language_switch()
        
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
        

    def change_language(self, e) -> None:
        LanguageManager.set_language(self.language_switch_button.content.value, self.page)


class ManageDialogWindow(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.lang_manager = LanguageManager()
        
    def dialog_window(self, e):  # Parameter e je pridaný pre podporu on_click
        # Vytvorenie dialógového okna
        dialog = ft.AlertDialog(
            bgcolor=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=10),
            open=False,
            # actions=[ft.TextButton(self.lang_manager.get_text["btn_cancelar"], on_click=self.close_dialog)],
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
                            text=self.lang_manager.get_text("abastecimento"),
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
                            text=self.lang_manager.get_text("servico"),
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
                            text=self.lang_manager.get_text("despesa"),
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
                            text=self.lang_manager.get_text("receita"),
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
                            text=self.lang_manager.get_text("percurso"),
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
                            text=self.lang_manager.get_text("checklist"),
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
                            text=self.lang_manager.get_text("lembrete"),
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
        
        