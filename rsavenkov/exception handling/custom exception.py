class NotNumberException(Exception):

    error_message = 'Ошибка! Вы ввели не число \'{}\'!'

    def __init__(self, message):
        self.message = NotNumberException.error_message.format(message)

class NotPositiveNmberException(NotNumberException):

    def __init__(self, message):
        super().message = message

input = input('Пожалуйста введите число:')

try:
    number = int(input)
    print('Спасибо, вы ввели число:', number)
except ValueError:
    try:
        raise NotNumberException(input)
    except NotNumberException as error:
        print(error.message)