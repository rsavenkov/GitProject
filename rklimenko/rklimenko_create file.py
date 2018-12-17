import os.path

file_name = input('Введите путь до файла: ')
test_file = 'C:/Users/Ruslan/PycharmProjects/GitProject/rklimenko'

if os.path.samefile(file_name, test_file) and os.path.exists(file_name):
    with open(file_name, 'w') as f:
        f.writelines(input())
        f.read()
        f.close()
else:
    print('Введите корректный путь до файла.')
