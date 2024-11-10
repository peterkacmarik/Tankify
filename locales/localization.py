import flet as ft
from typing import Dict, Optional, List, Callable
import json
import os
from dataclasses import dataclass
from enum import Enum

class TextDirection(Enum):
    LTR = "ltr"
    RTL = "rtl"

@dataclass
class LocaleInfo:
    code: str
    name: str
    direction: TextDirection
    flag_emoji: str

class LocalizationService:
    def __init__(self, translations_dir: str = "translations"):
        self.translations_dir = translations_dir
        self.current_locale: str = "en"
        self.translations: Dict[str, Dict[str, str]] = {}
        self.callbacks: List[Callable[[ft.Control], None]] = []
        self.supported_locales = {
            "en": LocaleInfo("en", "English", TextDirection.LTR, "🇬🇧"),
            "sk": LocaleInfo("sk", "Slovenčina", TextDirection.LTR, "🇸🇰"),
            "cs": LocaleInfo("cs", "Čeština", TextDirection.LTR, "🇨🇿"),
        }
        self._load_translations()

    def _load_translations(self):
        if not os.path.exists(self.translations_dir):
            os.makedirs(self.translations_dir)
        for locale in self.supported_locales:
            file_path = os.path.join(self.translations_dir, f"{locale}.json")
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.translations[locale] = json.load(f)
            else:
                self.translations[locale] = {}

    def get_text(self, key: str, default: Optional[str] = None) -> str:
        return self.translations[self.current_locale].get(key, default or key)

    def switch_locale(self, locale: str):
        if locale in self.supported_locales:
            self.current_locale = locale
            for callback in self.callbacks:
                callback(self)

    def add_listener(self, callback: Callable[[ft.Control], None]):
        if callback not in self.callbacks:
            self.callbacks.append(callback)

    def get_text_direction(self) -> TextDirection:
        return self.supported_locales[self.current_locale].direction

    def create_language_selector(self) -> ft.PopupMenuButton:
        def on_language_selected(e):
            # Prepneme jazyk na základe vybraného kľúča
            self.switch_locale(e.control.data)

        # Vytvoríme tlačidlo, ktoré zobrazuje aktuálny jazyk a umožňuje výber
        return ft.PopupMenuButton(
            icon=ft.icons.LANGUAGE,
            # tooltip="Select Language",
            items=[
                ft.PopupMenuItem(
                    text=f"{info.flag_emoji} {info.name}",
                    data=locale,  # Uložíme kód jazyka do data
                    on_click=on_language_selected
                )
                for locale, info in self.supported_locales.items()
            ]
        )


class LocalizedText(ft.Text):
    def __init__(self, localization: LocalizationService, text_key: str, default: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.localization = localization
        self.text_key = text_key
        self.default = default
        self.value = self.localization.get_text(text_key, default)

        def update_text(loc: LocalizationService):
            self.value = loc.get_text(self.text_key, self.default)

            # Skontrolujeme, či je komponent pridaný na stránku
            if self.page is not None:
                self.update()
            else:
                print("LocalizedText komponent ešte nebol pridaný na stránku.")
            # self.update()
        self.localization.add_listener(update_text)

    def did_mount(self):
        """Volá sa po pridaní komponentu na stránku."""
        super().did_mount()
        # Keď je komponent pridaný na stránku, zavoláme update_text na aktualizáciu textu
        self.value = self.localization.get_text(self.text_key, self.default)
        self.update()

class LocalizedTextField(ft.TextField):
    def __init__(self, localization: LocalizationService, text_key: str, **kwargs):
        super().__init__(**kwargs)
        self.localization = localization
        self.text_key = text_key
        self.label = self.localization.get_text(text_key)

        def update_label(loc: LocalizationService):
            self.label = loc.get_text(self.text_key)
            # self.update()

            # Skontrolujeme, či je komponent pridaný na stránku
            if self.page is not None:
                self.update()
            else:
                print("LocalizedText komponent ešte nebol pridaný na stránku.")

        self.localization.add_listener(update_label)

    def did_mount(self):
        """Volá sa po pridaní komponentu na stránku."""
        super().did_mount()
        # Keď je komponent pridaný na stránku, zavoláme update_label na aktualizáciu labelu
        self.label = self.localization.get_text(self.text_key)
        self.update()

class LocalizedRadio(ft.Radio):
    def __init__(self, localization: LocalizationService, text_key: str, **kwargs):
        super().__init__(**kwargs)
        self.localization = localization
        self.text_key = text_key
        self.label = self.localization.get_text(text_key)

        def update_label(loc: LocalizationService):
            self.label = loc.get_text(self.text_key)
            # self.update()

            # Skontrolujeme, či je komponent pridaný na stránku
            if self.page is not None:
                self.update()
            else:
                print("LocalizedText komponent ešte nebol pridaný na stránku.")

        self.localization.add_listener(update_label)

    def did_mount(self):
        """Volá sa po pridaní komponentu na stránku."""
        super().did_mount()
        # Keď je komponent pridaný na stránku, zavoláme update_label na aktualizáciu labelu
        self.label = self.localization.get_text(self.text_key)
        self.update()

class LocalizedDataTable(ft.DataTable):
    def __init__(self, localization: LocalizationService, column_keys: List[str], **kwargs):
        self.localization = localization
        self.column_keys = column_keys
        # Inicializuj stĺpce s predvolenými názvami (na základe aktuálneho jazyka)
        columns = [ft.DataColumn(label=ft.Text(self.localization.get_text(key))) for key in column_keys]

        # Volanie super().__init__ s vytvorenými stĺpcami
        super().__init__(columns=columns, **kwargs)

        # Listener pre dynamickú zmenu jazyka
        def update_columns(loc: LocalizationService):
            for i, key in enumerate(self.column_keys):
                # Aktualizácia názvu stĺpca
                self.columns[i].label.value = loc.get_text(key)
            # self.update()  # Aktualizuj komponent
            # Skontrolujeme, či je komponent pridaný na stránku
            if self.page is not None:
                self.update()  # Aktualizuj komponent
            else:
                print("LocalizedDataTable komponent ešte nebol pridaný na stránku.")

        # Pridaj listener
        self.localization.add_listener(update_columns)

    def did_mount(self):
        """Volá sa po pridaní komponentu na stránku."""
        super().did_mount()
        # Aktualizujeme stĺpce na základe aktuálneho jazyka
        for i, key in enumerate(self.column_keys):
            self.columns[i].label.value = self.localization.get_text(key)
        self.update()


# Localized Navigation
class LocalizedPopupMenuButton(ft.PopupMenuButton):
    def __init__(self, localization: LocalizationService, item_keys: List[Dict[str, str]], page: ft.Page, **kwargs):
        self.localization = localization
        self.item_keys = item_keys
        self.page = page  # Priradíme page, aby sme s ním mohli pracovať neskôr

        # Vytvor PopupMenuItem položky s predvolenými textami na základe aktuálneho jazyka
        items = [
            ft.PopupMenuItem(
                icon=item["icon"],
                text=self.localization.get_text(item["key"]),
                on_click=item["on_click"]
            )
            for item in item_keys
        ]

        # Inicializuj PopupMenuButton s položkami
        super().__init__(items=items, **kwargs)

        # Listener pre dynamickú zmenu jazyka
        def update_menu_items(loc: LocalizationService):
            # Skontrolujeme, či je `self.page` a či má atribút `controls`
            if self.page is not None and hasattr(self.page, 'controls'):
                for i, item in enumerate(self.item_keys):
                    # Aktualizujeme text položiek menu
                    self.items[i].text = loc.get_text(item["key"])

                self.update()  # Aktualizujeme komponent

        # Pridaj listener na zmeny lokalizácie
        self.localization.add_listener(update_menu_items)

class LocalizedNavigationBar(ft.NavigationBar):
    def __init__(self, localization: LocalizationService, navigation_items: List[Dict[str, str]], **kwargs):
        self.localization = localization
        self.navigation_items = navigation_items

        # Create localized navigation items
        items = [
            ft.NavigationRailDestination(
                icon=item["icon"],
                label=self.localization.get_text(item["key"]),
            )
            for item in navigation_items
        ]

        # Call the super constructor with the localized items
        super().__init__(destinations=items, **kwargs)

        # Add listener for language changes
        def update_navigation_items(loc: LocalizationService):
            if self.page is not None and hasattr(self.page, 'controls'):
                for i, item in enumerate(self.navigation_items):
                    self.destinations[i].label = loc.get_text(item["key"])
                self.update()  # Update the component

        self.localization.add_listener(update_navigation_items)

class LocalizedNavigationDrawer(ft.NavigationDrawer):
    def __init__(self, localization: LocalizationService, item_keys: List[Dict[str, str]], **kwargs):
        self.localization = localization
        self.item_keys = item_keys

        # Vytvorenie úvodných položiek - logo a podnadpis
        header = ft.Column(
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
                margin=ft.margin.only(top=20),
            ),
            ft.Text(
                value="TankiFy",
                size=26,
                weight=ft.FontWeight.NORMAL,
                font_family="Audiowide"
            ),
            ft.Divider(thickness=1),  # Oddelovač
        ])

        # Inicializácia položiek pre NavigationDrawer
        # destinations = [
        #     ft.NavigationDrawerDestination(
        #         icon=item["icon"],
        #         label=self.localization.get_text(item["key"])
        #     )
        #     for item in item_keys
        # ]

        # Pridanie úvodného layoutu a položiek do zoznamu ovládacích prvkov
        controls = [header]# + destinations

        # Pridáme prvé tri položky
        controls.extend(
            ft.NavigationDrawerDestination(
                icon=item["icon"],
                label=self.localization.get_text(item["key"])
            )
            for item in item_keys[:3]
        )

        # Prvý oddelovač po prvých troch položkách
        controls.append(ft.Divider(thickness=1))

        # Pridáme ďalšie dve položky
        controls.extend(
            ft.NavigationDrawerDestination(
                icon=item["icon"],
                label=self.localization.get_text(item["key"])
            )
            for item in item_keys[4:12]
        )

        # Druhý oddelovač po dvoch ďalších položkách
        controls.append(ft.Divider(thickness=1))

        # Ak sú ďalšie položky, pridáme ich nakoniec
        controls.extend(
            ft.NavigationDrawerDestination(
                icon=item["icon"],
                label=self.localization.get_text(item["key"])
            )
            for item in item_keys[13:]
        )

        # Vytvoríme NavigationDrawer s preloženými položkami
        super().__init__(controls=controls, **kwargs)

        # Funkcia na dynamickú aktualizáciu textov v NavigationDrawer
        def update_drawer(loc: LocalizationService):
            if self.page is not None and hasattr(self.page, 'controls'):
                for i, item in enumerate(self.item_keys):
                    # print(loc.get_text(item["key"]))
                    self.controls[i+1].label = loc.get_text(item["key"])
                self.update()  # Aktualizácia komponentu

        # Pridáme listener na lokalizáciu
        self.localization.add_listener(update_drawer)


# Localized Buttons
class LocalizedTextButton(ft.TextButton):
    def __init__(self, localization: LocalizationService, text_key: str, default: Optional[str] = None, **kwargs):
        self.localization_service = localization
        self.text_key = text_key
        self.default = default

        # Nastavenie textu tlačidla na základe aktuálneho jazyka
        initial_text = self.localization_service.get_text(text_key, default)
        super().__init__(text=initial_text, **kwargs)

        # Pridanie listenera pre dynamickú aktualizáciu textu
        self.localization_service.add_listener(self.update_text)

    def update_text(self, loc):
        """Aktualizuje text tlačidla pri zmene jazyka."""
        self.text = loc.get_text(self.text_key, self.default)
        # self.update()

        # Skontrolujeme, či je komponent pridaný na stránku
        if self.page is not None:
            self.update()
        else:
            print("LocalizedOutlinedButton komponent ešte nebol pridaný na stránku.")

    def did_mount(self):
        """Volá sa po pridaní komponentu na stránku."""
        super().did_mount()
        # Keď je komponent pridaný na stránku, zavoláme update_text na aktualizáciu textu
        self.update_text(self.localization_service)

    def dispose(self):
        """Odstráni listener, keď už nie je potrebný."""
        self.localization_service.remove_listener(self.update_text)
        super().dispose()

class LocalizedOutlinedButton(ft.OutlinedButton):
    def __init__(self, localization: LocalizationService, text_key: str, default: Optional[str] = None, **kwargs):
        self.localization_service = localization
        self.text_key = text_key
        self.default = default

        # Nastavenie počiatočného textu tlačidla na základe aktuálneho jazyka
        initial_text = self.localization_service.get_text(text_key, default)
        super().__init__(text=initial_text, **kwargs)

        # Pridanie listenera pre dynamickú aktualizáciu textu pri zmene jazyka
        self.localization_service.add_listener(self.update_text)

    def update_text(self, loc):
        """Aktualizuje text tlačidla pri zmene jazyka."""
        self.text = loc.get_text(self.text_key, self.default)
        # self.update()

        # Skontrolujeme, či je komponent pridaný na stránku
        if self.page is not None:
            self.update()
        else:
            print("LocalizedOutlinedButton komponent ešte nebol pridaný na stránku.")

    def did_mount(self):
        """Volá sa po pridaní komponentu na stránku."""
        super().did_mount()
        # Keď je komponent pridaný na stránku, zavoláme update_text na aktualizáciu textu
        self.update_text(self.localization_service)

    def dispose(self):
        """Odstráni listener pri uvoľnení tlačidla z pamäte."""
        self.localization_service.remove_listener(self.update_text)
        super().dispose()

class LocalizedElevatedButton(ft.ElevatedButton):
    def __init__(self, localization: LocalizationService, text_key: str, default: Optional[str] = None, **kwargs):
        self.localization_service = localization
        self.text_key = text_key
        self.default = default

        # Nastavenie počiatočného textu tlačidla na základe aktuálneho jazyka
        initial_text = self.localization_service.get_text(text_key, default)
        super().__init__(text=initial_text, **kwargs)

        # Pridanie listenera pre dynamickú aktualizáciu textu pri zmene jazyka
        self.localization_service.add_listener(self.update_text)

    def update_text(self, loc):
        """Aktualizuje text tlačidla pri zmene jazyka."""
        self.text = loc.get_text(self.text_key, self.default)
        # self.update()

        # Skontrolujeme, či je komponent pridaný na stránku
        if self.page is not None:
            self.update()
        else:
            print("LocalizedOutlinedButton komponent ešte nebol pridaný na stránku.")

    def did_mount(self):
        """Volá sa po pridaní komponentu na stránku."""
        super().did_mount()
        # Keď je komponent pridaný na stránku, zavoláme update_text na aktualizáciu textu
        self.update_text(self.localization_service)

    def dispose(self):
        """Odstráni listener pri uvoľnení tlačidla z pamäte."""
        self.localization_service.remove_listener(self.update_text)
        super().dispose()

# Localized Dropdown
class LocalizedDropdown(ft.Dropdown):
    def __init__(self, localization, label_key: str, options_keys: List[Dict[str, str]], **kwargs):
        self.localization_service = localization
        self.label_key = label_key
        self.options_keys = options_keys

        # Inicializácia dropdown s preloženými možnosťami
        initial_label = self.localization_service.get_text(self.label_key)
        initial_options = [
            ft.dropdown.Option(text=self.localization_service.get_text(item["key"]))
            for item in options_keys
        ]
        super().__init__(label=initial_label, options=initial_options, **kwargs)

        # Pridanie listenera pre dynamickú aktualizáciu prekladov
        self.localization_service.add_listener(self.update_options)

    def update_options(self, loc):
        """Aktualizuje texty možností pri zmene jazyka."""
        # Aktualizácia textu pre label
        self.label = loc.get_text(self.label_key)

        for option, item in zip(self.options, self.options_keys):
            option.text = loc.get_text(item["key"])

        # Skontrolujeme, či je komponent pridaný na stránku pred volaním update()
        if self.page is not None:
            self.update()
        else:
            print("LocalizedDropdown ešte nebol pridaný na stránku.")

    def dispose(self):
        """Odstráni listener pri uvoľnení dropdownu z pamäte."""
        self.localization_service.remove_listener(self.update_options)
        super().dispose()








