# -*- coding: utf-8 -*-


import urllib2, urllib
from ..config import *


def test_urllib2_get_method():
    urllib2.urlopen(URL_)
    return '[GET] urllib2 ok'


def test_urllib2_post_method():
    data = urllib.urlencode(DATA)
    urllib2.urlopen(URL_, data)
    return '[POST] urllib2 ok'


def test_urllib2_cookie_method():
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'cookiename=cookievalue'))
    opener.open(URL)
    return 'test_urllib2_cookie_method ok'