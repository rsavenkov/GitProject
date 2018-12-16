import type_moto
import type_bass
import type_truck
import type_cars


class ts:
    def tsinfo(self):
        a = len(type_moto.types_moto)
        print("Мотоциклов в гараже : ", a)
        b = len(type_bass.garage_bass)
        print("Автобусов в гараже : ", b)
        c = len(type_truck.garage_truks)
        print("Траков в гараже : ", c)
        d = len(type_cars.type_car)
        print("Машин в гараже :", d)
        return a + b + c + d


ts = ts()
print("Всего в гараже находится : ", ts.tsinfo(), "транспортных средств")


