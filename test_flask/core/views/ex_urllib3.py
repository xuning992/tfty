# -*- coding: utf-8 -*-


from flask import Blueprint, request
from public.http import ex_urllib3


urllib3_blueprint = Blueprint('urllib3_blueprint', __name__)


# @urllib3_blueprint.route('/urllib3/poolmanager/get')
# def test_urllib3_poolmanager_get_method():
#     return ex_urllib3.test_urllib3_poolmanager_get_method()
#
#
# @urllib3_blueprint.route('/urllib3/poolmanager/post')
# def test_urllib3_poolmanager_post_method():
#     return ex_urllib3.test_urllib3_poolmanager_post_method()
#
#
# @urllib3_blueprint.route('/urllib3/timeout_error')
# def test_urllib3_timeout_error():
#     return ex_urllib3.test_urllib3_timeout_error()
#
#
# @urllib3_blueprint.route('/urllib3/timeout_ok')
# def test_urllib3_timeout_ok():
#     return ex_urllib3.test_urllib3_timeout_ok()


@urllib3_blueprint.route('/urllib3/get/')
def urllib3_get():
    """
    :param v:作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '1.17')
    return ex_urllib3.test_urllib3_poolmanager_get_method(v)


@urllib3_blueprint.route('/external/urllib3/get')
def external_urllib3_get():
    """
    :param v: 作为参数出入，控制版本
    :return:
    """
    v = request.args.get("v", '1.17')
    return ex_urllib3.test_external_urllib3_poolmanager_get(v)


@urllib3_blueprint.route('/urllib3/post/')
def urllib3_post():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '1.17')
    return ex_urllib3.test_urllib3_poolmanager_post_method(v)


@urllib3_blueprint.route('/urllib3/error/<error_type>')
def urllib3_error(error_type):
    """
    用于测试urllib3包网络异常情况
    :param error_type: 1.区分url
                       2.定义urllib3抛错类型
    :param v: 作为参数传入，控制版本
    :return:

                    =======================================
                    --错误类型（error_type）----定义错误代码--
                        LocationValueError       900
                        HostChangedError         901
                        LocationParseError       901
                        ConnectTimeoutError      902    t---903
                        ProxyError               902
                        TimeoutError             903
                        ReadTimeoutError         903
                        ProtocolError            904
                        DecodeError              906
                        ResponseError            906
                        ResponseNotChunked       906
                        SSLError                 908
                    -----------（Exception）---------------
                        HTTPError               1000
                        HTTPWarning             1000
                        PoolError               1000
                        RequestError            1000
                        MaxRetryError           1000
                        TimeoutStateError       1000
                        NewConnectionError      1000
                        EmptyPoolError          1000
                        ClosedPoolError         1000
                        SecurityWarning         1000
                        SubjectAltNameWarning   1000
                        InsecureRequestWarning  1000
                        SystemTimeWarning       1000
                        InsecurePlatformWarning 1000
                        SNIMissingWarning       1000
                        DependencyWarning       1000
                        ProxySchemeUnknown      1000
                        HeaderParsingError      1000
                    =======================================

    """
    v = request.args.get('v', '1.17')
    return ex_urllib3.urllib3_error(v, error_type)
