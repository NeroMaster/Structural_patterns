from ..enemy import Enemy

class OrcWarrior(Enemy):

    def attack(self):
        print("The orc swings with axe!")

    def flee(self):
        print("The orc shrieks in horror and runs away!")
