from greeting.greeting import Greeting
from greeting.russian_greeting import RussianGreeting

class EnglishToRussianTranslator(Greeting):
    _greeting: RussianGreeting

    def __init__(self) -> None:
        self._greeting = RussianGreeting()

    def hello_to(self, name: str):
        self._greeting.common_greeting()
