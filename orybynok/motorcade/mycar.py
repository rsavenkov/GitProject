from mashina import Mashina

class MyCar(Mashina):

    def __init__(self, body, clirence):
        super().__init__('type', 'brend', 'model', 'color', 'year_of_man', 'distance', 'workability')
        self.clirence = clirence
        self.body = body

    def getBody(self):
        return self.body

    def getClirence(self):
        return self.clirence

    def fullInfoCar(self):
        return "\nbody = {}\nclirence = {}\n------------------".format(self.body, self.clirence)

cars = []

car1= Mashina("Car", 'Audi', 'A5', 'red', 2009, 120 * 1000, ' на ходу')
cars.append(car1)
car2 = Mashina('Car', 'Subary', 'Forester', 'white', 2016, 105 * 1000, ' на ходу')
cars.append(car2)
car3 = Mashina('Car', 'Mersedes', "black", '320,S-klass', 2017, 35 * 1000, ' не на ходу')
cars.append(car3)

MyCar1 = MyCar('sedan', '150 mm')
print("\nCar-1 :", car1.fullInfo + MyCar1.fullInfoCar())
MyCar2 = MyCar('sedan', '200 mm')
print("Car-2 :", car2.fullInfo + MyCar1.fullInfoCar())
MyCar3 = MyCar('sedan', '150 mm')
print("Car-3 :", car3.fullInfo + MyCar1.fullInfoCar())

print("Кол-во легковых машин - ",len(cars))




