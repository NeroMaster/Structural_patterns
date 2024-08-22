from ..worker import Worker

class MineDigger(Worker):
    def _get_profession(self):
        return "Gold Digger"
    
    def _work(self):
        return f"{self._get_profession()} digs for resources."
    