file_name = 'C:/Users/vinog/GitProject1/rsavenkov/io operations/стих ansi.txt'

f = open(file_name, 'r+')

print('File attributes:')
print('closed:', f.closed)
print('mode:', f.mode)
print('name:', f.name)
f.close()
print('closed:', f.closed)