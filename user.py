from lib import Lib
from sqlalchemy import *
from SqlAlchemyElements import SqlAlchemyElements

class User(SqlAlchemyElements.Base):
	__tablename__ = "User"

	ID = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String)
	libId = Column(Integer, ForeignKey(Lib.ID))

	def __repr__(self):
		return f"Nom d'utilisateur: {self.name})"
