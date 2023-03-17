from lib import Lib
from sqlalchemy import *
from SqlAlchemyElements import SqlAlchemyElements

class User(SqlAlchemyElements.Base):
	__tablename__ = "User"

	ID = Column(Integer, primary_key=True)
	name = Column(String)
	# comments = Column(String)

	def __repr__(self):
		return f"<User(ID='{self.ID}', name='{self.name}')>"

	# def __init__(self, Id: int, name: str):
	# 	self.Id = Id
	# 	self._name = name
	# 	self._lib = Lib()
	# 	self._comments = []
	
	# def buyGame(self, game):
	# 	self._lib.addGame(game)