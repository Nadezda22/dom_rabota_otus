from Figure import Figure


class Square(Figure):

    def __init__(self, a, b, c, d, name="Square"):
        super().__init__(self, a, b, c, d)
        self.a = 10
        self.b = 10

    @property
    def perimetr(self) -> int:
        (self.a + self.b) * 2

    @property
    def area(self) -> int:
        return self.area_formula(self.perimetr + ((self.a + self.b) * 2))

    @staticmethod
    def area_formula(p, (a, b) *2

    )
    p = 2
    return (p * ((p - a) * (p - b)) * 2) ** 0.5
