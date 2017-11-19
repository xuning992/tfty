# -*- coding: utf-8 -*-

"""
用于测试配置项的uri
"""

import time
from flask import Blueprint, abort, request
from public.db_mysql import db_mysqldb
from public.packages.ex_requests.v2100 import requests

dc_config_test_blueprint = Blueprint("dc_config_test_blueprint", __name__)


# @dc_config_test_blueprint.route('/rabbitmq/queue/time')
# def rabbitmq_queue_time():
#     """
#     :param t: 作为参数传入，控制访问数量
#     :return:
#     """
#     t = int(request.args.get("t", 1))
#     for i in range(1, t+1):
#         requests.get("http://127.0.0.1:5562/rabbitmq/producer/define/queue")
#     return u"共 %d 次" % t


@dc_config_test_blueprint.route('/normal/<id>')
def normal(id):
    """访问状态：200
       响应时间：小于100ms
    :param id:字母，用于区分uri
    :return:
    """
    time.sleep(2)
    # requests.get("http://192.168.2.201:5562/slow/action/a?timer=2500")
    return "success"


@dc_config_test_blueprint.route('/normal/with/sql')
def normal_with_sql():
    """访问状态：200
       响应时间：小于500ms
       sql：存在sql语句，查询时间大于10ms，小于500ms
    :return:
    """
    rlv = db_mysqldb.mysqldb_select()
    return str(rlv)


@dc_config_test_blueprint.route('/slow/action/with/sql')
def slow_action_with_sql():
    """访问状态：200
       响应时间：大于2000ms
       sql：存在sql语句，查询时间大于10ms，小于500ms
    :return:
    """
    time.sleep(3)
    rlv = db_mysqldb.mysqldb_select()
    return str(rlv)


@dc_config_test_blueprint.route('/slow/action/<id>')
def slow_action(id):
    """访问状态：200
    :param id: 用于区分uri
    :param timer: 作为参数传入，控制响应时间，单位ms
    :return:
    """
    timer = request.args.get('timer')
    if timer:
        timer = float(timer)/1000
        time.sleep(timer)
    # requests.get("http://192.168.5.140:8080/jdk1.6_AgentTest_External_01/urlGet?urlConnectUrl=http%3A%2F%2F192.168.2.152%3A4000%2Fone_transaction")
    return "success"


@dc_config_test_blueprint.route('/error/<id>')
def error(id):
    """访问状态：500
    :param id: 用于区分uri
    :param code: 作为参数传入，为响应码
    :return:
    """
    code = request.args.get('code')
    abort(int(code))


@dc_config_test_blueprint.route('/external/f_z_f')
def external_404():
    """访问状态:200
       被调用访问状态：404
    :return:
    """
    requests.get('http://127.0.0.1:5561/')
    return "success"


@dc_config_test_blueprint.route('/abcd/efg/hij')
def abcd():
    """访问状态：200
       访问时间：小于100ms
    :return:
    """
    return "success"


@dc_config_test_blueprint.route('/stack')
def stack():
    """访问状态：200
    :param num: 作为参数传入，控制time.sleep函数次数，正整数
    :param timer: 作为参数传入，控制一次time.sleep函数的等待时间，单位毫秒
    :return:
    """
    num = request.args.get('num')
    timer = request.args.get('timer')
    num = int(num)
    timer = float(timer)/1000
    for i in range(0, num):
        time.sleep(timer)
    return "success"


@dc_config_test_blueprint.route('/external/error/<id>')
def external_error(id):
    """访问状态：200
       调用外部应用方法：requests.get
    :param id: 用于区分uri
    :param code: 作为参数传入，为外部应用的响应代码
    :return:
    """
    code = request.args.get('code')
    param = {"code": code}
    requests.get("http://192.168.2.33:5577/error/%s" % id, params=param)
    return "success"


@dc_config_test_blueprint.route('/external/normal/<id>')
def external_normal(id):
    """访问状态：200
       调用外部应用方法：request.get
    :param id: 用于区分uri
    :return:
    """
    requests.get("http://127.0.0.1:5561/external/normal/%s" % id)
    return "success"


@dc_config_test_blueprint.route('/external/slow/action/<id>')
def external_slow_action(id):
    """访问状态：200
       调用外部应用方法：request.get
    :param id: 用于区分uri
    :param timer: 作为参数传入，作为外部应用的等待时间
    :return:
    """
    timer = request.args.get('timer')
    param = {"timer": timer}
    requests.get("http://127.0.0.1:5561/external/slow/action/%s" % id, params=param)
    return "success"


@dc_config_test_blueprint.route('/external/url/param/<id>')
def external_url_param(id):
    """访问状态：200
       调用外部应用方法：request.get
    :param id: 用于区分uri
    :param url: 作为参数传入，用于区分调用的uri
    :param a: 作为参数传入，作为调用url的参数
    :param b: 作为参数传入，作为调用url的参数
    :param c: 作为参数传入，作为调用url的参数
    :param d: 作为参数传入，作为调用url的参数
    :return:
    """
    url = request.args.get("url")
    a = request.args.get("a")
    b = request.args.get("b")
    c = request.args.get("c")
    d = request.args.get("d")

    param = {"a": a, "b": b, "c": c, "d": d}

    if url == "normal":
        requests.get("http://127.0.0.1:5561/external/normal/%s" % id, params=param)
    else:
        requests.get("http://127.0.0.1:5561/abcd/efg/hij", params=param)

    return "success"


@dc_config_test_blueprint.route('/external/test')
def external_test():

    time.sleep(3)
    # dotnet y  y
    requests.get("http://192.168.1.124:8027")

    # php y  y
    # requests.get("http://192.168.2.119/ob.php")

    # ruby n  y
    # requests.get("http://192.168.2.152:8000/mongo_tst")

    # nodejs y  y
    # requests.get("http://192.168.5.2")

    # java y y
    # requests.get("http://192.168.5.165:28080/")

    return "success"

