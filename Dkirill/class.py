class announcement():
    def print_announcement(self):
        print('объявление на авито')

class Car(announcement):
    def print_specifications(self):
        print('Машина:Premium class')

class cars(Car):
    def print_brand(self):
        print('Bmw_x6 2017г.')

class motor(cars):
    def print_motors(self):
        print('Характеристики двигателя: Объём двигателя: 3.0, Мощность двигателя: 313 л.с.')

class  condition(cars):
    def print_condition(self):
        print('Пробег: 3970 км, в хорошем состоянии!!')

class price(announcement):
    def print_price(self):
        print('ценна: 5 000 000')

class  information(announcement):
    def print_personal(self):
        print('номер телефона  :8 911 652 08 25- Кирилл Дроздов ')

class conclusion(announcement):
    def print_conclusion(self):
        print('Кого заинтересовало звоните, или пишите  на почту kirilldrozd12@gmail.com')



an=announcement()
c=Car()
ca=cars()
mo=motor()
con=condition()
pr=price()
inf=information()
conr=conclusion()



an.print_announcement()
ca.print_brand()
c.print_specifications()
mo.print_motors()
con.print_condition()
pr.print_price()
conr.print_conclusion()
inf.print_personal()
