from afrolov.Class import trucks, cars
from afrolov.Class.garage import *
from afrolov.Class.exeption import OnlyTrucksInGarage
from afrolov.Class.vehicle import Vehicle

park_trucks = []

truck1 = trucks.Zil('greenn')
print('Truck - 1: ' + truck1.fullTruckInfo())
park_trucks.append(truck1)

park_cars = []

car1 = cars.Maseratti(300)
print('Car - 1: ' + car1.fullCarInfo())
park_cars.append(car1)