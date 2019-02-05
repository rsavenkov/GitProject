from Прочее.machine import Machine


class Car(Machine):
    type = "Car"

    def __init__(self, firm, model, klass):
        super().__init__(Car.type, True)
        self.firm = firm
        self.model = model
        self.klass = klass



    def Info(self):
        return super().isWorkable() + "===============================\nBrend = {}\nModel = {}\nKlass = {}\n" \
            .format(self.firm, self.model, self.klass)
