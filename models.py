import os
from sqlalchemy import Column, String, create_engine, Date, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Person
Have title and release year
'''
class Person(db.Model):  
  __tablename__ = 'People'

  id = Column(db.Integer, primary_key=True)
  name = Column(String)
  catchphrase = Column(String)

  def __init__(self, name, catchphrase=""):
    self.name = name
    self.catchphrase = catchphrase

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'catchphrase': self.catchphrase}
  

Base = declarative_base()

# associating table for the many-to-many relationship
link_movie_actor = Table('link_movie_actor', db.Model.metadata,\
  Column('actor_id', Integer, ForeignKey('actor.id'),primary_key=True),\
  Column('movie_id', Integer, ForeignKey('movie.id'),primary_key=True))


# adding movies model
'''
Movie class with
title and
release date
'''
class Movie(db.Model):
  __tablename__ = 'movie'

  id = Column(db.Integer, primary_key=True)
  title = Column(String, nullable=False, unique=True)
  release_date = Column(Date, nullable=False)

  def __init__(self, title, release_date):
    self.title = title
    self.release_date = release_date

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  actors = db.relationship('Actor',
                           secondary=link_movie_actor,
                           back_populates='movies')

  def format(self):
    actor_names = [actor.name for actor in self.actors]
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date,
      'actors': actor_names}

# adding Actors model
'''
Actor class with
name, age and gender
'''
class Actor(db.Model):
  __tablename__ = 'actor'

  id = Column(db.Integer, primary_key=True)
  name = Column(db.String, nullable=False, unique=True)
  age = Column(Integer, nullable=False)
  gender = Column(String, nullable=False)

  movies = db.relationship('Movie', 
                           secondary=link_movie_actor,
                           back_populates='actors')

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    movies_format = [movie.title for movie in self.movies]
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender,
      'movies': movies_format}