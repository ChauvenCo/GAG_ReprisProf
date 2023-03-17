from sqlalchemy.orm import *
from sqlalchemy import *
from SqlAlchemyElements import SqlAlchemyElements

from lib import Lib
from game import Game


class GameLibrary(SqlAlchemyElements.Base):
    __tablename__ = "GameLibrary"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    libId = Column(Integer, ForeignKey(Lib.ID))
    gameId = Column(Integer, ForeignKey(Game.ID))
