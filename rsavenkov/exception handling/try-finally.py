try:
    f = open("C:\\Users\\Ruslan\\PycharmProjects\\GitProject\\trunk\\rsavenkov\\exception handling\\try-finally.py")
    print(f.read())
    print('try block executed')
finally:
    f.close()
    print('finally block executed')