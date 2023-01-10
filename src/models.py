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

    ##methods (validar inicio de usuario, lista de favoritos ->  eliminados y agregados)
    def loginVerification(self):
        """ Verifying Login """

    def favoritesToDelete(self):
        """ Remove from Favorites """

    def favoritesToAdd(self):
        """ Add to Favorites """


class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    character_id = Column (Integer, ForeignKey('character.id'), nullable=True)
    vehicle_id = Column (Integer, ForeignKey('vehicle.id'), nullable=True)
    starship_id = Column (Integer, ForeignKey('starship.id'), nullable=True)
    planet_id = Column (Integer, ForeignKey('planet.id'), nullable=True)
    characterfav = relationship('Character', back_populates='children1')
    vehiclefav = relationship('Vehicle', back_populates='children2')
    starshipfav = relationship('Starship', back_populates='children3')
    planetfav = relationship('Planet', back_populates='children4') 

    ##No es obligatorio escoger favoritos para cada categoria. Pueden tener o no tener, y en caso de haber, puede ser 1 o más.

class Character(Base):
    __tablename__ = 'character'
    id = Column (Integer, primary_key=True)
    name = Column(String(40), nullable=False, unique=True)
    gender = Column(String(60), nullable=False)
    birth_year = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    skin_color = Column(String(60), nullable=False)
    hair_color = Column(String(60), nullable=False)
    eye_color = Column(String(60), nullable=False)
    children1 = relationship('Favorite', back_populates='characterfav')


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column (Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    model = Column(String(50), nullable=False)
    vehicle_class = Column(String(50), nullable=False)
    length = Column(Integer, nullable=False)
    manufacturer = Column(String(50), nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(50), nullable=False)
    children2= relationship('Favorite', back_populates='vehiclefav')


class Starship(Base):
    __tablename__ = 'starship'
    id = Column (Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    model = Column(String(100), nullable=False)
    starship_class = Column(String(100), nullable=False)
    length = Column(Integer, nullable=False)
    manufacturer = Column(String(100), nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(100), nullable=False)
    children3 = relationship('Favorite', back_populates='starshipfav')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column (Integer, primary_key=True)
    name = Column(String(150), nullable=False, unique=True)
    population = Column(Integer, nullable=False)
    climate = Column(String(150), nullable=False)
    terrain = Column(String(150), nullable=False)
    surface_water = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    gravity = Column(String(150), nullable=False)
    orbital_period = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    children4 = relationship('Favorite', back_populates='planetfav')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
