from truck1 import Truck


class truks(Truck):

    def __init__(self, distance, weight, wereuse):
        super().__init__("Ford", "F-150 Fat Boy", "Pickup")
        self.distance = distance
        self.weight = weight
        self.wereuse = wereuse

    def Inform(self):
        return super().Inform() + "Distance (ml) = {}\nWeight (kg) = {}\nWhere it used = {}\n" \
            .format( self.distance, self.weight, self.wereuse) + "===============================\n"

garage_truks = []

truk1 = truks(45000, 3100, "Сonstruction Сompany")
print('Truk - 1: ' + truk1.Inform())
garage_truks.append(truk1)

truk2 = truks(210000, 4000, "Shipping Company")
truk2.setWorkable(False)
print('Truk - 2: ' + truk2.Inform())
garage_truks.append(truk2)

truk3 = truks(92000, 3200, "Shipping Company")
print('Truk - 3: ' + truk3.Inform())
garage_truks.append(truk3)

