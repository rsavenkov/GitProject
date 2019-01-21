import socket
with socket.socket() as soc:
    while True:
        soc.bind(('192.168.43.164', 2001))
        soc.listen()
        while True:
            conn, adr = soc.accept()
            conn.settimeout(5)
            with conn:
                while True:
                    try:
                        data = conn.recv(1024)
                    except socket.timeout:
                        print('close connection by timeout')
                        break
                    if not data:
                        break
                    print(data.decode('utf8'))
