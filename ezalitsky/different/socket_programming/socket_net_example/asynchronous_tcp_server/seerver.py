import select
import socket

SERVER_ADDRESS = ('localhost', 8686)

# Talk about how many descriptors can be open at a time
MAX_CONNECTIONS = 10

# From where and where to record information
INPUTS = list()
OUTPUTS = list()


def get_non_blocking_server_socket():

    # Create a socket that works without blocking the main thread
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(0)

    # Bind the server to the desired address and port
    server.bind(SERVER_ADDRESS)

    # Set the maximum number of connections
    server.listen(MAX_CONNECTIONS)

    return server


def handle_readables(readables, server):

# Handling the occurrence of events at the inputs

    for resource in readables:

        # If the event comes from a server socket, then we get a new connection
        if resource is server:
            connection, client_address = resource.accept()
            connection.setblocking(0)
            INPUTS.append(connection)
            print("new connection from {address}".format(address=client_address))

        # If the event does not originate from the server socket, but the interrupt has occurred for filling the input buffer
        else:
            data = ""
            try:
                data = resource.recv(1024)

            # If the socket was closed on the other side
            except ConnectionResetError:
                pass

            if data:

                # Output of the received data to the console
                print("getting data: {data}".format(data=str(data)))

                # We are talking about the fact that we will also write to this socket
                if resource not in OUTPUTS:
                    OUTPUTS.append(resource)

            # If there is no data, but the event worked, then the OS sends us a flag about the complete reading of the resource and its closing
            else:

                # Clearing data about the resource and closing the descriptor
                clear_resource(resource)


def clear_resource(resource):

    # Socket resource cleanup method
    if resource in OUTPUTS:
        OUTPUTS.remove(resource)
    if resource in INPUTS:
        INPUTS.remove(resource)
    resource.close()

    print('closing connection ' + str(resource))


def handle_writables(writables):

    # This event occurs when space is made available in the write buffer.
    for resource in writables:
        try:
            resource.send(bytes('Hello from server!', encoding='UTF-8'))
        except OSError:
            clear_resource(resource)


if __name__ == '__main__':

    # Create a server socket without blocking the main thread waiting for a connection
    server_socket = get_non_blocking_server_socket()
    INPUTS.append(server_socket)

    print("server is running, please, press ctrl+c to stop")
    try:
        while INPUTS:
            readables, writables, exceptional = select.select(INPUTS, OUTPUTS, INPUTS)
            handle_readables(readables, server_socket)
            handle_writables(writables)
    except KeyboardInterrupt:
        clear_resource(server_socket)
        print("Server stopped! Thank you for using!")