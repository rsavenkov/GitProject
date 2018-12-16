from machine import Machine


class Car_all(Machine):
    type = "Car"

    def __init__(self, firm, model, usability_class):
        super().__init__(Car_all.type, False)
        self.firm = firm
        self.model = model
        self.usability_class = usability_class

    def fullinf(self):
        return super().isWorkable() + "===============================\n" + "Brend = {}\nModel = {}\nType = {}\n" \
            .format(self.firm, self.model, self.usability_class)
  # f"Brend = {self.firm}\n, Model = {self.model}\n,Where use = {self.usability_class}\n"


