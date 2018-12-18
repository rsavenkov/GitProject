import os

disk_letters = ['A', 'B', 'C', 'D']

file = input('Введите имя файла:')

if os.name == 'nt':
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
            exit(0)

#os.path.isfile()

# доработать программу так чтобы последняя строчка сохранялась когда на ней нажимаю ctrl + z
first = input('Введите содержимое файла:')
with open(file, 'w', encoding='utf-8') as f:
    try:
        f.writelines(first + '\n')
        while True:
            line = input()
            f.writelines(line + '\n')
    except KeyboardInterrupt as e:
        print('Сеанс ввода завершен. Посмотрите содержимое файла {}'.format(f.name))
        exit(0)

exit(0)

