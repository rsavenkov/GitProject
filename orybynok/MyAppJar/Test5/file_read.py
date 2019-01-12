file_name = 'registration3.txt'
file_name2 = 'number.txt'

with open(file_name, 'r', encoding='utf-8') as f:
    contents = f.read()
    ds = eval(str(contents[1:-1]))
    for k,v in ds.items():
        print(v)
    print('\n')


with open(file_name2, 'r', encoding='utf-8') as f:
    text = f.read()
    bs = eval(str(text[1:-2]))
    print("Ваша запись:")
    print(bs['-Месяц-'])
    print(bs['-Дата-'])
    print(bs['-Время-'])
    print(bs['-Место-'])
