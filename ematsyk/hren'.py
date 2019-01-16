import threading


class Mclass1(threading.Thread):
    def __init__(self, dir):
        threading.Thread.__init__(self)
        self.dir = dir

    def run(self):
        with open(self.dir, 'r+', encoding='windows-1251') as x:
            print(x.readlines())


t1 = Mclass1("C:/Users/Mailz/PycharmProjects/GitProject/ematsyk/Chron.py")
t3 = Mclass1('C:/Users/Mailz/PycharmProjects/GitProject/ematsyk/123.py')
t2 = Mclass1(r'C:\Users\Mailz\PycharmProjects\GitProject\rsavenkov\serializing\111.txt')

t1.start()
t2.start()
t3.start()

# print('end of main thread')
