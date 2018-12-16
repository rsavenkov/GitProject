class Car:
    count = 0
    res = "can not change the number of wines"

    def __init__(self, b, c, w, cl):
        self.__brand = b
        self.__color = c
        self.__win = w
        self.__clss = cl
        Car.count += 1

    def get_brand(self):
        return self.__brand

    def set_brand(self, value):
        self.__brand = value
    brand = property(get_brand, set_brand)

    def get_color(self):
        return self.__color

    def set_color(self, value):
        self.__color = value
    color = property(get_color, set_color)

    def get_win(self):
        return self.__win

    def set_win(self,):
        return Car.res
    win = property(get_win, set_win)

    def get_clss(self):
        return self.__clss

    def set_clss(self, value):
        self.__clss = value
    clss = property(get_clss, set_clss)

    def show_info(self):
        print(f'model. :{self.__brand}')
        print(f'color avto :{self.__color}')
        print(f'win number :{self.__win}')
        print(f'class avto :{self.__clss}')


