import Inheritance
import Transport_trucks

class Garage:

    def __init__(self, number, volume, list1, list2):
        self.number = number
        self.volume = volume
        self.cars_list = list1
        self.trucks_list = list2

    def garageInfo(self):
        a=len(auto_garage)
        t=len(truck_garage)
        return a+t

Garage = Garage()
