file_name = 'C:/Users/Ruslan/PycharmProjects/GitProject/trunk/rsavenkov/io operations/стих.txt'

f = open(file_name, 'r+')
print('File attributes:')
print('closed:', f.closed)
print('mode:', f.mode)
print('name:', f.name)