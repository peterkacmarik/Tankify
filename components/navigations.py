# import flet as ft
# from components.language_toggle import LanguageToggle
# from core.supa_base import get_supabese_client
# from core.lang_manager import LanguageManager


# def logout_user(page, e):
#     try:
#         # Odstránenie session údajov z Flet session storage
#         page.client_storage.remove("access_token")
#         page.client_storage.remove("refresh_token")

#         supabase = get_supabese_client()
#         response = supabase.auth.sign_out()

#         page.go("/login")
#         page.open(ft.SnackBar(content=""))
#         page.update()
#     except Exception as ex:
#         page.open(ft.SnackBar(content=""))
#         page.update()


# class NavigationAppBar:
#     def __init__(self, page: ft.Page):
#         self.page = page
#         self.lang_manager = LanguageManager(self.page)
        
#     def app_bar(self):
#         return ft.AppBar(
#             leading=ft.Icon(ft.icons.PALETTE, color=ft.colors.TRANSPARENT),
#             center_title=False,
#             actions=[
#                 ft.PopupMenuButton(
#                     icon=ft.icons.LANGUAGE,
#                     icon_color=ft.colors.BLUE_GREY_400,
#                     items=[
#                         ft.PopupMenuItem(
#                             content=ft.Row([
#                                 ft.Image(
#                                     src="/icons/us.svg",
#                                     width=24,
#                                     height=24,
#                                     fit=ft.ImageFit.CONTAIN,
#                                 ),
#                                 ft.Text("English")
#                             ]),
#                             on_click=lambda _: self.change_language("en")
#                         ),
#                         ft.PopupMenuItem(
#                             content=ft.Row([
#                                 ft.Image(
#                                     src="/icons/sk.svg",
#                                     width=24,
#                                     height=24,
#                                     fit=ft.ImageFit.CONTAIN,
#                                 ),
#                                 ft.Text("Slovenčina")
#                             ]),
#                             on_click=lambda _: self.change_language("sk")
#                         ),
#                         ft.PopupMenuItem(
#                             content=ft.Row([
#                                 ft.Image(
#                                     src="/icons/cz.svg",
#                                     width=24,
#                                     height=24,
#                                     fit=ft.ImageFit.CONTAIN,
#                                 ),
#                                 ft.Text("Čeština")
#                             ]),
#                             on_click=lambda _: self.change_language("cs")
#                         ),
#                     ]
#                 ),
#                 ft.Container(
#                     padding=ft.padding.only(left=0, top=0, right=10, bottom=0),
#                     content=ft.Row(
#                         spacing=10,
#                         controls=[
#                             ft.IconButton(
#                                 icon=ft.icons.LIGHT_MODE_OUTLINED,
#                                 selected_icon=ft.icons.DARK_MODE_OUTLINED,
#                                 # on_click=lambda e: switch_theme(self.page, e),
#                             ),
#                             ft.PopupMenuButton(
#                                 items=[
#                                     ft.PopupMenuItem(
#                                         text=self.lang_manager.get_translation("minha_conta"),
#                                         icon=ft.icons.ACCOUNT_CIRCLE,
#                                         on_click=lambda e: self.page.go("/settings/account"),
#                                     ),
#                                     ft.PopupMenuItem(),  # divider
#                                     ft.PopupMenuItem(
#                                         text=self.lang_manager.get_translation("logoff"),
#                                         icon=ft.icons.LOGOUT, 
#                                         on_click=lambda e: self.logout_user(e),
#                                     ),
#                                 ]
#                             ),
#                         ]
#                     )
#                 )
#             ],
#         )
        
#     def logout_user(self, e):
#         try:
#             # Odstránenie session údajov z Flet session storage
#             self.page.client_storage.remove("access_token")
#             self.page.client_storage.remove("refresh_token")
            
#             supabase = get_supabese_client()
#             response = supabase.auth.sign_out()
            
#             self.page.go("/login")
#             self.page.open(ft.SnackBar(content=ft.Text(self.lang_manager.get_translation("logoff_sucesso"))))
#             self.page.update()
#         except Exception as exception:
#             # print("Error:", exception)
#             self.page.open(ft.SnackBar(content=ft.Text(self.lang_manager.get_translation("logoff_erro"))))
#             self.page.update()

#     # def update_view_texts(self):
#     #     self.app_bar().actions.content.controls[1].items[0].text = self.lang_manager.get_translation("minha_conta")
#     #     self.app_bar().actions.content.controls[1].items[2].text = self.lang_manager.get_translation("logoff")

#     #     self.update()
#     #     self.page.update()
        
    
#     def update_view_texts(self):
#         self.page.views[0].update_view_texts()
#         self.page.update()
        
        
        
# class Drawer:
#     def __init__(self, page: ft.Page):
#         self.page = page
#         self.lang_manager = LanguageManager(self.page)
    
#     def left_drawer(self):
#         return ft.NavigationDrawer(
#             position=ft.NavigationDrawerPosition.START,
#             on_change=lambda e: self.handle_change_drawer(e),
#             # on_dismiss=self.handle_dismissal,
#             selected_index=0,
#             indicator_color=ft.colors.TRANSPARENT,
#             indicator_shape=ft.ContinuousRectangleBorder(radius=50),
#             controls=[
#                 ft.Container(
#                     alignment=ft.alignment.center,
#                     padding=ft.padding.all(16),
#                     content=ft.Column(
#                         alignment=ft.MainAxisAlignment.CENTER,
#                         horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                         controls=[
#                             ft.Container(
#                                 alignment=ft.alignment.center,
#                                 content=ft.Image(
#                                     src="/logo/fuel_logo_transparent_1024_crop_128.png",
#                                     width=72,
#                                     height=72,
#                                 ),
#                                 # content=ft.Icon(ft.icons.ACCOUNT_CIRCLE, size=64),
#                                 margin=ft.margin.only(top=20, bottom=10),
#                             ),
#                             ft.Text(
#                                 self.lang_manager.get_translation("google_play_titulo"), 
#                                 size=16, 
#                                 weight="bold",
#                             ),
#                         ]
#                     )
#                 ),
#                 ft.Divider(thickness=1),
#                 ft.NavigationDrawerDestination(
#                     label=self.lang_manager.get_translation("historico"),
#                     icon=ft.icons.HISTORY_OUTLINED,
#                     selected_icon=ft.icons.MANAGE_HISTORY,
#                 ),
#                 ft.NavigationDrawerDestination(
#                     label=self.lang_manager.get_translation("relatorios"),
#                     icon=ft.icons.REPORT_GMAILERRORRED_OUTLINED,
#                     selected_icon=ft.icons.REPORT,
#                 ),
#                 ft.NavigationDrawerDestination(
#                     label=self.lang_manager.get_translation("lembretes"),
#                     icon=ft.icons.NOTIFICATIONS_OUTLINED,
#                     selected_icon=ft.icons.NOTIFICATIONS,
#                 ),
#                 ft.Divider(thickness=1),
#                 ft.NavigationDrawerDestination(
#                     label=self.lang_manager.get_translation("veiculos"),
#                     icon=ft.icons.DIRECTIONS_CAR_OUTLINED,
#                     selected_icon=ft.icons.DIRECTIONS_CAR,
#                 ),
#                 ft.NavigationDrawerDestination(
#                     label=self.lang_manager.get_translation("usuarios"),
#                     icon=ft.icons.SUPERVISED_USER_CIRCLE_OUTLINED,
#                     selected_icon=ft.icons.SUPERVISED_USER_CIRCLE,
#                 ),
#                 ft.NavigationDrawerDestination(
#                     label=self.lang_manager.get_translation("configuracoes"),
#                     icon=ft.icons.SETTINGS_OUTLINED,
#                     selected_icon=ft.icons.SETTINGS,
#                 ),
#                 ft.Divider(thickness=1, opacity=1.0),
#                 ft.NavigationDrawerDestination(
#                     label=self.lang_manager.get_translation("contato"),
#                     icon=ft.icons.EMAIL_OUTLINED,
#                     selected_icon=ft.icons.EMAIL,
#                 )
#             ]
#         )
        
#     def handle_change_drawer(self, e):
#         selected_index = e.control.selected_index
#         if selected_index == 0:   # History
#             e.page.go("/history")
#         elif selected_index == 1:   # Report
#             e.page.go("/reports/general")
#         elif selected_index == 2:   # Reminders
#             e.page.go("/reminders")
#         elif selected_index == 3:   # Vehicles
#             e.page.go("/vehicles")
#         elif selected_index == 4:   # Users
#             e.page.go("/users")
#         elif selected_index == 5:   # Settings
#             e.page.go("/settings/general")
#         elif selected_index == 6:   # Contact
#             e.page.go("/contact")
#         e.page.update()
    
#     def update_view_texts(self):
#         # self.app_bar().actions.content.controls[1].items[0].text = self.lang_manager.get_translation("minha_conta")
#         # self.app_bar().actions.content.controls[1].items[2].text = self.lang_manager.get_translation("logoff")

#         self.update()
#         self.page.update()
    
        
# class BottomNavBar:
#     def __init__(self, page: ft.Page):
#         self.page = page
#         self.lang_manager = LanguageManager(self.page)
    
#     def navigation_bottom_bar(self):
#         return ft.NavigationBar(
#             selected_index=0,
#             on_change=lambda e: self.handle_change_bottom_nav(e),
#             # bgcolor=ft.colors.WHITE,
#             indicator_color=ft.colors.TRANSPARENT,
#             indicator_shape=ft.CircleBorder(type="circle"),
#             destinations=[
#                 ft.NavigationBarDestination(
#                     bgcolor=ft.colors.BLACK12,
#                     icon=ft.icons.HISTORY_OUTLINED, 
#                     label=self.lang_manager.get_translation("historico"),
#                     selected_icon=ft.icons.MANAGE_HISTORY,
#                 ),
#                 ft.NavigationBarDestination(
#                     icon=ft.icons.REPORT_GMAILERRORRED_OUTLINED, 
#                     label=self.lang_manager.get_translation("relatorios"),
#                     selected_icon=ft.icons.REPORT,
#                 ),            
#                 ft.NavigationBarDestination(
#                     icon=ft.icons.NOTIFICATIONS_OUTLINED, 
#                     label=self.lang_manager.get_translation("lembretes"),
#                     selected_icon=ft.icons.NOTIFICATIONS,
#                 ),
#                 ft.NavigationBarDestination(
#                     icon=ft.icons.MORE_HORIZ_OUTLINED, 
#                     label=self.lang_manager.get_translation("mais"),
#                     selected_icon=ft.icons.MORE_HORIZ,
#                 ),
                
#             ],
#         )
        
#     def handle_change_bottom_nav(self, e):
#         selected_index = e.control.selected_index
#         if selected_index == 0:   # History
#             e.page.go("/history")
#         elif selected_index == 1:   # Report
#             e.page.go("/reports/general")
#         elif selected_index == 2:   # Reminders
#             e.page.go("/reminders")
#         elif selected_index == 3:   # More
#             self.open_drawer()
#         e.page.update()
        
#     def open_drawer(self):
#         self.page.drawer.open = True
#         self.page.update()
        
#     def update_view_texts(self):
#         # self.app_bar().actions.content.controls[1].items[0].text = self.lang_manager.get_translation("minha_conta")
#         # self.app_bar().actions.content.controls[1].items[2].text = self.lang_manager.get_translation("logoff")

#         self.update()
#         self.page.update()