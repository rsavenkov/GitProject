from car import Car

class AudiA5(Car):

    def __init__(self, color, distance, price, owner):
        super().__init__('audi', 'A5', 'sedan')
        self.color = color
        self.distance = distance
        self.price = price
        self.owner = owner

    def fullInfo(self):
        info = super().fullInfo()
        return info + 'Color = {}\nDistance = {}\nPrice = {}\n-----------------'.format(self.color, self.distance, self.price)


auto1 = AudiA5('white', 0, 500 * 1000, None)
print('Auto-1: ' + auto1.fullInfo())
auto2 = AudiA5('black', 10 * 1000, 350 * 1000, None)
print('Auto-2: ' + auto2.fullInfo())

auto1.setBody('cabriolet')
auto1.setWorkable(False)
print('Auto-1: ' + auto1.fullInfo())
