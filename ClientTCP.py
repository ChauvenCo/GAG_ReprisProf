import socket


class ClientTCP:
    def __init__(self, adress, port):
        self.adress = adress
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.adress, self.port))
        print("Connecté au serveur")

    def receive(self):
        message = self.socket.recv(2048)
        return message.decode()

    def send(self, message):
        self.socket.send(message.encode())

    def close(self):
        self.socket.close()