from Прочее.machine import Machine


class Buss(Machine):
    type = "Buss"

    def __init__(self, firm, model, type_work):
        super().__init__(Buss.type, True)
        self.firm = firm
        self.model = model
        self.type_work = type_work

    def Informat(self):
        return super().isWorkable() + "===============================\n" + "Brend = {}\nModel = {}\nWork = {}\n" \
            .format(self.firm, self.model, self.type_work)
