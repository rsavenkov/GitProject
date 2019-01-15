file_name = 'number.txt'
file_name1 = 'registration3.txt'
print("Ваши записи: \n")
S = []
with open(file_name1, 'r', encoding='utf-8') as f:
    contents = f.readlines()
    for line in contents:
        ds = eval(str(line[1:-2]))
        S.append(ds['Пациент'])
l = []
L = []
with open(file_name, 'r', encoding='utf-8') as f:
    text = f.readlines()
    for line in text:
        bs = eval(str(line[1:-2]))
        l.append(bs['-Месяц-'])
        l.append(bs['-Дата-'])
        l.append(bs['-Время-'])
        l.append(bs['-Место-'])
        L.append(l)
    for line in zip(S,L):
        for x in line:
            print(x)
        print('\n')