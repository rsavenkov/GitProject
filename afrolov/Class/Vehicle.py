class Vehicle:

    def __init__(self, type):
        self.type = type
        self.workable = True

    def setWorkable(self, isWork):
        self.workable = isWork

    def isWorkable(self):
        if (self.workable):
            return 'На ходу\n'
        return 'Не на ходу\n'
