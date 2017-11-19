#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
from DBUtils.PooledDB import PooledDB
from public.db_util import common_insert_sql, common_insert_many_sql, common_delete_sql, common_update_sql,\
    common_select_sql, common_execute, common_select, common_table_error_sql, common_field_error_sql,\
    common_fetch_one, common_fetch_many, common_fetch_all, common_execute_many, common_syntax_error_sql,\
    diff_common_insert_sql, diff_common_delete_sql, diff_common_update_sql, diff_common_select_sql, common_select_conn
from ..config import MYSQL_CONF

pool = PooledDB(MySQLdb, 1, host=MYSQL_CONF['host'], user=MYSQL_CONF['name'],
                passwd=MYSQL_CONF['pwd'], port=MYSQL_CONF['port'], db=MYSQL_CONF['db'])

mysqldb_conn = pool.connection()


def mysqldb_keyword_connect():
    keyword_conn = MySQLdb.connect(host=MYSQL_CONF['host'], user=MYSQL_CONF['name'],
                                   passwd=MYSQL_CONF['pwd'], port=MYSQL_CONF['port'], db=MYSQL_CONF['db'])
    sql = common_select_sql()
    res = common_select_conn(keyword_conn, sql)
    return res


def mysqldb_position_conn():
    position_conn = MySQLdb.connect(MYSQL_CONF['host'], MYSQL_CONF['name'], MYSQL_CONF['pwd'], MYSQL_CONF['db'])
    sql = common_select_sql()
    res = common_select_conn(position_conn, sql)
    return res


def mysqldb_pool_connect():
    sql = common_select_sql()
    res = common_select(mysqldb_conn, sql)
    return res


def mysqldb_diff_insert():
    sql = diff_common_insert_sql()
    common_execute(mysqldb_conn, sql)
    return "diff insert"


def mysqldb_diff_update():
    sql = diff_common_update_sql()
    common_execute(mysqldb_conn, sql)
    return "diff update"


def mysqldb_diff_delete():
    sql = diff_common_delete_sql()
    common_execute(mysqldb_conn, sql)
    return "diff delete"


def mysqldb_diff_select():
    sql = diff_common_select_sql()
    common_execute(mysqldb_conn, sql)
    return "diff delete"


def mysqldb_insert():
    sql = common_insert_sql()
    common_execute(mysqldb_conn, sql)
    return "success"


def mysqldb_delete():
    sql = common_delete_sql()
    common_execute(mysqldb_conn, sql)
    return "success"


def mysqldb_update():
    sql = common_update_sql()
    common_execute(mysqldb_conn, sql)
    return "success"


def mysqldb_select():
    sql = common_select_sql()
    res = common_select(mysqldb_conn, sql)
    return res


def mysqldb_fetch_one():
    sql = common_select_sql()
    res = common_fetch_one(mysqldb_conn, sql)
    return res


def mysqldb_fetch_many():
    sql = common_select_sql()
    res = common_fetch_many(mysqldb_conn, sql)
    return res


def mysqldb_fetch_all():
    sql = common_select_sql()
    res = common_fetch_all(mysqldb_conn, sql)
    return res


def mysqldb_execute_many():
    sql, data = common_insert_many_sql()
    common_execute_many(mysqldb_conn, sql, data)
    return 'success'


def mysqldb_table_error():
    sql = common_table_error_sql()
    res = common_select(mysqldb_conn, sql)
    return res


def mysqldb_field_error():
    sql = common_field_error_sql()
    res = common_select(mysqldb_conn, sql)
    return res


def mysqldb_syntax_error():
    sql = common_syntax_error_sql()
    res = common_execute(mysqldb_conn, sql)
    return res


