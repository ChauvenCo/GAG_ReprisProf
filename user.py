from lib import Lib

class User:
	def __init__(self, name):
		self._name = name
		self._lib = Lib()
		self._comments = []
	
	def buyGame(self, game):
		self._lib.addGame(game)