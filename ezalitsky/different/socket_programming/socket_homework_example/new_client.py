import socket

def Main():
    host = "127.0.0.1"  # ip server
    port = 5001         # port which is used for connect

    mySocket = socket.socket()
    mySocket.connect((host, port))

    message = input(" >> ")

    while message != "q":
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()

        print("Recived from server :  " + str(data))
        message = input(" ? >> ")

    mySocket.close()


if __name__ == "__main__":
    Main()
