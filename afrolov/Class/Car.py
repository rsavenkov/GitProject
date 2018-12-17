From Vehicle import vehicle

class car(vehicle):

    type = 'car'

    def __init__(self, brend, model):
        super().__init__(car.type, True)
        self.brend = brend
        self.model = model

    def getBrand(self):
        return self.brend

    def getModel(self):
        return self.model

    def fullInfo(self):
        return super().isWorkable() + "Brend = {}\nModel = {}\n"\
            .fornat(self.brend, self.model)