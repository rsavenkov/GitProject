class OnlygroundTransport(Exception):

    text = '''
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
           !!!!!! Only ground transport are acceptable to be parked in this garage {} !!!!!!!!!!!!!
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''

    def __init__(self, message):
        self.message = OnlygroundTransport.text.format(message)


class OnlyMotoKTMTransport(OnlygroundTransport):

    text = '''
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
           !!!!!!!!!!!! Only Moto KTM are acceptable to be parked in this BOX  {} !!!!!!!!!!!!!!!!
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
           '''

    def __init__(self, message):
        self.message = OnlyMotoKTMTransport.text.format(message)


class OnlyMotoDucatiTransport(OnlygroundTransport):

    text = '''
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
           !!!!!!!!!!!! Only Moto Ducati are acceptable to be parked in this BOX  {} !!!!!!!!!!!!!
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
           '''

    def __init__(self, message):
        self.message = OnlyMotoDucatiTransport.text.format(message)


class OnlyCarMitsubishiTransport(OnlygroundTransport):

    text = '''
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
           !!!!!!!!!!!! Only Car Mitsubishi are acceptable to be parked in this BOX  {} !!!!!!!!!!
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
           '''

    def __init__(self, message):
        self.message = OnlyCarMitsubishiTransport.text.format(message)


class OnlyCarNissanTransport(OnlygroundTransport):

    text = '''
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
           !!!!!!!!!!!! Only Car Nissan are acceptable to be parked in this BOX  {} !!!!!!!!!!!!!
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
           '''

    def __init__(self, message):
        self.message = OnlyCarNissanTransport.text.format(message)


class OnlyTruckFordTransport(OnlygroundTransport):

    text = '''
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
           !!!!!!!!!!!! Only Truck Ford are acceptable to be parked in this BOX  {} !!!!!!!!!!!!!
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
           '''

    def __init__(self, message):
        self.message = OnlyTruckFordTransport.text.format(message)


class OnlyTruckGMCTransport(OnlygroundTransport):

    text = '''
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
           !!!!!!!!!!!! Only Truck GMC are acceptable to be parked in this BOX  {} !!!!!!!!!!!!!
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
           '''

    def __init__(self, message):
        self.message = OnlyTruckGMCTransport.text.format(message)


class OnlyBussGMTransport(OnlygroundTransport):

    text = '''
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
           !!!!!!!!!!!! Only Buss GM are acceptable to be parked in this BOX  {} !!!!!!!!!!!!!
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
           '''

    def __init__(self, message):
        self.message = OnlyBussGMTransport.text.format(message)


class OnlyBussBlueBirdTransport(OnlygroundTransport):

    text = '''
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
           !!!!!!!!!!!! Only Buss Bluer Bird are acceptable to be parked in this BOX  {} !!!!!!!!!!!!!
           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
           '''

    def __init__(self, message):
        self.message = OnlyBussBlueBirdTransport.text.format(message)

