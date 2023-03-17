from sqlalchemy import *
from SqlAlchemyElements import SqlAlchemyElements


class Store(SqlAlchemyElements.Base):
	__tablename__ = "Store"

	ID = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String)

	# def createGame(self, ID, name, tag, image, price):
	# 	game = Game(ID, name, tag, image, price)
	# 	self._games.add(game)
	#
	# def buyGame(self, name, user):
	# 	for game in self._games:
	# 		if game._name == name:
	# 			user.buyGame(game)
	#
	# def removeGame(self, game):
	# 	self._games.discard(game)

	def __repr__(self):
		return f"Nom de dépôt: {self.name})"
