class Car:
    total_wheels = '4'
    def __init__(self, Volvo = 0, Land_cruiser = 0, LADA_Vesta = 0):
        self.__Volvo = Volvo
        self.__Land_cruiser = Land_cruiser
        self.__LADA_Vesta = LADA_Vesta
        
    @property 
    def Volvo(self):
        return self.__Volvo

    @Volvo.setter
    def Volvo(self, value):
        self.__Volvo = value
    @property 
    def Land_cruiser(self):
        return self.__Land_cruiser

    @Land_cruiser.setter
    def Land_cruiser(self, value):
        self.__Land_cruiser = value
    @property 
    def LADA_Vesta(self):
        return self.__LADA_Vesta

    @LADA_Vesta.setter
    def LADA_Vesta(self, value):
        self.__LADA_Vesta = value
       
    def __repr__(self):
        return f'''car is a sedan {self.__Volvo} easy to control on the track,
                            {self.__Land_cruiser} Universal SUV 
Russian car is full of surprisese {self.__LADA_Vesta} can not get home '''
    def volvo(self, engine, all_places):
        return  ('power=' + engine), ('seats=' + all_places)
    def cruiser(self, engine1, all_places1):
        return  ('power=' + engine1), ('seats=' + all_places1)
    def LADA(self, engine2, all_places2):
        return  ('power=' + engine2), ('seats=' + all_places2)
class Truck(Car):
    pass

car = Truck("Volvo x60", "Land cruiser Prado", "LADA Vesta cross")
print(car)   
s = car.volvo(' 2.0', '4')
s1 = car.cruiser(' 5.0', ' 6')
s2 = car.LADA(' 2.5', ' 5')
res = getattr(car, 'Volvo')
print(res,'- total wheels = ' + car.total_wheels)
print(s)
res1 = getattr(car, 'Land_cruiser')
print(res1,'- total wheels = ' + car.total_wheels)
print(s1)
res2 = getattr(car, 'LADA_Vesta')
print(res2,'- total wheels = ' + car.total_wheels)
print(s2)

