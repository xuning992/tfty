# -*- coding: utf-8 -*-


import random
from flask import Blueprint, request
from ..models.sqlalchemy_mysql import db, User, app, ENGINE

sqlalchemy_mysql = Blueprint('sqlalchemy_mysql', __name__)


@sqlalchemy_mysql.route('/sqlalchemy/insert')
def sqlalchemy_mysql_insert():
    """
    :sql: 作为参数传入，控制数据库种类
    :return:
    """
    sql_type = request.args.get("sql")
    ensure_engine(sql_type)

    rand = random.randint(0, 100000000000000000000000000)
    rand_ = random.randint(0, 150)

    if sql_type == "oracle":
        data = User(id=rand, username="mz_%d" % rand, grade=rand_)
    else:
        data = User(username="mz_%d" % rand, grade=rand_)

    db.session.add(data)
    db.session.commit()
    return "<h1> %s insert is success</h1>" % sql_type


@sqlalchemy_mysql.route('/sqlalchemy/delete')
def sqlalchemy_mysql_delete():
    """
    :sql: 作为参数传入，控制数据库种类
    :return:
    """
    sql_type = request.args.get("sql")
    ensure_engine(sql_type)

    data = User.query.first()
    db.session.delete(data)
    db.session.commit()
    return "<h1> %s delete is success</h1>" % sql_type


@sqlalchemy_mysql.route('/sqlalchemy/update')
def sqlalchemy_mysql_update():
    """
    :sql: 作为参数传入，控制数据库种类
    :return:
    """
    sql_type = request.args.get("sql")
    ensure_engine(sql_type)

    data = User.query.first()
    data.username = "super_mz"
    db.session.commit()
    return "<h1> %s update is success</h1>" % sql_type


@sqlalchemy_mysql.route('/sqlalchemy/select')
def sqlalchemy_mysql_select():
    """
    :sql: 作为参数传入，控制数据库种类
    :return:
    """
    sql_type = request.args.get("sql")
    ensure_engine(sql_type)

    data = User.query.filter(User.username.notlike("super_mz")).all()
    try:
        username_ = data[0].username
    except:
        username_ = "get None"
    return "<h1> %s select is success \n%s </h1>" % (sql_type, username_)


def ensure_engine(sql_):
    app.config['SQLALCHEMY_DATABASE_URI'] = ENGINE[sql_]
