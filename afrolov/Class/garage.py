from afrolov.Class.truck import Truck
from afrolov.Class.exeption import OnlyTrucksInGarage

class Garage:

    def __init__(self, number, volume, car_list, truck_list):
        self.number = number
        self.volume = volume
        self.car_list = car_list
        self.truck_list = truck_list

    def setTrucks(self, trucks):
        for truck in trucks:
            if (isinstance(truck, Truck)):
                self.truck_list.append(truck)
            else:
                raise OnlyTrucksInGarage(truck.type)


