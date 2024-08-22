from ..shape import Shape

class Square(Shape):

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

    def __str__(self) -> str:
        return f"Square. X: {self.get_x()}; Y: {self.get_y()}"
    