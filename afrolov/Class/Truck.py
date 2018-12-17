from Vehicle import vehicle

class Truck(vehicle):

    type = 'truck'

    def __init__(self, brend, horse_power):
        super().__init__(Truck.type, True)
        self.brend = brend
        self.horse_power = horse_power

