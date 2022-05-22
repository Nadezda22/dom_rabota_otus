from class Figure import class Figure


from class Triangle import class Triangle


class Test_Triangle:
    def test_create_triangle(self):
        triangle = Triangle(13, 15, 14)
        assert isinstance(Triangle, Figure)
        assert isinstance(triangle, Triangle)
        assert triangle.name == "Triangle"
        assert triangle.a == 13
        assert triangle.b == 15
        assert triangle.c == 14

    def test_perimetr_triangle(self):
        triangle == Triangle(13, 15, 14)
        assert triangle.perimetr == 42

    def test_test_area_triangle(self):
        assert triangle.area == 84
