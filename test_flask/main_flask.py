# !/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, g, abort, request
import requests

from core.views.dc_config_test import dc_config_test_blueprint
from core.views.frame_flask_test import frame_flask_test_blueprint

from core.views.db_oracle import db_oracle_blueprint
from core.views.db_mysql import db_mysql_blueprint
from core.views.db_sqlserver import db_sqlserver_blueprint
from core.views.db_psycopg2 import psycopg2_blueprint
from core.views.db_psycopg2ct import psycopg2ct_blueprint
from core.views.db_psycopg2cffi import psycopg2cffi_blueprint
from core.views.db_mongodb import db_mongodb_blueprint
from core.views.db_memcache import db_memcache_blueprint
from core.views.db_redis import db_redis_blueprint

from core.views.ex_urllib import urllib_blueprint
from core.views.ex_urllib2 import urllib2_blueprint
from core.views.ex_urllib3 import urllib3_blueprint
from core.views.ex_httplib2 import httplib2_blueprint
from core.views.ex_requests import requests_blueprint
# from core.views.test_cross_app_trace import cross_app_trace_blueprint
from core.views.ex_thrift import ex_thrift_blueprint
from core.views.ex_network_error import ex_network_error_blueprint

from core.views.block_code import block_code_blueprint
from core.views.db_sqlchemy_mysql import sqlalchemy_mysql
from core.views.message_rabbitmq import rabbitmq_blueprint


application = Flask(__name__, template_folder="core/templates")


application.register_blueprint(dc_config_test_blueprint)
application.register_blueprint(frame_flask_test_blueprint)

application.register_blueprint(db_oracle_blueprint)
application.register_blueprint(db_mysql_blueprint)
application.register_blueprint(db_sqlserver_blueprint)
application.register_blueprint(psycopg2_blueprint)
application.register_blueprint(psycopg2ct_blueprint)
application.register_blueprint(psycopg2cffi_blueprint)
application.register_blueprint(db_mongodb_blueprint)
application.register_blueprint(db_memcache_blueprint)
application.register_blueprint(db_redis_blueprint)

application.register_blueprint(urllib_blueprint)
application.register_blueprint(urllib2_blueprint)
application.register_blueprint(urllib3_blueprint)
application.register_blueprint(httplib2_blueprint)
application.register_blueprint(requests_blueprint)
# application.register_blueprint(cross_app_trace_blueprint)
application.register_blueprint(ex_thrift_blueprint)
application.register_blueprint(ex_network_error_blueprint)

application.register_blueprint(block_code_blueprint)
application.register_blueprint(sqlalchemy_mysql)
application.register_blueprint(rabbitmq_blueprint)


@application.before_first_request
def before_first_request():
    pass


@application.before_request
def before_request():
    g.a = 0


def add_url_rule():
    if not hasattr(g, "a"):
        return "fail"
    g.a += 1
    return "success, %d" % g.a

application.add_url_rule('/add_url_rule', 'add_url_rule', add_url_rule)


def register_error_handler(f):
    return "<h1>page not found!</h1>", 500
application.register_error_handler(500, register_error_handler)


@application.errorhandler(404)
def errorhandler(f):
    return "<h1>Internal Server Error!</h1>", 404


@application.after_request
def after_request(response):
    return response


@application.teardown_request
def teardown_request(response_error):
    return response_error


@application.route('/java')
def requests_java():
    # requests.get('http://192.168.2.206:38080/urlGet')
    requests.get('http://192.168.5.140:8080/jdk1.6_External_02_httpclient3.1-4.5/test')
    return "java"


@application.route('/net')
def requests_net():
    requests.get("http://192.168.5.173:8011/")
    return "net"


@application.route('/python')
def response_python():
    # fp = requests.get("http://192.168.2.33:5562/db/mysql/pymysql-select/")
    # fp = requests.get("http://192.168.2.33:5562/db/oracle/select/")
    # fp = requests.get("http://192.168.2.33:5562/db/oracle/insert/")
    fp = requests.get("http://192.168.2.201:5662/resp_200/")
    return u"响应状态: %s" % fp.status_code


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5562, debug=True)
