import os
from sqlalchemy import Column, String, create_engine, Date, Integer
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
  

  # adding movies model
'''
Movie class with
title and
release date
'''
class Movie(db.Model):
  __tablename__ = 'Movie'

  id = Column(db.Integer, primary_key=True)
  title = Column(String, nullable=False)
  release_date = Column(Date, nullable=False)

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date}

  # adding Actors model
'''
Actor class with
name, age and gender
'''
class Actor(db.Model):
  __tablename__ = 'Actor'

  id = Column(db.Integer, primary_key=True)
  name = Column(db.String, nullable=False)
  age = Column(Integer, nullable=False)
  gender = Column(String, nullable=False)

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender}