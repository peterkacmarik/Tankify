import flet as ft

        

def app_bar(open_draver, switch_theme):
    return ft.AppBar(
        leading=ft.IconButton(
            ft.icons.MENU,
            on_click=open_draver,
            icon_color=ft.colors.SURFACE_VARIANT,
        ),
        leading_width=40,
        title=ft.Text("tankify"),
        title_text_style=ft.TextStyle(
            font_family="PoiretOne",
            size=18,
            color=ft.colors.SURFACE_VARIANT,
            
        ),
        center_title=False,
        bgcolor="#03aac0",
        actions=[
            ft.IconButton(
                ft.icons.WB_SUNNY_OUTLINED,
                on_click=switch_theme,
                icon_color=ft.colors.SURFACE_VARIANT,
            ),
            ft.PopupMenuButton(
                icon_color=ft.colors.SURFACE_VARIANT,
                items=[
                    ft.PopupMenuItem(
                        text="Profil",
                        icon=ft.icons.PERSON
                    ),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Odhlásiť sa",
                        icon=ft.icons.LOGOUT
                    ),
                ]
            ),
        ],
    )
        
        
def left_drawer(handle_change):
    return ft.NavigationDrawer(
        position=ft.NavigationDrawerPosition.END,
        on_change=handle_change,
        # on_dismiss=self.handle_dismissal,
        controls=[
            ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=ft.Icon(ft.icons.ACCOUNT_CIRCLE, size=64),
                        margin=ft.margin.only(top=20, bottom=10),
                    ),
                    ft.Text("Dôchodkový kalkulátor", size=16, weight="bold"),
                ], 
                horizontal_alignment="center"
                ),
                padding=ft.padding.all(16),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                label="Dashboard",
                icon=ft.icons.HOME_OUTLINED,
                selected_icon=ft.icons.HOME,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.CALCULATE_OUTLINED),
                label="Kalkulačka",
                selected_icon=ft.icons.CALCULATE,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.SETTINGS_OUTLINED),
                label="Nastavenia",
                selected_icon=ft.icons.SETTINGS,
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.INFO_OUTLINED),
                label="O aplikácii",
                selected_icon=ft.icons.INFO,
            ),
        ],
        selected_index=0,
    )
        
        
def bottom_navigation_bar():
    return ft.NavigationBar(
        border=ft.border.all(10, ft.colors.SURFACE_VARIANT),
        # on_change=lambda e: self.handle_navigation_change(e),
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.icons.SEARCH, label="Search"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Settings"),
        ],
        selected_index=0,
        # bgcolor="#03aac0",
        indicator_color="#00bcd4",
    )
        
        