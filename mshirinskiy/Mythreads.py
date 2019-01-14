import threading

class MyThreads(threading.Thread):

    def __init__(self, Foldername):
        threading.Thread.__init__(self)
        self.Foldername=Foldername

    def run(self):
        with open(self.Foldername, 'r+', encoding='utf-8')as f:
            print(f.readline())


thread1 = MyThreads('C:/Users/mikle/PycharmProjects/GitProject/mshirinskiy/Garage/car.py')
thread2 = MyThreads('C:/Users/mikle/PycharmProjects/GitProject/mshirinskiy/Garage/Garage.py')


thread1.start()
thread2.start()

