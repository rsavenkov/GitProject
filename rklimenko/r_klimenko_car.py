from r_klimenko_machine import Machine

class Car(Machine):

    type = 'car'

    def __init__(self, brend, model, body):
        super(). __init__(Car.type, True)
        self.brend = brend
        self.model = model
        self.body = body

    def getBrend(self):
        return self.brend

    def getModel(self):
        return self.model

    def setBody(self, body):
        self.body = body

    def fullInfo(self):
        return super().isWorkable() + 'Brend = {}\nModel = {}\nBody = {}\n'\
            .format(self.brend, self.model, self.body)