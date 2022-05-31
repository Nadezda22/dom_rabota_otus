# тест для класса  "круг" (унаследован от "фигура")
from src.Circle import Circle
from src.Figure import Figure


class Test_Circle:
    def test_create_circle(self):
        circle = Circle(a)
        assert isinstance(Circle, Figure)
        assert isinstance(circle, Circle)
        assert circle.radius == a
        assert circle.name == "Circle"

    def test_perimetr_circle(self):
        circle = Circle(a)
        assert circle.perimetr == a * 2
