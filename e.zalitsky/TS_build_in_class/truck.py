from ts import Ts


class Truk(Ts):
    type = "Truck"

    def __init__(self, firm, model, type_body):
        super().__init__(Truk.type, True)
        self.firm = firm
        self.model = model
        self.type_body = type_body

    def GetFirm(self):
        return self.firm

    def GetModel(self):
        return self.model

    def Body(self):
        return self.type_body

    def Inform(self):
        return super().worked() + "Brend = {}\nModel = {}\nBody = {}\n" \
            .format(self.firm, self.model, self, self.type_body)