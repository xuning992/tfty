#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cx_Oracle

from public.db_util import common_insert_sql, common_oracle_insert_many_sql, common_delete_sql, common_update_sql,\
        common_select_sql, common_execute, common_select, common_table_error_sql, common_field_error_sql,\
        common_fetch_one, common_fetch_many, common_fetch_all, common_execute_many, common_syntax_error_sql, \
        common_select_conn
from ..config import ORACLE_CONF


# oracle_uri = '%s:%s/%s' % (ORACLE_CONF['host'], ORACLE_CONF['port'], ORACLE_CONF['xe'])
# position_conn = cx_Oracle.connect(ORACLE_CONF['name'], ORACLE_CONF['pwd'], oracle_uri)


class OracleConnect():

    def __init__(self):
        self.oracle_uri = '%s:%s/%s' % (ORACLE_CONF['host'], ORACLE_CONF['port'], ORACLE_CONF['xe'])

    def __enter__(self):
        self.position_conn = cx_Oracle.connect(ORACLE_CONF['name'], ORACLE_CONF['pwd'], self.oracle_uri)
        return self.position_conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.position_conn.close()


def oracle_position_conn():
    with OracleConnect() as conn:
        sql = common_select_sql()
        res = common_select(conn, sql)
        return res


def oracle_connectstring_conn():
    connectstring_conn = cx_Oracle.connect("%s/%s@%s:%s/%s" % (ORACLE_CONF['name'], ORACLE_CONF['pwd'], ORACLE_CONF['host'],
                                                           ORACLE_CONF['port'], ORACLE_CONF['xe']))
    sql = common_select_sql()
    res = common_select_conn(connectstring_conn, sql)
    return res


def oracle_makedsn_conn():
    makedsn_conn = cx_Oracle.connect(ORACLE_CONF['name'], ORACLE_CONF['pwd'], cx_Oracle.makedsn(ORACLE_CONF['host'],
                                                                                            ORACLE_CONF['port'],
                                                                                            ORACLE_CONF['xe']))
    sql = common_select_sql()
    res = common_select_conn(makedsn_conn, sql)
    return res


def oracle_insert():
    with OracleConnect() as conn:
        sql = common_insert_sql()
        common_execute(conn, sql)
        return "success"


def oracle_delete():
    with OracleConnect() as conn:
        sql = common_delete_sql()
        common_execute(conn, sql)
        return "success"


def oracle_update():
    with OracleConnect() as conn:
        sql = common_update_sql()
        common_execute(conn, sql)
        return "success"


def oracle_select():
    with OracleConnect() as conn:
        sql = common_select_sql()
        res = common_select(conn, sql)
        return res


def oracle_fetch_one():
    with OracleConnect() as conn:
        sql = common_select_sql()
        res = common_fetch_one(conn, sql)
        return res


def oracle_fetch_many():
    with OracleConnect() as conn:
        sql = common_select_sql()
        res = common_fetch_many(conn, sql)
        return res


def oracle_fetch_all():
    with OracleConnect() as conn:
        sql = common_select_sql()
        res = common_fetch_all(conn, sql)
        return res


def oracle_execute_many():
    with OracleConnect() as conn:
        sql, data = common_oracle_insert_many_sql()
        common_execute_many(conn, sql, data)
        return 'success'


def oracle_table_error():
    with OracleConnect() as conn:
        sql = common_table_error_sql()
        res = common_select(conn, sql)
        return res


def oracle_field_error():
    with OracleConnect() as conn:
        sql = common_field_error_sql()
        res = common_select(conn, sql)
        return res


def oracle_syntax_error():
    with OracleConnect() as conn:
        sql = common_syntax_error_sql()
        res = common_execute(conn, sql)
        return res
