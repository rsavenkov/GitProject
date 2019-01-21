import socket

with socket.create_connection(('192.168.43.164', 2001),5) as sock:
    sock.settimeout(2)
    try:
        sock.sendall('ping'.encode('utf8'))
    except socket.timeout:
        print('send data timeout')
    except socket.error as ex:
        print('send data error:',ex)