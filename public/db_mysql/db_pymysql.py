#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pymysql
from DBUtils.PooledDB import PooledDB
from public.db_util import common_insert_sql, common_insert_many_sql, common_delete_sql, common_update_sql,\
    common_select_sql, common_execute, common_select, common_table_error_sql, common_field_error_sql,\
    common_fetch_one, common_fetch_many, common_fetch_all, common_execute_many, common_syntax_error_sql, \
    common_select_conn
from ..config import MYSQL_CONF

pool = PooledDB(pymysql, 1, host=MYSQL_CONF['host'], port=MYSQL_CONF['port'], user=MYSQL_CONF['name'],
                passwd=MYSQL_CONF['pwd'], db=MYSQL_CONF['db'])
try:
    pymysql_conn = pool.connection()
except Exception as err:
    pymysql_conn = pymysql.connect(MYSQL_CONF['host'], MYSQL_CONF['name'], MYSQL_CONF['pwd'], MYSQL_CONF['db'])


def pymysql_dict_conn():
    connection_param = {
        'host': MYSQL_CONF['host'],
        'port': MYSQL_CONF['port'],
        'user': MYSQL_CONF['name'],
        # 0.7.9
        # 'password': MYSQL_CONF['pwd'],
        # 0.6
        'passwd': MYSQL_CONF['pwd'],

        'db': MYSQL_CONF['db']
    }

    dict_conn = pymysql.connect(**connection_param)
    sql = common_select_sql()
    res = common_select_conn(dict_conn, sql)
    return res


def pymysql_no_port_connect():
    no_port_conn = pymysql.connect(MYSQL_CONF['host'], MYSQL_CONF['name'], MYSQL_CONF['pwd'], MYSQL_CONF['db'])
    sql = common_select_sql()
    res = common_select_conn(no_port_conn, sql)
    return res


def pymysql_position_connect():
    position_conn = pymysql.connect(MYSQL_CONF['host'], MYSQL_CONF['name'], MYSQL_CONF['pwd'],
                                    MYSQL_CONF['db'], MYSQL_CONF['port'])
    sql = common_select_sql()
    res = common_select_conn(position_conn, sql)
    return res


def pymysql_keyword_connect():
    keyword_conn = pymysql.connect(host=MYSQL_CONF['host'], port=MYSQL_CONF['port'], user=MYSQL_CONF['name'],
                               passwd=MYSQL_CONF['pwd'], db=MYSQL_CONF['db'])
    sql = common_select_sql()
    res = common_select(keyword_conn, sql)
    return res


def pymysql_insert():
    sql = common_insert_sql()
    common_execute(pymysql_conn, sql)
    return "success"


def pymysql_delete():
    sql = common_delete_sql()
    common_execute(pymysql_conn, sql)
    return "success"


def pymysql_update():
    sql = common_update_sql()
    common_execute(pymysql_conn, sql)
    return "success"


def pymysql_select():
    sql = common_select_sql()
    res = common_select(pymysql_conn, sql)
    return res


def pymysql_table_error():
    sql = common_table_error_sql()
    res = common_select(pymysql_conn, sql)
    return res


def pymysql_field_error():
    sql = common_field_error_sql()
    res = common_select(pymysql_conn, sql)
    return res


def pymysql_syntax_error():
    sql = common_syntax_error_sql()
    res = common_execute(pymysql_conn, sql)
    return res


def pymysql_fetch_one():
    sql = common_select_sql()
    res = common_fetch_one(pymysql_conn, sql)
    return res


def pymysql_fetch_many():
    sql = common_select_sql()
    res = common_fetch_many(pymysql_conn, sql)
    return res


def pymysql_fetch_all():
    sql = common_select_sql()
    res = common_fetch_all(pymysql_conn, sql)
    return res


def pymysql_execute_many():
    sql, data = common_insert_many_sql()
    common_execute_many(pymysql_conn, sql, data)
    return 'success'