# file_name = 'C:/Users/vinog/GitProject1/P.vinogradov/12.12.2018 open file/file'

# f = open(file_name, 'r+', encoding='utf-8')
# data = f.read(20)
# print('Прочитали первые 20 символов:', data)
# 
# position = f.tell()
# print('Текущая позиция в файле:', position)
# 
# position = f.seek(position, 0)
# data = f.read(10)
# print('И еще 10 символом от текущей позиции в файле: ', data)
# 
# f.close()
# print('----------------------------')

file_name = open("C:/Users/vinog/GitProject1/P.vinogradov/12.12.2018 open file/file", "w")
file_name.write("hello world!")
file_name.close()
