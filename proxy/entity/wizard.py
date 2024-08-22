class Wizard:
    _name: str

    def __init__(self, name) -> None:
        self._name = name

    def __str__(self) -> str:
        return self._name
