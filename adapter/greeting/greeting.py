from abc import ABCMeta, abstractmethod

class Greeting:
    __metaclass__ = ABCMeta

    @abstractmethod
    def hello_to(self, name: str):
        pass