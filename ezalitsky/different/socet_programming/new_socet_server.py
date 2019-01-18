import socket
import _thread

# Srver sets
host = "127.0.0.1"  # ip server
port = 5001         # port which is used for connect

newSocket = socket.socket()  # make socket
newSocket.bind((host, port))  # soket stik with host_ip and port
newSocket.listen(10)  #listen input connections


def new_client():
    while True:
        message = connection.recv(1024).decode()
        if not message:
            break
        print("From user: {} message : {}".format(address, message))

        ansver = input(" ? >> ")
        connection.send(ansver.encode())
    # ending connection
    connection.close()


while True:
    connection, address = newSocket.accept()
    print("accept connection : ", connection)
    print("accept address : ", address)
    _thread.start_new_thread(new_client(), (connection, address))

newSocket.close()


if __name__ == "__main__":
    Main()