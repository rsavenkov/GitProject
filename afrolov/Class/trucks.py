from afrolov.Class.truck import Truck

class Zil(Truck):
    def __init__(self, color):
        super().__init__('Zil', '400')
        self.color = color

    def fullTruckInfo(self):
        return super().infoTruck() + 'color = {}\n' \
        .format(self.color) + '-------------------------\n'