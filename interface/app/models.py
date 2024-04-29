from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    tracks = db.relationship('Track', backref='user', lazy=True)


class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    youtube_link = db.Column(db.String(255), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    length = db.Column(db.String(255), nullable=False)
    filesize = db.Column(db.Float, nullable=False)
    downloads = db.Column(db.Integer, default=0)


class TopTrack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    youtube_link = db.Column(db.String(255), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    downloads = db.Column(db.Integer, default=0)
