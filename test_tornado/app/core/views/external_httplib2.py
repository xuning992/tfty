# -*- coding: utf-8 -*-
from core.views.base import BaseHandler
from public.http import ex_httplib2


class Httplib2Get(BaseHandler):
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    def get(self):
        v = self.get_argument("v", '0.9.2')
        self.write(ex_httplib2.httplib2_get(v))


class Httplib2Post(BaseHandler):
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    def get(self):
        v = self.get_argument("v", '0.9.2')
        if not checker(v):
            self.write("sorry, but httplib2 doesn`t have version %s " % v)
        self.write(ex_httplib2.httplib2_post(v))


class Httplib2Error(BaseHandler):
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
    def get(self, error_type=None):
        v = self.get_argument('v', '0.9.2')
        self.write(ex_httplib2.httplib2_error(v, error_type))


def checker(v):
    if v not in ['0.9.2', '0.8', '0.7.5']:
        return False
    return True
