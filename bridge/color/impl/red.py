from ..color import Color

class Red(Color):
    _MAX_BRIGHTNESS_BORDER = 50

    def set_brightness(self, brightness: int):
        if brightness > self._MAX_BRIGHTNESS_BORDER:
            raise Exception(f"Red Color brightness can't be greater than {self._MAX_BRIGHTNESS_BORDER}!")
        super().set_brightness(brightness)

    def __str__(self):
        return f"Red. Transparency: {self.get_transparency()}; Brightness: {self.get_brigtness()}"
