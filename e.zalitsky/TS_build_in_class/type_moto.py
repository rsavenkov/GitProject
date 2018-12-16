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


class Ducati(Moto):

    def __init__(self, color, power, price, speed):
        super().__init__('Ducati', 'Pinegale', 'Super sport')
        self.color = color
        self.power = power
        self.price = price
        self.speed = speed

    def fullInfo(self):
         return super().Info() + 'Color = {}\nPower (hp) = {}\nPrice ($) = {}\nTop speed (km/h) = {}\n' \
             .format(self.color, self.power, self.price, self.speed) + "" \
                                                                   "===============================\n"


types_moto = []

moto1 = KTM("black", 54, 5000, 130)
print('Moto - 1: ' + moto1.fullInfo())
types_moto.append(moto1)

moto2 = KTM("orange", 84, 6500, 150)
print('Moto - 2: ' + moto2.fullInfo())
types_moto.append(moto2)

moto3 = Ducati("Red", 230, 12000, 310)
print("Moto - 3: " + moto3.fullInfo())
types_moto.append(moto3)

moto4 = Ducati("Black", 230, 11000, 300)
moto4.setWorkable(False)
# moto4.setStyle("Sport")
print("Moto - 4: " + moto4.fullInfo())
types_moto.append(moto3)

