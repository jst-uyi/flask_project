from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Title(db.Model):
    id = db.Column(db.String, primary_key=True)
    type = db.Column(db.String)
    title = db.Column(db.String)
    country = db.Column(db.String)
    date_added = db.Column(db.String)
    release_year = db.Column(db.Integer)
    rating = db.Column(db.String)
    duration = db.Column(db.String)
    description = db.Column(db.String)
    poster_url = db.Column(db.String)
    genres = db.relationship('Genre', secondary='title_genre', back_populates='titles')

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    titles = db.relationship('Title', secondary='title_genre', back_populates='genres')

class TitleGenre(db.Model):
    __tablename__ = 'title_genre'
    title_id = db.Column(db.String, db.ForeignKey('title.id'), primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), primary_key=True)
