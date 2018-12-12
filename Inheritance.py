from car import Car
from truck import Truck
from garage import Garage, NotMachineLikeTruckAcceptableInGarage

class Owner:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

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

class VolvoFE(Truck):

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

class AudiA5(Car):

    def __init__(self, color, distance, price, owner):
        super().__init__('audi', 'A5', 'sedan')
        self.color = color
        self.distance = distance
        self.price = price
        self.owner = owner

    def fullInfo(self):
        info = super().fullInfo()
        return info + 'Color = {}\nDistance = {}\nPrice = {}\n-----------------'.format(self.color, self.distance, self.price)


auto1 = AudiA5('white', 0, 500 * 1000, None)
print('Auto-1: ' + auto1.fullInfo())
auto2 = AudiA5('black', 10 * 1000, 350 * 1000, None)
print('Auto-2: ' + auto2.fullInfo())

auto1.setBody('cabriolet')
auto1.setWorkable(False)
print('Auto-1: ' + auto1.fullInfo())

owner1 = Owner('Misha', 'Petrov')
truck1 = VolvoFE('white', 10000, 2000000, 'auto', owner1)

owner2 = Owner('Petya', 'Ivanov')
truck2 = VolvoFMX('black', 20000, 1000000, 'auto', owner2)

garage = Garage('10', 5, [], [])
try:
    garage.setTrucks([truck1, truck2, auto1])
except NotMachineLikeTruckAcceptableInGarage as e:
    print(e.message)



