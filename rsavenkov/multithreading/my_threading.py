import threading, datetime


class myThread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        print('{}[{}]: {}'.format(self.name, self.counter, datetime.datetime.now().microsecond))
        print("Exiting " + self.name)


thread1 = myThread("Thread-first", 1)
thread2 = myThread("Thread-second", 2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Exiting the Program!!!")
