from moto import Moto


class KTM(Moto):

    def __init__(self, color, power, price, speed):
        super().__init__('KTM', 'XTR-F', 'Hard Enduro')
        self.color = color
        self.power = power
        self.price = price
        self.speed = speed

    def fullInfo(self):
        return super().Info() + 'Color = {}\nPower = {}\nPrice = {}\nTop speed = {}\n' \
            .format(self.color, self.power, self.price, self.speed)


moto1 = KTM("black", "54 hp", 520000, 130)
print('KTM - 1: ' + moto1.fullInfo())

moto2 = KTM("orange", "84 hp", 640000, 150)
print('KTM - 2: ' + moto2.fullInfo())
