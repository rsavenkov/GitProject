class MyCar:
    def __init__(self, type, brend, model, body, color, year_of_man, distance, workability):
        self.type = type
        self.brend = brend
        self.model = model
        self.body = body
        self.color = color
        self.year_of_man = year_of_man
        self.distance = distance
        self.workability = workability

    def getType(self):
        return self.type

    def getBrend(self):
        return self.brend

    def getModel(self):
        return self.model

    def getBody(self):
        return self.body

    def getColor(self):
        return self.color

    def getYear_of_man(self):
        return self.year_of_man

    def getDistance(self):
        return self.distance

    def getWorkability(self):
        return self.workability

    @property
    def fullInfo(self):
        return 'Tipe = {}\nBrend = {}\nModel = {}\nBody = {}\nColor = {}' \
               '\nYear_of_man = {}\nDistance = {}\nWorkability ={}'\
            .format(self.type, self.brend, self.model, self.body, self.color,
                    self.year_of_man, self.distance, self.workability)

cars = []

car1 = 'Car', 'Audi', 'A5', 'sedan', 'red', 2009, 120*1000, 'на ходу'
cars.append(car1)
car2 = 'Car', 'Subary', 'Forester', 'sedan', 'white', 2016, 105*1000, 'на ходу'
cars.append(car2)
car3 = 'Car', 'Mersedes', '320,S-klass', 'sedan', 'black', 2017, 35*1000, 'на ходу'
cars.append(car3)
print('\n')
l = 0
for car in cars:
    if 'workability' == 'на ходу':
        l= l+1
    else:
        l= l+0
    print(car)

print("Кол-во машин - ",len(cars))
print("Из них не на ходу - ",l)
