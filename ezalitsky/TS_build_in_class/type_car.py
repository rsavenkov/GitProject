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
        super().__init__("Nissan", "Patrol", "Внедорожник")
        self.color = color
        self.power = power
        self.price = price

    def fullInfo(self):
        return super().Info() + 'Color = {}\nPower (hp) = {}\nPrice ($) = {}\n' \
            .format(self.color, self.power, self.price) + "===============================\n"


