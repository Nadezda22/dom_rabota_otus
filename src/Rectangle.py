# создание класса "прямоугольник" (унаследован от "фигура")
from Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b, name="Rectangle"):
        super().__init__(self, a, b)
        self.a = a
        self.b = b

    @property
    def perimetr(self) -> int:
        return (self.a + self.b) * 2

    @property
    def area(self) -> int:
        return self.a * self.b

    @classmethod
    def area_formula(p, (a, b) *2)
    p = 2
    return (p * ((p - a) * (p - b)) * 2) ** 0.5
