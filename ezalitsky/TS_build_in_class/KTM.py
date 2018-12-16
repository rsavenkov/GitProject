from moto import Moto


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

moto_ktm = []

moto1 = KTM("black", 54, 5000, 130)
print('Moto - 1: ' + moto1.fullInfo())
moto_ktm.append(moto1)

moto2 = KTM("orange", 84, 6500, 150)
print('Moto - 2: ' + moto2.fullInfo())
moto_ktm.append(moto2)


