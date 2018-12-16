class NotNumberException(Exception):

    error_message = 'Ошибка! Вы ввели не число \'{}\'!'

    def __init__(self, message):
        self.message = NotNumberException.error_message.format(message)

class NotPositiveNumberException(NotNumberException):

    error_message = 'Ошибка! Отрицательное число {}!'

    def __init__(self, message):
        self.message = NotPositiveNumberException.error_message.format(message)

my_input = input('Пожалуйста введите число:')

try:
    number = int(my_input)
    if number < 0:
        try:
            raise NotPositiveNumberException(my_input)  # raise передает ошибку на уровень вверх
        except NotPositiveNumberException as e:
            print(e.message)
    else:
        print('Спасибо, вы ввели число:', number)

except ValueError:
    try:
        raise NotNumberException(my_input)
    except NotNumberException as error:
        print(error.message)