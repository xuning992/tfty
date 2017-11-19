# -*- coding: utf-8 -*-

# from test_flask
import urllib
from ..config import *


def test_urllib_get_method():
    urllib.urlopen(URL_)
    return '[GET] urllib ok'


def test_urllib_urlencode_method():
    data = {"key1": "value1", "key2": "value2"}
    urllib.urlencode(data)
    return 'test_urllib_urlencode_method ok'


def test_urllib_post_method():
    data = urllib.urlencode(DATA)
    urllib.urlopen(URL_, data)
    return '[POST] urllib ok'

