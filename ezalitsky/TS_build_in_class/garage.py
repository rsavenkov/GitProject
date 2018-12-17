from ezalitsky.TS_build_in_class.moto import *
from ezalitsky.TS_build_in_class.car import *
from ezalitsky.TS_build_in_class.truck import *
from ezalitsky.TS_build_in_class.buss import *
from ezalitsky.TS_build_in_class.exeption_messages import *
from ezalitsky.TS_build_in_class.type_moto import *



class Garage:

    def __init__(self, number, volume, list_moto, list_car, list_truck, list_buss ):
        self.number = number
        self.volume = volume
        self.list_moto = list_moto
        self.list_car = list_car
        self.list_truck = list_truck
        self.list_buss = list_buss

    def setTs(self, transport):
        for ts in transport:
            if isinstance(ts, Moto):
                self.list_moto.append(ts)
            elif isinstance(ts, Car):
                self.list_car.append(ts)
            elif isinstance(ts, Truck):
                self.list_truck.append(ts)
            elif isinstance(ts, Buss):
                self.list_buss.append(ts)
            else:
                raise OnlygroundTransport(ts.type)


class Garage_Box_Moto(Garage):

    def __init__(self, number, list_moto):
        self.number = number
        self.list_moto = list_moto

    def setKTMBox(self, moto):
        for mot in moto:
            if isinstance(Moto.firm, "KTM"):
                self.list_moto.append(mot)
            else:
                raise OnlyMotoKTMTransport(mot.model)

    def setDucatiBox(self, moto):
        for mot in moto:
            if isinstance(Moto.firm, "Ducati"):
                self.list_moto.append(mot)
            else:
                raise OnlyMotoDucatiTransport(mot.model)


class Garage_Box_Car(Garage):

    def __init__(self, number, list_car):
        self.number = number
        self.list_car = list_car

    def setMitsubishiBox(self, cars):
        for car in cars:
            if isinstance(Car.firm, "Mitsubishi"):
                self.list_car.append(car)
            else:
                raise OnlyCarMitsubishiTransport(car.model)

    def setNissanBox(self, cars):
        for car in cars:
            if isinstance(Car.firm, "Nissan"):
                self.list_moto.append(car)
            else:
                raise OnlyCarNissanTransport(car.model)


class Garage_Box_Truck(Garage):

    def __init__(self, number, list_truck):
        self.number = number
        self.list_truck = list_truck

    def setFordBox(self, trucks):
        for truck in trucks:
            if isinstance(Truck.brend, "Ford"):
                self.list_car.append(truck)
            else:
                raise OnlyTruckFordTransport(truck.model)

    def setGMCBox(self, trucks):
        for truck in trucks:
            if isinstance(Truck.brend, "GMC"):
                self.list_moto.append(truck)
            else:
                raise OnlyTruckGMCTransport(truck.model)


class Garage_Box_Buss(Garage):

    def __init__(self, number, list_buss):
        self.number = number
        self.list_buss = list_buss

    def setGMBox(self, busses):
        for buss in busses:
            if isinstance(Buss.firm, "GM"):
                self.list_car.append(buss)
            else:
                raise OnlyBussGMTransport(buss.model)

    def setBlueBirdBox(self, busses):
        for buss in busses:
            if isinstance(Buss.firm, "Blue Bird"):
                self.list_moto.append(buss)
            else:
                raise OnlyBussBlueBirdTransport(buss.model)
