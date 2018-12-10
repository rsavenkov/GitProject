from ts import Ts


class Car(Ts):
    type = 'Car'

    def __init__(self, firm, model, power, speed, body):
        super().__init__(Car.type, True)
        self.firm = firm
        self.model = model
        self.power = power
        self.speed = speed
        self.body = body

    def Brend(self):
        return self.firm

    def Model(self):
        return self.model

    def Power(self):
        return self.power

    def Speed(self):
        return self.speed

    def Body(self):
        return self.body

    def Infos(self):
        return super().worked() + "Brend = {}\nModel = {}\nPower = {}\nSpeed = {}\nBody = {}\n" \
            .format(self.firm, self.model, self.power, self.speed, self.body)
