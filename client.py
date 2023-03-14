import socket


class Client:
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


if __name__ == '__main__':
    client = Client("127.0.0.1", 8000)
    client.connect()

    option = "0"
    while int(option) != 8:
        print(client.receive())
        option = input("Choix : ")
        final = option

        if int(option) in [2, 3, 4, 5, 6, 7]:
            name = input("name : ")
            final += "_" + name

        if int(option) == 2:
            comment = input('comment: ')
            grade = input('grade(1..5): ')
            final += "_" + comment + "_" + grade

        if int(option) == 5:
            tag = input('tag: ')
            price = input('price: ')
            image = input('image: ')
            final += "_" + tag + "_" + price + "_" + image

        client.send(final)
        print(client.receive())