import flet as ft
from core.theme import BgColor
from core.supa_base import get_supabese_client
from locales.language_manager import LanguageManager

lang_manager = LanguageManager()


def app_bar(page: ft.Page):
    return ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE, color=ft.colors.TRANSPARENT),
        # title=ft.Text(lang_manager.get_text("historico"), size=18),
        center_title=True,
        actions=[
            ft.Container(
                padding=ft.padding.only(left=0, top=0, right=10, bottom=0),
                content=ft.Row(
                    spacing=10,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.LIGHT_MODE_OUTLINED,
                            selected_icon=ft.icons.DARK_MODE_OUTLINED,
                            on_click=lambda e: switch_theme(page, e),
                        ),
                        ft.PopupMenuButton(
                            items=[
                                ft.PopupMenuItem(
                                    text=lang_manager.get_text("minha_conta"),
                                    icon=ft.icons.ACCOUNT_CIRCLE,
                                    on_click=lambda e: page.go("/settings/account"),
                                ),
                                ft.PopupMenuItem(),  # divider
                                ft.PopupMenuItem(
                                    text=lang_manager.get_text("logoff"),
                                    icon=ft.icons.LOGOUT, 
                                    on_click=lambda e: logout_user(page, e),
                                ),
                            ]
                        ),
                    ]
                )
            )
        ],
    )
    
def logout_user(page: ft.Page, e):
    try:
        # Odstránenie session údajov z Flet session storage
        page.client_storage.remove("access_token")
        page.client_storage.remove("refresh_token")
        
        supabase = get_supabese_client()
        response = supabase.auth.sign_out()
        
        page.go("/login")
        page.open(ft.SnackBar(content=ft.Text(lang_manager.get_text("logoff_sucesso"))))
        page.update()
    except Exception as exception:
        # print("Error:", exception)
        page.open(ft.SnackBar(content=ft.Text(lang_manager.get_text("logoff_erro"))))
        page.update()

def switch_theme(page: ft.Page, e):
    """
    Prepína medzi svetlou a tmavou témou a aktualizuje všetky komponenty.
    """
    # Prepne tému
    new_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
    page.theme_mode = new_mode
    
    # Uloží nastavenie
    page.client_storage.set("theme_mode", "dark" if new_mode == ft.ThemeMode.DARK else "light")
    
    # Aktualizuje ikonu
    e.control.selected = page.theme_mode == ft.ThemeMode.DARK
    
    # Aktualizuje pozadie
    new_bgcolor = BgColor(page).get_background_color()
    page.bgcolor = new_bgcolor
    
    # Aktualizuje témy
    page.theme = ft.Theme(
        color_scheme_seed="blue",
        use_material3=True
    )
    
    if new_mode == ft.ThemeMode.DARK:
        page.dark_theme = ft.Theme(
            color_scheme_seed="blue",
            use_material3=True
        )
    
    # Aktualizuje pozadie pre všetky views
    if hasattr(page, 'views') and page.views:
        for view in page.views:
            view.bgcolor = new_bgcolor
            if hasattr(view, 'controls'):
                for control in view.controls:
                    if isinstance(control, ft.Container):
                        control.bgcolor = new_bgcolor
    
    # Vynúti prekreslenie celej stránky
    page.update()

def update_theme(page: ft.Page):
    """
    Aktualizuje tému aplikácie podľa uloženého nastavenia.
    """
    # Načíta uloženú tému
    saved_theme = page.client_storage.get("theme_mode")
    
    # Nastaví tému
    new_mode = ft.ThemeMode.DARK if saved_theme == "dark" else ft.ThemeMode.LIGHT
    page.theme_mode = new_mode
    
    if not saved_theme:
        page.client_storage.set("theme_mode", "light")
    
    # Nastaví pozadie
    new_bgcolor = BgColor(page).get_background_color()
    page.bgcolor = new_bgcolor
    
    # Nastaví témy
    page.theme = ft.Theme(
        color_scheme_seed="blue",
        use_material3=True
    )
    
    if new_mode == ft.ThemeMode.DARK:
        page.dark_theme = ft.Theme(
            color_scheme_seed="blue",
            use_material3=True
        )
    
    # Aktualizuje pozadie pre všetky views
    if hasattr(page, 'views') and page.views:
        for view in page.views:
            view.bgcolor = new_bgcolor
            if hasattr(view, 'controls'):
                for control in view.controls:
                    if isinstance(control, ft.Container):
                        control.bgcolor = new_bgcolor
    
    # Vynúti prekreslenie
    page.update()

    
    
def left_drawer(page: ft.Page):
    return ft.NavigationDrawer(
        position=ft.NavigationDrawerPosition.START,
        on_change=lambda e: handle_change_drawer(page, e),
        # on_dismiss=self.handle_dismissal,
        selected_index=0,
        indicator_color=ft.colors.TRANSPARENT,
        indicator_shape=ft.ContinuousRectangleBorder(radius=50),
        controls=[
            ft.Container(
                alignment=ft.alignment.center,
                padding=ft.padding.all(16),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=ft.Image(
                                src="/logo/fuel_logo_transparent_1024_crop_128.png",
                                width=72,
                                height=72,
                            ),
                            # content=ft.Icon(ft.icons.ACCOUNT_CIRCLE, size=64),
                            margin=ft.margin.only(top=20, bottom=10),
                        ),
                        ft.Text(
                            lang_manager.get_text("google_play_titulo"), 
                            size=16, 
                            weight="bold",
                        ),
                    ]
                )
            ),
            ft.Divider(thickness=1),
            ft.NavigationDrawerDestination(
                label=lang_manager.get_text("historico"),
                icon=ft.icons.HISTORY_OUTLINED,
                selected_icon=ft.icons.MANAGE_HISTORY,
            ),
            ft.NavigationDrawerDestination(
                label=lang_manager.get_text("relatorios"),
                icon=ft.icons.REPORT_GMAILERRORRED_OUTLINED,
                selected_icon=ft.icons.REPORT,
            ),
            ft.NavigationDrawerDestination(
                label=lang_manager.get_text("lembretes"),
                icon=ft.icons.NOTIFICATIONS_OUTLINED,
                selected_icon=ft.icons.NOTIFICATIONS,
            ),
            ft.Divider(thickness=1),
            ft.NavigationDrawerDestination(
                label=lang_manager.get_text("veiculos"),
                icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
                selected_icon=ft.icons.DIRECTIONS_CAR,
            ),
            ft.NavigationDrawerDestination(
                label=lang_manager.get_text("usuarios"),
                icon=ft.icons.SUPERVISED_USER_CIRCLE_OUTLINED,
                selected_icon=ft.icons.SUPERVISED_USER_CIRCLE,
            ),
            ft.NavigationDrawerDestination(
                label=lang_manager.get_text("configuracoes"),
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon=ft.icons.SETTINGS,
            ),
            ft.Divider(thickness=1, opacity=1.0),
            ft.NavigationDrawerDestination(
                label=lang_manager.get_text("contato"),
                icon=ft.icons.EMAIL_OUTLINED,
                selected_icon=ft.icons.EMAIL,
            )
        ]
    )
    
def handle_change_drawer(page: ft.Page, e):
    selected_index = e.control.selected_index
    if selected_index == 0:   # History
        e.page.go("/history")
    elif selected_index == 1:   # Report
        e.page.go("/reports/general")
    elif selected_index == 2:   # Reminders
        e.page.go("/reminders")
    elif selected_index == 3:   # Vehicles
        e.page.go("/vehicles")
    elif selected_index == 4:   # Users
        e.page.go("/users")
    elif selected_index == 5:   # Settings
        e.page.go("/settings/general")
    elif selected_index == 6:   # Contact
        e.page.go("/contact")
    e.page.update()
    
    
    
def navigation_bottom_bar(page: ft.Page):
    return ft.NavigationBar(
        selected_index=0,
        on_change=lambda e: handle_change_bottom_nav(page, e),
        # bgcolor=ft.colors.WHITE,
        indicator_color=ft.colors.TRANSPARENT,
        indicator_shape=ft.CircleBorder(type="circle"),
        destinations=[
            ft.NavigationBarDestination(
                bgcolor=ft.colors.BLACK12,
                icon=ft.icons.HISTORY_OUTLINED, 
                label=lang_manager.get_text("historico"),
                selected_icon=ft.icons.MANAGE_HISTORY,
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.REPORT_GMAILERRORRED_OUTLINED, 
                label=lang_manager.get_text("relatorios"),
                selected_icon=ft.icons.REPORT,
            ),            
            ft.NavigationBarDestination(
                icon=ft.icons.NOTIFICATIONS_OUTLINED, 
                label=lang_manager.get_text("lembretes"),
                selected_icon=ft.icons.NOTIFICATIONS,
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.MORE_HORIZ_OUTLINED, 
                label=lang_manager.get_text("mais"),
                selected_icon=ft.icons.MORE_HORIZ,
            ),
            
        ],
    )
    
def open_drawer(page: ft.Page):
    page.drawer.open = True
    page.update()
    
def handle_change_bottom_nav(page, e):
    selected_index = e.control.selected_index
    if selected_index == 0:   # History
        e.page.go("/history")
    elif selected_index == 1:   # Report
        e.page.go("/reports/general")
    elif selected_index == 2:   # Reminders
        e.page.go("/reminders")
    elif selected_index == 3:   # More
        open_drawer(page)
    e.page.update()