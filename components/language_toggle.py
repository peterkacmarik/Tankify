# from typing import Callable
# import flet as ft

# from core.lang_manager import LanguageManager


# class LanguageToggle(ft.UserControl):
#     def __init__(self, page: ft.Page):
#         super().__init__()
#         self.page = page
#         self.lang_manager = LanguageManager(self.page)

#     def build(self):
#         return ft.PopupMenuButton(
#             icon=ft.icons.LANGUAGE,
#             icon_color=ft.colors.BLUE_GREY_400,
#             items=[
#                 ft.PopupMenuItem(
#                     content=ft.Row([
#                         ft.Image(
#                             src="/icons/us.svg",
#                             width=24,
#                             height=24,
#                             fit=ft.ImageFit.CONTAIN,
#                         ),
#                         ft.Text("English")
#                     ]),
#                     on_click=lambda _: self.change_language("en")
#                 ),
#                 ft.PopupMenuItem(
#                     content=ft.Row([
#                         ft.Image(
#                             src="/icons/sk.svg",
#                             width=24,
#                             height=24,
#                             fit=ft.ImageFit.CONTAIN,
#                         ),
#                         ft.Text("Slovenčina")
#                     ]),
#                     on_click=lambda _: self.change_language("sk")
#                 ),
#                 ft.PopupMenuItem(
#                     content=ft.Row([
#                         ft.Image(
#                             src="/icons/cz.svg",
#                             width=24,
#                             height=24,
#                             fit=ft.ImageFit.CONTAIN,
#                         ),
#                         ft.Text("Čeština")
#                     ]),
#                     on_click=lambda _: self.change_language("cs")
#                 ),
#             ]
#         )

#     def change_language(self, language_code: str):
#         # Zmení jazyk a uloží nový výber do client_storage
#         self.lang_manager.set_language(language_code)

#         # Obnoví stránku, aby sa nový jazyk prejavil
#         self.page.update()



        
        
        
        
        
        
        
# # class LanguageToggle(ft.UserControl):
# #     def __init__(self, page: ft.Page):
# #         super().__init__()
# #         self.page = page
# #         self.lang_manager = LanguageManager(self.page)
        
# #     def build(self):
# #         return ft.PopupMenuButton(
# #             icon=ft.icons.LANGUAGE,
# #             icon_color=ft.colors.BLUE_GREY_400,
# #             items=[
# #                 ft.PopupMenuItem(
# #                     content=ft.Row([
# #                         ft.Image(
# #                             src="/icons/us.svg",
# #                             width=24,
# #                             height=24,
# #                             fit=ft.ImageFit.CONTAIN,
# #                         ),
# #                         ft.Text("English")
# #                     ]),
# #                     on_click=lambda _: self.change_language("en")
# #                 ),
# #                 ft.PopupMenuItem(
# #                     content=ft.Row([
# #                         ft.Image(
# #                             src="/icons/sk.svg",
# #                             width=24,
# #                             height=24,
# #                             fit=ft.ImageFit.CONTAIN,
# #                         ),
# #                         ft.Text("Slovenčina")
# #                     ]),
# #                     on_click=lambda _: self.change_language("sk")
# #                 ),
# #                 ft.PopupMenuItem(
# #                     content=ft.Row([
# #                         ft.Image(
# #                             src="/icons/cz.svg",
# #                             width=24,
# #                             height=24,
# #                             fit=ft.ImageFit.CONTAIN,
# #                         ),
# #                         ft.Text("Čeština")
# #                     ]),
# #                     on_click=lambda _: self.change_language("cs")
# #                 ),
# #             ]
# #         )
    
                
# #     def change_language(self, language_code: str):
# #         # Zmení jazyk a uloží nový výber do client_storage
# #         self.lang_manager.set_language(language_code)  # Nastavenie nového jazyka v lang_manager

# #         # Uloženie nového jazyka do client_storage
# #         self.page.client_storage.set("language", language_code)

# #         # Obnoví stránku, aby sa nový jazyk prejavil
# #         self.page.update()  # Aktualizuje stránku s novými textami
            
            