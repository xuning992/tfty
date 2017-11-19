#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.views.base import BaseHandler
from public.db_mongo import db_pymongo


class MongodbInsert(BaseHandler):
    """
    :ver: 作为参数传入，区分版本号
    :return:
    """
    def get(self):
        version = self.get_argument("ver", "3.4.0")
        self.write(db_pymongo.mongodb_insert(version))


class MongodbDelete(BaseHandler):
    """
    :ver: 作为参数传入，区分版本号
    :return:
    """
    def get(self):
        version = self.get_argument("ver", "3.4.0")
        self.write(db_pymongo.mongodb_delete(version))


class MongodbUpdate(BaseHandler):
    """
    :ver: 作为参数传入，区分版本号
    :return:
    """
    def get(self):
        version = self.get_argument("ver", "3.4.0")
        self.write(db_pymongo.mongodb_update(version))


class MongodbSelect(BaseHandler):
    """
    :ver: 作为参数传入，区分版本号
    :return:
    """
    def get(self):
        version = self.get_argument("ver", "3.4.0")
        self.write(db_pymongo.mongodb_select(version))


class MongodbConnClass(BaseHandler):
    """
    :ver: 作为参数传入，区分版本号
    :return:
    """
    def get(self):
        version = self.get_argument("ver", "3.4.0")
        self.write(db_pymongo.mongodb_conn_by_connection(version))


class MongodbConnParams(BaseHandler):
    """
    :ver: 作为参数传入，区分版本号
    :return:
    """
    def get(self):
        version = self.get_argument("ver", "3.4.0")
        self.write(db_pymongo.mongodb_conn_by_mongoclient_params(version))


class MongodbConnStr(BaseHandler):
    """
    :ver: 作为参数传入，区分版本号
    :return:
    """
    def get(self):
        version = self.get_argument("ver", "3.4.0")
        self.write(db_pymongo.mongodb_conn_by_mongoclient_str(version))
