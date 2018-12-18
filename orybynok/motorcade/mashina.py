import self as self

class Mashina:

    def __init__(self, type: object, brend: object, model: object, color: object, year_of_man: object,
                 distance: object, workability: object) -> object:
        """

        :rtype: object
        """
        self.type = type
        self.brend = brend
        self.model = model
        self.color = color
        self.year_of_man = year_of_man
        self.distance = distance
        assert isinstance(workability, object)
        self.workability = workability

    def getType(self):
        return self.type

    def getBrend(self):
        return self.brend

    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    def getYear_of_man(self):
        return self.year_of_man

    def getDistance(self):
        assert isinstance(self.distance, object)
        return self.distance

    def getWorkability(self):
        return self.workability

    @property
    def fullInfo(self) -> object:
        return 'Tipe = {}\nBrend = {}\nModel = {}\nColor = {}' \
               '\nYear_of_man = {}\nDistance = {}\nWorkability ={}' \
            .format(self.type, self.brend, self.model, self.color,
                    self.year_of_man, self.distance, self.workability)
