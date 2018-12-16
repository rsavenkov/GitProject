from truck import Truck


class NotMachineLikeTruckAcceptableInGarage(Exception):

    text = '''
           !!!!!!!!!!!!!!!!!!!!!!
           !!!!!! Only trucks are acceptable to be parked in this garage   {} !!!!!!!!!!!!
           !!!!!!!!!!!!!!!!!!!!!!
    '''

    def __init__(self, message):
        self.message = NotMachineLikeTruckAcceptableInGarage.text.format(message)

class NotVolvoFMXInBox(NotMachineLikeTruckAcceptableInGarage):

    text = '''!!!!!!!!!!!!!!!!!!!!!!!
           !!!!!!!!!!!!   One or more trucks you have parked are not VolvoFMX model !!!!!!!!!!!!!
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!
           '''

    def __init__(self, message):
        self.message = NotVolvoFMXInBox.text.format(message)

class NotVolvoFEInBox(NotMachineLikeTruckAcceptableInGarage):

    text = '''!!!!!!!!!!!!!!!!!!!!!!!
           !!!!!!!!!!!!   One or more trucks you have parked are not VolvoFE model !!!!!!!!!!!!!
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!
           '''

    def __init__(self, message):
        self.message = NotVolvoFEInBox.text.format(message)

class Garage:

    def __init__(self, number, volume, list1, list2):
        self.number = number
        self.volume = volume
        self.cars_list = list1
        self.trucks_list = list2

    def setTrucks(self, trucks):
        for truck in trucks:
            if (isinstance(truck, Truck)):#Если у нас грузовик, то мы добавляем его в список
                self.trucks_list.append(truck)
            else:
                raise NotMachineLikeTruckAcceptableInGarage(truck.type)

class Garage_Box(Garage):

    def __init__(self, number, list1):
        self.number = number
        self.trucks_list = list1

    def setVolvoFMXBox(self, trucks):
        for truck in trucks:
            if(isinstance(truck, FMX)):
                self.trucks_list.append(truck.model)
            else:
                raise NotVolvoFMXInBox

    def setVolvoFEBox(self, trucks):
        for truck in trucks:
            if(isinstance(truck, FE)):
                self.trucks_list.append(truck)
            else:
                raise NotVolvoFEInBox(truck.model)



