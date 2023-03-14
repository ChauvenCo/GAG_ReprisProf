from user import User

class Game:
	def __init__(self, name, tag, image, price = 0):
		self._name = name
		self._tag = tag
		self._image = image
		self._comments = []
		self._price = price

	def addComment(self, user, comment, grade):
		comment = Comment(game=self, content=comment, grade=grade, user=user)
		self._comments.append(comment)
		return True

	def run(self):
		print(f'run {self._name}')

	def __hash__(self) -> int:
		return hash((self._name, self._image))

	def __repr__(self) -> str:
		return 'name: ' + self._name 

class GameNone(Game):
	def __init__(self):
		super().__init__('', '', '')

	def addComment(self, user, comment, grade):
		return False

	def run(self):
		pass

class Comment:
	def __init__(self, content, user : User, game : Game, grade):
		self._content = content
		self._user = user
		self._game = game
		self._grade = grade

	def __repr__(self) -> str:
		return f'comment: {self._content} ({self._grade})'