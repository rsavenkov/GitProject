# импортим библиотеку threading, она появилась в Python 3, написана в ооп стиле, рекомендуема к использованию
import threading, time

# некоторый общий разделяемый ресурс
shared_resource = 0

'''
Создаем поток в стиле Python 3. Cоздаем собственный класс - потомок класса threading.Thread
'''
class myThread(threading.Thread):

    # параметры: name - имя потока, counter - счетчик, algorithm - тип алгоритма
    def __init__(self, name, counter, algorithm):
        threading.Thread.__init__(self)
        self.threadID = counter; self.name = name; self.algorithm = algorithm; self.counter = counter

    # метод - это то что будет делать кадый поток.
    # в методе происходит блокировка кода в котором анализируется переменная algorithm и выбирается тип алгоритма
    # далее увеличивается + 1 значение общего ресурса и его печать
    # в конце блокировка освобождается
    def run(self):
        global shared_resource
        print("Starting " + self.name)
        threadLock.acquire()
        if self.algorithm:
            for i in range(10):
                time.sleep(1)
                shared_resource += 1
                print('{}[{}]: resource is {}\n'.format(self.name, self.counter, shared_resource))
        else:
            for i in range(10):
                time.sleep(1)
                shared_resource -= 1
                print('{}[{}]: resource is {}\n'.format(self.name, self.counter, shared_resource))
        threadLock.release()
        print("Exiting " + self.name)

# создаем объект блокировки
threadLock = threading.Lock()
# создаем два потока, объекта класса myThread
thread1 = myThread("Thread", 1, True); thread2 = myThread("Thread", 2, False)
# стартуем их, начинает выполнятся метод run
thread1.start(); thread2.start()
# родительский поток здесь останавливается и ждет пока первый и второй поток не завершаться
thread1.join(); thread1.join()
print("Exiting the Program!!!")