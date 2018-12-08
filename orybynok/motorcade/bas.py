from mycar import MyCar

class Bass(MyCar):
    def __init__(self, passenger_capacity):
        assert isinstance(passenger_capacity, object)
        self.passenger_capacity = passenger_capacity

    def getPassenger_capacity(self):
        return self.passenger_capacity

    @property
    def fullInfo(self):
        return 'type = {}\nbrend = {}\nmodel = {}\nbody = {}\ncolor = {}\nyear_of_man = {}' \
               '\ndistance = {}\nworkability = {}\nPassenger_capacity = {}'.format(self.Passenger_capacity)


basses = []

bass1 = 'Bass', 'Liaz', '1500', 'bass', 'yellow', 2012, 80 * 1000, 'на ходу',  '47 passenger'
basses.append(bass1)
bass2 = 'Bass', 'Ford', '1900', 'minibass', 'white', 2016, 40 * 1000, 'не на ходу', '20 passenger'
basses.append(bass2)
print('\n')
l = 0
for bass in basses:
    if 'workability' == 'на ходу':
        l = 1 + 1
    else:
        l = 1 + 0
    print(bass)

print("Кол-во машин - ", len(basses))
print("Из них не на ходу - ", l)

