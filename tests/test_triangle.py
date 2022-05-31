# тест для класса  "треугольник" (унаследован от "фигура")

from src.Figure import Figure
from src.Triangle import Triangle


class Test_Triangle:
    def test_create_triangle(self):
        triangle = Triangle(a, b, c)
        assert isinstance(Triangle, Figure)
        assert isinstance(triangle, Triangle)
        assert triangle.name == "Triangle"
        assert triangle.a == a
        assert triangle.b == b
        assert triangle.c == c

    def test_perimetr_triangle(self):
        triangle == Triangle(a, b, c)
        assert triangle.perimetr == a + b + c

    def test_area_triangle(self):
        assert triangle.area == a * b * c
