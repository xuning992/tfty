# -*- coding: utf-8 -*-

from ..config import *


def get_package(v):

    if v == "0.9.2":
        from public.packages.ex_httplib2.v092 import httplib2 as hl2
    elif v == "0.8":
        from public.packages.ex_httplib2.v080 import httplib2 as hl2
    elif v == "0.7.5":
        from public.packages.ex_httplib2.v075 import httplib2 as hl2
    else:
        pass

    return hl2


def httplib2_get(v):
    hl2 = get_package(v)
    http = hl2.Http()
    http.request(URL_, method='GET')
    return "[GET]httplib2 is OK"


def httplib2_post(v):
    hl2 = get_package(v)
    http = hl2.Http()
    http.request(URL_, method='POST', body=BODY)
    return "[POST]httplib2 is OK"


def external_httplib2_get(v):
    hl2 = get_package(v)
    http = hl2.Http()
    http.request(EX_URL, method='GET')
    return "[GET]external OK"


def httplib2_error(v, error_type):
    hl2 = get_package(v)
    http = hl2.Http()
    http.request(URL, error_type=error_type)

# def test_httplib2_http():
#     http = httplib2.Http()
#     # http.request(URL)
#     http.request(URL, method='GET', body="this is body")
#     return 'test_httplib2_http ok'
#
#
# def test_httplib2_http_timeout_error():
#     http = httplib2.Http(timeout=TIME_OUT)
#     url = 'http://localhost:5555/urllib/get'
#     http.request(url)
#     return 'test_httplib2_http_timeout_error ok'
#
#
# def test_httplib2_http_timeout_ok():
#     http = httplib2.Http(timeout=TIME_OUT)
#     url = 'http://localhost:5555/urllib/get'
#     http.request(url)
#     return 'test_httplib2_http_timeout_ok ok'
#
#
# def test_httplib2_https_timeout_error():
#     http = httplib2.Http(timeout=TIME_OUT)
#     http.request(URL)
#     return 'test_httplib2_https_timeout_error ok'
#
#
# def test_httplib2_https_timeout_ok():
#     http = httplib2.Http(timeout=60)
#     http.request(URL)
#     return 'test_httplib2_https_timeout_ok ok'




