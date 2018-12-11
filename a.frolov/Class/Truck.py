from Vehicle import vehicle

class Truck(vehicle):

    type = 'Truck' #зачем указывать тип здест если мы указываем тип в 8 строке?

    def __init__(self, brend, horse_power):
        super().__init__(Truck, True)
        self.brend = brend
        self.horse_power = horse_power

auto_park = []
zil = Truck('zil', 400)
auto_park.append(zil)
vaz = Truck('vaz', 500)
auto_park.append(vaz)

print(auto_park)

