from user import User
from lib import Lib
from game import Game, Comment
from store import Store
from GameLibrary import GameLibrary


class Menu:
	def __init__(self, application, session):
		self.application = application
		self.session = session
		self.main_entries = {
			# '1': self.displayGames,
			'2': self.addComment,
			'3': self.detailGame,
			# '4': self.removeGame,
			# '5': self.createGame,
			# '6': self.deleteGame,
			'7': self.buyGame,
			'8': self.quit
		}
		self.request = ""
	
	@classmethod
	def prompt(cls):
		returnValue = '1. Display games'
		returnValue += '\n2. Add comment'
		returnValue += '\n3. Detail store game'
		returnValue += '\n4. Remove game'
		returnValue += '\n5. Create game in store'
		returnValue += '\n6. Delete game from store'
		returnValue += '\n7. Buy game'
		returnValue += '\n8. Bye'
		return returnValue

	def save(self):
		self.session.commit()

	def detailGame(self):
		name = self.request.split("_")[1]

		games = self.session.query(Game).filter(Game.storeId == self.application.store.ID, Game.name == name).all()

		if len(games) == 0:
			returnValue = str("Aucun jeu à ce nom")
		else:
			game_selected = games[0]
			returnValue = str(game_selected)
			comments = self.session.query(Comment).filter(Comment.gameId == game_selected.ID).all()
			for comment in comments:
				returnValue += "\n" + str(comment)

		return returnValue

	def addComment(self):
		name = self.request.split("_")[1]
		comment = self.request.split("_")[2]
		grade = self.request.split("_")[3]

		gamesInLibrary = self.session.query(GameLibrary.gameId).filter(GameLibrary.libId == self.application.user.libId)
		games = self.session.query(Game).filter(Game.ID.in_(gamesInLibrary), Game.name == name).all()

		if len(games) == 0:
			returnValue = str("Aucun jeu à ce nom dans la bibliothèque")
		else:
			game_selected = games[0]
			comment = Comment(content=comment, grade=grade, userId=self.application.user.ID, gameId=game_selected.ID)
			self.session.add(comment)

			returnValue = "Commentaire ajouté"

		return returnValue
	#
	# def removeGame(self):
	# 	name = self.request.split("_")[1]
	# 	game_to_delete = None
	# 	for game in self.application.store._games:
	# 		if game._name == name:
	# 			game_to_delete = game
	# 			break
	# 	self.application.store.removeGame(game_to_delete)
	# 	return "Jeu retiré"
	#
	# def deleteGame(self):
	# 	name = self.request.split("_")[1]
	# 	game_to_delete = None
	# 	for game in self.application.user._lib._games:
	# 		if game._name == name:
	# 			game_to_delete = game
	# 			break
	# 	self.application.user._lib.removeGame(game_to_delete)
	# 	return "Jeu supprimé"
	#
	# def displayGames(self):
	# 	returnValue = 'List of games'
	# 	returnValue += "\n" + str(self.application.user._lib)
	# 	return returnValue
	#
	# def createGame(self):
	# 	name = self.request.split("_")[1]
	# 	tag = self.request.split("_")[2]
	# 	price = self.request.split("_")[3]
	# 	image = self.request.split("_")[4]
	# 	self.application.store.createGame(0, name, tag, image, price)
	# 	return "Jeu ajouté"
	#
	def buyGame(self):
		name = self.request.split("_")[1]

		games = self.session.query(Game).filter(Game.storeId == self.application.store.ID, Game.name == name).all()

		if len(games) == 0:
			returnValue = "Jeu acheté"
		else:
			game_selected = games[0]
			gameLibrary = GameLibrary(libId=self.application.user.libId, gameId=game_selected.ID)
			self.session.add(gameLibrary)
			returnValue = "Jeu acheté"

		return returnValue

	def quit(self):
		return 'Goodbye'
