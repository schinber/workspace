# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    # Columns

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(64), unique=True, index=True)

    pwd = db.Column(db.Integer, default=0)

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

    def __repr__(self):
        return '<User %r>' % self.name

    def __str__(self):
        return '<User %s>' % self.name
