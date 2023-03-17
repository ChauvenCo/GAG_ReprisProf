# Imports pour les fonctionnalités du logiciel
from persist import *
from menu import Menu
from user import User
from lib import Lib
from game import Game, Comment
from store import Store
from GameLibrary import GameLibrary

# Imports pour la communication TCP
# from ServerTCP import ServerTCP

# Imports pour la communication HTTP
from http.server import BaseHTTPRequestHandler
import socketserver
from urllib.parse import urlparse, parse_qs

# Imports pour l'utilisation de SQLAlchemy
from SqlAlchemyElements import SqlAlchemyElements


usersMenu = {}

SqlAlchemyElements.Base.metadata.create_all(SqlAlchemyElements.engine)
session = SqlAlchemyElements.Session()


class Handler(BaseHTTPRequestHandler):
    def __init__(self, *args):
        super().__init__(*args)

    def do_GET(self):
        global usersMenu, session

        params = parse_qs(urlparse(self.path).query)

        if self.path.startswith("/start"):
            self.sendResponse("Avec quel magasin voulez-vous vous connecter : \n1 - Magasin central")

        elif self.path.startswith("/storeId"):
            if self.client_address not in usersMenu.keys():
                application = Application(session.query(Store).get(int(params["idStore"][0])), session.query(User).get(int(params["idUser"][0])))
                usersMenu[int(params["idUser"][0])] = Menu(application, session)
            self.sendResponse("Id set up")

        elif self.path.startswith("/options"):
            self.sendResponse(usersMenu[int(params["idUser"][0])].prompt())

        elif self.path.startswith("/doAction"):
            usersMenu[int(params["idUser"][0])].request = str(params["choice"][0])
            returnValue = usersMenu[int(params["idUser"][0])].main_entries[str(params["choice"][0]).split("_")[0]]()

            usersMenu[int(params["idUser"][0])].save()
            self.sendResponse(returnValue)

        else:
            self.sendResponse("Aucune action")


    def sendResponse(self, message: str):
        self.send_response(200)
        self.send_header('Content-type', "text/html")
        self.end_headers()
        self.wfile.write(bytes(message, "UTF-8"))


class ServerHTTP:
    def __init__(self, port):
        self.port = port

    def launch(self):
        with socketserver.TCPServer(("127.0.0.1", self.port), Handler) as httpd:
            httpd.serve_forever()


if __name__ == '__main__':
    server = ServerHTTP(8000)
    server.launch()

    # store = session.query(Store).get(1)
    # games = session.query(Game).filter(Game.storeId == store.ID).all()



    # store = session.query(Store).get(1)
    #
    # game1 = Game(name="Elden Ring", tag="Souls-Like", image="C:/image.png", price=59.99, storeId=store.ID)
    # game2 = Game(name="Cyberpunk", tag="Buggé", image="C:/image.png", price=19.99, storeId=store.ID)
    # game3 = Game(name="Doom", tag="Action", image="C:/image.png", price=11119.99, storeId=store.ID)
    # session.add(game1)
    # session.add(game2)
    # session.add(game3)

    # store = Store(name="Magasin Central")
    # session.add(store)

    # lib = session.query(Lib).get(1)
    # user = User(name="Damien", libId=1)
    # session.add(user)

    # lib = Lib(name="Bibliothèque locale")
    # session.add(lib)

    # session.commit()







    # persist = PersistBDD()
    #
    # server = ServerTCP("127.0.0.1", 8000)
    # server.launch()
    #
    # server.send("Avec quel magasin voulez-vous vous connecter : \n1 - Magasin central")
    # persist._idStore = int(server.receive())
    # application = persist.load()
    #
    # menu = Menu(application)
    #
    # selection = ""
    # while selection != "8":
    #     server.send(Menu.prompt())
    #     selection = server.receive()
    #     menu.request = selection
    #     server.send(menu._main_entries[selection.split("_")[0]]())
    #     persist.save(menu._application)
