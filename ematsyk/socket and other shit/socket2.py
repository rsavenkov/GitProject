import _socket
import socket

def Main():
    host = "192.168.50.103"
    port = 5001

    mySocket = _socket.socket() # made socket
    mySocket.bind((host, port))

    mySocket.listen(3)
    conn, addr = mySocket._accept(2)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from con user:" + str(data))

        data = str(data).upper()
        print("recived from user" + str(data))

        data = input(" ? ")
        conn.send(data.encode())

    conn.close()

if __name__ == "__main__":
    Main()