import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

##DATA MODELING A STAR WARS BLOG:
    ##1ero, definir número de tablas/clases.
    ##2do, definir nombres de tablas.
    ##3ero, pK (primary key) a las tablas, después de esto puedo generar diagrama ($python src/models.py). 
    ##4to, ya puedo empezar con las relaciones y especificar fK (foreign key) y quitar pK (del 3er paso) a tablas cuando corresponda.



class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column (Integer, primary_key=True)


class User(Base):
    __tablename__ = 'user'
    id = Column (Integer, primary_key=True)


class Character(Base):
    __tablename__ = 'character'
    id = Column (Integer, primary_key=True)


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column (Integer, primary_key=True)


class Starship(Base):
    __tablename__ = 'starship'
    id = Column (Integer, primary_key=True)


class Planet(Base):
    __tablename__ = 'planet'
    id = Column (Integer, primary_key=True)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
