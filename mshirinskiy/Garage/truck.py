from Прочее.machine import Machine

class Truck(Machine):

    type = 'truck'

    def __init__(self, brand, model, body):
        super().__init__(Truck.type, True)
        self.brand = brand
        self.model = model
        self.body = body

    def getBrand(self):
        return self.brand

    def getModel(self):
        return self.model

    def setBody(self, body):
        self.body = body

    def fullInfo(self):
        return super().isWorkable() + 'Brand = {} \nModel = {} \nBody = {}\n'\
            .format(self.brand, self.model, self.body)