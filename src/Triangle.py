#создание класса "треугольник" (унаследован от "фигура")
from Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c, name="Triangle"):
        super().__init__(self, a, b, c)
        self.a = 13
        self.b = 15
        self.c = 14

    @property
    def perimetr(self) -> int:
        self.a + self.b + self.c

    @property
    def area(self) -> int:
        return self.area_formula(self.perimetr + self.a + self.b + self.c)

    @classmethod
    def area_formula(p, a, b, c):
        p = 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
