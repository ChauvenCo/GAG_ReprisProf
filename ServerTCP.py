import socket


class ServerTCP:
    def __init__(self, adress, port):
        self.connexion = None
        self.adresse_client = None

        self.adress = adress
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.adress, self.port))

    def launch(self):
        self.socket.listen(1)
        print("Le serveur est en attente de connexions...")
        self.connexion, self.adresse_client = self.socket.accept()
        print("Connexion établie avec {}".format(self.adresse_client))

    def receive(self):
        message = self.connexion.recv(2048)
        return message.decode()

    def send(self, message):
        self.connexion.send(message.encode())

    def close(self):
        self.connexion.close()
        self.socket.close()