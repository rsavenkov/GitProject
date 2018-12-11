from machine import Machine

class Truck(Machine):

    type = 'truck'

    def __init__(self, brend, model, body):
        super().__init__(Truck.type, True)
        self.brend = brend
        self.model = model
        self.body = body

    def Inform(self):
        return super().isWorkable() + "===============================\n" + "Brend = {}\nModel = {}\nBody = {}\n"\
            .format(self.brend, self.model, self.body)
