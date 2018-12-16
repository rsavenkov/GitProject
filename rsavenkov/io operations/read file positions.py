file_name = 'C:/Users/Public/Projects/GitProject/trunk/rsavenkov/io operations/стих utf8.txt'

f = open(file_name, 'r+', encoding='utf-8')
data = f.read(20)
print('Прочитали первые 20 символов:', data)

position = f.tell()
print('Текущая позиция в файле:', position)

position = f.seek(position, 0)
data = f.read(10)
print('И еще 10 символом от текущей позиции в файле: ', data)

f.close()


print('--------------------------------')

with open('C:/Users/Public/Projects/GitProject/trunk/rsavenkov/io operations/myfile.txt', 'r+') as f:
    f.write('0123456789abcdef')
    f.seek(5, 0)  # Перемещаемся к 6-му байту от начала файла.
    data = f.read(3)  # '5'
    print(data)
    # f.seek(-3, 2)  # Перемещаемся к третьему байту от конца файла.
    # f.read(1)  # 'd