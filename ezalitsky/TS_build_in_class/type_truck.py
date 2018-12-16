from ezalitsky.TS_build_in_class.truck import Truck


class Ford(Truck):

    def __init__(self, distance, weight, wereuse):
        super().__init__("Ford", "F-150 Fat Boy", "Pickup")
        self.distance = distance
        self.weight = weight
        self.wereuse = wereuse

    def Inform(self):
        return super().Inform() + "Distance (ml) = {}\nWeight (kg) = {}\nWhere it used = {}\n" \
            .format(self.distance, self.weight, self.wereuse) + "===============================\n"

class GMC(Truck):

    def __init__(self, distance, weight, wereuse):
        super().__init__("GMC", "4005", "Wagon")
        self.distance = distance
        self.weight = weight
        self.wereuse = wereuse

    def Inform(self):
        return super().Inform() + "Distance (ml) = {}\nWeight (kg) = {}\nWhere it used = {}\n" \
            .format( self.distance, self.weight, self.wereuse) + "===============================\n"


parck_truks = []

truck1 = Ford(45000, 3100, "Сonstruction Сompany")
print('Truk - 1: ' + truck1.Inform())
parck_truks.append(truck1)

truck2 = Ford(210000, 4000, "Shipping Company")
truck2.setWorkable(False)
print('Truk - 2: ' + truck2.Inform())
parck_truks.append(truck2)

truck3 = Ford(92000, 3200, "Shipping Company")
print('Truk - 3: ' + truck3.Inform())
parck_truks.append(truck3)

truck4 = GMC(74000, 10000, "Shipping Company")
print('Truk - 4: ' + truck4.Inform())
parck_truks.append(truck4)

truck5 = GMC(54000, 10000, "Shipping Company")
print('Truk - 4: ' + truck5.Inform())
parck_truks.append(truck5)