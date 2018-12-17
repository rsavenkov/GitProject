from mycar import car1

class Truck():
    def __init__(self, destination, login_capfbility):
        self.destination = destination
        assert isinstance(login_capfbility, object)
        self.login_capfbility = login_capfbility

    def getDestination(self):
        return self.destination

    def getLogin_capfbility(self):
        return self.login_capability

    @property
    def fullInfo(self):
        return 'type = {}\nbrend = {}\nmodel = {}\nbody = {}\ncolor = {}\nyear_of_man = {}' \
               '\ndistance = {}\nworkability = {}\ndestination = {}\nlogin_capability = {}'\
            .format(self.destination, self.login_capability)


trucks = []

truck1 = 'Truck', 'Kamaz', '1300', 'truk', 'red', 2012, 80*1000, 'на ходу','dump truck','5,0 ton'
trucks.append(truck1)
truck2 = 'Truck', 'Tatra', '2500', 'tractor', 'red', 2014, 60 * 1000, 'нa ходу', 'tractor', '15,0 ton'
trucks.append(truck2)
print('\n')
m = 0
for truck in trucks:
    if 'workability' == 'на ходу':
        m= m+1
    else:
        m= m+0
    print(truck)
b: int = len(trucks)
print("Кол-во грузовых машин - ",b)
print("Из них не на ходу - ",m)

