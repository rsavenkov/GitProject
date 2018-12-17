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





