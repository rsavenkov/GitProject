import socket


def Main():
    host = '192.168.43.164'

    port = 5002

    mySocket = socket.socket()
    mySocket.bind((host, port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print('from connected user: ' + str(addr))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print('from connected user: ' + str(data))

        data = str(data).upper()
        print(' Recived from user ' + str(data))

        data = input(' ? ')
        conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    Main()
