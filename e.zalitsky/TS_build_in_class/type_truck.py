from truck1 import Truck
from garage_boxes import *

class Ford(Truck):

    def __init__(self, distance, weight, wereuse):
        super().__init__("Ford", "F-150 Fat Boy", "Pickup")
        self.distance = distance
        self.weight = weight
        self.wereuse = wereuse

    def Inform(self):
        return super().Inform() + "Distance (ml) = {}\nWeight (kg) = {}\nWhere it used = {}\n" \
            .format( self.distance, self.weight, self.wereuse) + "===============================\n"

class GMC(Truck):

    def __init__(self, distance, weight, wereuse):
        super().__init__("GMC", "4005", "Wagon")
        self.distance = distance
        self.weight = weight
        self.wereuse = wereuse

    def Inform(self):
        return super().Inform() + "Distance (ml) = {}\nWeight (kg) = {}\nWhere it used = {}\n" \
            .format( self.distance, self.weight, self.wereuse) + "===============================\n"

garage_truks = []

truk1 = Ford(45000, 3100, "Сonstruction Сompany")
print('Truk - 1: ' + truk1.Inform())
garage_truks.append(truk1)

truk2 = Ford(210000, 4000, "Shipping Company")
truk2.setWorkable(False)
print('Truk - 2: ' + truk2.Inform())
garage_truks.append(truk2)

truk3 = Ford(92000, 3200, "Shipping Company")
print('Truk - 3: ' + truk3.Inform())
garage_truks.append(truk3)

truk4 = GMC(75000, 10000, "Shipping Company")
print('Truk - 3: ' + truk4.Inform())
garage_truks.append(truk4)

garage = Garage("3", 10, [], [], [], [])
try:
    garage.setTruck([truk1, truk2, truk3, truk4])
except OnlyTruckAcceptable:
    print(OnlyTruckAcceptable.message)

garage_box_ford = Garage_boxes_Truck("3", [])
try:
    garage_box_ford.setFord([truk1, truk2, truk3, truk4])
except OnlyFordAcceptable:
    print(OnlyFordAcceptable.message)
