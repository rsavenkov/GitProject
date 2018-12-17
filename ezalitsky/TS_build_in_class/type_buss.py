from ezalitsky.TS_build_in_class.buss import Buss


class GM(Buss):

    def __init__(self, number, distance, state):
        super().__init__('GM', 'TDH', 'Street')
        self.number = number
        self.distance = distance
        self.state = state

    def fullInfo(self):
        return super().Informat() + 'Route № = {}\nDistance (ml) = {}\nState = {}\n' \
            .format(self.number, self.distance, self.state) + "===============================\n"


class Blue_Bird(Buss):

    def __init__(self, school, distance, state):
        super().__init__('Blue Bird', 'Vision', 'School Buss')
        self.school = school
        self.distance = distance
        self.state = state

    def fullInfo(self):
        return super().Informat() + 'School name = {}\nDistance (ml) = {}\nState = {}\n' \
            .format(self.school, self.distance, self.state) + "===============================\n"


parck_buss = []

buss1 = GM(213, 180000, 'Colorado')
print('Buss - 1: ' + buss1.fullInfo())
parck_buss.append(buss1)

buss2 = GM(843, 143600, 'Orisone')
print('Buss - 2: ' + buss2.fullInfo())
parck_buss.append(buss2)

buss3 = Blue_Bird("Horace Mann School", 74000, 'Missuri')
print(' Buss - 3: ' + buss3.fullInfo())
parck_buss.append(buss3)

buss4 = Blue_Bird('Likeside School', 95400, 'Cansass')
buss4.setWorkable(False)
print('Buss - 4: ' + buss4.fullInfo())
parck_buss.append(buss4)


