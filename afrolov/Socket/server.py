import socket

host = '127.0.0.1'
port = 9090

clients = []

s = socket.socket()
s.bind((host,port))

quit = False
print('Server started')

while not quit:
    try:
        data, addr = s.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        print(data.decode('utf-8'))

        for client in clients:
            if addr != client:
                s.sendto(data,client)
    except:
        print('\nServer stop')
        quit = True

s.close()