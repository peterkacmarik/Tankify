# language_manager.py
import json
import os
from typing import Dict, Optional
import flet as ft

class LanguageManager:
    _current_language: str = "en"
    _translations: Dict[str, Dict] = {}
    _observers: list = []
    _storage_key = "selected_language"

    @classmethod
    def initialize(cls, page: ft.Page) -> None:
        """Načíta všetky jazykové súbory a obnoví uložený jazyk"""
        cls._load_translations()
        cls._load_saved_language(page)

    @classmethod
    def _load_translations(cls) -> None:
        """Načíta všetky jazykové súbory z priečinka locales"""
        locales_dir = "locales"
        supported_languages = ["sk", "cs", "en"]
        
        for lang in supported_languages:
            file_path = os.path.join(locales_dir, f"{lang}.json")
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    cls._translations[lang] = json.load(file)
            except FileNotFoundError:
                print(f"Warning: Missing language file for {lang}")

    @classmethod
    def _load_saved_language(cls, page: ft.Page) -> None:
        """Načíta uložené nastavenie jazyka"""
        saved_lang = page.client_storage.get(cls._storage_key)
        if saved_lang and saved_lang in cls._translations:
            cls._current_language = saved_lang

    @classmethod
    def get_text(cls, key: str) -> str:
        """Získa preložený text podľa kľúča v aktuálnom jazyku"""
        try:
            return cls._translations[cls._current_language].get(key, key)
        except KeyError:
            return key

    @classmethod
    def set_language(cls, language: str, page: ft.Page) -> None:
        """Nastaví nový jazyk, uloží ho a notifikuje observerov"""
        if language in cls._translations:
            cls._current_language = language
            page.client_storage.set(cls._storage_key, language)
            cls._notify_observers()

    @classmethod
    def add_observer(cls, observer) -> None:
        if observer not in cls._observers:
            cls._observers.append(observer)

    @classmethod
    def remove_observer(cls, observer) -> None:
        if observer in cls._observers:
            cls._observers.remove(observer)

    @classmethod
    def _notify_observers(cls) -> None:
        for observer in cls._observers:
            observer.update_language()



























# class LanguageManager:
#     _instance = None
#     _current_language = "en"
#     _subscribers = []

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(LanguageManager, cls).__new__(cls)
#         return cls._instance

#     @classmethod
#     def get_current_language(cls):
#         return cls._current_language

#     @classmethod
#     def set_language(cls, language: str):
#         cls._current_language = language
#         # Notify all subscribers about the language change
#         for subscriber in cls._subscribers:
#             subscriber()

#     @classmethod
#     def subscribe(cls, callback):
#         if callback not in cls._subscribers:
#             cls._subscribers.append(callback)

#     @classmethod
#     def unsubscribe(cls, callback):
#         if callback in cls._subscribers:
#             cls._subscribers.remove(callback)

