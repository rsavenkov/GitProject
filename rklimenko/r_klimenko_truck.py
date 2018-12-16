from r_klimenko_machine import Machine

class Track(Machine):

    type = 'truck'

    def __init__(self, brend, country, marketinglevel):
        super().__init__(Track.type, True)
        self.brend = brend
        self.country = country
        self.marketing = marketinglevel

