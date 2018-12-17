from typing import List, Any

from mycar import car1, a
from truck import Truck, m, b
from bas import Bass, n, c

cars: List[Any] = []
l = 0
for car in cars:
    if 'workability' == 'на ходу':
        l = l + 1
    else:
        l = l + 0
    print(car)
trucks = []
l = 0
for truck in trucks:
    if 'workability' == 'на ходу':
        l = l + 1
    else:
        l = l + 0
    print(truck)
basses = []
l = 0
for bass in basses:
    if 'workability' == 'на ходу':
        l = 1 + 1
    else:
        l = 1 + 0
    print(bass)
d = a + b + c
z = l + m + n
print("\nВ гараже всего - ", d," машин.")
print("Из них: \n", a," - легковых; \n", b," - грузовых; \n", c," - автобуса. ")
print("Не находу в автопарке - ", z," машин(а).")