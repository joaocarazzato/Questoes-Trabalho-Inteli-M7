from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

class Account(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(100), nullable=False)
        password = db.Column(db.String(300), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(100), nullable=False)
    post_text = db.Column(db.String(400), nullable=False)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Integer, nullable=False)
    cp = db.Column(db.Integer, nullable=False)
    trtbps = db.Column(db.Integer, nullable=False)
    chol = db.Column(db.Integer, nullable=False)
    fbs = db.Column(db.Integer, nullable=False)
    restecg = db.Column(db.Integer, nullable=False)
    thalachh = db.Column(db.Integer, nullable=False)
    exng = db.Column(db.Integer, nullable=False)
    oldpeak = db.Column(db.Float, nullable=False)
    slp = db.Column(db.Integer, nullable=False)
    caa = db.Column(db.Integer, nullable=False)
    thall = db.Column(db.Integer, nullable=False)
    output = db.Column(db.Integer, nullable=False)

def create_table(app):

    with app.app_context():
        db.create_all()

def main():
    create_table()

if __name__ == "__main__":
    main()