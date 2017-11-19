# -*- coding: utf-8 -*-


from flask import Blueprint
from public.http import ex_urllib


urllib_blueprint = Blueprint('urllib_blueprint', __name__)


@urllib_blueprint.route('/urllib/get/')
def test_urllib_get_method():
    return ex_urllib.test_urllib_get_method()


@urllib_blueprint.route('/urllib/urlencode')
def test_urllib_urlencode_method():
    return ex_urllib.test_urllib_urlencode_method()


@urllib_blueprint.route('/urllib/post/')
def test_urllib_post_method():
    return ex_urllib.test_urllib_post_method()
