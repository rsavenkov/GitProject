from r_klimenko_machine import Machine

class Truck(Machine):

    type = 'truck'

    def __init__(self, brend, country, marketinglevel):
        super().__init__(Truck.type, True)
        self.brend = brend
        self.country = country
        self.marketinglevel = marketinglevel

