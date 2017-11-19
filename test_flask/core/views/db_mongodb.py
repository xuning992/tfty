#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Blueprint, request
from public.db_mongo import db_pymongo
# from pymongo import MongoClient


db_mongodb_blueprint = Blueprint(__name__, __name__)


@db_mongodb_blueprint.route("/db/mongodb/insert/")
def mongodb_insert():
    """
    :ver: 作为参数传入，区分版本号
    :return:
    """
    version = request.args.get("ver", "3.4.0")

    return db_pymongo.mongodb_insert(version)


@db_mongodb_blueprint.route("/db/mongodb/delete/")
def mongodb_delete():
    """
    :ver: 作为参数传入，区分版本号
    :return:
    """
    version = request.args.get("ver", "3.4.0")
    return db_pymongo.mongodb_delete(version)


@db_mongodb_blueprint.route("/db/mongodb/update/")
def mongodb_update():
    """
    :ver: 作为参数传入，区分版本号
    :return:
    """
    version = request.args.get("ver", "3.4.0")
    return db_pymongo.mongodb_update(version)


@db_mongodb_blueprint.route("/db/mongodb/select/")
def mongodb_select():
    """
    :ver: 作为参数传入，区分版本号
    :return:
    """
    version = request.args.get("ver", "3.4.0")
    return db_pymongo.mongodb_select(version)


@db_mongodb_blueprint.route("/db/mongodb/conn/connection/")
def mongodb_conn_def():
    """
    :ver: 作为参数传入，区分版本号
    :return:
    """
    version = request.args.get("ver", "3.4.0")
    return db_pymongo.mongodb_conn_by_connection(version)


@db_mongodb_blueprint.route("/db/mongodb/conn/mongoclient/params/")
def mongodb_conn_params():
    """
    :ver: 作为参数传入，区分版本号
    :return:
    """
    version = request.args.get("ver", "3.4.0")
    return db_pymongo.mongodb_conn_by_mongoclient_params(version)


@db_mongodb_blueprint.route("/db/mongodb/conn/mongoclient/str/")
def mongodb_conn_str():
    """
    :ver: 作为参数传入，区分版本号
    :return:
    """
    version = request.args.get("ver", "3.4.0")
    return db_pymongo.mongodb_conn_by_mongoclient_str(version)
