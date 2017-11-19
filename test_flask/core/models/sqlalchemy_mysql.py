# -*- coding: utf-8 -*-

"""
practice for sqlalchemy
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

app = Flask(__name__)

ENGINE = {
    "mysql": 'mysql://tingyun:tingyun@mysql.db.com:3306/xiguago?charset=utf8',
    "oracle": 'oracle://tingyun:tingyun@192.168.1.15:1521/nbsdb',
    "postgresql": "postgresql://tingyun:tingyun@192.168.2.43:5432/xiguago"
}


app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
manager = Manager(app)


class User(db.Model):
    __tablename__ = 'flask_sqlalchemy_test'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80))
    grade = db.Column(db.String(50))

    def __repr__(self):
        return self.username

    # def __unicode__(self):
    #     return '%s' % self.username


