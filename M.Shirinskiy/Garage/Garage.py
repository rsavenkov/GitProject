import Transport_trucks
import Inheritance

class Garage:
    type = int
    def __init__(self):
        pass

    def garageInfo(self):
        a=len(auto_garage)
        t=len(truck_garage)
        return a+t

Garage = Garage()
print('And thus there are ', Garage.garageInfo(), ' machines in the garage.')