#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.views.base import BaseHandler
from public.http.ex_thrift import rcp_call, thrift_error_


class ExThrift(BaseHandler):
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    def get(self):
        v = self.get_argument('v', '0.9.3')
        return rcp_call(v)


class ThriftError(BaseHandler):
    """
    用于测试thrift包网络异常情况
    :param error_type: 1.区分url
                       2.定义thrift抛错类型
    :param v: 作为参数传入，控制版本
    :return:

                    =======================================
                    --错误类型（error_type）----定义错误代码--
                        TTransportException      901
                        TProtocolException       906
                    -----------（Exception）---------------
                        TException              1000
                        TApplicationException   1000
                    =======================================
    """
    def initialize(self, error_type):
        self.error_type = error_type

    def get(self):
        v = self.get_argument('v', '0.9.3.2')
        self.write(thrift_error_(v, self.error_type))
