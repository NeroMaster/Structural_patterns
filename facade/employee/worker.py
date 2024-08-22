from typing import List
from .action import Action
from abc import ABCMeta, abstractmethod

class Worker:
    __metaclass__ = ABCMeta

    @abstractmethod
    def _work(self):
        pass

    @abstractmethod
    def _get_profession(self):
        pass

    def _go_to_sleep(self):
        print(f"{self._get_profession()} goes to sleep.")

    def _wake_up(self):
        print(f"{self._get_profession()} wakes up.")

    def _go_home(self):
        print(f"{self._get_profession()} goes home.")   

    def _go_to_work(self):
        print(f"{self._get_profession()} goes to work.")

    def process(self, actions: List[Action]):
        for action in actions:
            if action == Action.GO_TO_SLEEP:
                self._go_to_sleep()
            elif action == Action.WAKE_UP:
                self._wake_up()
            elif action == Action.GO_HOME:
                self._go_home()
            elif action == Action.GO_TO_WORK:
                self._go_to_work()
            elif action == Action.WORK:
                self._work()

