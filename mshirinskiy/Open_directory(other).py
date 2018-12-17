import os

new_file=input('Please, enter the name of the new file')
file_contents=input(('Enter the text for the new file'))


try:
    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(file_contents)
except Exception as e:
    print(e)
