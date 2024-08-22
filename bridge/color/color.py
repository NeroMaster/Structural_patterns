from abc import ABCMeta, abstractmethod

class Color:
    __metaclass__ = ABCMeta

    _MAX_BORDER: int = 100
    _MIN_BORDER: int = 0

    _brightness: int
    _transparency: int


    def _return_if_valid_borders(self, target: int):
        if (target > self._MAX_BORDER) or (target < self._MIN_BORDER):
            raise Exception(f"Value can't be lesser than {self._MIN_BORDER} or greater than {self._MAX_BORDER}!")
        return target

    def __init__(self, brightness: int=50, transparency: int=50) -> None:
        self._brightness = self._return_if_valid_borders(brightness)
        self._transparency = self._return_if_valid_borders(transparency)

    def get_brigtness(self):
        return self._brightness
    
    def get_transparency(self):
        return self._transparency
    
    def set_brightness(self, brightness: int):
        self._brightness = self._return_if_valid_borders(brightness)

    def set_transparency(self, transparency: int):
        self._transparency = self._return_if_valid_borders(transparency)
