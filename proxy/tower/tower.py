from abc import ABCMeta, abstractmethod
from entity.wizard import Wizard

class Tower:
    @abstractmethod
    def enter(self, wizard: Wizard):
        pass

