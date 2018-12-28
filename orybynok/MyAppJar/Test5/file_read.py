file_name = 'registration3.txt'


with open(file_name, 'r', encoding='utf-8') as f:
    contents: list = f.read()
    print("Список:\n")
    print(contents)


