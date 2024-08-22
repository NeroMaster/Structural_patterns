from ..enemy import Enemy

class OrcWarlord(Enemy):
    _decorated: Enemy

    def __init__(self, decorated: Enemy) -> None:
        self._decorated = decorated

    def attack(self):
        print("Orc lets out a powerful war cry!")
        self._decorated.attack()

    def flee(self):
        self._decorated.flee()
