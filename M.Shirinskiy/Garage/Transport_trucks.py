from truck import Truck

class VolvoFMX(Truck):

    def __init__(self, color, distance, price, transmission, owner):
        super().__init__('Volvo', 'FMX', 'cargo truck')
        self.color = color
        self.distance = distance
        self.price = price
        self.transmission = transmission
        self.owner = owner

    def fullInfo(self):
        info = super().fullInfo()
        return info + 'Color = {}\nDistance = {}\nPrice = {}\nTransmission = {}\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'\
            .format(self.color, self.distance, self.price, self.transmission)


truck1 = VolvoFMX('lime', 0, 500000*79, '12-gear mechanical transmission', None)
print('Truck-1: ' + truck1.fullInfo())

truck2 = VolvoFMX('red', 0, 450000*79, '10-gear mechanical transmission', None)
print('Truck-2: ' + truck2.fullInfo())

truck1.setBody('cargo truck')
