import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'apollonia'
    SQLALCHEMY_DATABASE_URI = 'postgresql://daddyzaring:JnqXNQlbaZZKOjzd4jFVUjY9mtdOk1ND@dpg-cokl20ljm4es73918lj0-a.oregon-postgres.render.com/purplemusic'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
