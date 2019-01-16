import threading, os


# files in directory visual as list
class dirmyThread(threading.Thread):
    def __init__(self, dir):
        threading.Thread.__init__(self)
        self.dir = dir

    def run(self):
        list = os.listdir(self.dir)
        print("Dir data :", list)

# file content
class filemyThread(threading.Thread):
     def __init__(self, dirn):
        threading.Thread.__init__(self)
        self.dirn = dirn

     def run(self):
        with open(self.dirn, "r", encoding="UTF-8") as f:
            print(f.readlines())


thread1 = dirmyThread(r"C:\Users\Xiaomi\Documents\Study\Python\ItMonopoly")
thread2 = dirmyThread(r"C:\Users\Xiaomi\Documents\Study\Python")
thread3 = filemyThread(r"C:\Users\Xiaomi\Documents\Exploit_directories\Python\PycharmProjects\itmonopoly\ezalitsky\text_RUN")
thread4 = filemyThread(r"C:\Users\Xiaomi\Documents\Exploit_directories\Python\PycharmProjects\itmonopoly\ezalitsky\different\console_hot_key.py")

thread1.start()
thread2.start()
thread3.start()
thread4.start()

# thread1.join()
# thread2.join()

