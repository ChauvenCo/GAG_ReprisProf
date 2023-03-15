from game import Game


class Store:
	def __init__(self):
		self._games = set()

	def createGame(self, ID, name, tag, image, price):
		game = Game(ID, name, tag, image, price)
		self._games.add(game)

	def buyGame(self, name, user):
		for game in self._games:
			if game._name == name:
				user.buyGame(game)
	
	def removeGame(self, game):
		self._games.discard(game)