#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Blueprint, request
from public.db_oracle import db_cx_oracle


db_oracle_blueprint = Blueprint(__name__, __name__)


@db_oracle_blueprint.route('/db/oracle/position-conn/')
def oracle_position_conn():
    return db_cx_oracle.oracle_position_conn()


@db_oracle_blueprint.route('/db/oracle/connecting-conn/')
def oracle_connecting_conn():
    return db_cx_oracle.oracle_connectstring_conn()


@db_oracle_blueprint.route('/db/oracle/makedsn-conn/')
def oracle_makedsn_conn():
    return db_cx_oracle.oracle_makedsn_conn()


@db_oracle_blueprint.route("/db/oracle/insert/")
def oracle_insert():
    return db_cx_oracle.oracle_insert()


@db_oracle_blueprint.route("/db/oracle/delete/")
def oracle_delete():
    return db_cx_oracle.oracle_delete()


@db_oracle_blueprint.route("/db/oracle/update/")
def oracle_update():
    return db_cx_oracle.oracle_update()


@db_oracle_blueprint.route("/db/oracle/select/")
def oracle_select():
    """
    :param count: 作为参数传入，控制select操作次数
    :return:
    """
    count = request.args.get("count")
    if not count:
        count = 1

    count = int(count)
    for i in range(count):
        db_cx_oracle.oracle_select()
    return "select count is %d" % count


@db_oracle_blueprint.route("/db/oracle/fetch-one/")
def oracle_fetch_one():
    return db_cx_oracle.oracle_fetch_one()


@db_oracle_blueprint.route("/db/oracle/fetch-many/")
def oracle_fetch_many():
    return db_cx_oracle.oracle_fetch_many()


@db_oracle_blueprint.route("/db/oracle/fetch-all/")
def oracle_fetch_all():
    return db_cx_oracle.oracle_fetch_all()


@db_oracle_blueprint.route("/db/oracle/execute-many/")
def oracle_execute_many():
    return db_cx_oracle.oracle_execute_many()


@db_oracle_blueprint.route("/db/oracle/table-error/")
def oracle_table_error():
    return db_cx_oracle.oracle_table_error()


@db_oracle_blueprint.route("/db/oracle/field-error/")
def oracle_field_error():
    return db_cx_oracle.oracle_field_error()


@db_oracle_blueprint.route('/db/oracle/syntax-error/')
def oracle_syntax_error():
    return db_cx_oracle.oracle_syntax_error()


@db_oracle_blueprint.route("/db/oracle/operates/")
def oracle_operates():
    res_1 = db_cx_oracle.oracle_insert()
    res_2 = db_cx_oracle.oracle_delete()
    res_3 = db_cx_oracle.oracle_update()
    res_4 = db_cx_oracle.oracle_select()
    return "cx_oracle\ninsert: %s\ndelete: %s\nupdate: %s\nselect: %s" % (res_1, res_2, res_3, res_4)


@db_oracle_blueprint.route("/db/oracle/connections/")
def oracle_connections():
    res_1 = db_cx_oracle.oracle_position_conn()
    res_2 = db_cx_oracle.oracle_connectstring_conn()
    res_3 = db_cx_oracle.oracle_makedsn_conn()
    return "cx_oracle\nposition: %s\nconnectstring: %s\nmakedsn: %s" % (res_1, res_2, res_3)
