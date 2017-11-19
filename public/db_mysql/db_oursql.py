# -*- coding: utf-8 -*-


import oursql
from DBUtils.PooledDB import PooledDB
from ..config import MYSQL_CONF
from public.db_util import common_insert_sql, common_delete_sql, common_update_sql, common_insert_many_sql, \
    common_select_sql, common_execute, common_select, common_table_error_sql, common_field_error_sql, \
    common_fetch_one, common_fetch_many, common_fetch_all, common_execute_many, common_syntax_error_sql, \
    diff_common_insert_sql, diff_common_delete_sql, diff_common_update_sql, diff_common_select_sql, common_select_conn

# 关键字参数连接
pool = PooledDB(oursql, host=MYSQL_CONF['host'], port=MYSQL_CONF['port'], user=MYSQL_CONF['name'],
                passwd=MYSQL_CONF['pwd'], db=MYSQL_CONF['db'])
oursql_conn = pool.connection()


def oursql_keyword_connect():
    keyword_conn = oursql.connect(host=MYSQL_CONF['host'], port=MYSQL_CONF['port'], user=MYSQL_CONF['name'],
                                  passwd=MYSQL_CONF['pwd'], db=MYSQL_CONF['db'])
    sql = common_select_sql()
    res = common_select_conn(keyword_conn, sql)
    return res


def oursql_position_connect():
    # 标准位置参数连接
    position_conn = oursql.connect(MYSQL_CONF['host'], MYSQL_CONF['name'], MYSQL_CONF['pwd'],
                                   port=MYSQL_CONF['port'], db=MYSQL_CONF['db'])
    sql = common_select_sql()
    res = common_select_conn(position_conn, sql)
    return res


def oursql_no_port_connect():
    # 省略port
    no_port_conn = oursql.connect(MYSQL_CONF['host'], MYSQL_CONF['name'], MYSQL_CONF['pwd'],
                                  db=MYSQL_CONF['db'])
    sql = common_select_sql()
    res = common_select_conn(no_port_conn, sql)
    return res


def oursql_insert():
    sql = common_insert_sql()
    common_execute(oursql_conn, sql)
    return "success"


def oursql_delete():
    sql = common_delete_sql()
    common_execute(oursql_conn, sql)
    return "success"


def oursql_update():
    sql = common_update_sql()
    common_execute(oursql_conn, sql)
    return "success"


def oursql_select():
    sql = common_select_sql()
    res = common_select(oursql_conn, sql)
    return res


def oursql_fetch_one():
    sql = common_select_sql()
    res = common_fetch_one(oursql_conn, sql)
    return res


def oursql_fetch_many():
    sql = common_select_sql()
    res = common_fetch_many(oursql_conn, sql)
    return res


def oursql_fetch_all():
    sql = common_select_sql()
    res = common_fetch_all(oursql_conn, sql)
    return res
