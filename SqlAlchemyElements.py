from sqlalchemy import *
from sqlalchemy.orm import *

class SqlAlchemyElements:
    engine = create_engine("sqlite:///C:\\Users\\boiza\Documents\\1-Epsi\\Architecture N-Tiers\\ProfRepo\\memory.db", echo=True)
    Base = declarative_base()
    Session = sessionmaker(bind=engine)