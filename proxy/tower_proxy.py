from entity.wizard import Wizard
from tower.tower import Tower

class TowerProxy(Tower):
    _MAX_WIZARD_NUMBER = 5
    _allowed_wizards: int = 0
    _tower: Tower

    def __init__(self, tower: Tower) -> None:
        self._tower = tower

    def enter(self, wizard: Wizard):
        if self._allowed_wizards < self._MAX_WIZARD_NUMBER:
            self._tower.enter(wizard)
            self._allowed_wizards += 1
        else:
            print(f"{wizard} is not allowed to ivory tower!")
