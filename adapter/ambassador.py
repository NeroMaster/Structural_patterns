from greeting.greeting import Greeting

class Ambassador:
    _greeting: Greeting

    def __init__(self, greeting: Greeting) -> None:
        self._greeting = greeting

    def greet(self, name: str):
        self._greeting.hello_to(name)
