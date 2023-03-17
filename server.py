# Imports pour les foncitonnalités du logiciel
from persist import *
from menu import Menu
from user import User

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
        persist = PersistBDD()

        if self.path.startswith("/start"):
            self.sendResponse("Avec quel magasin voulez-vous vous connecter : \n1 - Magasin central")

        elif self.path.startswith("/storeId"):
            if self.client_address not in usersMenu.keys():
                persist._idStore = int(params["idStore"][0])
                persist._idUser = int(params["idUser"][0])
                usersMenu[persist._idUser] = Menu(persist.load())
            self.sendResponse("Id set up")

        elif self.path.startswith("/options"):
            self.sendResponse(usersMenu[int(params["idUser"][0])].prompt())

        elif self.path.startswith("/doAction"):
            usersMenu[int(params["idUser"][0])].request = str(params["choice"][0])
            returnValue = usersMenu[int(params["idUser"][0])]._main_entries[str(params["choice"][0]).split("_")[0]]()

            persist.save(usersMenu[int(params["idUser"][0])]._application)
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
    # server = ServerHTTP(8000)
    # server.launch()

    # user = User(name="David")
    # session.add(user)

    query = (session.query(User).all())
    print(query)

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
