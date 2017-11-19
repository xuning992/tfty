# -*- coding: utf-8 -*-

import psycopg2ct
import psycopg2ct.pool

from public.db_util import (
    common_insert_sql, common_update_sql, common_select_sql, common_delete_sql, common_table_error_sql, common_select,
    common_execute, psycopg2_timeout_sql, psycopg2_sleep_sql, common_field_error_sql, common_syntax_error_sql,
    common_select_conn)
from ..config import PG_CONF


conn = psycopg2ct.connect(
    host=PG_CONF['host'], port=PG_CONF['port'], user=PG_CONF['user'], password=PG_CONF['password'],
    database=PG_CONF['database'])

conn_pool = psycopg2ct.pool.SimpleConnectionPool(
    minconn=PG_CONF['minconn'], maxconn=PG_CONF['maxconn'], host=PG_CONF['host'], port=PG_CONF['port'],
    user=PG_CONF['user'], password=PG_CONF['password'], database=PG_CONF['database'])


conn_pool = conn_pool.getconn()


def psycopg2ct_no_support_connect():
    conn_no_support = psycopg2ct.connect("postgresql:///%s?host=%s&port=%s&user=%s&password=%s" % (PG_CONF['database'], PG_CONF['host'], PG_CONF['port'], PG_CONF['user'], PG_CONF['password']))
    sql = common_select_sql()
    res = common_select(conn_no_support, sql)
    return res


def psycopg2ct_no_support_connect_two():
    conn_no_support_two = psycopg2ct.connect("postgresql://%s:%s@[%s]:%s/%s" % (PG_CONF['user'], PG_CONF['password'],
                                            PG_CONF['IPv6_address'], PG_CONF['port'], PG_CONF['database']))
    sql = common_select_sql()
    res = common_select(conn_no_support_two, sql)
    return res


def psycopg2ct_database_connect():
    conn_database = psycopg2ct.connect(host=PG_CONF['host'], port=PG_CONF['port'], user=PG_CONF['user'],
                                       password=PG_CONF['password'], database=PG_CONF['database'])
    sql = common_select_sql()
    res = common_select_conn(conn_database, sql)
    return res


def psycopg2ct_uri_connect():
    conn_uri = psycopg2ct.connect("postgresql://%s:%s@%s:%s/%s" % (PG_CONF['user'], PG_CONF['password'],
                                                                 PG_CONF['host'], PG_CONF['port'],
                                                                 PG_CONF['database']))
    sql = common_select_sql()
    res = common_select_conn(conn_uri, sql)
    return res


def psycopg2ct_uri_no_port_connect():
    conn_uri_no_port = psycopg2ct.connect("postgresql://%s:%s@%s/%s" % (PG_CONF['user'], PG_CONF['password'],
                                                                      PG_CONF['host'], PG_CONF['database']))
    sql = common_select_sql()
    res = common_select_conn(conn_uri_no_port, sql)
    return res


def psycopg2ct_connectstring_no_port_connect():
    conn_connectstring = psycopg2ct.connect("dbname=%s user=%s password=%s host=%s" % (PG_CONF['database'],
                                                                PG_CONF['user'], PG_CONF['password'], PG_CONF['host']))
    sql = common_select_sql()
    res = common_select_conn(conn_connectstring, sql)
    return res


def psycopg2ct_connectstring_connect():
    conn_connectstring = psycopg2ct.connect("dbname=%s user=%s password=%s host=%s port=%s" % (PG_CONF['database'],
                                                                PG_CONF['user'], PG_CONF['password'], PG_CONF['host'],
                                                                PG_CONF['port']))
    sql = common_select_sql()
    res = common_select_conn(conn_connectstring, sql)
    return res


def psycopg2ct_dbname_connect():
    conn_dbname = psycopg2ct.connect(host=PG_CONF['host'], port=PG_CONF['port'], user=PG_CONF['user'],
                                     password=PG_CONF['password'], dbname=PG_CONF['database'])
    sql = common_select_sql()
    res = common_select_conn(conn_dbname, sql)
    return res


def psycopg2ct_no_port_connect():
    conn_no_port = psycopg2ct.connect(host=PG_CONF['host'], user=PG_CONF['user'], password=PG_CONF['password'],
                                      database=PG_CONF['database'])
    sql = common_select_sql()
    res = common_select_conn(conn_no_port, sql)
    return res


def test_psycopg2ct_insert():
    sql = common_insert_sql()
    common_execute(conn, sql)
    return 'test_psycopg2ct_insert ok'


def test_psycopg2ct_update():
    sql = common_update_sql()
    common_execute(conn, sql)
    return 'test_psycopg2ct_update ok'


def test_psycopg2ct_select():
    sql = common_select_sql()
    common_execute(conn, sql)
    return 'test_psycopg2ct_select ok'


def test_psycopg2ct_delete():
    sql = common_delete_sql()
    common_execute(conn, sql)
    return 'test_psycopg2ct_delete ok'


def test_psycopg2ct_connection_pool():
    sql = common_insert_sql()
    common_execute(conn_pool, sql)
    return 'test_psycopg2ct_connection_pool ok'


def test_psycopg2ct_timeout_error():
    try:
        common_execute(conn, psycopg2_timeout_sql(2000))
        common_execute(conn, psycopg2_sleep_sql(4))
        return 'test_psycopg2ct_timeout_error ok'
    except Exception:
        _start_new_connection()
        raise


def test_psycopg2ct_table_error():
    sql = common_table_error_sql()
    common_execute(conn, sql)
    return "psycopg2ct table error"


def test_psycopg2ct_field_error():
    sql = common_field_error_sql()
    common_execute(conn, sql)
    return "psycopg2ct field error"


def test_psycopg2ct_syntax_error():
    sql = common_syntax_error_sql()
    common_execute(conn, sql)
    return "psycopg2ct syntax error"


def test_psycopg2ct_timeout_ok():
    common_execute(conn, psycopg2_timeout_sql(2000))
    common_execute(conn, psycopg2_sleep_sql(1))
    return 'test_psycopg2ct_timeout_ok ok'


def _start_new_connection():
    global conn
    global conn_pool
    global conn_pool
    conn = psycopg2ct.connect(
        host=PG_CONF['host'], port=PG_CONF['port'], user=PG_CONF['user'], password=PG_CONF['password'],
        database=PG_CONF['database'])
    conn_pool = psycopg2ct.pool.SimpleConnectionPool(
        minconn=PG_CONF['minconn'], maxconn=PG_CONF['maxconn'], host=PG_CONF['host'], port=PG_CONF['port'],
        user=PG_CONF['user'], password=PG_CONF['password'], database=PG_CONF['database'])
    conn_pool = conn_pool.getconn()


