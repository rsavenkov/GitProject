"""server worked with queue"""

import socket
import time
from ezalitsky.different.socket_programming.socket_net_example.socket_broker.queue import Queue

class Server:
    def __init__(self, ip, port):
        self.queue = Queue(ip, port)

    def start_server(self):
        self.queue.start_server()

    def stop_server(self):
        self.queue.stop_server()

    def send(self, ip, port, message):
        # send to socket function
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        try:
            sock.sendall(bytes(message, 'ascii'))
        finally:
            sock.close()

    def loop(self):
        while True:
            time.sleep(1)
            while self.queue.exists():
                self.handle(self.queue.get())

    # def handle(self, message):
    #     """    Prototype    """
    #     pass

"""A loop function that checks if there is data in the queue,
taking one element from there and passing it to the handle method for processing. """



