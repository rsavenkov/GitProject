file_name = 'registration.txt'

with open(file_name, 'r', encoding='utf-8') as f:
    contents = f.read()
    print(contents)