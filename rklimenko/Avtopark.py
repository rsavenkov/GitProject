from r_klimenko_car import Car
from r_klimenko_truck import Truck

class Avtopark(Car, Truck):

    def __init__(self, type):
        self.type = type

    def Car(self):
        self.type = 'truck'
        Cat = Truck('Cat', 'China', '3/10')

    def Truck(self):
        self.type = 'car'
        Bmw = Car('BMW', '5x', 'big')

cars_park = []
trucks_park = []
if type == 'car':
    cars_park.append(Car)
if type == 'truck':
    trucks_park.append(Truck)
print(cars_park, ',', trucks_park)





