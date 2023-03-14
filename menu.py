from game import GameNone

class Menu:
	def __init__(self, application):
		self._application = application
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
		returnValue = '1. Display games'
		returnValue += '\n2. Add comment'
		returnValue += '\n3. Detail game'
		returnValue += '\n4. Remove game'
		returnValue += '\n5. Create game in store'
		returnValue += '\n6. Delete game from store'
		returnValue += '\n7. Buy game'
		returnValue += '\n8. Bye'
		return returnValue

	def detailGame(self):
		# name = input('name: ')
		name = self.request.split("_")[1]
		game_selected = GameNone()
		for game in self._application._store._games:
			if game._name == name:
				game_selected = game
				break
		returnValue = str(game_selected)
		for comment in game_selected._comments:
			returnValue += "\n" + str(comment)
		return returnValue
	
	def addComment(self):
		# name = input('name: ')
		# comment = input('comment: ')
		# grade = input('grade(1..5): ')
		name = self.request.split("_")[1]
		comment = self.request.split("_")[2]
		grade = self.request.split("_")[3]
		game_selected = GameNone()
		for game in self._application._user._lib._games:
			if game._name == name:
				game_selected = game
				break
		if not game_selected.addComment(self._application._user, comment, grade):
			return "Jeu inexistant dans la biliothèque locale"
		return "Commentaire ajouté"

	def removeGame(self):
		# name = input('name: ')
		name = self.request.split("_")[1]
		game_to_delete = None
		for game in self._application._store._games:
			if game._name == name:
				game_to_delete = game
				break
		self._application._store.removeGame(game_to_delete)
		return "Jeu retiré"
	
	def deleteGame(self):
		# name = input('name: ')
		name = self.request.split("_")[1]
		game_to_delete = None
		for game in self._application._user._lib._games:
			if game._name == name:
				game_to_delete = game
				break
		self._application._user._lib.removeGame(game_to_delete)
		return "Jeu supprimé"

	def displayGames(self):
		returnValue = 'List of games'
		returnValue += "\n" + str(self._application._user._lib)
		return returnValue
	
	def createGame(self):
		# name = input('name: ')
		# tag = input('tag: ')
		# price = input('price: ')
		# image = input('image: ')
		name = self.request.split("_")[1]
		tag = self.request.split("_")[2]
		price = self.request.split("_")[3]
		image = self.request.split("_")[4]
		self._application._store.createGame(name, tag, image, price)
		return "Jeu ajouté"

	def buyGame(self):
		returnValue = 'List of games in store'
		for game in self._application._store._games:
			returnValue += "\n" + str(game)
		# name = input('name: ')
		name = self.request.split("_")[1]
		self._application._store.buyGame(name, self._application._user)
		return returnValue

	def quit(self):
		return 'Goodbye'
