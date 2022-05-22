from Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b, name="Rectangle"):
        super().__init__(self, a, b)
        self.a = 10
        self.b = 12

    @property
    def perimetr(self) -> int:
        return (self.a + self.b) * 2

    @property
    def area(self) -> int:
        return self.a * self.b
