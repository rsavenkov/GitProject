from ezalitsky.TS_build_in_class.car import Car


class Mitsubishi(Car):

    def __init__(self, color, power, price):
        super().__init__("Mitsubishi", "Pajero", "Внедорожник")
        self.color = color
        self.power = power
        self.price = price

    def fullInfo(self):
        return super().Info() + 'Color = {}\nPower (hp) = {}\nPrice ($) = {}\n' \
            .format(self.color, self.power, self.price) + "===============================\n"


class Nissan(Car):

    def __init__(self, color, power, price):
        super().__init__('Nissan', 'Patrol', 'Внедорожник')
        self.color = color
        self.power = power
        self.price = price

    def fullInfo(self):
        return super().Info() + 'Color = {}\nPower (hp) = {}\nPrice ($) = {}\n' \
            .format(self.color, self.power, self.price) + "===============================\n"


parck_car = []

car1 = Mitsubishi("Black", 178, 15000)
print('Car - 1: ' + car1.fullInfo())
parck_car.append(car1)

car2 = Mitsubishi("Silver", 210, 17500)
print('Car - 2: ' + car2.fullInfo())
parck_car.append(car2)


car3 = Nissan("Silver", 190, 16000)
print('Car - 3: ' + car3.fullInfo())
parck_car.append(car3)

car4 = Nissan("White", 200, 17000)
print('Car - 4: ' + car4.fullInfo())
parck_car.append(car4)
