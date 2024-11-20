import flet as ft
from components.logo import home_page_logo, page_logo
from components.buttons import LoginButtons
from core.lang_manager import LanguageManager



class LinkSeparatorText:
    def __init__(self, page: ft.Page):
        self.page = page
        self.lang_manager = LanguageManager(self.page)
        
    def line_separator(self):
        return ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    bgcolor=ft.colors.GREY,
                    height=0.5,
                    width=130,
                    # expand=True
                ),
                ft.Text(
                    value=self.lang_manager.get_translation("ou").lower(),
                ),
                ft.Container(
                    bgcolor=ft.colors.GREY,
                    height=0.5,
                    width=130,
                    # expand=True
                ),
            ]
        )
        
        
#     def main_login_text(self):
#         return ft.Text(
#             self.lang_manager.get_translation("login"),
#             size=24,
#             weight=ft.FontWeight.NORMAL,
#             font_family="Roboto_Slap",
#         )
        
        
#     def forgot_password_link(self):
#         return ft.Container(
#             # border=ft.border.all(0),
#             alignment=ft.alignment.center,
#             content=ft.TextButton(
#                 style=ft.ButtonStyle(
#                     alignment=ft.alignment.center,
#                     bgcolor=ft.colors.TRANSPARENT
#                 ),
#                 content=ft.Text(
#                     value=self.lang_manager.get_translation("esqueceu_sua_senha"),
#                     style=ft.TextStyle(
#                         size=13,
#                         decoration=ft.TextDecoration.UNDERLINE
#                     )
#                 ),

#             )
#         )
        
        
#     def create_account_link(self):
#         return ft.Container(
#             alignment=ft.alignment.center,
#             content=ft.TextButton(
#                 text=self.lang_manager.get_translation("criar_conta").upper(),
#                 style=ft.ButtonStyle(
#                     overlay_color=ft.colors.TRANSPARENT,
#                 ),
#                 on_click=lambda _: self.page.go("/register"),
#             )
#         )
        
        
#     def main_register_text(self):
#         return ft.Container(
#             # border=ft.border.all(0),
#             alignment=ft.alignment.center,
#             content=ft.Text(
#                 self.lang_manager.get_translation("criar_conta_tankify"),
#                 size=24,
#                 weight=ft.FontWeight.NORMAL,
#                 font_family="Roboto_Slap",
#             )        
#         )
        
        
#     def sub_register_text(self):
#         return ft.Container(
#             # border=ft.border.all(0),
#             alignment=ft.alignment.center,
#             content=ft.Text(
#                 self.lang_manager.get_translation("comece_gerenciamento_gratuito"),
#                 size=15,
#                 weight=ft.FontWeight.NORMAL,
#                 color=ft.colors.GREY_600,
#             )
#         )
        
        
#     def main_forgot_password_text(self):
#         return ft.Container(
#             alignment=ft.alignment.center,
#             content=ft.Text(
#                 self.lang_manager.get_translation("esqueceu_sua_senha"),
#                 size=24,
#                 weight=ft.FontWeight.NORMAL,
#                 font_family="Roboto_Slap",
#             )
#         )
        
        
#     def sub_forgot_password_text(self):
#         return ft.Container(
#             padding=ft.padding.only(bottom=20),
#             alignment=ft.alignment.center,
#             content=ft.Text(
#                 self.lang_manager.get_translation("ajudaremos_redefinir"),
#                 size=16,
#                 weight=ft.FontWeight.NORMAL,
#                 font_family="Roboto_Slab",
#             )
#         )
        
        
#     def cancel_link(self):
#         return ft.Container(
#             alignment=ft.alignment.center,
#             content=ft.TextButton(
#                 text=self.lang_manager.get_translation("btn_cancelar").upper(),
#                 style=ft.ButtonStyle(
#                     overlay_color=ft.colors.TRANSPARENT,
#                 ),
#                 on_click=lambda _: self.page.go("/login")
#             )
#         )
        
    
# def home_page_box(page: ft.Page):
#     return ft.Container(
#         alignment=ft.alignment.center,
#         content=ft.Column(
#             alignment=ft.alignment.center,
#             controls=[
#                 ft.Stack(
#                     alignment=ft.alignment.center,
#                     controls=[
#                         # Spodný rámček
#                         ft.Container(
#                             alignment=ft.alignment.center,
#                             width=300,
#                             height=500,
#                             top=100,  # posunie rámček nižšie
#                             border_radius=20,
#                             border=ft.border.all(1, ft.colors.GREY_500),
#                             bgcolor=ft.colors.WHITE,
#                             padding=ft.padding.only(left=20, top=70, right=20, bottom=20),
#                             content=ft.Column(
#                                 spacing=10,
#                                 alignment=ft.alignment.center,
#                                 controls=[
#                                     ft.Text(
#                                         value="Text...",
#                                         size=16,
#                                         weight=ft.FontWeight.NORMAL,
#                                         font_family="Roboto_Slap",
#                                     ),
                                    
#                                 ]
#                             )
#                         ),
                        
#                         # Logo prekrývajúce rámček
#                         ft.Column(
#                             alignment=ft.alignment.center,
#                             top=35,
#                             controls=[
#                                 ft.Container(
#                                     content=ft.Image(
#                                         src="/logo/logo_147.png",
#                                         width=128,
#                                         height=128,
#                                     ),
#                                     width=128,
#                                     height=128,
#                                     # bgcolor=ft.colors.WHITE,
#                                     # border=ft.border.all(1, ft.colors.GREY_500),
#                                     border_radius=100,
#                                 )
#                             ]
#                         )
#                     ],
#                     width=350,
#                     height=800,
#                 )
#             ]
#         )
#     )
    
    
    
    