file_name = 'C:/Users/vinog/GitProject1/P.vinogradov/12.12.2018 open file/file'

with open(file_name, 'w', encoding="utf-8") as f:
    f.write('Это первая строка которую я записал в файл из программы/n')
    f.write('Это вторая строка которую я записал в файл из программы/n')
    f.write('Конец/n')

with open(file_name, 'r', encoding='utf-8') as f:
    content = f.readlines()
     #content = f.read()

for line in content:
    print(line)
