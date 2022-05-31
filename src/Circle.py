# создание класса "круг" (унаследован от "фигура")
import math

from Figure import Figure


class Circle(Figure):
    def __init__(self, radius, name="Circle"):
        super().__init__(self, radius)
        self.radius = radius

    @property
    def perimetr(self) -> int:
        return self.radius * 2

    @property
    def area(self) -> int:
        return math.pi * (self.radius * 2)

    @classmethod
    def area_formula(p, (self.radius * 2))
    return perimetr(self) + figure.area(self)
