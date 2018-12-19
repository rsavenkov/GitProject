import os

class QuitProgramException(Exception):
    '''
    My program quit exception
    '''
    def __init__(self):
        self.message = 'Сеанс ввода завершен. Посмотрите содержимое файла {}'

disk_letters = ['A', 'B', 'C', 'D']

print('Добро пожаловать в консольную программу записи файла! Для выхода из нее введите команду quit()')

file = input('Введите имя файла:')
if (file[0] not in disk_letters) or (file[1:3] != ':\\'):
    print('Введенное значение не является файлом!')
    exit(-1)

dirs = file.split('\\')[1:-1]

#os.path.exists()
path = ''
for dir in dirs:
    path = path + '\\' + dir
    if not os.path.isdir(file[0:3] + path):
        print('Введенное значение не является файлом!')
        exit(-1)

#os.path.isfile()

error_code = 0
first = input('Введите содержимое файла:')
with open(file, 'w', encoding='utf-8') as f:
    try:
        f.writelines(first + '\n')
        while True:
            line = input()
            if line == 'quit()':
                raise QuitProgramException()
            f.writelines(line + '\n')
    except QuitProgramException as e:
        print(e.message.format(f.name))
        error_code = 0
    except KeyboardInterrupt as e:
        print('Непредвиденное завершение программы! Фалй не создан!')
        error_code = 2

if error_code != 0:
    os.remove(file)

exit(error_code)

