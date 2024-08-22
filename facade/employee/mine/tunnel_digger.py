from ..worker import Worker

class TunnelDigger(Worker):
    def _get_profession(self):
        return "Tunnel Digger"
    
    def _work(self):
        return f"{self._get_profession()} creates another tunnel."
