from typing import List
from employee.worker import Worker
from employee.mine.cart_operator import CartOperator
from employee.mine.mine_digger import MineDigger
from employee.mine.tunnel_digger import TunnelDigger
from employee.action import Action

class MineFacade:
    _workers: List[Worker]

    def __init__(self) -> None:
        self._workers = [
            TunnelDigger(),
            CartOperator(),
            MineDigger()
        ]

    def process(self, workers: List[Worker], actions: List[Action]):
        for worker in workers:
            worker.process(actions)        

    def start_new_day(self):
        print("\n-- New day arrives! --\n")
        self.process(self._workers, [Action.WAKE_UP, Action.GO_TO_WORK])

    def dig_out(self):
        print("\n-- Work hard! Die hard! --\n")
        self.process(self._workers, [Action.WORK,])

    def end_day(self):
        print("\n-- It's time to rest, buddies!--\n")        
        self.process(self._workers, [Action.GO_HOME, Action.GO_TO_SLEEP])
