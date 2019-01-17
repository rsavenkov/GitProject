import socket

sock = socket.socket()
sock.connect(('192.168.43.164', 9090))
sock.send('hello, world!')

data = sock.recv(1024)
sock.close()

print(data)
'''Единственное новое здесь — это метод connect,
 с помощью которого мы подключаемся к серверу.
 Дальше мы читаем 1024 байт данных и закрываем сокет.'''