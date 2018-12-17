import os

message = 'This directory already exists'
directory = input('Пожалуйста введите имя файла')

try:
    home = os.path.expanduser('~')
    print(home)

    if not os.path.exists(os.path.join(home, directory)):
        os.makedirs(os.path(home, directory))
    else:
        print(message)
except Exception as e:
    print(e)