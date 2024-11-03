import flet as ft
from core.theme import BgColor
from locales.language_manager import LanguageManager



class BaseView(ft.View):
    """Základná trieda pre všetky views s podporou viacjazyčnosti"""
    def __init__(self, route: str, page: ft.Page):
        super().__init__(route=route)
        self.page = page
        self.bgcolor = BgColor(self.page).get_background_color()
        LanguageManager.add_observer(self)
        
        self.scroll = ft.ScrollMode.HIDDEN
        self.fullscreen_dialog = True
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.horizontal_alignment = ft.MainAxisAlignment.CENTER
        
        self.snack_bar = ft.SnackBar(
            content=ft.Text(""),
            show_close_icon=True
        )
        self.page.overlay.append(self.snack_bar)
        
        # Zabezpečí, že všetky containery v controls budú mať správne pozadie
        def update_container_backgrounds(controls):
            for control in controls:
                if isinstance(control, ft.Container):
                    control.bgcolor = self.bgcolor
                if hasattr(control, 'content'):
                    if isinstance(control.content, (ft.Control, ft.Container)):
                        update_container_backgrounds([control.content])
                    elif isinstance(control.content, (list, ft.Row, ft.Column)):
                        update_container_backgrounds(control.content.controls)
                elif hasattr(control, 'controls'):
                    update_container_backgrounds(control.controls)
        
        # Aplikuje aktualizáciu pozadia po nastavení controls
        def _original_set_controls(controls):
            super(BaseView, self).__setattr__('controls', controls)
            update_container_backgrounds(controls)
        
        # Override setter pre controls
        self.__setattr__ = lambda name, value: _original_set_controls(value) if name == 'controls' else super(BaseView, self).__setattr__(name, value)

    def update_language(self) -> None:
        self.update_texts()
        self.page.update()

    def update_texts(self) -> None:
        pass

    def __del__(self):
        LanguageManager.remove_observer(self)
        
        