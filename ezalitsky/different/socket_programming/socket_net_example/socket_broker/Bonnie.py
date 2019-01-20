import ezalitsky.different.socket_programming.socket_net_example.socket_broker.Server_Casper as server

class Bonnie(server.Server):
    def handle(self, message):
        try:
            print("Got: {}".format(message))
        except Exception as e:
            print("Error: {}".format(e))


if __name__ == "__main__":
    print("Bonnie started.")
    app = Bonnie("localhost", 8889)
    app.start_server()
    app.loop()
    app.stop_server()

