# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://anjian:topcom123@115.28.72.158/wechat"

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://anjian:topcom123@115.28.72.158/wechat'
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"]=True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app
