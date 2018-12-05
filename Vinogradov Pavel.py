class Person:
    legs = 'количество ног ' + str(2)

    def __init__(self, name, weigth, growth):
        self.name = name
        self.weigth = weigth
        self.growth = growth

    def dif(self, name, weigth, growth):
        print('имя ' + name, 'вес ' + weigth, 'рост ' + growth)


ee = Person('Igorb', '75', '190')

print(ee.name)
print(ee.weigth)
print(ee.legs)
print(ee.growth)
ee.dif('Dimon', '50', '160')
print(ee.legs)
