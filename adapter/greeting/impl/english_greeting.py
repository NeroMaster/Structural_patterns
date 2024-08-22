from ..greeting import Greeting

class EnglishGreeting(Greeting):

    @classmethod
    def hello_to(cls, name: str):
        print(f"Hello, {name}!")