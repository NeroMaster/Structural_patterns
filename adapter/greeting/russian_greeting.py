from abc import ABCMeta, abstractmethod

class RussianGreeting:
    __metaclass__ = ABCMeta

    @abstractmethod
    def common_greeting(self):
        print("Добрый день, Товарищ!")