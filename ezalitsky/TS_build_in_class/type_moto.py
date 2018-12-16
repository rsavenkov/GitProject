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


parck_moto = []

moto1 = KTM("black", 54, 5000, 130)
print('Moto - 1: ' + moto1.fullInfo())
parck_moto.append(moto1)

moto2 = KTM("orange", 84, 6500, 150)
print('Moto - 2: ' + moto2.fullInfo())
parck_moto.append(moto2)


moto3 = Ducati("black", 200, 11000, 299)
print('Moto - 1: ' + moto3.fullInfo())
parck_moto.append(moto3)

moto4 = Ducati("Red", 210, 15000, 310)
print('Moto - 2: ' + moto4.fullInfo())
parck_moto.append(moto4)

