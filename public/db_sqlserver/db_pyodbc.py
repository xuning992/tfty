#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyodbc
from public.db_util import common_insert_sql, common_sqlserver_insert_many_sql, common_delete_sql, common_update_sql,\
    common_select_sql, common_execute, common_select, common_table_error_sql, common_field_error_sql,\
    common_fetch_one, common_fetch_many, common_fetch_all, common_execute_many, common_syntax_error_sql, \
    common_select_conn
from ..config import SQL_SERVER_CONF

# SQL Server Native Client 11.0
driver = 'DRIVER={FreeTDS};SERVER=%s,%s;DATABASE=%s;UID=%s;PWD=%s;TDS_Version=%s' % \
        (SQL_SERVER_CONF['host'], SQL_SERVER_CONF['port'], SQL_SERVER_CONF['db'], SQL_SERVER_CONF['name'],
         SQL_SERVER_CONF['pwd'], SQL_SERVER_CONF['tds_version'])

conn = pyodbc.connect(driver)


def sqlserver_keyword_connect():
    driver_ = 'DRIVER={FreeTDS};SERVER=%s;PORT=%s;DATABASE=%s;UID=%s;PWD=%s' %\
            (SQL_SERVER_CONF['host'], SQL_SERVER_CONF['port'], SQL_SERVER_CONF['db'], SQL_SERVER_CONF['name'],
             SQL_SERVER_CONF['pwd'])
    keyword_conn = pyodbc.connect(driver_)
    sql = common_select_sql()
    res = common_select_conn(keyword_conn, sql)
    return res


def sqlserver_dsn_connect():
    driver_ = ''


def sqlserver_server_connect():
    sql = common_select_sql()
    res = common_select(conn, sql)
    return res


def sqlserver_insert():
    sql = common_insert_sql()
    common_execute(conn, sql)
    return "success"


def sqlserver_delete():
    sql = common_delete_sql()
    common_execute(conn, sql)
    return "success"


def sqlserver_update():
    sql = common_update_sql()
    common_execute(conn, sql)
    return "success"


def sqlserver_select():
    sql = common_select_sql()
    res = common_select(conn, sql)
    return res


def sqlserver_fetch_one():
    sql = common_select_sql()
    res = common_fetch_one(conn, sql)
    return res


def sqlserver_fetch_many():
    sql = common_select_sql()
    res = common_fetch_many(conn, sql)
    return res


def sqlserver_fetch_all():
    sql = common_select_sql()
    res = common_fetch_all(conn, sql)
    return res


def sqlserver_execute_many():
    sql, data = common_sqlserver_insert_many_sql()
    common_execute_many(conn, sql, data)
    return 'success'


def sqlserver_table_error():
    sql = common_table_error_sql()
    res = common_select(conn, sql)
    return res


def sqlserver_field_error():
    sql = common_field_error_sql()
    res = common_select(conn, sql)
    return res


def sqlserver_syntax_error():
    sql = common_syntax_error_sql()
    res = common_execute(conn, sql)
    return res

