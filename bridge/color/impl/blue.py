from ..color import Color

class Blue(Color):
    _MIN_TRANSPARENCY_BORDER = 50

    def set_transparency(self, transparency: int):
        if transparency < self._MIN_TRANSPARENCY_BORDER:
            raise Exception(f"Transparency can't be lesser than {self._MIN_TRANSPARENCY_BORDER}!")
        super().set_transparency(transparency)

    def __str__(self):
        return f"Blue. Transparency: {self.get_transparency()}; Brightness: {self.get_brigtness()}"
