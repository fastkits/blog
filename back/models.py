"""__author__ = pengshengbing"""
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False)
    is_delete = db.Column(db.Boolean, default=0)
    create_time = db.Column(db.DateTime, default=datetime.now())

    __tablename__ = 'user'


class ArticleType(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    t_name = db.Column(db.String(25), unique=True, nullable=False)
    arts = db.relationship('Article', backref='tp')
    __tablename__ = 'art_type'


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    desc = db.Column(db.String(100), unique=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
    type = db.Column(db.Integer, db.ForeignKey('art_type.id'))

