from afrolov.Class.vehicle import Vehicle

class Car(Vehicle):

    type = 'Car'

    def __init__(self, brend, model):
        super().__init__(Car)# почему не работает Car.type
        self.brend = brend
        self.model = model

    def getBrand(self):
        return self.brend

    def getModel(self):
        return self.model

    def infoCar(self):
        return super().isWorkable() + "Brend = {}\nModel = {}\n"\
            .format(self.brend, self.model)