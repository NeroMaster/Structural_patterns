from color.color import Color
from shape.shape import Shape

class Artist:
    _STEP = 5
    _shape: Shape
    _color: Color

    def __init__(self, shape: Shape, color: Color) -> None:
        self._shape = shape
        self._color = color

    def repaint(self, x: int, y: int):
        self._shape.move(x, y)

    def lighter(self):
        self._color.set_brightness(self._color.get_brigtness() + self._STEP)
        self._color.set_transparency(self._color.get_transparency() + self._STEP)

    def darker(self):
        self._color.set_brightness(self._color.get_brigtness() - self._STEP)
        self._color.set_transparency(self._color.get_transparency() - self._STEP)

    def present(self):
        print("My current painting:\n")
        print(self._shape)
        print(self._color)

