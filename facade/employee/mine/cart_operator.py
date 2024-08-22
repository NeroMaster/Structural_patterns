from ..worker import Worker

class CartOperator(Worker):
    def _get_profession(self):
        return "Cart Operator"
    
    def _work(self):
        return f"{self._get_profession()} moves resource chunks out of the mine."
