# -*- coding: utf-8 -*-
from core.views.base import BaseHandler
from public.http import ex_requests


class RequestsGet(BaseHandler):
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    def get(self):
        v = self.get_argument('v', '2.10.0')
        self.write(ex_requests.test_requests_get(v))


class ExternalRequestsGet(BaseHandler):
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    def get(self):
        v = self.get_argument('v', '2.10.0')
        self.write(ex_requests.test_external_requests_get(v))


class RequestsPost(BaseHandler):
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    def get(self):
        v = self.get_argument('v', '2.10.0')
        self.write(ex_requests.test_requests_post(v))


class ExternalRequestsPost(BaseHandler):
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    def get(self):
        v = self.get_argument('v', '2.10.0')
        self.write(ex_requests.test_external_requests_post(v))


class RequestsError(BaseHandler):
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
    def get(self, error_type=None):
        v = self.get_argument('v', '2.10.0')
        print ("v:%s" % v).center(60, '*')
        self.write(ex_requests.requests_error(v, error_type))

