from truck1 import Truck
from type_truck import Ford, GMC
from car import Carall
from type_cars import datsun, hundai
from moto import Moto
from type_moto import KTM, Ducati
from bass import Buss
from type_bass import Street, School


class OnlyMotoAcceptable(Exception):
    text = """
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!! Only moto acceptable {}  !!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            """

    def __init__(self, message):
        self.message = OnlyMotoAcceptable.text.format(message)


class OnlyCarAcceptable(Exception):
    text = """
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!! Only Car acceptable {}  !!!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            """

    def __init__(self, message):
        self.message = OnlyCarAcceptable.text.format(message)


class OnlyTruckAcceptable(Exception):
    text = """
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!! Only Truck acceptable {}  !!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            """

    def __init__(self, message):
        self.message = OnlyTruckAcceptable.text.format(message)


class OnlyBussAcceptable(Exception):
    text = """
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!! Only Buss acceptable {}  !!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            """

    def __init__(self, message):
        self.message = OnlyBussAcceptable.text.format(message)


class OnlyKTMAcceptable(Exception):
    text = """
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!! Only KTM acceptable {}  !!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            """

    def __init__(self, message):
        self.message = OnlyKTMAcceptable.text.format(message)


class OnlyDucatiAcceptable(Exception):
    text = """
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!! Only Ducati acceptable {}  !!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            """

    def __init__(self, message):
        self.message = OnlyDucatiAcceptable.text.format(message)


class OnlydatsunAcceptable(Exception):
    text = """
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!! Only Datsun acceptable {}  !!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            """

    def __init__(self, message):
        self.message = OnlydatsunAcceptable.text.format(message)


class OnlyhundaiAcceptable(Exception):
    text = """
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!! Only Hundai acceptable {}  !!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            """

    def __init__(self, message):
        self.message = OnlyhundaiAcceptable.text.format(message)


class OnlyFordAcceptable(Exception):
    text = """
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!! Only Ford Truck acceptable {}  !!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            """

    def __init__(self, message):
        self.message = OnlyFordAcceptable.text.format(message)


class OnlyGMCAcceptable(Exception):
    text = """
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!! Only GMC acceptable {}  !!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            """

    def __init__(self, message):
        self.message = OnlyGMCAcceptable.text.format(message)


class OnlyStreetBussAcceptable(Exception):
    text = """
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!! Only Street Buss acceptable {}  !!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            """

    def __init__(self, message):
        self.message = OnlyStreetBussAcceptable.text.format(message)


class OnlySchoolBussAcceptable(Exception):
    text = """
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!! Only School Buss acceptable {}  !!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            """

    def __init__(self, message):
        self.message = OnlySchoolBussAcceptable.text.format(message)


class Garage:

    def __init__(self, number, list_moto, list_car, list_truck, list_buss):
        self.number = number
        self.list_moto = list_moto
        self.list_car = list_car
        self.list_truck = list_truck
        self.list_buss = list_buss

    def setMoto(self, motos):
        for moto in motos:
            if isinstance(moto, Moto):
                self.list_moto.append(moto)
            else:
                raise OnlyMotoAcceptable(moto.type)

    def setCars(self, cars):
        for car in cars:
            if isinstance(car, Carall):
                self.list_car.append(car)
            else:
                raise OnlyCarAcceptable(car.type)

    def setTruck(self, trucks):
        for truck in trucks:
            if isinstance(truck, Truck):
                self.list_truck.append(truck)
            else:
                raise OnlyTruckAcceptable(truck.type)

    def setBass(self, busses):
        for buss in busses:
            if isinstance(buss, Buss):
                self.list_buss.append(buss)
            else:
                raise OnlyBussAcceptable(buss.type)


class Garage_boxes_Moto(Garage):

    def __init__(self, number, list_moto):
        self.number = number
        self.list_moto = list_moto

    def setKTM(self, moto):
        for mot in moto:
            if isinstance(mot, KTM):
                self.list_moto.append(moto)
            else:
                raise OnlyKTMAcceptable(mot.type)

    def setDucati(self, moto):
        for mot in moto:
            if isinstance(mot, Ducati):
                self.list_moto.append(moto)
            else:
                raise OnlyDucatiAcceptable(mot.type)


class Garage_boxes_Car(Garage):

    def __init__(self, number, list_car):
        self.number = number
        self.list_car = list_car

    def setDatsun(self, cars):
        for car in cars:
            if isinstance(car, datsun):
                self.list_car.append(car)
            else:
                raise OnlydatsunAcceptable(car.type)

    def setHundai(self, cars):
        for car in cars:
            if isinstance(car, hundai):
                self.list_car.append(car)
            else:
                raise OnlyhundaiAcceptable(car.type)


class Garage_boxes_Truck(Garage):

    def __init__(self, number, list_truck):
        self.number = number
        self.list_truck = list_truck

    def setFord(self, trucks):
        for truck in trucks:
            if isinstance(truck, Ford):
                self.list_truck.append(truck)
            else:
                raise OnlyGMCAcceptable(truck.type)

    def setHundai(self, trucks):
        for truck in trucks:
            if isinstance(truck, GMC):
                self.list_truck.append(truck)
            else:
                raise OnlyGMCAcceptable(truck.type)


class Garage_boxes_Buss(Garage):

    def __init__(self, number, list_buss):
        self.number = number
        self.list_buss = list_buss

    def setFord(self, busses):
        for buss in busses:
            if isinstance(buss, Street):
                self.list_buss.append(buss)
            else:
                raise OnlyStreetBussAcceptable(buss.type)

    def setHundai(self, busses):
        for buss in busses:
            if isinstance(buss, School):
                self.list_buss.append(buss)
            else:
                raise OnlySchoolBussAcceptable(buss.type)
