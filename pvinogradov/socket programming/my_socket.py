import socket
import sys

try:  #
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err_msg:
    print('Unable to instantate socket. Error code : ' + str(err_msg[0]) + ', Error Message : ' + err_msg[1])
    sys.exit()

print('socket Initialized')
