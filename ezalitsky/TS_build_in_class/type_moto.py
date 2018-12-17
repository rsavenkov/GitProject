from ezalitsky.TS_build_in_class.moto import Moto


class KTM(Moto):

    def __init__(self, color, power, price, speed):
        super().__init__('KTM', 'XTR-F', 'Hard Enduro')
        self.color = color
        self.power = power
        self.price = price
        self.speed = speed

    def fullInfo(self):
        return super().Info() + 'Color = {}\nPower (hp) = {}\nPrice ($) = {}\nTop speed (km/h) = {}\n' \
            .format(self.color, self.power, self.price, self.speed) + "" \
                                                                      "===============================\n"


class Ducati(Moto):

    def __init__(self, color, power, price, speed):
        super().__init__('Ducati', 'Pinegale', 'Super Sport')
        self.color = color
        self.power = power
        self.price = price
        self.speed = speed

    def fullInfo(self):
        return super().Info() + 'Color = {}\nPower (hp) = {}\nPrice ($) = {}\nTop speed (km/h) = {}\n' \
            .format(self.color, self.power, self.price, self.speed) + "" \
                                                                      "===============================\n"


