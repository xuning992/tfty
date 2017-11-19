# -*- coding: utf-8 -*-

import httplib2
import urllib3
from flask import Blueprint

from http_config import *
#from test_flask
import requests

cross_app_trace_blueprint = Blueprint('cross_app_trace_blueprint', __name__)
URL = CROSS_APP_TRACE_URL


@cross_app_trace_blueprint.route('/cross_app_trace/urllib3/get')
def test_urllib3_get_cross_app_trace():
    pool = urllib3.poolmanager.PoolManager()
    pool.request('GET', URL)
    return 'test_urllib3_get_cross_app_trace ok'


@cross_app_trace_blueprint.route('/cross_app_trace/urllib3/post')
def test_urllib3_post_cross_app_trace():
    pool = urllib3.poolmanager.PoolManager()
    pool.request('POST', URL)
    return 'test_urllib3_post_cross_app_trace ok'


@cross_app_trace_blueprint.route('/cross_app_trace/httplib2/get')
def test_httplib2_get_cross_app_trace():
    http = httplib2.Http()
    http.request(uri=URL, method='GET')
    return 'test_httplib2_get_cross_app_trace ok'


@cross_app_trace_blueprint.route('/cross_app_trace/httplib2/post')
def test_httplib2_post_cross_app_trace():
    http = httplib2.Http()
    http.request(uri=URL, method='POST')
    return 'test_httplib2_post_cross_app_trace ok'


@cross_app_trace_blueprint.route('/cross_app_trace/requests/get')
def test_requests_get_cross_app_trace():
    requests.get(URL)
    return 'test_requests_get_cross_app_trace ok'


@cross_app_trace_blueprint.route('/cross_app_trace/requests/post')
def test_requests_post_cross_app_trace():
    requests.post(URL)
    return 'test_requests_get_cross_app_trace ok'
