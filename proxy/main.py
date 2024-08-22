from entity.wizard import Wizard
from tower.tower import Tower
from tower.impl.ivory_tower import IvoryTower
from tower_proxy import TowerProxy

def main():
    ivory_tower = IvoryTower()
    protected_tower = TowerProxy(ivory_tower)

    protected_tower.enter(Wizard("Red wizard"))
    protected_tower.enter(Wizard("Orange wizard"))
    protected_tower.enter(Wizard("Yellow wizard"))
    protected_tower.enter(Wizard("Green wizard"))
    protected_tower.enter(Wizard("Cyan wizard"))
    protected_tower.enter(Wizard("Blue wizard"))
    protected_tower.enter(Wizard("Purple wizard"))

if __name__ == "__main__":
    main()
