# -*- coding: utf-8 -*-
from core.views.base import BaseHandler
from public.http import ex_urllib3


class Urllib3Get(BaseHandler):
    """
    :param v:作为参数传入，控制版本
    :return:
    """
    def get(self):
        v = self.get_argument("v", '1.17')
        self.write(ex_urllib3.test_urllib3_poolmanager_get_method(v))


class Urllib3Post(BaseHandler):
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    def get(self):
        v = self.get_argument("v", '1.17')
        self.write(ex_urllib3.test_urllib3_poolmanager_post_method(v))


class Urllib3Error(BaseHandler):
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
    def get(self, error_type=None):
        v = self.get_argument('v', '1.17')
        self.write(ex_urllib3.urllib3_error(v, error_type))
