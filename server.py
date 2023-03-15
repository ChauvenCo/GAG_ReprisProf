from Application import Application
from store import Store
from user import User
from menu import Menu
from persist import *
import socket


class Server:
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

if __name__ == '__main__':
    persist = PersistBDD()

    server = Server("127.0.0.1", 8000)
    server.launch()

    server.send("Avec quel magasin voulez-vous vous connecter : \n1 - Magasin central")
    persist._idStore = int(server.receive())
    application = persist.load()

    menu = Menu(application)
    selection = ""
    while selection != "8":
        server.send(Menu.prompt())
        selection = server.receive()
        menu.request = selection
        server.send(menu._main_entries[selection.split("_")[0]]())
        persist.save(menu._application)
