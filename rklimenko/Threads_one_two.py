from threading import Thread

class MyClass1(Thread):
    def __init__(self,dir):
        Thread.__init__(self)
        self.dir = dir

    def run(self):
        with open(self.dir, 'r+', encoding='utf-8') as f:
            print(f.readlines())

t1 = MyClass1('C:/Users/Ruslan/PycharmProjects/GitProject/rklimenko/Threads_one_two.py')
t2 = MyClass1('C:/Users/Ruslan/PycharmProjects/GitProject/rklimenko/rklimenko_create file.py')

t1.start()
t2.start()

