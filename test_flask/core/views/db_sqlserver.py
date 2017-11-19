#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Blueprint
from public.db_sqlserver import db_pyodbc


db_sqlserver_blueprint = Blueprint(__name__, __name__)


@db_sqlserver_blueprint.route('/db/sqlserver/keyword-connect/')
def sqlserver_keyword_connect():
    return db_pyodbc.sqlserver_keyword_connect()


@db_sqlserver_blueprint.route('/db/sqlserver/server-connect/')
def sqlserver_server_connect():
    return db_pyodbc.sqlserver_server_connect()


@db_sqlserver_blueprint.route("/db/sqlserver/insert/")
def sqlserver_insert():
    return db_pyodbc.sqlserver_insert()


@db_sqlserver_blueprint.route("/db/sqlserver/delete/")
def sqlserver_delete():
    return db_pyodbc.sqlserver_delete()


@db_sqlserver_blueprint.route("/db/sqlserver/update/")
def sqlserver_update():
    return db_pyodbc.sqlserver_update()


@db_sqlserver_blueprint.route("/db/sqlserver/select/")
def sqlserver_select():
    return db_pyodbc.sqlserver_select()


@db_sqlserver_blueprint.route("/db/sqlserver/fetch-one/")
def sqlserver_fetch_one():
    return db_pyodbc.sqlserver_fetch_one()


@db_sqlserver_blueprint.route("/db/sqlserver/fetch-many/")
def sqlserver_fetch_many():
    return db_pyodbc.sqlserver_fetch_many()


@db_sqlserver_blueprint.route("/db/sqlserver/fetch-all/")
def sqlserver_fetch_all():
    return db_pyodbc.sqlserver_fetch_all()


@db_sqlserver_blueprint.route("/db/sqlserver/execute-many/")
def sqlserver_execute_many():
    return db_pyodbc.sqlserver_execute_many()


@db_sqlserver_blueprint.route("/db/sqlserver/table-error/")
def sqlserver_table_error():
    return db_pyodbc.sqlserver_table_error()


@db_sqlserver_blueprint.route("/db/sqlserver/field-error/")
def sqlserver_field_error():
    return db_pyodbc.sqlserver_field_error()


@db_sqlserver_blueprint.route("/db/sqlserver/syntax-error/")
def sqlserver_syntax_error():
    return db_pyodbc.sqlserver_syntax_error()
