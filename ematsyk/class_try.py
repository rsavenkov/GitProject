class Figure:
    def __init__(self,color):
        self.color = color

    def get_color(self):
        return self.color

class Rectangle(Figure):
    def __init__(self, color, width = 100, heigth = 100):
        super().__init__(color)
        self.width = width
        self.heigth = heigth

    def square(self):
        return self.width * self.heigth
rect1 = Rectangle('blue')
print(rect1.get_color())
print(rect1.square())

print('----------')

rect2 = Rectangle('green', 20, 20)
print(rect2.get_color())
print(rect2.square())
