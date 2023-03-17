from user import User
from store import Store

from sqlalchemy.orm import *
from sqlalchemy import *
from SqlAlchemyElements import SqlAlchemyElements


class Game(SqlAlchemyElements.Base):
	__tablename__ = "Game"

	ID = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String)
	tag = Column(String)
	image = Column(String)
	price = Column(Float)
	storeId = Column(Integer, ForeignKey(User.ID))

	# def addComment(self, user, comment, grade):
	# 	comment = Comment(ID=0, game=self, content=comment, grade=grade, user=user)
	# 	self._comments.append(comment)
	# 	return True
	#
	# def run(self):
	# 	print(f'run {self._name}')

	def __hash__(self) -> int:
		return hash((self.name, self.image))

	def __repr__(self) -> str:
		return f"name: {self.name}"


# class GameNone(Game):
# 	def __init__(self):
# 		super().__init__(0, '', '', '')
#
# 	def addComment(self, user, comment, grade):
# 		return False
#
# 	def run(self):
# 		pass


class Comment(SqlAlchemyElements.Base):
	__tablename__ = "Comment"

	ID = Column(Integer, primary_key=True, autoincrement=True)
	content = Column(String)
	grade = Column(Integer)
	userId = Column(Integer, ForeignKey(User.ID))
	gameId = Column(Integer, ForeignKey(Game.ID))

	def __repr__(self) -> str:
		return f'comment: {self.content} ({self.grade})'
