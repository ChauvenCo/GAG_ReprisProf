# Imports Pour la communication TCP
# from ClientTCP import ClientTCP

# Imports Pour la communication HTTP
import requests


class ClientHTTP:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, path: str, **kwargs):
        url = self.base_url + path
        response = requests.get(url, **kwargs)
        return response


if __name__ == '__main__':
    userId = 1

    client = ClientHTTP("http://127.0.0.1:8000")
    print(client.get("/start").content.decode("UTF-8"))
    storeId = input("Choix : ")
    client.get("/storeId", params={"idStore": storeId, "idUser": userId})

    option = "0"
    while int(option) != 8:
        print(client.get("/options", params={"idUser": userId}).content.decode("UTF-8"))
        option = input("Choix : ")

        final = option

        if int(option) in [1, 2, 3, 4, 5, 6, 7]:
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

        print(client.get("/doAction", params={"choice": final, "idUser": userId}).content.decode("UTF-8"))








    # client = ClientTCP("127.0.0.1", 8000)
    # client.connect()
    #
    # print(client.receive())
    # option = input("Choix : ")
    # client.send(option)
    #
    # option = "0"
    # while int(option) != 8:
    #     print(client.receive())
    #     option = input("Choix : ")
    #     final = option
    #
    #     if int(option) in [2, 3, 4, 5, 6, 7]:
    #         name = input("name : ")
    #         final += "_" + name
    #
    #     if int(option) == 2:
    #         comment = input('comment: ')
    #         grade = input('grade(1..5): ')
    #         final += "_" + comment + "_" + grade
    #
    #     if int(option) == 5:
    #         tag = input('tag: ')
    #         price = input('price: ')
    #         image = input('image: ')
    #         final += "_" + tag + "_" + price + "_" + image
    #
    #     client.send(final)
    #     print(client.receive())
    #
    # client.close()