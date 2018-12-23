class OnlyTrucksInGarage:

    text = '''
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        !!! Only trucks in garage {} !!!
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        '''
    def __init__(self, message):
        self.message = OnlyTrucksInGarage.text.format(message)

