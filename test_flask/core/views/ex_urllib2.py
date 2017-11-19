# -*- coding: utf-8 -*-


from flask import Blueprint
from public.http import ex_urllib2


urllib2_blueprint = Blueprint('urllib2_blueprint', __name__)


@urllib2_blueprint.route('/urllib2/get/')
def test_urllib2_get_method():
    return ex_urllib2.test_urllib2_get_method()


@urllib2_blueprint.route('/urllib2/post/')
def test_urllib2_post_method():
    return ex_urllib2.test_urllib2_post_method()


@urllib2_blueprint.route('/urllib2/cookie/')
def test_urllib2_cookie_method():
    return ex_urllib2.test_urllib2_cookie_method()
