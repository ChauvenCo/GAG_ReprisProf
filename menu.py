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
		returnValue = '1. Display all local games'
		returnValue += '\n2. Add comment to local game'
		returnValue += '\n3. Detail a store game'
		returnValue += '\n4. Remove game from local library'
		returnValue += '\n5. Create game in store'
		returnValue += '\n6. Delete game from store'
		returnValue += '\n7. Buy a store game'
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

	def removeGame(self):
		name = self.request.split("_")[1]

		gamesInLibrary = self.session.query(GameLibrary.gameId).filter(GameLibrary.libId == self.application.user.libId)
		games = self.session.query(Game).filter(Game.ID.in_(gamesInLibrary), Game.name == name).all()

		if len(games) == 0:
			returnValue = str("Aucun jeu à ce nom dans la bibliothèque")
		else:
			game_selected = games[0]
			elementsToRemove = self.session.query(GameLibrary).filter(GameLibrary.gameId == game_selected.ID).all()
			for element in elementsToRemove:
				self.session.delete(element)
			returnValue = "Jeu retiré"

		return returnValue

	def deleteGame(self):
		name = self.request.split("_")[1]

		games = self.session.query(Game).filter(Game.storeId == self.application.store.ID, Game.name == name).all()

		if len(games) == 0:
			returnValue = str("Aucun jeu à ce nom")
		else:
			self.session.delete(games[0])
			returnValue = "Jeu supprimé"

		return returnValue

	def displayGames(self):
		gamesInLibrary = self.session.query(GameLibrary.gameId).filter(GameLibrary.libId == self.application.user.libId)
		games = self.session.query(Game).filter(Game.ID.in_(gamesInLibrary)).all()

		returnValue = 'List of games'
		for game in games:
			returnValue += "\n" + str(game)

		return returnValue

	def createGame(self):
		name = self.request.split("_")[1]
		tag = self.request.split("_")[2]
		price = self.request.split("_")[3]
		image = self.request.split("_")[4]

		game = Game(name=name, tag=tag, price=price, image=image, storeId=self.application.store.ID)
		self.session.add(game)
		return "Jeu ajouté"

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
