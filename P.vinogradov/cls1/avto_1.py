from avto import *


class ATVs(Car):
    count = 0

    def __init__(self, b, c, w, cl, p):
        super().__init__(b, c, w, cl)
        self.__price = p
        ATVs.count += 1
        Car.count -= 1

    def get_price(self):
        return self.__price

    def set_price(self, value):
        self.__price = value
    track = property(get_price, set_price)

    def show_info(self):
        super().show_info()
        print(f"'transport cost :{self.__price}")


car1 = Car('suzuki', 'green', 1111, 'car')
car2 = Car('BMV', 'white', 222222, 'car')
car3 = Car('Mersedes', 'blue', 33333, 'car')
car4 = Car('Lada', 'black', 44444, 'car')
car = ATVs('Volvo C202 ', 'yellow', 5555, 'wagon', 55555)
ves = ATVs
c = Car

s = c.count
ss = ves.count
print(car.show_info())
print('total cars in the garage : ' + str(s))
print("total SUVs in the garage : " + str(ss))
