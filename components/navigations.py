import flet as ft

from locales.language_manager import LanguageManager

lang_manager = LanguageManager()


def app_bar(page: ft.Page, switch_theme):
    return ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE, color=ft.colors.TRANSPARENT),
        title=ft.Text(lang_manager.get_text("historico"), size=18),
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
                            on_click=switch_theme,
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
                                    on_click=lambda e: page.go("/login"),
                                ),
                            ]
                        ),
                    ]
                )
            )
        ],
    )
        
        
def left_drawer(handle_change_drawer):
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
            # ft.NavigationDrawerDestination(
            #     label=translation["adicionar_novo"],
            #     icon=ft.icons.ADD_OUTLINED,
            #     selected_icon=ft.icons.ADD_CIRCLE,
            # ),
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
            ),
        ],
        
    )
        
    
def navigation_bottom_bar(handle_change_bottom_nav):
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
    
    
# def bottom_appbar_nav(translation):
#     return ft.BottomAppBar(
#         shape=ft.NotchShape.CIRCULAR,
#         content=ft.Container(
#             alignment=ft.alignment.center,
#             padding=ft.padding.only(left=20, right=20, top=0, bottom=0),
#             content=ft.Row(
#                 spacing=20,
#                 # expand=True,
#                 vertical_alignment=ft.CrossAxisAlignment.CENTER,
#                 alignment=ft.MainAxisAlignment.CENTER,
#                 controls=[
#                     ft.Column(
#                         spacing=-10,
#                         controls=[
#                             ft.IconButton(
#                                 icon=ft.icons.HISTORY_OUTLINED, 
#                                 selected_icon=ft.icons.MANAGE_HISTORY,
#                             ),
#                             ft.Text(translation["historico"], size=12),
#                         ]
#                     ),
#                     ft.Column(
#                         spacing=-10,
#                         controls=[
#                             ft.IconButton(
#                                 icon=ft.icons.REPORT_GMAILERRORRED_OUTLINED, 
#                                 selected_icon=ft.icons.REPORT,
#                             ),
#                             ft.Text(translation["relatorios"], size=12),
#                         ]
#                     ),
#                     ft.Container(expand=True),
#                     ft.Column(
#                         spacing=-10,
#                         controls=[
#                             ft.IconButton(
#                                 icon=ft.icons.NOTIFICATIONS_OUTLINED, 
#                                 selected_icon=ft.icons.NOTIFICATIONS,
#                             ),
#                             ft.Text(translation["lembretes"], size=12),
#                         ]
#                     ),
#                     ft.Column(
#                         spacing=-10,
#                         controls=[
#                             ft.IconButton(
#                                 icon=ft.icons.MORE_HORIZ_OUTLINED, 
#                                 selected_icon=ft.icons.MORE_HORIZ,
#                             ),
#                             ft.Text(translation["mais"], size=12),
#                         ]
#                     ),
#                 ],
#             )
#         )
#     )
    
        