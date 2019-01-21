import threading
import socket


def process_request(conn, addr):
    print('connected client :', addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode('utf8'))


with socket.socket()as sock:
    sock.bind(('192.168.43.164', 4001))
    sock.listen()
    while True:
        conn, addr = sock.accept()
        th = threading.Thread(target=process_request, args=(conn, addr))
        th.start()
