from machine import Machine


class Moto(Machine):
    type = "Moto"

    def __init__(self, firm, model, style):
        super().__init__(Moto.type, True)
        self.firm = firm
        self.model = model
        self.style = style

    def Info(self):
        return super().isWorkable() + "===============================\nBrend = {}\nModel = {}\nStyle = {}\n" \
            .format(self.firm, self.model, self.style)
