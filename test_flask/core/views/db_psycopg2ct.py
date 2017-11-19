# -*- coding: utf-8 -*-


from flask import Blueprint
from public.db_postgresql import db_psycopg2ct

psycopg2ct_blueprint = Blueprint('psycopg2ct_blueprint', __name__)


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-parameters-connnect/')
def test_psycopg2ct_parameters_connect():
    return db_psycopg2ct.psycopg2ct_no_support_connect()


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-keyword-database-connect/')
def test_psycopg2ct_basedata_connect():
    return db_psycopg2ct.psycopg2ct_database_connect()


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-uri-connect/')
def test_psycopg2ct_uri_connect():
    return db_psycopg2ct.psycopg2ct_uri_connect()


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-uri-no-port-connect/')
def test_psycopg2ct_uri_no_port_connect():
    return db_psycopg2ct.psycopg2ct_uri_no_port_connect()


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-connectstring-no-port-connect/')
def test_psycopg2ct_connectstring_no_port():
    return db_psycopg2ct.psycopg2ct_connectstring_no_port_connect()


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-connectstring-connect/')
def test_psycopg2ct_dbname_user_connect():
    return db_psycopg2ct.psycopg2ct_connectstring_connect()


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-keyword-dbname-connect/')
def test_psycopg2ct_dbname_connect():
    return db_psycopg2ct.psycopg2ct_dbname_connect()


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-no-port-connect/')
def test_psycopg2ct_no_pot_connect():
    return db_psycopg2ct.psycopg2ct_no_port_connect()


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-insert/')
def test_psycopg2ct_insert():
    return db_psycopg2ct.test_psycopg2ct_insert()


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-update/')
def test_psycopg2ct_update():
    return db_psycopg2ct.test_psycopg2ct_update()


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-select/')
def test_psycopg2ct_select():
    return db_psycopg2ct.test_psycopg2ct_select()


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-delete/')
def test_psycopg2ct_delete():
    return db_psycopg2ct.test_psycopg2ct_delete()


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-connection-pool/')
def test_psycopg2ct_connection_pool():
    return db_psycopg2ct.test_psycopg2ct_connection_pool()


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-timeout-error/')
def test_psycopg2ct_timeout_error():
    return db_psycopg2ct.test_psycopg2ct_timeout_error()


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-timeout-ok/')
def test_psycopg2ct_timeout_ok():
    return db_psycopg2ct.test_psycopg2ct_timeout_ok()


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-table-error/')
def test_psycopg2ct_table_error():
    return db_psycopg2ct.test_psycopg2ct_table_error()


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-field-error/')
def test_psycopg2ct_field_error():
    return db_psycopg2ct.test_psycopg2ct_field_error()


@psycopg2ct_blueprint.route('/db/postgresql/psycopg2ct-syntax-error/')
def test_psycopg2ct_syntax_error():
    return db_psycopg2ct.test_psycopg2ct_syntax_error()