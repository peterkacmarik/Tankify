# language_manager.py
class LanguageManager:
    _instance = None
    _current_language = "en"
    _subscribers = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LanguageManager, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_current_language(cls):
        return cls._current_language

    @classmethod
    def set_language(cls, language: str):
        cls._current_language = language
        # Notify all subscribers about the language change
        for subscriber in cls._subscribers:
            subscriber()

    @classmethod
    def subscribe(cls, callback):
        if callback not in cls._subscribers:
            cls._subscribers.append(callback)

    @classmethod
    def unsubscribe(cls, callback):
        if callback in cls._subscribers:
            cls._subscribers.remove(callback)

