import socket
import _thread as thread

'''
Функция которая принимает объект соединения и клиентский адрес.
Получает из соединения буфер данных и печатает его. Читает ввод с клавиатуры и отправляет клиенту.
Подразумевается что функция будет передана в поток на выполнение.
'''
def on_new_client(connection, address):
    while True:
        message = connection.recv(1024).decode()
        if not message:
            break
        print("From {} >> {}".format(address, message))

        response = input(" ? ")
        connection.send(response.encode())
    # закрываем соединение
    connection.close()

# создаем серверный сокет
mySocket = socket.socket()
# привязываем его к хосту и порту
mySocket.bind(('127.0.0.1', 5001))

# начинаем слушать входящие соединения, до 5 штук
mySocket.listen(5)

# в бесконечном цикле ждем подключения по сети на методе .accept()
# как только к нам кто-то стучится, то полученное соединение передаем во вновь созданный новый поток
# таким образом каждый новый клиент из сети будет обрабытваться в отдельном потоке
while True:
    connection, address = mySocket.accept()
    thread.start_new_thread(on_new_client, (connection, address))

# закрываем серверный сокет
mySocket.close()
