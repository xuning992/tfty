#!/usr/bin/env python
# -*- coding: utf-8 -*-


from genpy.tutorial import Calculator
from genpy.tutorial.ttypes import InvalidOperation, Operation, Work
from ..config import THRIFT_CONF
# from thrift.protocol import TBinaryProtocol
# from thrift.transport import TSocket
# from thrift.transport import TTransport


def get_package(v):

    if v == "0.9.3":
        from public.packages.ex_thrift.v093.thrift.protocol import TBinaryProtocol as TB
        from public.packages.ex_thrift.v093.thrift.transport import TSocket as TS
        from public.packages.ex_thrift.v093.thrift.transport import TTransport as TT

    elif v == "0.8.0":
        from public.packages.ex_thrift.v080.thrift.protocol import TBinaryProtocol as TB
        from public.packages.ex_thrift.v080.thrift.transport import TSocket as TS
        from public.packages.ex_thrift.v080.thrift.transport import TTransport as TT

    else:
        pass

    return TB, TS, TT


def rcp_call(v):

    TB, TS, TT = get_package(v)
    # Make socket
    transport = TS.TSocket(THRIFT_CONF['host'], THRIFT_CONF['port'])
    # transport = TS.TSocket('192.168.2.126', 8000)

    # Buffering is critical. Raw sockets are very slow
    transport = TT.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TB.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Calculator.Client(protocol)

    # Connect!
    transport.open()

    ping_res = client.ping()

    sum_ = client.add(1, 1)

    work = Work()

    work.op = Operation.DIVIDE
    work.num1 = 1
    work.num2 = 0

    try:
        quotient = client.calculate(1, work)
    except InvalidOperation as e:
        print('InvalidOperation: %r' % e)

    work.op = Operation.SUBTRACT
    work.num1 = 15
    work.num2 = 10

    diff = client.calculate(1, work)

    log = client.getStruct(1)

    # Close!
    transport.close()
    res = {
        'client_ping': ping_res,
        'client_add': sum_,
        'client_calculate': diff,
        'client_getStruct': log
    }
    return str(res)

    # TB, TS, TT = get_package(v)
    # transport = TS.TSocket(THRIFT_CONF['host'], THRIFT_CONF['port'])
    #
    # # Buffering is critical. Raw sockets are very slow
    # transport = TT.TBufferedTransport(transport)
    #
    # # Wrap in a protocol
    # protocol = TB.TBinaryProtocol(transport)
    #
    # # Create a client to use the protocol encoder
    # client = Calculator.Client(protocol)
    #
    # # Connect!
    # transport.open()
    # rtv = client.add("http://192.168.5.176", "/normal/a")
    #
    # transport.close()
    # return rtv


def thrift_error_(v, error_type):

    TB, TS, TT = get_package(v)
    transport = TS.TSocket("127.0.0.1", 5561)

    # Buffering is critical. Raw sockets are very slow
    transport = TT.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TB.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Calculator.Client(protocol)

    # Connect!
    transport.open(error_type=error_type)
    rtv = client.add_dir("/external/normal/a")

    transport.close()
    return rtv