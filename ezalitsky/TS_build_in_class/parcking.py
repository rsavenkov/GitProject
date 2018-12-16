from ezalitsky.TS_build_in_class import type_moto, type_car, type_truck, type_buss


class ts:
    def tsinfo(self):
        a = len(type_moto.parck_moto)
        print("Мотоциклов в гараже : ", a)
        b = len(type_car.parck_car)
        print("Машин в гараже : ", b)
        c = len(type_truck.parck_truks)
        print("Траков в гараже : ", c)
        d = len(type_buss.parck_buss)
        print("Автобусов в гараже :", d)

        return a + b + c + d


ts = ts()
print("Всего в гараже находится : ", ts.tsinfo(), "транспортных средств")


