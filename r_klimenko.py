from math import cos
from random import randint

l = [1,2]
max = 0

for i in range(1,7):
    l.append(randint(1,10))
    if l[i] > l[i-1]:
        l[i+1] = max
    else:
        l[i] = max

print('WOW!', cos(max))
