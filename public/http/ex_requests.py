# -*- coding: utf-8 -*-

from ..config import *
import time


def get_package(v):

    if v == '2.10.0':
        from public.packages.ex_requests.v2100 import requests as req
    elif v == '2.9.0':
        from public.packages.ex_requests.v290 import requests as req
    elif v == '2.8.0':
        from public.packages.ex_requests.v280 import requests as req
    elif v == '2.7.0':
        from public.packages.ex_requests.v270 import requests as req
    elif v == '2.6.0':
        from public.packages.ex_requests.v260 import requests as req
    elif v == '2.5.0':
        from public.packages.ex_requests.v250 import requests as req
    elif v == '2.4.0':
        from public.packages.ex_requests.v240 import requests as req
    elif v == '2.3.0':
        from public.packages.ex_requests.v230 import requests as req
    elif v == '2.2.0':
        from public.packages.ex_requests.v220 import requests as req
    elif v == '2.1.0':
        from public.packages.ex_requests.v210 import requests as req
    elif v == '2.0.0':
        from public.packages.ex_requests.v200 import requests as req
    else:
        pass

    return req


# def test_requests_api():
#     requests.api.get(URL)
#     requests.api.post(URL, data=DATA)
#     return 'test_requests_api ok'
#
#
# def test_requests_session():
#     session = requests.session()
#     session.post(URL, data=DATA)
#     return 'test_requests_session ok'
#
#
# def test_requests_timeout_error():
#     requests.get(URL, timeout=TIME_OUT)
#     return 'test_requests_timeout_error ok'
#
#
# def test_requests_timeout_ok():
#     requests.get(URL, timeout=60)
#     return 'test_requests_timeout_ok ok'


def test_requests_get(v):
    requests = get_package(v)
    time.sleep(3)
    start = time.time()
    fp = requests.get(URL_)
    stop = time.time()
    return "[GET]status code is : %s, called time is : %s" % (fp.status_code, stop-start)


def test_external_requests_get(v):
    requests = get_package(v)
    fp = requests.get(EX_URL)
    return "{v%s}[GET] External status code is: %s" % (v, fp.status_code)


def test_external_requests_get_no_agent(v):
    requests = get_package(v)
    fp = requests.get(URL_)
    return "[GET](no agent) External status code is: %s" % fp.status_code


def test_external_requests_get_self(v):
    requests = get_package(v)
    fp = requests.get(SELF_URL)
    return "[GET](self) External status code is: %s" % fp.status_code


def test_external_requests_lang(v, lang):
    requests = get_package(v)
    fp = requests.get(URLS[lang])
    return "[GET](to %s) External status code is: %s" % (lang, fp.status_code)


def test_requests_post(v):
    requests = get_package(v)
    fp = requests.post(URL_, data=DATA)
    return "[POST]status code is : %s" % fp.status_code


def test_external_requests_post(v):
    requests = get_package(v)
    fp = requests.post(EX_URL, data=DATA)
    return "[POST] External status code is ： %s" % fp.status_code


def requests_error(v, error_type):
    print "in requests error function"
    req = get_package(v)
    return req.get(URL, error_type=error_type)






