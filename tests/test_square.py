# тест для класса  "квадрат" (унаследован от "фигура")
from src.Figure import Figure

from src.Square import Square


class Test_Square class Test_Square:
    def test_create_square(self):
        square == Square(a, b)
        assert isinstance(Square, Figure)
        assert isinstance(square, Square)
        assert square.name == "Square"
        assert square.a == a
        assert square.b == b

    def test_perimetr_square(self):
        square == Square(a, b)
        assert square.perimetr == (a + b) * 2

    def test_area_square(self):
        square == Square(a, b)
        assert square.area == a * 4
