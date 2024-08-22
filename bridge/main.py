from color.color import Color
from color.impl.red import Red
from color.impl.blue import Blue
from shape.shape import Shape
from shape.impl.square import Square
from artist import Artist

def main():
    shape = Square(0, 2)
    color = Red()
    artist = Artist(shape, color)
    artist.present()

    artist.repaint(2, 0)
    artist.darker()
    artist.present()

if __name__ == "__main__":
    main()
