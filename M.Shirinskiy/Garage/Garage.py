from truck import Truck


class NotMachineLikeTruckAcceptableInGarage:

    text = '''
           !!!!!!!!!!!!!!!!!!!!!!
           !!!!!! Only trucks are acceptable to be parked in this garage   {} !!!!!!!!!!!!
           !!!!!!!!!!!!!!!!!!!!!!
    '''

    def __init__(self, message):
        self.message = NotMachineLikeTruckAcceptableInGarage.text.format(message)

class Truck_Garage:

    def __init__(self, number, volume, list1, list2):
        self.number = number
        self.volume = volume
        self.cars_list = list1
        self.trucks_list = list2

    def setTrucks(self, trucks):
        for truck in trucks:
            if (isinstance(truck, Truck)):#Если у нас грузовик, то мы добавляем его в список
                self.trucks_list.append(truck)
            else
                raise NotMachineLikeTruckAcceptableInGarage(truck.type)

Garage = Garage()
