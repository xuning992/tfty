#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, request
from public.db_mysql import db_mysqldb, db_pymysql, db_oursql

db_mysql_blueprint = Blueprint(__name__, __name__)


@db_mysql_blueprint.route('/db/mysql/mysqldb-position-connect/')
def mysqldb_position_connect():
    return db_mysqldb.mysqldb_position_conn()


@db_mysql_blueprint.route('/db/mysql/mysqldb-keyword-connect/')
def mysqldb_keyword_connect():
    return db_mysqldb.mysqldb_keyword_connect()


@db_mysql_blueprint.route('/db/mysql/mysqldb-pool-connect/')
def mysqldb_pool_connect():
    return db_mysqldb.mysqldb_pool_connect()


@db_mysql_blueprint.route("/db/mysql/mysqldb-insert/")
def mysqldb_insert():
    return db_mysqldb.mysqldb_insert()


@db_mysql_blueprint.route("/db/mysql/mysqldb-delete/")
def mysqldb_delete():
    return db_mysqldb.mysqldb_delete()


@db_mysql_blueprint.route("/db/mysql/mysqldb-update/")
def mysqldb_update():
    return db_mysqldb.mysqldb_update()


@db_mysql_blueprint.route("/db/mysql/mysqldb-select/")
def mysqldb_select():
    """
    :param count: 作为参数传入，控制执行select操作次数
    :return:
    """
    count = request.args.get("count")
    if not count:
        count = 1

    count = int(count)
    for i in range(count):
        db_mysqldb.mysqldb_select()
    return "select count is %d" % count


@db_mysql_blueprint.route("/db/mysql/mysqldb-fetch-one/")
def mysqldb_fetch_one():
    return db_mysqldb.mysqldb_fetch_one()


@db_mysql_blueprint.route("/db/mysql/mysqldb-fetch-many/")
def mysqldb_fetch_many():
    return db_mysqldb.mysqldb_fetch_many()


@db_mysql_blueprint.route("/db/mysql/mysqldb-fetch-all/")
def mysqldb_fetch_all():
    return db_mysqldb.mysqldb_fetch_all()


@db_mysql_blueprint.route("/db/mysql/mysqldb-execute-many/")
def mysqldb_execute_many():
    return db_mysqldb.mysqldb_execute_many()


@db_mysql_blueprint.route("/db/mysql/mysqldb-table-error/")
def mysqldb_table_error():
    return db_mysqldb.mysqldb_table_error()


@db_mysql_blueprint.route("/db/mysql/mysqldb-field-error/")
def mysqldb_field_error():
    return db_mysqldb.mysqldb_field_error()


@db_mysql_blueprint.route('/db/mysql/mysqldb-syntax-error/')
def mysqldb_syntax_error():
    return db_mysqldb.mysqldb_syntax_error()


@db_mysql_blueprint.route('/db/mysql/pymysql-no-port-connect/')
def pymysql_no_port_connect():
    return db_pymysql.pymysql_no_port_connect()


@db_mysql_blueprint.route('/db/mysql/pymysql-dict-connect/')
def pymysql_dict_connect():
    return db_pymysql.pymysql_dict_conn()


@db_mysql_blueprint.route('/db/mysql/pymysql-position-connect/')
def pymysql_position_connect():
    return db_pymysql.pymysql_position_connect()


@db_mysql_blueprint.route('/db/mysql/pymysql-keyword-connect/')
def pymysql_keyword_connect():
    return db_pymysql.pymysql_keyword_connect()


@db_mysql_blueprint.route("/db/mysql/pymysql-insert/")
def pymysql_insert():
    return db_pymysql.pymysql_insert()


@db_mysql_blueprint.route("/db/mysql/pymysql-delete/")
def pymysql_delete():
    return db_pymysql.pymysql_delete()


@db_mysql_blueprint.route("/db/mysql/pymysql-update/")
def pymysql_update():
    return db_pymysql.pymysql_update()


@db_mysql_blueprint.route("/db/mysql/pymysql-select/")
def pymysql_select():
    return db_pymysql.pymysql_select()


@db_mysql_blueprint.route("/db/mysql/pymysql-table-error/")
def pymysql_table_error():
    return db_pymysql.pymysql_table_error()


@db_mysql_blueprint.route("/db/mysql/pymysql-field-error/")
def pymysql_field_error():
    return db_pymysql.pymysql_field_error()


@db_mysql_blueprint.route('/db/mysql/pymysql-syntax-error/')
def pymysql_syntax_error():
    return db_pymysql.pymysql_syntax_error()


@db_mysql_blueprint.route("/db/mysql/pymysql-fetch-one/")
def pymysql_fetch_one():
    return db_pymysql.pymysql_fetch_one()


@db_mysql_blueprint.route("/db/mysql/pymysql-fetch-many/")
def pymysql_fetch_many():
    return db_pymysql.pymysql_fetch_many()


@db_mysql_blueprint.route("/db/mysql/pymysql-fetch-all/")
def pymysql_fetch_all():
    return db_pymysql.pymysql_fetch_all()


@db_mysql_blueprint.route("/db/mysql/pymysql-execute-many/")
def pymysql_execute_many():
    return db_pymysql.pymysql_execute_many()


@db_mysql_blueprint.route("/db/mysql/oursql-keyword-connect/")
def oursql_keyword_connect():
    return db_oursql.oursql_keyword_connect()


@db_mysql_blueprint.route("/db/mysql/oursql-position-connect/")
def oursql_position_connect():
    return db_oursql.oursql_position_connect()


@db_mysql_blueprint.route("/db/mysql/oursql-no-port-connect/")
def oursql_no_port_connect():
    return db_oursql.oursql_no_port_connect()


@db_mysql_blueprint.route("/db/mysql/oursql-insert/")
def oursql_insert():
    return db_oursql.oursql_insert()


@db_mysql_blueprint.route("/db/mysql/oursql-delete/")
def oursql_delete():
    return db_oursql.oursql_delete()


@db_mysql_blueprint.route("/db/mysql/oursql-update/")
def oursql_update():
    return db_oursql.oursql_update()


@db_mysql_blueprint.route("/db/mysql/oursql-select/")
def oursql_select():
    return db_oursql.oursql_select()


@db_mysql_blueprint.route("/db/mysql/oursql-fetch-one/")
def oursql_fetch_one():
    return db_oursql.oursql_fetch_one()


@db_mysql_blueprint.route("/db/mysql/oursql-fetch-many/")
def oursql_fetch_many():
    return db_oursql.oursql_fetch_many()


@db_mysql_blueprint.route("/db/mysql/oursql-fetch-all/")
def oursql_fetch_all():
    return db_oursql.oursql_fetch_all()


@db_mysql_blueprint.route("/db/mysql/mysqldb-operates/")
def mysqldb_operates():
    res_1 = db_mysqldb.mysqldb_insert()
    res_2 = db_mysqldb.mysqldb_delete()
    res_3 = db_mysqldb.mysqldb_update()
    res_4 = db_mysqldb.mysqldb_select()
    return "mysqldb\ninsert: %s\ndelete: %s\nupdate: %s\nselect: %s" % (res_1, res_2, res_3, res_4)


@db_mysql_blueprint.route("/db/mysql/pymysql-operates/")
def pymysql_operates():
    res_1 = db_pymysql.pymysql_insert()
    res_2 = db_pymysql.pymysql_delete()
    res_3 = db_pymysql.pymysql_update()
    res_4 = db_pymysql.pymysql_select()
    return "pymysql\ninsert: %s\ndelete: %s\nupdate: %s\nselect: %s" % (res_1, res_2, res_3, res_4)


@db_mysql_blueprint.route("/db/mysql/oursql-operates/")
def oursql_operates():
    res_1 = db_oursql.oursql_insert()
    res_2 = db_oursql.oursql_delete()
    res_3 = db_oursql.oursql_update()
    res_4 = db_oursql.oursql_select()
    return "oursql\ninsert: %s\ndelete: %s\nupdate: %s\nselect: %s" % (res_1, res_2, res_3, res_4)


@db_mysql_blueprint.route("/db/mysql/mysqldb-connections/")
def mysqldb_connections():
    res_1 = db_mysqldb.mysqldb_keyword_connect()
    res_2 = db_mysqldb.mysqldb_position_conn()
    res_3 = db_mysqldb.mysqldb_pool_connect()
    return "mysqldb\nkeyword: %s\nposition: %s\npool: %s" % (res_1, res_2, res_3)


@db_mysql_blueprint.route("/db/mysql/pymysql-connections/")
def pymysql_connections():
    res_1 = db_pymysql.pymysql_position_connect()
    res_2 = db_pymysql.pymysql_no_port_connect()
    res_3 = db_pymysql.pymysql_keyword_connect()
    res_4 = db_pymysql.pymysql_dict_conn()
    return "pymysql\nposition: %s\nno_port: %s\nkeyword: %s\ndict: %s" % (res_1, res_2, res_3, res_4)


@db_mysql_blueprint.route("/db/mysql/oursql-connections/")
def oursql_connections():
    res_1 = db_oursql.oursql_position_connect()
    res_2 = db_oursql.oursql_keyword_connect()
    res_3 = db_oursql.oursql_no_port_connect()
    return "pymsql\nposition: %s\nkeyword: %s\nno_port: %s" % (res_1, res_2, res_3)
