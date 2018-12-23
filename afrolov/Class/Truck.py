from afrolov.Class.vehicle import Vehicle

class Truck(Vehicle):

    type = 'truck'

    def __init__(self, brend, horse_power):
        super().__init__(Truck)
        self.brend = brend
        self.horse_power = horse_power

    def getBrand(self):
        return self.brend

    def getHorsePower(self):
        return self.horse_power

    def infoTruck(self):
        return super().isWorkable() + "Brend = {}\nhorse_power = {}\n"\
            .format(self.brend, self.horse_power)