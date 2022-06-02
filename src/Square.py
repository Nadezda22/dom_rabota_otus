# создание класса "квадрат" (унаследован от "прямоугольника" (родительский класс "фигура))

from Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, a, b, name="Square"):
        super().__init__(self, a, b)
        self.a = a
        self.b = b

    @property
    def perimetr(self) -> int:
        (self.a + self.b) * 2

    @property
    def area(self) -> int:
        return self.area_formula(self.perimetr + ((self.a + self.b) * 2))

    @staticmethod
    def area_formula(p, (a, b) *2)
    p = 2
    return (p * ((p - a) * (p - b)) * 2) ** 0.5
