import socket


def Main():
    host = 'local host'
    port = 2001

    mySocket = socket.socket()
    mySocket.connect((host, port))

    message = input(' ? ')

    while message != 'q':
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()

        print('receive from server: ' + data)
        message = input(' ? ')
    mySocket.close()
Main()


