from class Figure import class Figure


from class Circle import class Circle


class Test_Circle:
    def test_create_circle(self):
        circle = Circle(16)
        assert isinstance(Circle, Figure)
        assert isinstance(circle, Circle)
        assert circle.radius == 16
        assert circle.name == "Circle"

    def test_perimetr_circle(self):
        circle = Circle(16)
        assert circle.perimetr == 32
