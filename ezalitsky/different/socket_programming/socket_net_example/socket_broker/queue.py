import threading
import socketserver

# Own message queue to which it can send data.
# As required, the application takes messages from this queue and processes them.


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        print(data)


class Queue:

    # In the __init__ constructor, the socket server is initialized to work in a separate thread.

    def __init__(self, ip, port):
        self.server = ThreadedTCPServer((ip, port), ThreadedTCPRequestHandler)
        self.server.queue = self # writes a pointer to the queue object in the socket server so that it can be accessed from another thread.
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.messages = []  # message queue

    def start_server(self):
        self.server_thread.start()
        print("Server loop running in thread: ", self.server_thread.name)

    def stop_server(self):
        self.server.shutdown()
        self.server.server_close()

    def add(self, message):
        self.messages.append(message)

    def view(self):
        return self.messages

    def get(self):
        return self.messages.pop()

    def exists(self):
        return len(self.messages)

