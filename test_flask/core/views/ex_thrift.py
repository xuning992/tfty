#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, request
from public.http.ex_thrift import rcp_call, thrift_error_


ex_thrift_blueprint = Blueprint(__name__, __name__)


@ex_thrift_blueprint.route("/ex/thrift/")
def ex_thrift():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get('v', '0.9.3')
    return rcp_call(v)


@ex_thrift_blueprint.route('/thrift/error/<error_type>')
def thrift_error(error_type):
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
    v = request.args.get('v', '0.9.3')
    return thrift_error_(v, error_type)
