import socket
import sys


try:
    sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err_msg:
    print("Unable to instantiate. Error code:" + str(err_msg[0]) + " , Error message : " + err_msg[1])
    sys.exit()

print("Socet Initialized")