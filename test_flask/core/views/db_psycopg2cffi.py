# -*- coding: utf-8 -*-


from flask import Blueprint, request
from public.db_postgresql import db_psycopg2cffi


psycopg2cffi_blueprint = Blueprint('psycopg2cffi_blueprint', __name__)


@psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-parameters-connect/')
def test_psycopg2cffi_parameters_connect():
    return db_psycopg2cffi.psycopg2cffi_no_support_connect()


@psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-keyword-database-connect/')
def test_psycopg2cffi_basedata_connect():
    return db_psycopg2cffi.psycopg2cffi_database_connect()


@psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-uri-connect/')
def test_psycopg2cffi_uri_connect():
    return db_psycopg2cffi.psycopg2cffi_uri_connect()


@psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-uri-no-port-connect/')
def test_psycopg2cffi_uri_no_port_connect():
    return db_psycopg2cffi.psycopg2cffi_uri_no_port_connect()


@psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-connectstring-no-port-connect/')
def test_psycopg2cffi_connectstring_no_port():
    return db_psycopg2cffi.psycopg2cffi_connectstring_no_port_connect()


@psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-connectstring-connect/')
def test_psycopg2cffi_dbname_user_connect():
    return db_psycopg2cffi.psycopg2cffi_connectstring_connect()


@psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-keyword-dbname-connect/')
def test_psycopg2cffi_dbname_connect():
    return db_psycopg2cffi.psycopg2cffi_dbname_connect()


@psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-no-port-connect/')
def test_psycopg2cffi_no_pot_connect():
    return db_psycopg2cffi.psycopg2cffi_no_port_connect()


@psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-insert/')
def test_psycopg2cffi_insert():
    return db_psycopg2cffi.test_psycopg2cffi_insert()


@psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-update/')
def test_psycopg2cffi_update():
    return db_psycopg2cffi.test_psycopg2cffi_update()


@psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-select/')
def test_psycopg2cffi_select():
    return db_psycopg2cffi.test_psycopg2cffi_select()


@psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-delete/')
def test_psycopg2cffi_delete():
    return db_psycopg2cffi.test_psycopg2cffi_delete()


@psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-connection-pool/')
def test_psycopg2cffi_connection_pool():
    return db_psycopg2cffi.test_psycopg2cffi_connection_pool()


# @psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-timeout-error/')
# def test_psycopg2cffi_timeout_error():
#     """
#     :ver: 作为参数传入，控制版本
#     :return:
#     """
#     version = request.args.get("ver")
#     if not version:
#         version = "2.6"
#
#     return db_psycopg2cffi.test_psycopg2cffi_timeout_error(version)


# @psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-timeout-ok/')
# def test_psycopg2cffi_timeout_ok():
#     return db_psycopg2cffi.test_psycopg2cffi_timeout_ok()


@psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-table-error/')
def test_psycopg2cffi_table_error():
    return db_psycopg2cffi.test_psycopg2cffi_table_error()


@psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-field-error/')
def test_psycopg2cffi_field_error():
    return db_psycopg2cffi.test_psycopg2cffi_field_error()


@psycopg2cffi_blueprint.route('/db/postgresql/psycopg2cffi-syntax-error/')
def test_psycopg2cffi_syntax_error():
    return db_psycopg2cffi.test_psycopg2cffi_syntax_error()


