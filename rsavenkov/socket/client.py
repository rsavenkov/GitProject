import socket

'''
������� ������� ����������� ����� ������
'''
def Main():
    host = "000.000.000"
    port = 10001

    # ������� ���������� �����
    mySocket = socket.socket()
    # ����������� ����� ����� � �������� �� ��������� ������ connect
    mySocket.connect((host, port))

    # ������ ������������ ����
    message = input(" ? ")

    # � ����� ���� ��������� ���� �� ����� 'q'
    while message != 'q':
        # ���������� ������� ���������
        mySocket.send(message.encode())
        # ��������� �� ������� ���������
        data = mySocket.recv(1024).decode('utf8')

        # �������� ���
        print('Received from server: ' + data)
        # ������ ������������ ���� � ��� ������
        message = input(" ? ")
    # ��������� ���������� �����
    mySocket.close()

# � ������ ���� ���� ������ ������� ���������������, �� ������� Main() ����������.
# � ������ ���� ���� ������ ��������� � ������ ������, �� ������� �� ���������
if __name__ == '__main__':
    Main()
