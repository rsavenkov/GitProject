from math import fabs
class NotNumberException(Exception):

    error_message = 'Ошибка! Вы ввели не число \'{}\'!'

    def __init__(self, message):
        self.message = NotNumberException.error_message.format(message)


class NotPositiveNumberException(NotNumberException):

    error1_message = 'Ошибка! Вы ввели отрицательное число!'

    def __init__(self, message1):
        self.message1 = NotPositiveNumberException.error1_message.format(message1)


input = input('Пожалуйста введите число:')

try:
    number = int(input)
    if number < 0:
        try:
            raise NotPositiveNumberException(input)
        except NotPositiveNumberException as error1:
            print(error1.message1)
    else:
        print('Спасибо, вы ввели положительное число:', number)
except ValueError:
    try:
        raise NotNumberException(input)
    except NotNumberException as error:
        print(error.message)