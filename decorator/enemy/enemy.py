from abc import ABCMeta, abstractmethod

class Enemy:
    __metaclass__ = ABCMeta

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def flee(self):
        pass
