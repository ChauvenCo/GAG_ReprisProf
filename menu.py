class Menu:
	def __init__(self, store, user):
		self._store = store
		self._user = user
		self._main_entries = {
			'1': self.displayGames,
			'2': self.addComment,
			'3': self.detailGame,
			'4': self.removeGame,
			'5': self.createGame,
			'6': self.deleteGame,
			'7': self.buyGame,
			'8': self.quit
		}
		self.request = ""
	
	@classmethod
	def prompt(cls):
		print('1. Display games')
		print('2. Add comment')
		print('3. Detail game')
		print('4. Remove game')
		print('5. Create game in store')
		print('6. Delete game from store')
		print('7. Buy game')
		print('8. Bye')

	def detailGame(self):
		# name = input('name: ')
		name = self.request.split("_")[1]
		game_selected = None
		for game in self._store._games:
			if game._name == name:
				game_selected = game
				break
		print(game_selected)
		for comment in game_selected._comments:
			print(comment)
	
	def addComment(self):
		# name = input('name: ')
		# comment = input('comment: ')
		# grade = input('grade(1..5): ')
		name = self.request.split("_")[1]
		comment = self.request.split("_")[2]
		grade = self.request.split("_")[3]
		game_selected = None
		for game in self._user._lib._games:
			if game._name == name:
				game_selected = game
				break
		game_selected.addComment(self._user, comment, grade)

	def removeGame(self):
		# name = input('name: ')
		name = self.request.split("_")[1]
		game_to_delete = None
		for game in self._store._games:
			if game._name == name:
				game_to_delete = game
				break
		self._store.removeGame(game_to_delete)
	
	def deleteGame(self):
		# name = input('name: ')
		name = self.request.split("_")[1]
		game_to_delete = None
		for game in self._user._lib._games:
			if game._name == name:
				game_to_delete = game
				break
		self._user._lib.removeGame(game_to_delete)

	def displayGames(self):
		print('List of games')
		print(self._user._lib)
	
	def createGame(self):
		# name = input('name: ')
		# tag = input('tag: ')
		# price = input('price: ')
		# image = input('image: ')
		name = self.request.split("_")[1]
		tag = self.request.split("_")[2]
		price = self.request.split("_")[3]
		image = self.request.split("_")[4]
		self._store.createGame(name, tag, image, price)

	def buyGame(self):
		print('List of games in store')
		for game in self._store._games:
			print(game)
		# name = input('name: ')
		name = self.request.split("_")[1]
		self._store.buyGame(name, self._user)

	def quit(self):
		print('Goodbye')
		exit()