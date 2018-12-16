import KTM
import type_bass
import type_truck

class ts:
    def tsinfo(self):
        a = len(KTM.moto_ktm)
        print("Мотоциклов в гараже : ", a)
        b = len(type_bass.garage_bass)
        print("Автобусов в гараже : ", b)
        c = len(type_truck.garage_truks)
        print("Траков в гараже : ", c)
        return a + b + c


ts = ts()
print("Всего в гараже находится : ", ts.tsinfo(), "транспортных средств")


