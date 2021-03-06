

class VolvoFMX():

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

class VolvoFE(VolvoFMX):

    def __init__(self, color, distance, price, transmission, owner):
        super().__init__('Volvo', 'FE', 'cargo trunk truck')
        self.color = color
        self.distance = distance
        self.price = price
        self.transmission = transmission
        self.owner = owner

    def fullInfo(self):
        info = super().fullInfo()
        return info + 'Color = {}\nDistance = {}\nPrice = {}\nTransmission = {}\nOwner = {}\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'\
            .format(self.color, self.distance, self.price, self.transmission, self.owner)

truck_garage = []

truck1 = VolvoFMX('lime', 0, 500000*79, '12-gear mechanical transmission', None)
print('Truck-1: ' + truck1.fullInfo())
truck_garage.append(truck1)

truck2 = VolvoFMX('red', 0, 450000*79, '10-gear mechanical transmission', None)
print('Truck-2: ' + truck2.fullInfo())
truck_garage.append(truck2)

truck3 = VolvoFE('blue', 500000, 100000*79, '9-gear mechanical transmission', 'IE "Frolov"')
print('Truck-3: ' + truck3.fullInfo())
truck_garage.append(truck3)

truck4 = VolvoFE('gray', 700000, 50000*79, '9-gear mechanical transmission', 'IE "Soloviev"')
truck4.setWorkable(False)
print('Truck-4: ' + truck4.fullInfo())
truck_garage.append(truck4)

print('And thus there are', len(truck_garage), 'trucks in the garage.')
