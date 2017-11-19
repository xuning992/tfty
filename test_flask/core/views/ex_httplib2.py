# -*- coding: utf-8 -*-


from flask import Blueprint, request, redirect
from public.http import ex_httplib2

httplib2_blueprint = Blueprint('httplib2_blueprint', __name__)


# @httplib2_blueprint.route('/httplib2/http')
# def test_httplib2_http():
#     return ex_httplib2.test_httplib2_http()
#
#
# @httplib2_blueprint.route('/httplib2/http_timeout_error')
# def test_httplib2_http_timeout_error():
#     return ex_httplib2.test_httplib2_http_timeout_error()
#
#
# @httplib2_blueprint.route('/httplib2/http_timeout_ok')
# def test_httplib2_http_timeout_ok():
#     return ex_httplib2.test_httplib2_http_timeout_ok()
#
#
# @httplib2_blueprint.route('/httplib2/https_timeout_ok')
# def test_httplib2_https_timeout_error():
#     return ex_httplib2.test_httplib2_https_timeout_ok()
#
#
# @httplib2_blueprint.route('/httplib2/https_timeout_error')
# def test_httplib2_https_timeout_ok():
#     return ex_httplib2.test_httplib2_https_timeout_error()


@httplib2_blueprint.route('/httplib2/get/')
def httplib2_get():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.9.2')
    return ex_httplib2.httplib2_get(v)


@httplib2_blueprint.route('/external/httplib2/get')
def external_httplib2_get():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.9.2')
    return ex_httplib2.external_httplib2_get(v)


@httplib2_blueprint.route('/httplib2/post/')
def httplib2_post():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.9.2')
    if not checker(v):
        return "sorry, but httplib2 doesn`t have version %s " % v
    return ex_httplib2.httplib2_post(v)


@httplib2_blueprint.route('/httplib2/error/<error_type>')
def httplib2_error(error_type):
    """
    用于测试httplib2包网络异常情况
    :param error_type: 1.区分url
                       2.定义httplib2抛错类型
    :param v: 作为参数传入，控制版本
    :return:

                    =====================================================
                    -------错误类型（error_type）-------------定义错误代码--
                        RelativeURIError                        900
                        RedirectMissingLocation                 900
                        ServerNotFoundError                     901
                        FailedToDecompressContent               906
                        HttpLib2ErrorWithResponse               906
                        CertificateHostnameMismatch             908
                        CertificateValidationUnsupported        908
                    -------------------（Exception）---------------------
                        ProxiesUnavailableError                1000
                        RedirectLimit                          1000
                        UnimplementedDigestAuthOptionError     1000
                        UnimplementedHmacDigestAuthOptionError 1000
                        MalformedHeader                        1000
                        SSLHandshakeError                      1000
                        NotSupportedOnThisPlatform             1000
                        HttpLib2Error                          1000
                    =====================================================

    """
    v =request.args.get('v', '0.9.2')
    return ex_httplib2.httplib2_error(v, error_type)


def checker(v):
    if v not in ['0.9.2', '0.8', '0.7.5']:
        return False
    return True