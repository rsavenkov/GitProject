import socket
import threading  # многопоточность


# создаем сокет из 2 компонентов(айпи и порт)
sock = socket.socket()
sock.bind(('192.168.43.164', 1080))# связь (IP port)
# (.listen()) этот параметр определяет размер очереди
# Если он установлен в единицу, а кто-то, явно лишний,
# пытается еще подстроится сзади, то его пошлют :)
sock.listen(3)
conn = []


def Reciver():
    while 1:
        for i in range(len(conn)):
            try:
                data = conn[i].recv(1024)
                if data:
                    print(data.decode())
            except socket.error as e:
                if e.errno == 10053:
                    conn.pop(i)
                    print("Подключено пользователй:", len(conn))
                else:
                    raise


def Sender():
    while 1:
        global conn
        message = input()
        if message:
            for i in range(len(conn)):
                conn[i].send(message.encode())


def Accepter():
    while 1:
        global conn
        conn.append(sock.accept()[0])
        print("Подключено пользователй:", len(conn))


# подключаем потоки передаем в параметры наши функции
t1 = threading.Thread(target=Reciver)
t2 = threading.Thread(target=Sender)
t3 = threading.Thread(target=Accepter)

# даем старт потокам
t1.start()
t2.start()
t3.start()
