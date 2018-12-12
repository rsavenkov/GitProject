file_name = 'C:/Users/Ruslan/PycharmProjects/GitProject/trunk/rsavenkov/io operations/стих utf8.txt'

f = open(file_name, 'r+', encoding='utf-8')
data = f.read(20)
print('Прочитали первые 20 символов:', data)

position = f.tell()
print('Текущая позиция в файле:', position)

position = f.seek(position, 0)
data = f.read(10)
print('И еще 10 символом от текущей позиции в файле: ', data)

f.close()