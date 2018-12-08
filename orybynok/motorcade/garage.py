class Garage:
    def __ini__(self, number_of_car, type, workable):
        self.number_of_car = number_of_car
        self.type = type
        self.workable = True

        car = []
        truck = []
        bass = []
        traktor = []

        number_of_car: int = len(car) + len(truck) + len(bass) + len(traktor)

    def setWorkable(self, isWork):
        self.workable = isWork

    def isWorkable(self):
        if (self.workable):
            return 'На ходу\n'
        return 'Не на ходу\n'