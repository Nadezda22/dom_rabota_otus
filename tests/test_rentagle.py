#тест для класса  "прямоугольник" (унаследован от "фигура")
from class Figure import class Figure


from class Rectangle import class Rectangle


class Test_Rectangle:
    def test_create_rectangle(self):
        rectangle == Rectangle(10, 12)
        assert isinstance(Rectangle, Figure)
        assert isinstance(rectangle, Rectangle)
        assert rectangle.name == "Rectangle"
        assert rectangle.a == 10
        assert rectangle.b == 12

    def test_perimetr_rectangle(self):
        rectangle == Rectangle(10, 12)
        assert rectangle.perimetr == 44

    def test_area_rectangle(self):
        rectangle == Rectangle(10, 12)
        assert rectangle.area == 120
