# -*- coding: utf-8 -*-

from ..config import *


def get_package(v):

    if v == "1.17":
        from public.packages.ex_urllib3.v117 import urllib3 as ul3
    elif v == "1.16":
        from public.packages.ex_urllib3.v116 import urllib3 as ul3
    elif v == "1.15":
        from public.packages.ex_urllib3.v115 import urllib3 as ul3
    elif v == "1.14":
        from public.packages.ex_urllib3.v114 import urllib3 as ul3
    elif v == "1.13":
        from public.packages.ex_urllib3.v113 import urllib3 as ul3
    elif v == "1.12":
        from public.packages.ex_urllib3.v112 import urllib3 as ul3
    elif v == "1.11":
        from public.packages.ex_urllib3.v111 import urllib3 as ul3
    elif v == "1.10":
        from public.packages.ex_urllib3.v110 import urllib3 as ul3
    elif v == "1.9":
        from public.packages.ex_urllib3.v109 import urllib3 as ul3
    elif v == "1.8":
        from public.packages.ex_urllib3.v108 import urllib3 as ul3
    elif v == "1.7":
        from public.packages.ex_urllib3.v107 import urllib3 as ul3
    elif v == "1.6":
        from public.packages.ex_urllib3.v106 import urllib3 as ul3
    else:
        pass

    return ul3


def test_urllib3_poolmanager_get_method(v):
    ul3 = get_package(v)
    pool = ul3.PoolManager()
    pool.request('GET', URL_)
    return '[GET] urllib3 OK'


def test_external_urllib3_poolmanager_get(v):
    ul3 = get_package(v)
    pool = ul3.PoolManager()
    pool.request('GET', EX_URL)
    return "[GET] external urllib3 OK"


def test_urllib3_poolmanager_post_method(v):
    ul3 = get_package(v)
    pool = ul3.PoolManager()
    pool.request('POST', URL_, fields=FIELDS)
    return '[POST] urllib3 OK'


def urllib3_error(v, error_type):
    ul3 = get_package(v)
    pool = ul3.PoolManager()
    return pool.urlopen('GET', URL, error_type=error_type)


# def test_urllib3_timeout_error():
#     pool = urllib3.poolmanager.PoolManager(timeout=TIME_OUT)
#     pool.request('POST', URL, fields=FIELDS)
#     return 'test_urllib3_timeout_error ok'
#
#
# def test_urllib3_timeout_ok():
#     pool = urllib3.poolmanager.PoolManager(timeout=60)
#     pool.request('POST', URL, fields=FIELDS)
#     return 'test_urllib3_timeout_ok ok'