from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    fname = db.Column(db.String(120), unique=True)
    lname = db.Column(db.String(120), unique=True)
    password = db.Column(db.String)
