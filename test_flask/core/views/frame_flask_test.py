# -*- coding: utf-8 -*-

"""
用于测试python框架flask
"""
import flask
from flask import Blueprint, g, abort, request
from public.db_mysql import db_mysqldb


# conn = MySQLdb.connect(host='192.168.2.43', port=3306, user='tingyun', passwd='tingyun', db='python_test')
# cur = conn.cursor()
sql_one = "select name,sex from many_info where name like \"c%\" and age=1234 order by name desc"
wrong_table = "select name from many_in where age=1234"
syntas_error = "selec name from many_info where ager=1234"

frame_flask_test_blueprint = Blueprint("frame_flask_test_blueprint", __name__)


@frame_flask_test_blueprint.route('/blueprint/normal')
def do_thing():
    rtv = db_mysqldb.mysqldb_select()
    return str(rtv)


@frame_flask_test_blueprint.route('/blueprint/error/<id>')
def do_thing_http_error(id):
    """
    :param code:作为参数传入，作为响应码
    :param id:作为参数传入，用于区分uri
    :return:
    """
    code = request.args.get("code")
    abort(int(code))


# @frame_flask_test_blueprint.route('/blueprint/operation_error')
# def do_thing_operation_error():
#     if not hasattr(g, 'cur'):
#         g.conn = MySQLdb.connect(host='192.168.2.43', port=3306, user='tingyun', passwd='tingyun', db='python_test')
#         g.cur = g.conn.cursor()
#
#     g.cur.execute(wrong_table)
#     return "success"


@frame_flask_test_blueprint.errorhandler(404)
def errorhandler(f):
    return "<h1>Page Not Found</h1>"


def register_error_handler(f):
    return "<h1>Internal Server Error</h1>", 500

try:
    frame_flask_test_blueprint.register_error_handler(500, register_error_handler)
except AttributeError:
    pass


@frame_flask_test_blueprint.before_request
def blueprint_before_request():
    pass
    # g.conn = MySQLdb.connect(host='192.168.2.43', port=3306, user='tingyun', passwd='tingyun', db='python_test')
    # g.cur = g.conn.cursor()


@frame_flask_test_blueprint.after_request
def blueprint_after_request(f):
    return f


@frame_flask_test_blueprint.teardown_request
def blueprint_teardown_request(f):
    return f


@frame_flask_test_blueprint.before_app_first_request
def blueprint_before_app_first_request():
    pass


@frame_flask_test_blueprint.before_app_request
def blueprint_before_app_request():
    pass


@frame_flask_test_blueprint.after_app_request
def blueprint_after_app_request(f):
    return f


@frame_flask_test_blueprint.teardown_app_request
def blueprint_teardown_app_request(f):
    return f




