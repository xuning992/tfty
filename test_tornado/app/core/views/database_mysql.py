#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.views.base import BaseHandler
from public.db_mysql import db_mysqldb, db_pymysql, db_oursql


class MysqldbPositionConnect(BaseHandler):
    def get(self):
        self.write(db_mysqldb.mysqldb_position_conn())


class MysqldbKeyworkConnect(BaseHandler):
    def get(self):
        self.write(db_mysqldb.mysqldb_keyword_connect())


class MysqldbPoolConnect(BaseHandler):
    def get(self):
        self.write(db_mysqldb.mysqldb_pool_connect())


class MysqldbInsert(BaseHandler):
    def get(self):
        self.write(db_mysqldb.mysqldb_insert())


class MysqldbDelete(BaseHandler):
    def get(self):
        self.write(db_mysqldb.mysqldb_delete())


class MysqldbUpdate(BaseHandler):
    def get(self):
        self.write(db_mysqldb.mysqldb_update())


class MysqldbSelect(BaseHandler):
    def get(self):
        count = self.get_argument("count", 1)
        count = int(count)
        for i in range(count):
            db_mysqldb.mysqldb_select()
        self.write("select count is %d" % count)


class MysqldbFetchOne(BaseHandler):
    def get(self):
        self.write(db_mysqldb.mysqldb_fetch_one())


class MysqldbFetchMany(BaseHandler):
    def get(self):
        self.write(db_mysqldb.mysqldb_fetch_many())


class MysqldbFetchAll(BaseHandler):
    def get(self):
        self.write(db_mysqldb.mysqldb_fetch_all())


class MysqldbExecuteMany(BaseHandler):
    def get(self):
        self.write(db_mysqldb.mysqldb_execute_many())


class MysqldbTableError(BaseHandler):
    def get(self):
        self.write(db_mysqldb.mysqldb_table_error())


class MysqldbFieldError(BaseHandler):
    def get(self):
        self.write(db_mysqldb.mysqldb_field_error())


class MysqldbSyntaxError(BaseHandler):
    def get(self):
        self.write(db_mysqldb.mysqldb_syntax_error())


class PymysqlNoPortConnect(BaseHandler):
    def get(self):
        self.write(db_pymysql.pymysql_no_port_connect())


class PymysqlDictConnect(BaseHandler):
    def get(self):
        self.write(db_pymysql.pymysql_dict_conn())


class PymysqlPositionConnect(BaseHandler):
    def get(self):
        self.write(db_pymysql.pymysql_position_connect())


class PymysqlKeywordConnect(BaseHandler):
    def get(self):
        self.write(db_pymysql.pymysql_keyword_connect())


class PymysqlInsert(BaseHandler):
    def get(self):
        self.write(db_pymysql.pymysql_insert())


class PymysqlDelete(BaseHandler):
    def get(self):
        self.write(db_pymysql.pymysql_delete())


class PymysqlUpdate(BaseHandler):
    def get(self):
        self.write(db_pymysql.pymysql_update())


class PymysqlSelect(BaseHandler):
    def get(self):
        self.write(db_pymysql.pymysql_select())


class PymysqlTableError(BaseHandler):
    def get(self):
        self.write(db_pymysql.pymysql_table_error())


class PymysqlFieldError(BaseHandler):
    def get(self):
        self.write(db_pymysql.pymysql_field_error())


class PymysqlSyntaxError(BaseHandler):
    def get(self):
        self.write(db_pymysql.pymysql_syntax_error())


class PymysqlFetchOne(BaseHandler):
    def get(self):
        self.write(db_pymysql.pymysql_fetch_one())


class PymysqlFetchMany(BaseHandler):
    def get(self):
        self.write(db_pymysql.pymysql_fetch_many())


class PymysqlFetchAll(BaseHandler):
    def get(self):
        self.write(db_pymysql.pymysql_fetch_all())


class PymysqlExecuteMany(BaseHandler):
    def get(self):
        self.write(db_pymysql.pymysql_execute_many())


class OursqlKeywordConnect(BaseHandler):
    def get(self):
        self.write(db_oursql.oursql_keyword_connect())


class OursqlPositionConnect(BaseHandler):
    def get(self):
        self.write(db_oursql.oursql_position_connect())


class OursqlNoPortConnect(BaseHandler):
    def get(self):
        self.write(db_oursql.oursql_no_port_connect())


class OursqlInsert(BaseHandler):
    def get(self):
        self.write(db_oursql.oursql_insert())


class OursqlDelete(BaseHandler):
    def get(self):
        self.write(db_oursql.oursql_delete())


class OursqlUpdate(BaseHandler):
    def get(self):
        self.write(db_oursql.oursql_update())


class OursqlSelect(BaseHandler):
    def get(self):
        self.write(db_oursql.oursql_select())


class OursqlFetchOne(BaseHandler):
    def get(self):
        self.write(db_oursql.oursql_fetch_one())


class OursqlFetchMany(BaseHandler):
    def get(self):
        self.write(db_oursql.oursql_fetch_many())


class OursqlFetchAll(BaseHandler):
    def get(self):
        self.write(db_oursql.oursql_fetch_all())


class MysqldbOperates(BaseHandler):
    def get(self):
        res_1 = db_mysqldb.mysqldb_insert()
        res_2 = db_mysqldb.mysqldb_delete()
        res_3 = db_mysqldb.mysqldb_update()
        res_4 = db_mysqldb.mysqldb_select()
        self.write("mysqldb\ninsert: %s\ndelete: %s\nupdate: %s\nselect: %s" % (res_1, res_2, res_3, res_4))


class PymysqlOperates(BaseHandler):
    def get(self):
        res_1 = db_pymysql.pymysql_insert()
        res_2 = db_pymysql.pymysql_delete()
        res_3 = db_pymysql.pymysql_update()
        res_4 = db_pymysql.pymysql_select()
        self.write("pymysql\ninsert: %s\ndelete: %s\nupdate: %s\nselect: %s" % (res_1, res_2, res_3, res_4))


class OursqlOperates(BaseHandler):
    def get(self):
        res_1 = db_oursql.oursql_insert()
        res_2 = db_oursql.oursql_delete()
        res_3 = db_oursql.oursql_update()
        res_4 = db_oursql.oursql_select()
        self.write("oursql\ninsert: %s\ndelete: %s\nupdate: %s\nselect: %s" % (res_1, res_2, res_3, res_4))


class MysqldbConnections(BaseHandler):
    def get(self):
        res_1 = db_mysqldb.mysqldb_keyword_connect()
        res_2 = db_mysqldb.mysqldb_position_conn()
        res_3 = db_mysqldb.mysqldb_pool_connect()
        self.write("mysqldb\nkeyword: %s\nposition: %s\npool: %s" % (res_1, res_2, res_3))


class PymysqlConnections(BaseHandler):
    def get(self):
        res_1 = db_pymysql.pymysql_position_connect()
        res_2 = db_pymysql.pymysql_no_port_connect()
        res_3 = db_pymysql.pymysql_keyword_connect()
        res_4 = db_pymysql.pymysql_dict_conn()
        self.write("pymysql\nposition: %s\nno_port: %s\nkeyword: %s\ndict: %s" % (res_1, res_2, res_3, res_4))


class OursqlConnections(BaseHandler):
    def get(self):
        res_1 = db_oursql.oursql_position_connect()
        res_2 = db_oursql.oursql_keyword_connect()
        res_3 = db_oursql.oursql_no_port_connect()
        self.write("pymsql\nposition: %s\nkeyword: %s\nno_port: %s" % (res_1, res_2, res_3))
