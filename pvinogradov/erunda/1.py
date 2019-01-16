from threading import Thread


class Myclass(Thread):

    def __init__(self, dir):
        Thread.__init__(self)
        self.dir = dir

    def run(self):
        with open(self.dir, 'r+', encoding='UTF-8')as f:
            print(f.readlines())


t1 = Myclass('C:/svn/untitled1/trunk/pythonator b2 easy/LICENSE.TXT')
t2 = Myclass('C:/svn/untitled1/trunk/pythonator b2 easy/LICENSE.TXT')

t1.start()
t2.start()

print('hello')
