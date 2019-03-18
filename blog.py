"""__author__ = pengshengbing"""
import redis
from flask import Flask
from flask_script import Manager
from flask_session import Session

from back.models import db
from back.views import blue
from web.views import web_blue

app = Flask(__name__)
# app.register_blueprint(blueprint=blue, url_prefix='/back')
app.register_blueprint(blueprint=blue)
app.register_blueprint(blueprint=web_blue, url_prefix='/web')

app.config['SESSION_TYPE'] = 'redis'
# app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)
app.config['SESSION_REDIS'] = redis.Redis(host='47.101.203.226', port=6379, password='qwer1234')


app.secret_key = '124567sdawdaw654'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:qwer1234@47.101.203.226:3306/blog9'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Session(app)
db.init_app(app)
manage = Manager(app)


if __name__ == '__main__':
    manage.run()
