from random import randint

class Football_club:
    def __init__(self,club,age):
        self.club = club
        self.age = age


l = []

for i in range(1,11):
    Fan = Football_club('Spartak', randint(20, 30))
    if Fan.age > 25:
        l.append(Fan.age)
print('FCSM fans with age: ',l)
