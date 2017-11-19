# -*- coding: utf-8 -*-


from flask import Blueprint, request
from time import sleep
from public.message import msg_rabbitmq
# from pika import LibevConnection, ConnectionParameters


rabbitmq_blueprint = Blueprint('rabbitmq_blueprint', __name__)


@rabbitmq_blueprint.route('/rabbitmq/producer/define/queue')
def rabbitmq_define_queue():
    """
    :param v:作为参数传入，控制版本

    :param t: 作为参数传入，控制生产次数
    :return:
    """
    v = request.args.get("v", '0.10.0')
    t = int(request.args.get("t", 1))
    for i in range(t):
        rlt = msg_rabbitmq.rabbitmq_define_queue(v)
    sleep(2)
    return u"共 %s 次， 最后一次数据： %s" % (t, rlt)


@rabbitmq_blueprint.route('/rabbitmq/producer/define/queue/with/dot')
def rabbitmq_define_queue_with_dot():
    v = request.args.get("v", '0.10.0')
    return msg_rabbitmq.rabbitmq_define_queue_with_dot(v)


@rabbitmq_blueprint.route('/rabbitmq/producer/round/robin')
def rabbitmq_round_robin():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.10.0')
    return msg_rabbitmq.rabbitmq_round_robin(v)


@rabbitmq_blueprint.route('/rabbitmq/producer/exchange/fanout')
def rabbitmq_exchange_fanout():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.10.0')
    return msg_rabbitmq.rabbitmq_exchange_fanout(v)


@rabbitmq_blueprint.route('/rabbitmq/producer/exchange/direct')
def rabbitmq_exchange_direct():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.10.0')
    return msg_rabbitmq.rabbitmq_exchange_direct(v)


@rabbitmq_blueprint.route('/rabbitmq/producer/exchange/topic')
def rabbitmq_exchange_topic():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.10.0')
    return msg_rabbitmq.rabbitmq_exchange_topic(v)


@rabbitmq_blueprint.route('/rabbitmq/producer/rpc/')
def rabbitmq_rpc():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.10.0')
    return msg_rabbitmq.rabbitmq_rpc(v)


@rabbitmq_blueprint.route('/rabbitmq/producer/blocking-connect')
def rabbitmq_blocking_connect():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.10.0')
    return msg_rabbitmq.rabbitmq_blocking_connect(v)


@rabbitmq_blueprint.route('/rabbitmq/producer/asyn-consume')
def rabbitmq_asyn_consume():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.10.0')
    return msg_rabbitmq.rabbitmq_asyn_consume(v)


@rabbitmq_blueprint.route('/rabbitmq/producer/select-connect')
def rabbitmq_select_connect():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.10.0')
    return msg_rabbitmq.rabbitmq_select_connect(v)


# @rabbitmq_blueprint.route('/rabbitmq/producer/libev-connect')
# def rabbitmq_libev_connect():
#     """
#     :param v: 作为参数传入，控制版本
#     :return:
#     """
#     queue_name = "l_connection"
#
#     def on_channel(connection):
#         connection.channel(on_open_callback=on_declare)
#
#     def on_declare(channel):
#         channel.queue_declare(publisher(channel), queue_name)
#
#     def publisher(channel):
#         channel.basic_publish(exchange='',
#                               routing_key=queue_name,
#                               body='[%s]It is libev-connection publish' % queue_name)
#         connection.ioloop.stop()
#
#     connection = LibevConnection(ConnectionParameters(),
#                                  on_open_callback=on_channel,
#                                  stop_ioloop_on_close=False)
#     connection.ioloop.start()
#     return "success"


@rabbitmq_blueprint.route('/rabbitmq/producer/blocking/publish')
def rabbitmq_blocking_connection_publish():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.10.0')
    return msg_rabbitmq.rabbitmq_blocking_connection_publish(v)


@rabbitmq_blueprint.route('/rabbitmq/producer/headers')
def rabbitmq_headers():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.10.0')
    return msg_rabbitmq.rabbitmq_headers(v)


@rabbitmq_blueprint.route('/rabbitmq/producer/errors')
def rabbitmq_error():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.10.0')
    return msg_rabbitmq.rabbitmq_error(v)


@rabbitmq_blueprint.route('/rabbitmq/producer/sql')
def rabbitmq_sql():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.10.0')
    return msg_rabbitmq.rabbitmq_sql(v)


@rabbitmq_blueprint.route('/rabbitmq/producer/nosql/redis')
def rabbitmq_nosql_redis():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.10.0')
    return msg_rabbitmq.rabbitmq_nosql_redis(v)


@rabbitmq_blueprint.route('/rabbitmq/producer/nosql/memcache')
def rabbitmq_nosql_memcache():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.10.0')
    return msg_rabbitmq.rabbitmq_nosql_memcache(v)


@rabbitmq_blueprint.route('/rabbitmq/producer/nosql/mongodb')
def rabbitmq_nosql_mongodb():
    """
    :param v: 作为参数传入，控制版本
    :return:
    """
    v = request.args.get("v", '0.10.0')
    return msg_rabbitmq.rabbitmq_nosql_mongodb(v)


@rabbitmq_blueprint.route('/rabbitmq/to-java')
def rabbitmq_to_java():
    """
    :return:
    """
    return msg_rabbitmq.rabbitmq_to_java()


@rabbitmq_blueprint.route('/rabbitmq/to-dotnet')
def rabbitmq_to_dotnet():
    """
    :return:
    """
    return msg_rabbitmq.rabbitmq_to_dotnet()


@rabbitmq_blueprint.route('/rabbitmq/to-ruby')
def rabbitmq_to_ruby():
    """
    :return:
    """
    return msg_rabbitmq.rabbitmq_exchange_to_ruby()


@rabbitmq_blueprint.route('/rabbitmq/to-nodejs')
def rabbitmq_to_nodejs():
    """
    :return:
    """
    return msg_rabbitmq.rabbitmq_to_nodejs()


@rabbitmq_blueprint.route('/rabbitmq/exchange/to-java')
def rabbitmq_exchange_to_java():
    """
    :return:
    """
    return msg_rabbitmq.rabbitmq_exchange_to_java()


@rabbitmq_blueprint.route('/rabbitmq/exchange/to-dotnet')
def rabbitmq_exchange_to_dotnet():
    """
    :return:
    """
    return msg_rabbitmq.rabbitmq_exchange_to_dotnet()


@rabbitmq_blueprint.route('/rabbitmq/exchange/to-ruby')
def rabbitmq_exchange_to_ruby():
    """
    :return:
    """
    return msg_rabbitmq.rabbitmq_exchange_to_ruby()


@rabbitmq_blueprint.route('/rabbitmq/exchange/to-nodejs')
def rabbitmq_exchange_to_nodejs():
    """
    :return:
    """
    return msg_rabbitmq.rabbitmq_exchange_to_nodejs()

















