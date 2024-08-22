from tower.tower import Tower
from entity.wizard import Wizard

class IvoryTower(Tower):
    def enter(self, wizard: Wizard):
        print(f"{wizard} enters the ivory tower!")
