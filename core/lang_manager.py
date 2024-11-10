import json
import os
import flet as ft
from typing import Callable, Dict, Optional

    
class LanguageManager:
    def __init__(self, page: ft.Page):
        self.page = page
        # Skontroluj, či `client_storage` existuje, inak nastav predvolený jazyk
        if hasattr(self.page, "client_storage") and self.page.client_storage:
            stored_language = self.page.client_storage.get("language")
        else:
            stored_language = None

        # Nastav aktuálny jazyk na základe uloženého jazyka alebo predvoleného "en"
        self.current_language = stored_language if stored_language else "en"
        self.translations = self.load_language(self.current_language)
        self.language_change_callbacks = []  # Uchovávanie callback funkcií

    def load_language(self, lang_code):
        file_path = os.path.join("locales", f"{lang_code}.json")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Warning: Language file for '{lang_code}' not found. Falling back to default language.")
            return {}

    def set_language(self, lang_code):
        # Nastaví nový jazyk a uloží ho do client_storage
        self.current_language = lang_code
        self.page.client_storage.set("language", lang_code)
        self.translations = self.load_language(lang_code)
        
        # Spustí všetky registrované callback funkcie na aktualizáciu jazyka
        for callback in self.language_change_callbacks:
            callback()

    def get_translation(self, key, default=""):
        return self.translations.get(key, default)

    def register_language_change_callback(self, callback):
        # Zaregistruje callback funkciu, ktorá sa zavolá pri zmene jazyka
        self.language_change_callbacks.append(callback)


    def get_supported_languages(self):
        # Vráti slovník podporovaných jazykov
        return {
            "en": "English",
            "sk": "Slovenčina",
            "cs": "Čeština",
        }
    
    