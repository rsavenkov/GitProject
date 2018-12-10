from ts import Ts


class Moto(Ts):
    type = "Moto"

    def __init__(self, firm, model, style):
        super().__init__(Moto.type, True)
        self.firm = firm
        self.model = model
        self.style = style

    def GetFirm(self):
        return self.firm

    def GetModel(self):
        return self.model

    def Style(self):
        return self.style

    def Info(self):
        return super().worked() + "\nBrend = {}\nModel = {}\nStyle = {}\n" \
            .format(self.firm, self.model, self.style)
