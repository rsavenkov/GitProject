file_name = 'registration3.txt'
file_name2 = 'number.txt'

with open(file_name, 'r', encoding='utf-8') as f:
    contents = f.readlines()
    for line in contents:
        ds = eval(str(line[1:-2]))
        for k, v in ds.items():
            print(v)
        print('\n')


with open(file_name2, 'r', encoding='utf-8') as f:
    text = f.readlines()
    for line in text:
        bs = eval(str(line[1:-2]))
        print(bs['E-mail'])
        print("Ваша запись:")
        print(bs['-Месяц-'])
        print(bs['-Дата-'])
        print(bs['-Время-'])
        print(bs['-Место-'])
        print('\n')


