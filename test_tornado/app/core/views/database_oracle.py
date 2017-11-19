#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.views.base import BaseHandler
from public.db_oracle import db_cx_oracle


class OraclePositionConn(BaseHandler):
    def get(self):
        self.write(db_cx_oracle.oracle_position_conn())


class OracleConnectingConn(BaseHandler):
    def get(self):
        self.write(db_cx_oracle.oracle_connectstring_conn())


class OracleMakesnConn(BaseHandler):
    def get(self):
        self.write(db_cx_oracle.oracle_makedsn_conn())


class OracleInsert(BaseHandler):
    def get(self):
        self.write(db_cx_oracle.oracle_insert())


class OracleDelete(BaseHandler):
    def get(self):
        self.write(db_cx_oracle.oracle_delete())


class OracleUpdate(BaseHandler):
    def get(self):
        self.write(db_cx_oracle.oracle_update())


def oracle_select(BaseHandler):
    """
    :param count: 作为参数传入，控制select操作次数
    :return:
    """
class OracleSelect(BaseHandler):
    def get(self):
        count = self.get_argument("count", 1)
        count = int(count)
        for i in range(count):
            db_cx_oracle.oracle_select()
        self.write("select count is %d" % count)


class OracleFetchOne(BaseHandler):
    def get(self):
        self.write(db_cx_oracle.oracle_fetch_one())


class OracleFetchMany(BaseHandler):
    def get(self):
        self.write(db_cx_oracle.oracle_fetch_many())


class OracleFetchAll(BaseHandler):
    def get(self):
        self.write(db_cx_oracle.oracle_fetch_all())


class OracleExecuteMany(BaseHandler):
    def get(self):
        self.write(db_cx_oracle.oracle_execute_many())


class OracleTableError(BaseHandler):
    def get(self):
        self.write(db_cx_oracle.oracle_table_error())


class OracleFieldError(BaseHandler):
    def get(self):
        self.write(db_cx_oracle.oracle_field_error())


class OracleSyntaxError(BaseHandler):
    def get(self):
        self.write(db_cx_oracle.oracle_syntax_error())


class OracleOperates(BaseHandler):
    def get(self):
        res_1 = db_cx_oracle.oracle_insert()
        res_2 = db_cx_oracle.oracle_delete()
        res_3 = db_cx_oracle.oracle_update()
        res_4 = db_cx_oracle.oracle_select()
        self.write("cx_oracle\ninsert: %s\ndelete: %s\nupdate: %s\nselect: %s" % (res_1, res_2, res_3, res_4))


class OracleConnections(BaseHandler):
    def get(self):
        res_1 = db_cx_oracle.oracle_position_conn()
        res_2 = db_cx_oracle.oracle_connectstring_conn()
        res_3 = db_cx_oracle.oracle_makedsn_conn()
        self.write("cx_oracle\nposition: %s\nconnectstring: %s\nmakedsn: %s" % (res_1, res_2, res_3))
