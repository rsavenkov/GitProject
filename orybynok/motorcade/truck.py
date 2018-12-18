from mashina import Mashina

class Truck(Mashina):
    def __init__(self, destination, login_capfbility) -> object:
        super().__init__('type', 'brend', 'model', 'color', 'year_of_man', 'distance', 'workability')
        self.destination = destination
        self.login_capfbility = login_capfbility

    def getDestination(self):
        return self.destination

    def getLogin_capfbility(self):
        assert isinstance(self.login_capfbility, object)
        return self.login_capfbility

    def fullInfoTruck(self) -> object:
        return '\ndestination = {}\nlogin_capability = {}\n--------------------------'.format(self.destination, self.login_capfbility)

trucks = []

truck1 = Mashina('Truck', 'Kamaz', '1300','red', 2012, 80*1000, 'на ходу')
trucks.append(truck1)
truck2 = Mashina('Truck', 'Tatra', '2500', 'red', 2014, 60 * 1000, 'нa ходу')
trucks.append(truck2)

Truck1 = Truck('dump truck','5,0 ton')
print("\nTruck-1 :", truck1.fullInfo + Truck1.fullInfoTruck())
Truck2 = Truck('tractor', '15,0 ton')
print("\nTruck-2 :", truck2.fullInfo + Truck2.fullInfoTruck())

print("\nКол-во грузовых машин - ",len(trucks))
b = len(trucks)

