import flet as ft
from core.lang_manager import LanguageManager


class ManageDialogWindow(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.lang_manager = LanguageManager(self.page)
        
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
                            text=self.lang_manager.get_translation("abastecimento"),
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
                            text=self.lang_manager.get_translation("servico"),
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
                            text=self.lang_manager.get_translation("despesa"),
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
                            text=self.lang_manager.get_translation("receita"),
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
                            text=self.lang_manager.get_translation("percurso"),
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
                            text=self.lang_manager.get_translation("checklist"),
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
                            text=self.lang_manager.get_translation("lembrete"),
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
        
        