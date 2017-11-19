# -*- coding: utf-8 -*-


from flask import Blueprint, request
from public.http import ex_requests


requests_blueprint = Blueprint('requests_blueprint', __name__)


# @requests_blueprint.route('/requests/api')
# def test_requests_api():
#     return ex_requests.test_requests_api()
#
#
# @requests_blueprint.route('/requests/session')
# def test_requests_session():
#     return ex_requests.test_requests_session()
#
#
# @requests_blueprint.route('/requests/timeout_error')
# def test_requests_timeout_error():
#     return ex_requests.test_requests_timeout_error()
#
#
# @requests_blueprint.route('/requests/timeout_ok')
# def test_requests_timeout_ok():
#     return ex_requests.test_requests_timeout_ok()


@requests_blueprint.route('/requests/get/')
def requests_get():
    """
    :param v: 作为参数传入，控制版本
    :param n: 作为参数传入，控制调用次数
    :return:
    """
    v = request.args.get('v', '2.10.0')
    n = int(request.args.get("n", '1'))
    for i in range(n):
        rlv = ex_requests.test_requests_get(v)

    return u"共访问 %d 次， 访问结果：[%s]" % (n, rlv)


@requests_blueprint.route('/external/requests/get/')
def external_requests_get():
    """
    :param v: 作为参数传入，控制版本
    :param n: 作为参数传入，控制调用次数
    :return:
    """
    v = request.args.get('v', '2.10.0')
    n = int(request.args.get('n', 1))
    for i in range(n):
        rlv = ex_requests.test_external_requests_get(v)

    return u"共访问 %d 次， 访问结果：[%s]" % (n, rlv)


@requests_blueprint.route('/external/requests/two')
def external_requests_get_two():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get('v', '2.10.0')

    no_agent = ex_requests.test_external_requests_get_no_agent(v)
    have_agent = ex_requests.test_external_requests_get(v)
    return "<h3>agent: %s</h3>\n<h3>no agent: %s</h3>" % (have_agent, no_agent)


@requests_blueprint.route('/external/requests/self')
def external_requests_self():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '2.10.0')
    return ex_requests.test_external_requests_get_self(v)


@requests_blueprint.route('/external/requests/lang')
def external_requests_lang():
    """
    :param v: 作为参数传入，控制版本
    :param lang: 作为参数传入，控制调用语言
    :return:
    """
    v = request.args.get("v", '2.10.0')
    lang = request.args.get("lang", "n")
    if lang == "n":
        return "sorry, please select a language with param `lang`"

    return ex_requests.test_external_requests_lang(v, lang)


@requests_blueprint.route('/requests/post/')
def requests_post():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get('v', '2.10.0')
    return ex_requests.test_requests_post(v)


@requests_blueprint.route('/external/requests/post/')
def external_requests_post():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get('v', '2.10.0')
    return ex_requests.test_external_requests_post(v)


@requests_blueprint.route('/requests/error/<error_type>')
def requests_error(error_type):
    """
    用于测试requests包网络异常情况
    :param error_type: 1.区分url
                       2.定义requests抛错类型
    :param v: 作为参数传入，控制版本
    :return:

                    =======================================
                    --错误类型（error_type）----定义错误代码--
                        InvalidURL               900
                        URLRequired              900
                        ConnectTimeout           902
                        ConnectionError          902
                        SSLError                 902
                        ReadTimeout              903
                        InvalidSchema            904
                        MissingSchema            904
                        ChunkedEncodingError     906
                        ContentDecodingError     906
                        StreamConsumedError      906
                    -----------（Exception）---------------
                        TooManyRedirects        1000
                        RequestException        1000
                        HTTPError               1000
                        ProxyError              1000     t---902
                        Timeout                 1000
                        RetryError              1000
                    =======================================
    """
    v = request.args.get('v', '2.10.0')
    print ("v:%s" % v).center(60, '*')
    return ex_requests.requests_error(v, error_type)

