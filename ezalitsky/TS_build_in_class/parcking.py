from ezalitsky.TS_build_in_class import type_moto, type_car, type_truck, type_buss
from ezalitsky.TS_build_in_class.exeption_messages import *
from ezalitsky.TS_build_in_class.garage import *
parck_moto = []

moto1 = type_moto.KTM("black", 54, 5000, 130)
print('Moto - 1: ' + moto1.fullInfo())
parck_moto.append(moto1)

moto2 = type_moto.KTM("orange", 84, 6500, 150)
print('Moto - 2: ' + moto2.fullInfo())
parck_moto.append(moto2)

moto3 = type_moto.Ducati("black", 200, 11000, 299)
print('Moto - 1: ' + moto3.fullInfo())
parck_moto.append(moto3)

moto4 = type_moto.Ducati("Red", 210, 15000, 310)
print('Moto - 2: ' + moto4.fullInfo())
parck_moto.append(moto4)

parck_car = []

car1 = type_car.Mitsubishi("Black", 178, 15000)
print('Car - 1: ' + car1.fullInfo())
parck_car.append(car1)

car2 = type_car.Mitsubishi("Silver", 210, 17500)
print('Car - 2: ' + car2.fullInfo())
parck_car.append(car2)

car3 = type_car.Nissan("Silver", 190, 16000)
print('Car - 3: ' + car3.fullInfo())
parck_car.append(car3)

car4 = type_car.Nissan("White", 200, 17000)
print('Car - 4: ' + car4.fullInfo())
parck_car.append(car4)

parck_truks = []

truck1 = type_truck.Ford(45000, 3100, "Сonstruction Сompany")
print('Truk - 1: ' + truck1.Inform())
parck_truks.append(truck1)

truck2 = type_truck.Ford(210000, 4000, "Shipping Company")
truck2.setWorkable(False)
print('Truk - 2: ' + truck2.Inform())
parck_truks.append(truck2)

truck3 = type_truck.Ford(92000, 3200, "Shipping Company")
print('Truk - 3: ' + truck3.Inform())
parck_truks.append(truck3)

truck4 = type_truck.GMC(74000, 10000, "Shipping Company")
print('Truk - 4: ' + truck4.Inform())
parck_truks.append(truck4)

truck5 = type_truck.GMC(54000, 10000, "Shipping Company")
print('Truk - 4: ' + truck5.Inform())
parck_truks.append(truck5)

parck_buss = []

buss1 = type_buss.GM(213, 180000, 'Colorado')
print('Buss - 1: ' + buss1.fullInfo())
parck_buss.append(buss1)

buss2 = type_buss.GM(843, 143600, 'Orisone')
print('Buss - 2: ' + buss2.fullInfo())
parck_buss.append(buss2)

buss3 = type_buss.Blue_Bird("Horace Mann School", 74000, 'Missuri')
print(' Buss - 3: ' + buss3.fullInfo())
parck_buss.append(buss3)

buss4 = type_buss.Blue_Bird('Likeside School', 95400, 'Cansass')
buss4.setWorkable(False)
print('Buss - 4: ' + buss4.fullInfo())
parck_buss.append(buss4)


print("$" * 55)
class ts:
    def tsinfo(self):
        a = len(parck_moto)
        print("$ Мотоциклов в гараже : ", a)
        b = len(parck_car)
        print("$ Машин в гараже : ", b)
        c = len(parck_truks)
        print("$ Траков в гараже : ", c)
        d = len(parck_buss)
        print("$ Автобусов в гараже :", d)

        return a + b + c + d


ts = ts()
print("$ Всего в гараже находится : ", ts.tsinfo(), "транспортных средств")
print("$" * 55)

garage = Garage('8', 200, [], [], [], [])
try:
    garage.setTs([car1, car2, car3, truck3, truck4])
except OnlygroundTransport:
    print(OnlygroundTransport.message)

garage_moto = Garage_Box_Moto('2', [])


try:
    Garage_Box_Moto.setKTMBox([moto1, moto2, moto3])
except OnlyMotoKTMTransport:
    print(OnlyMotoKTMTransport.message)

