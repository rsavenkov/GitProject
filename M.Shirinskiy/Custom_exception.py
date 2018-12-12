class NotNumberException(Exception):

    error_message = 'Ошибка! Вы ввели не число {}!'

    def __init__(self, message):
        self.message = NotNumberException.error_message.format(message)

class NotPositiveNumberException(Exception):

    error_message = 'Ошибка! Вы ввели отрицательное число {}!'

    def __init__(self, message):
        self.message = NotPositiveNumberException.error_message.format(message)

input = input('Пожалуйста, введите число:')

try:
    number = int(input)
    if number < 0:
        try:
            raise NotPositiveNumberException(number)
        except NotPositiveNumberException as error:
            print(error.message)
    else:
        print('Спасибо, вы ввели число:', number)
except ValueError:
    try:
        NotNumberException(number)
    except NotNumberException as error:
        print(error.message)