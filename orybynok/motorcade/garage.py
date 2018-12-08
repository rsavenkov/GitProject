from typing import List, Any

from mycar import MyCar
from truck import Truck, m
from bas import Bass, x2, n

cars: List[Any] = []
l = 0
for car in cars:
    if 'workability' == 'на ходу':
        l= l+1
    else:
        l= l+0
    print(car)
trucks = []
l = 0
for truck in trucks:
    if 'workability' == 'на ходу':
        l= l+1
    else:
        l= l+0
    print(truck)
basses = []
l = 0
for bass in basses:
    if 'workability' == 'на ходу':
        l = 1 + 1
    else:
        l = 1 + 0
    print(bass)

z = l + m + n
print("\nНе находу в автопарке - ",z)