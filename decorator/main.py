from enemy.impl.orc_warlord import OrcWarlord
from enemy.impl.orc_warrior import OrcWarrior
from enemy.enemy import Enemy

def main():
    print("\nOrc warrior approaches!\n")
    warrior = OrcWarrior()
    warrior.attack()

    print("\nOrc warrior promoted to Warlord!\n")
    promoted = OrcWarlord(warrior)
    promoted.attack()

if __name__ == "__main__":
    main()

