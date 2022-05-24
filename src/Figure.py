#Создание класса "Фигура"
class Figure:
    def __init__(self, side, name=None):
        if self.__class__ == Figure:
            raise Exception("Невозможно нарисовать фигуру")
        self.side = side
        self.name = name

    @property
    def perimetr(self) -> int:
        pass

    @property
    def area(self) -> int:
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Использован неправильный класс")
        return self.area + figure.area()
