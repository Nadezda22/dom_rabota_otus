from Figure import Figure


class Circle(Figure):
    def __init__(self, radius, name="Circle"):
        super().__init__(self, radius)
        self.radius = 16

    @property
    def perimetr(self) -> int:
        return self.radius * 2
