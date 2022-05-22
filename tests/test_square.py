from class Figure import class Figure


from class Square import class Square


class Test_Square class Test_Rectangle:
    def test_create_square(self):
        square == Square(10, 10)
        assert isinstance(Square, Figure)
        assert isinstance(square, Square)
        assert square.name == "Square"
        assert square.a == 10
        assert square.b == 10

    def test_perimetr_square(self):
        square == Square(10, 10)
        assert square.perimetr == 40

    def test_area_square(self):
        square == Square(10, 10)
        assert square.area == 1000
