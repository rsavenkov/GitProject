from mashina import Mashina

class Bass(Mashina):

    def __init__(self, passenger_capacity):
        super().__init__('type', 'brend', 'model', 'color', 'year_of_man', 'distance', 'workability')
        self.passenger_capacity = passenger_capacity

    def getPassenger_capacity(self):
        return self.passenger_capacity

    def fullInfoBass(self):
        return '\nPassenger_capacity = {}'.format(self.passenger_capacity)

basses = []

bass1 = Mashina('Bass', 'Liaz', '1500', 'yellow', 2012, 80 * 1000, 'на ходу')
basses.append(bass1)
bass2 = Mashina('MiniBass', 'Ford', '1900', 'white', 2016, 40 * 1000, 'не на ходу')
basses.append(bass2)
Bass1 = Bass('47 passenger')
print("\nBass-1 :", bass1.fullInfo + Bass1.fullInfoBass())
Bass2 = Bass('20 passenger')
print("\nBass-2 :", bass1.fullInfo + Bass2.fullInfoBass())

print("\nКол-во машин - ",len(basses))
c = len(basses)

