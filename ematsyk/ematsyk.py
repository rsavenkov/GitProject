class Rectangle:
    def __init__(self, color ='green', width = 100, heigth = 100):
        self.color = color
        self.width = width
        self.heigth = heigth

    color = 'green'
    width = 100
    height = 100
    def square(self):
        return self.width * self.height

rect1 = Rectangle()
print(rect1.color)
print(rect1.square())

print('----------')

rect2 = Rectangle()
rect2.width = 200
rect2.color = 'brown'
print(rect2.color)
print(rect2.square())

print('----------')

rect = Rectangle()
print(rect.color)
print(rect.square())
rect = Rectangle('yelow', 23, 34)
print(rect.color)
print(rect.square())

print('----------')