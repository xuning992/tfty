# -*- coding: utf-8 -*-


from flask import Blueprint
from public.db_postgresql import db_psycopg2

#
psycopg2_blueprint = Blueprint('psycopg2_blueprint', __name__)


@psycopg2_blueprint.route('/db/postgresql/psycopg2-parameters-connect/')
def test_psycopg2_parameters_connect():
    return db_psycopg2.psycopg2_no_support_connect()


@psycopg2_blueprint.route('/db/postgresql/psycopg2-keyword-database-connect/')
def test_psycopg2_basedata_connect():
    return db_psycopg2.psycopg2_database_connect()


@psycopg2_blueprint.route('/db/postgresql/psycopg2-uri-connect/')
def test_psycopg2_uri_connect():
    return db_psycopg2.psycopg2_uri_connect()


@psycopg2_blueprint.route('/db/postgresql/psycopg2-uri-no-port-connect/')
def test_psycopg2_uri_no_port_connect():
    return db_psycopg2.psycopg2_uri_no_port_connect()


@psycopg2_blueprint.route('/db/postgresql/psycopg2-connectstring-no-port-connect/')
def test_psycopg2_connectstring_no_port():
    return db_psycopg2.psycopg2_connectstring_no_port_connect()


@psycopg2_blueprint.route('/db/postgresql/psycopg2-connectstring-connect/')
def test_psycopg2_dbname_user_connect():
    return db_psycopg2.psycopg2_connectstring_connect()


@psycopg2_blueprint.route('/db/postgresql/psycopg2-keyword-dbname-connect/')
def test_psycopg2_dbname_connect():
    return db_psycopg2.psycopg2_dbname_connect()


@psycopg2_blueprint.route('/db/postgresql/psycopg2-no-port-connect/')
def test_psycopg2_no_pot_connect():
    return db_psycopg2.psycopg2_no_port_connect()


@psycopg2_blueprint.route('/db/postgresql/psycopg2-insert/')
def test_psycopg2_insert():
    return db_psycopg2.test_psycopg2_insert()


@psycopg2_blueprint.route('/db/postgresql/psycopg2-update/')
def test_psycopg2_update():
    return db_psycopg2.test_psycopg2_update()


@psycopg2_blueprint.route('/db/postgresql/psycopg2-select/')
def test_psycopg2_select():
    return db_psycopg2.test_psycopg2_select()


@psycopg2_blueprint.route('/db/postgresql/psycopg2-delete/')
def test_psycopg2_delete():
    return db_psycopg2.test_psycopg2_delete()


@psycopg2_blueprint.route('/db/postgresql/psycopg2-connection-pool/')
def test_psycopg2_connection_pool():
    return db_psycopg2.test_psycopg2_connection_pool()


@psycopg2_blueprint.route('/db/postgresql/psycopg2-timeout-error/')
def test_psycopg2_timeout_error():
    return db_psycopg2.test_psycopg2_timeout_error()


@psycopg2_blueprint.route('/db/postgresql/psycopg2-timeout-ok/')
def test_psycopg2_timeout_ok():
    return db_psycopg2.test_psycopg2_timeout_ok()


@psycopg2_blueprint.route('/db/postgresql/psycopg2-table-error/')
def psycopg2_table_error():
    return db_psycopg2.test_psycopg2_table_error()


@psycopg2_blueprint.route('/db/postgresql/psycopg2-field-error/')
def psycopg2_field_error():
    return db_psycopg2.test_psycopg2_field_error()


@psycopg2_blueprint.route('/db/postgresql/psycopg2-syntax-error/')
def psycopg2_syntax_error():
    return db_psycopg2.test_psycopg2_syntax_error()


@psycopg2_blueprint.route("/db/postgresql/psycopg2-operates/")
def psycopg2_operates():
    res_1 = db_psycopg2.test_psycopg2_insert()
    res_2 = db_psycopg2.test_psycopg2_delete()
    res_3 = db_psycopg2.test_psycopg2_update()
    res_4 = db_psycopg2.test_psycopg2_select()
    return "psycopg2\ninsert: %s\ndelete: %s\nupdate: %s\nselect: %s" % (res_1, res_2, res_3, res_4)


@psycopg2_blueprint.route("/db/postgresql/psycopg2-connections/")
def psycopg2_connections():
    res_1 = db_psycopg2.test_psycopg2_connection_pool()
    res_2 = db_psycopg2.psycopg2_no_port_connect()
    res_3 = db_psycopg2.psycopg2_connectstring_connect()
    res_4 = db_psycopg2.psycopg2_connectstring_no_port_connect()
    res_5 = db_psycopg2.psycopg2_uri_connect()
    res_6 = db_psycopg2.psycopg2_uri_no_port_connect()
    res_7 = db_psycopg2.psycopg2_database_connect()
    res_8 = db_psycopg2.psycopg2_dbname_connect()
    return "psycopg2\npool: %s\nno_port: %s\nconnectstring: %s\nconnectstring_no_port: %s\nuri: %s\nuri_no_port: %s\n"\
           "database: %s\ndbname: %s" % (res_1, res_2, res_3, res_4, res_5, res_6, res_7, res_8)


