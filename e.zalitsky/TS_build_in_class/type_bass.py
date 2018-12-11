from bass import Buss


class Street(Buss):

    def __init__(self, number, distance, state):
        super().__init__('GM', 'TDH', 'Street')
        self.number = number
        self.distance = distance
        self.state = state

    def fullInfo(self):
        return super().Informat() + 'Route № = {}\nDistance (ml) = {}\nState = {}\n' \
            .format(self.number, self.distance, self.state) + "===============================\n"


class School(Buss):

    def __init__(self, school, distance, state):
        super().__init__('Blue Bird', 'Vision', 'School Buss')
        self.school = school
        self.distance = distance
        self.state = state

    def fullInfo(self):
        return super().Informat() + 'School name = {}\nDistance (ml) = {}\nState = {}\n' \
            .format(self.school, self.distance, self.state) + "===============================\n"


garage_bass = []

buss1 = Street(213, 180000, 'Colorado')
print('Buss - 1: ' + buss1.fullInfo())
garage_bass.append(buss1)

buss2 = Street(843, 143600, 'Orisone')
print('Buss - 2: ' + buss2.fullInfo())
garage_bass.append(buss2)

buss3 = School("Horace Mann School", 74000, 'Missuri')
print(' Buss - 3: ' + buss3.fullInfo())
garage_bass.append(buss3)

buss4 = School('Likeside School', 95400, 'Cansass')
buss4.setWorkable(False)
print('Buss - 4: ' + buss4.fullInfo())
garage_bass.append(buss4)
