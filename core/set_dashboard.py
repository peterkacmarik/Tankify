import flet as ft





def update_theme(page: ft.Page, light_bgcolor: str, dark_bgcolor: str):
    bgcolor = light_bgcolor if page.theme_mode == ft.ThemeMode.LIGHT else dark_bgcolor
    page.update()
    return bgcolor
    