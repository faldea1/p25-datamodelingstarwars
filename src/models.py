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
    ##tips, nullable=false indica campo obligatorio/nullable=true es opcional, unique=true indica que una vez que se ingresa un valor en un "field", el mismo valor no puede ingresarse en ninguna otra instancia del modelo.
    ##fk, corresponden a datos externos/se abastece de otra tabla. Es una condición

class User(Base):
    __tablename__ = 'user'
    id = Column (Integer, primary_key=True)
    user_name = Column (String(25), nullable=False, unique=True)
    email = Column (String(30), nullable=False, unique=True)
    favorite_id = Column(Integer, ForeignKey('favorite.id'))

    ##methods (validar inicio de usuario, favoritos eliminados/descartados, favoritos agregados/guardados)
    def loginVerification(self):
        """ Verifying Login """

    def favoritesToDelete(self):
        """ Remove from Favorites """

    def favoritesToAdd(self):
        """ Add to Favorites """


class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column (Integer, primary_key=True)
    character_id = Column (Integer, nullable=True, ForeignKey('character.id'))
    vehicle_id = Column (Integer, nullable=True, ForeignKey('vehicle.id') )
    starship_id = Column (Integer, nullable=True, ForeignKey('starship.id') )
    planet_id = Column (Integer, nullable=True, ForeignKey('planet.id') )

    ##No es obligatorio escoger favoritos para cada categoria. Pueden tener o no tener, y en caso de haber, puede ser 1 o más.

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
