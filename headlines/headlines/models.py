from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()

def db_connect():
	return create_engine(URL(**settings.DATABASE))

def create_headlines_table(engine):
	DeclarativeBase.metadata.create_all(engine)

class Headlines(DeclarativeBase):
	__tablename__ = "headlines"
	
	id = Column(Integer, primary_key=True)
	title = Column('title', String, nullable=True)
	link = Column('link', String, nullable=True)
	description = Column('description', String, nullable=True)





