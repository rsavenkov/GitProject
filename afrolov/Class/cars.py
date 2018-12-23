from afrolov.Class.car import Car

class Maseratti(Car):

    def __init__(self, speed):
        super().__init__('Maseratti', 'XR')
        self.speed = speed

    def fullCarInfo(self):
        return super().infoCar() + 'speed = {}\n' \
            .format(self.speed) + '---------------------------\n'