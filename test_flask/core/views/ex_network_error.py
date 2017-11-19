# -*- coding:utf-8 -*-


from flask import Blueprint

# import requests
# import urllib3
import urllib2
import urllib
# import httplib2
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket
from thrift.transport import TTransport
from ..utils.genpy.tutorial import Calculator

ex_network_error_blueprint = Blueprint("ex_network_error_blueprint", __name__)


# @ex_network_error_blueprint.route('/requests/error/<error_type>')

@ex_network_error_blueprint.route('/urllib/error/<error_type>')
def urllib_error(error_type):
    """
    用于测试urllib包网络异常情况
    :param error_type: 1.区分url
                       2.定义urllib抛错类型
    :return:

                    =======================================
                    --错误类型（error_type）----定义错误代码--
                        ContentTooShortError     906
                    -----------（Exception）---------------
                        IOError                 1000
                    =======================================
    """
    urllib.urlopen("http://127.0.0.1:5561/external/normal/a", error_type=error_type)
    return "error : urllib has no error"


@ex_network_error_blueprint.route('/urllib2/error/<error_type>')
def urllib2_error(error_type):
    """
    用于测试urllib2包网络异常情况
    :param error_type: 1.区分url
                       2.定义urllib2抛错类型
    :return:

                    =======================================
                    --错误类型（error_type）----定义错误代码--
                        URLError                 900
                        HTTPError               1000     t---900
                    -----------（Exception）---------------
                        ValueError              1000
                    =======================================

    """
    urllib2.urlopen("http://127.0.0.1:5561/external/normal/a", error_type=error_type)
    return "error: urllib2 has no error"


# @ex_network_error_blueprint.route('/urllib3/error/<error_type>')


# @ex_network_error_blueprint.route('/httplib2/error/<error_type>')


# @ex_network_error_blueprint.route('/thrift/error/<error_type>')
# def thrift_error(error_type):
#     """
#     用于测试thrift包网络异常情况
#     :param error_type: 1.区分url
#                        2.定义thrift抛错类型
#     :return:
#
#                     =======================================
#                     --错误类型（error_type）----定义错误代码--
#                         TTransportException      901
#                         TProtocolException       906
#                     -----------（Exception）---------------
#                         TException              1000
#                         TApplicationException   1000
#                     =======================================
#     """
#     transport = TSocket.TSocket("127.0.0.1", 5561)
#
#     # Buffering is critical. Raw sockets are very slow
#     transport = TTransport.TBufferedTransport(transport)
#
#     # Wrap in a protocol
#     protocol = TBinaryProtocol.TBinaryProtocol(transport)
#
#     # Create a client to use the protocol encoder
#     client = Calculator.Client(protocol)
#
#     # Connect!
#     transport.open(error_type=error_type)
#     rtv = client.add_dir("/external/normal/a")
#
#     transport.close()
#     return rtv







