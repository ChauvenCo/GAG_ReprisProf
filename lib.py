from sqlalchemy import *
from SqlAlchemyElements import SqlAlchemyElements


class Lib(SqlAlchemyElements.Base):
	__tablename__ = "Lib"

	ID = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String)
	
	# def addGame(self, game):
	# 	self._games.add(game)
	#
	# def launchGame(self, name):
	# 	for game in self._games:
	# 		if game._name == name:
	# 			game.run()
	#
	# def displayGames(self):
	# 	for game in self._games:
	# 		print(game)
	#
	# def removeGame(self, game):
	# 	self._games.discard(game)
	#
	# def __repr__(self) -> str:
	# 	result = ''
	# 	for game in self._games:
	# 		result += str(game)
	# 	return result

