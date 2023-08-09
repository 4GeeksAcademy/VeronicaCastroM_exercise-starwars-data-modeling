import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    name = Column(String(250))
    terrain = Column(String(250))
    rotation_Period = Column(Integer)
    diameter = Column(Integer)

class Starships(Base):
     __tablename__ = 'starships'
     ID = Column(Integer, primary_key=True)
     name = Column(String(250))
     model = Column(String(250))
     passengers = Column(Integer)
     length = Column(Integer)
     
    
class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True, unique=True)
    name = Column(String(250))
    hair_color = Column(String(50))
    Height = Column(Integer)
    Mass = Column(Integer)
    planet_id = Column(Integer, ForeignKey('planets.ID'))
    planets = relationship(Planets)
    starships_id = Column(Integer, ForeignKey('starships.ID'))
    starships = relationship(Starships)

class Favorite_Interships(Base):
    __tablename__ = 'favorite_interships'
    ID = Column(Integer, primary_key=True)
    ID_Starships = Column(Integer, ForeignKey('starships.ID'), unique=True)
    starships = relationship(Starships)

class Favorite_Character(Base):
    __tablename__ = 'favorite_character'
    ID = Column(Integer, primary_key=True)
    ID_Character = Column(Integer,ForeignKey('characters.ID'), unique=True)
    characters = relationship(Characters)    

class Favorite_Planets(Base):
    __tablename__ = 'favorite_planets'
    ID = Column(Integer, primary_key=True)
    ID_Planet = Column(Integer, ForeignKey('planets.ID'), unique=True)
    planets = relationship(Planets)       
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
