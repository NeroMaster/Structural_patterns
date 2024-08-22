from abc import ABCMeta

class Shape:
    __metaclass__ = ABCMeta

    _x: int
    _y: int

    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def move(self, x: int, y: int):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
