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


