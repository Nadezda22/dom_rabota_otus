# тест для класса  "прямоугольник" (унаследован от "фигура")

from src.Figure import Figure
from src.Rectangle import Rectangle


class Test_Rectangle:
    def test_create_rectangle(self):
        rectangle == Rectangle(a, b)
        assert isinstance(Rectangle, Figure)
        assert isinstance(rectangle, Rectangle)
        assert rectangle.name == "Rectangle"
        assert rectangle.a == a
        assert rectangle.b == b

    def test_perimetr_rectangle(self):
        rectangle == Rectangle(a, b)
        assert rectangle.perimetr == (a + b) * 2

    def test_area_rectangle(self):
        rectangle == Rectangle(a, b)
        assert rectangle.area == a * b
