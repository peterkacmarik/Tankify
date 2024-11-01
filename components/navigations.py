import flet as ft

        

def app_bar(page: ft.Page, open_draver, switch_theme, translation):
    return ft.AppBar(
        leading=ft.IconButton(
            ft.icons.MENU,
            on_click=open_draver,
        ),
        leading_width=40,
        center_title=False,
        actions=[
            ft.IconButton(
                ft.icons.WB_SUNNY_OUTLINED,
                on_click=switch_theme,
            ),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        text=translation["minha_conta"],
                        icon=ft.icons.ACCOUNT_CIRCLE,
                        on_click=lambda e: page.go("/settings/account"),
                    ),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text=translation["logoff"],
                        icon=ft.icons.LOGOUT, 
                        on_click=lambda e: page.go("/logout"),
                    ),
                ]
            ),
        ],
    )
        
        
def left_drawer(translation, handle_change_drawer):
    return ft.NavigationDrawer(
        position=ft.NavigationDrawerPosition.START,
        on_change=handle_change_drawer,
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
                            content=ft.Icon(ft.icons.ACCOUNT_CIRCLE, size=64),
                            margin=ft.margin.only(top=20, bottom=10),
                        ),
                        ft.Text(
                            translation["google_play_titulo"], 
                            size=16, 
                            weight="bold",
                        ),
                    ]
                )
            ),
            ft.Divider(thickness=1),
            ft.NavigationDrawerDestination(
                label=translation["historico"],
                icon=ft.icons.HISTORY_OUTLINED,
                selected_icon=ft.icons.MANAGE_HISTORY,
            ),
            ft.NavigationDrawerDestination(
                label=translation["adicionar_novo"],
                icon=ft.icons.ADD_OUTLINED,
                selected_icon=ft.icons.ADD_CIRCLE,
            ),
            ft.NavigationDrawerDestination(
                label=translation["lembretes"],
                icon=ft.icons.NOTIFICATIONS_OUTLINED,
                selected_icon=ft.icons.NOTIFICATIONS,
            ),
            ft.NavigationDrawerDestination(
                label=translation["relatorios"],
                icon=ft.icons.REPORT_GMAILERRORRED_OUTLINED,
                selected_icon=ft.icons.REPORT,
            ),
            ft.Divider(thickness=1),
            ft.NavigationDrawerDestination(
                label=translation["veiculos"],
                icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
                selected_icon=ft.icons.DIRECTIONS_CAR,
            ),
            ft.NavigationDrawerDestination(
                label=translation["usuarios"],
                icon=ft.icons.SUPERVISED_USER_CIRCLE_OUTLINED,
                selected_icon=ft.icons.SUPERVISED_USER_CIRCLE,
            ),
            ft.NavigationDrawerDestination(
                label=translation["configuracoes"],
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon=ft.icons.SETTINGS,
            ),
            ft.Divider(thickness=1, opacity=1.0),
            ft.NavigationDrawerDestination(
                label=translation["contato"],
                icon=ft.icons.EMAIL_OUTLINED,
                selected_icon=ft.icons.EMAIL,
            ),
        ],
        
    )
        
        
def bottom_navigation_bar(translation, handle_change_bottom_nav):
    return ft.NavigationBar(
            selected_index=0,
            on_change=handle_change_bottom_nav,
            # bgcolor=ft.colors.WHITE,
            indicator_color=ft.colors.TRANSPARENT,
            indicator_shape=ft.CircleBorder(type="circle"),
            destinations=[
                ft.NavigationBarDestination(
                    bgcolor=ft.colors.BLACK12,
                    icon=ft.icons.HISTORY_OUTLINED, 
                    label=translation["historico"],
                    selected_icon=ft.icons.MANAGE_HISTORY,
                ),
                ft.NavigationBarDestination(
                    icon=ft.icons.REPORT_GMAILERRORRED_OUTLINED, 
                    label=translation["relatorios"],
                    selected_icon=ft.icons.REPORT,
                ),
                ft.NavigationBarDestination(
                    icon=ft.icons.ADD_OUTLINED, 
                    selected_icon=ft.icons.ADD_CIRCLE,
                ),
                ft.NavigationBarDestination(
                    icon=ft.icons.NOTIFICATIONS_OUTLINED, 
                    label=translation["lembretes"],
                    selected_icon=ft.icons.NOTIFICATIONS,
                ),
                ft.NavigationBarDestination(
                    icon=ft.icons.MORE_HORIZ_OUTLINED, 
                    label=translation["mais"],
                    selected_icon=ft.icons.MORE_HORIZ,
                ),
            ],
        )
        
        