from ts import Ts


class Buss(Ts):
    type = "Buss"

    def __init__(self, firm, model, type_work):
        super().__init__(Buss.type, True)
        self.firm = firm
        self.model = model
        self.type_work = type_work

    def GetFirm(self):
        return self.firm

    def GetModel(self):
        return self.model

    def Get_Work(self):
        return self.type_work

    def Informat(self):
        return super().worked() + "Brend = {}\nModel = {}\nWork = {}\n" \
            .format(self.firm, self.model, self, self.type_work)
