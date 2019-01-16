import pickle
import os

'''
Change file's directory
'''

a = True

l = []

with open('C:/Users/Ruslan/PycharmProjects/GitProject/rklimenko/example.py', 'wb') as f:
    c = pickle.dump(a,f)

with open('C:/Users/Ruslan/PycharmProjects/GitProject/rklimenko/example.py', 'rb') as f:
    b = pickle.load(f)
    print(b)

c = int(input('Do you want to delete the file? Print "1" if yes, print "0" if no: '))
l.append(c)

d = l[0]
if d == 1:
    os.remove('example.py')
else:
    print('Well, well...')