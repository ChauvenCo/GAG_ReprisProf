from abc import ABC, abstractmethod
from SqlServer import SqlServer
from Application import Application
from store import Store
from user import User
from lib import Lib
from game import Game, Comment
import pickle
import jsonpickle


class Persist(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self):
        pass


class PersistBinary(Persist):
    def __init__(self) -> None:
        super().__init__()
        self._gagfile = './gag.bjson'

    def save(self, data):
        with open(self._gagfile, mode='wb') as bin_file:
            pickle.dump(data, bin_file)

    def load(self):
        with open(self._gagfile, mode='wb') as bin_file:
            data = pickle.load(bin_file)
        return data


class PersistJson(Persist):
    def __init__(self) -> None:
        super().__init__()
        self._gagfile = './gag.json'

    def save(self, data):
        with open(self._gagfile, 'w') as json_file:
            data_str = jsonpickle.encode(data)
            json_file.write(data_str)

    def load(self):
        data = None
        with open(self._gagfile, 'r') as json_file:
            data_str = json_file.read()
            try:
                data = jsonpickle.decode(data_str)
            except:
                print('Unable to load file')
        return data


class PersistBDD(Persist):
    def __init__(self):
        super().__init__()
        self.sql = SqlServer("127.0.0.1", "GAG", "sa", "administrateur")
        self.sql.connect()
        self._idStore = 0
        self._idUser = 0

    def close(self):
        self.sql.disconnect()

    def save(self, data: Application):
        self.sql.execute_query("DELETE FROM Comment WHERE IdUser = " + str(data._user.Id))
        self.sql.execute_query("DELETE FROM Game WHERE IdStore = " + str(self._idStore))
        self.sql.execute_query("DELETE FROM GameLibrary WHERE IdLibrary = " + str(data._user._lib._id))

        insertGames = "INSERT INTO Game (Name, Tag, Price, Image, IdStore) OUTPUT INSERTED.ID VALUES "
        virgule = False
        for game in data._user._lib._games:
            if virgule:
                insertGames += " ,"
            insertGames += f" ('{game._name}', '{game._tag}', {game._price}, '{game._image}', {str(self._idStore)}) "
            virgule = True
        someId = self.sql.execute_query(insertGames)

        index = 0
        for game in data._user._lib._games:
            game._id = someId[index][0]
            index += 1

        insertGameLibraries = "INSERT INTO GameLibrary (IdGame, IdLibrary) VALUES "
        virgule = False
        for id in someId:
            if virgule:
                insertGameLibraries += " ,"
            insertGameLibraries += f" ({id[0]}, {data._user._lib._id}) "
            virgule = True
        self.sql.execute_query(insertGameLibraries)

        if len(data._user._comments) != 0:
            insertComment = "INSERT INTO Comment (Content, Grade, IdUser, IdGame) VALUES "
            virgule = False
            for comment in data._user._comments:
                if virgule:
                    insertComment += " ,"
                insertComment += f" ('{comment._content}', {comment._grade}, {data._user.Id}, {comment._game.ID}) "
                virgule = True
            self.sql.execute_query(insertComment)

    def load(self):
        data = None

        userReq = self.sql.execute_query(f"SELECT ID, Name FROM [User] WHERE ID = {self._idUser}")[0]
        user = User(userReq[0], userReq[1])

        commentsReq = self.sql.execute_query(
            "SELECT Comment.ID, Comment.Content, Comment.Grade, Comment.IdGame, Game.Name, Game.Tag, Game.Image "
            " FROM Comment "
            " INNER JOIN Game ON Game.ID = Comment.IdGame "
            " WHERE IdUser = " + str(user.Id))
        user._comments = []
        for index in range(0, len(commentsReq)):
            user._comments.append(Comment(commentsReq[index][0], commentsReq[index][1], user, Game(commentsReq[index][3], commentsReq[index][4], commentsReq[index][5], commentsReq[index][6]), commentsReq[index][2]))

        user._lib = Lib()
        user._lib._id = self.sql.execute_query("SELECT IdLibrary FROM [User] WHERE ID = " + str(user.Id))[0][0]

        libReq = self.sql.execute_query(
            "SELECT Game.ID, Game.Name, Game.Tag, Game.Image, Game.Price "
            " FROM Game "
            " INNER JOIN GameLibrary ON GameLibrary.IdGame = Game.ID "
            " INNER JOIN Library ON Library.ID = GameLibrary.IdLibrary "
            f" WHERE Library.ID  = {user._lib._id}")
        for index in range(0, len(libReq)):
            user._lib.addGame(Game(libReq[index][0], libReq[index][1], libReq[index][2], libReq[index][3], libReq[index][4]))

        storeReq = self.sql.execute_query(
            "SELECT Game.ID, Game.Name, Game.Tag, Game.Image, Game.Price FROM Game WHERE Game.IdStore = " + str(self._idStore))
        store = Store()
        store._games = set()
        for index in range(0, len(storeReq)):
            store.createGame(storeReq[index][0], storeReq[index][1], storeReq[index][2], storeReq[index][3], storeReq[index][4])

        data = Application(store, user)

        return data
