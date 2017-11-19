# -*- coding: utf-8 -*-

import uuid
import time
from public.config import *
from public.util import do_something
# from pika import BlockingConnection, ConnectionParameters, SelectConnection, BasicProperties
MQ_SERVER = "10.194.1.2"


class GetVersion(object):
    def __init__(self, v):
        if v == "0.10.0":
            from public.packages.msg_rabbitmq.v0100 import pika as pk
        elif v == '0.10.0b1':
            from public.packages.msg_rabbitmq.v0100b1 import pika as pk
        elif v == "0.10.0b2":
            from public.packages.msg_rabbitmq.v0100b2 import pika as pk
        else:
            pass
        self.pk = pk

    def __enter__(self):
        return self.pk

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class RabbitmqConnect(object):
    def __init__(self, v):
        if v == "0.10.0":
            from public.packages.msg_rabbitmq.v0100 import pika as pk
        elif v == "0.10.0b1":
            from public.packages.msg_rabbitmq.v0100b1 import pika as pk
        elif v == "0.10.0b2":
            from public.packages.msg_rabbitmq.v0100b2 import pika as pk
        self.pk = pk
        # self.connection = self.pk.BlockingConnection(self.pk.ConnectionParameters('localhost'))
        self.connection = self.pk.BlockingConnection(self.pk.ConnectionParameters(MQ_SERVER, 5672, '/',
                                                     self.pk.PlainCredentials('guest', 'guest')))

    def __enter__(self):
        self.channel = self.connection.channel()
        return self.channel, self.pk

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


class FibonacciRpcClient(object):
    def __init__(self, v):
        self.v = v
        with GetVersion(v) as pk:
            self.connection = pk.BlockingConnection(pk.ConnectionParameters())
            # self.connection = self.pk.BlockingConnection(MQ_SERVER, '5672', '/',
            #                                              self.pk.PlainCredentials('guest', 'guest'))
            self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_request, queue=self.callback_queue, no_ack=True)

    def on_request(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        with GetVersion(self.v) as pk:
            self.response = None
            self.corr_id = str(uuid.uuid4())
            self.channel.basic_publish(exchange='',
                                       routing_key='rpc_queue',
                                       properties=pk.BasicProperties(
                                           reply_to=self.callback_queue,
                                           correlation_id=self.corr_id
                                           ),
                                       body=str(n))
            while self.response is None:
                self.connection.process_data_events()

        return int(self.response)


def rabbitmq_define_queue(v):
    """
    :return:
    """
    queue_name = 'hello'
    s, item = do_something()
    with RabbitmqConnect(v) as channel:
        channel, pk = channel
        channel.queue_declare(queue_name)
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body='Hello World! sleep(%s) get(%s)' % (0, 0))

    return "{%s}[RabbitMQ]\n[producer]\ndefine queue name is ok sleep(%s)" % (v, 0)


def rabbitmq_define_queue_with_dot(v):

    with RabbitmqConnect(v) as channel:
        channel, pk = channel
        channel.queue_declare('key.a')
        channel.basic_publish(exchange='',
                              routing_key='key.a',
                              body='hello World (dot)')

    return "{%s}[RabbitMQ]\n[producer]\ndefine queue name with dot is ok" % v


def rabbitmq_round_robin(v):
    """
    :return:
    """
    bodys = ['hello.', 'hello..', 'hello...', 'hello....', 'hello.....']

    for body in bodys:
        with RabbitmqConnect(v) as channel:
            channel, pk = channel
            channel.queue_declare('task_queue')
            channel.basic_publish(exchange='',
                                  routing_key='task_queue',
                                  body=body)

    return "{%s}[RabbitMQ]\n[producer]\nround-robin task queue" % v


def rabbitmq_exchange_fanout(v):
    """
    :param routing_key: 作为参数传入，控制routing_key数值
    :return:
    """
    routing_keys = ['info', 'error', 'debug']
    for routing_key in routing_keys:
        with RabbitmqConnect(v) as channel:
            channel, pk = channel
            channel.exchange_declare(exchange='fanout_logs', type='fanout')
            channel.basic_publish(exchange='fanout_logs',
                                  routing_key=routing_key,
                                  body="[%s]It is exchange fanout" % routing_key)

    return "{%s}[RabbitMQ]\n[producer]\ndefine exchange name, type is fanout" % v


def rabbitmq_exchange_direct(v):
    """
    :param routing_key: 作为参数传入，控制routing_key数值
    :return:
    """
    routing_keys = ['red', 'yellow', 'blue', 'white', 'back']
    s, item = do_something()
    for routing_key in routing_keys:
        with RabbitmqConnect(v) as channel:
            channel, pk = channel
            channel.exchange_declare(exchange='direct_logs', type='direct')
            channel.basic_publish(exchange='direct_logs',
                                  routing_key=routing_key,
                                  body='[%s]It is exchange direct sleep(%s) get(%s)' % (routing_key, 0, 0))

    return "{%s}[RabbitMQ]\n[producer]\ndefine exchange name, type is direct sleep(%s)" % (v, 0)


def rabbitmq_exchange_topic(v):
    """
    :param routing_key: 作为参数传入，控制routing_key数值
                        形式：【x.x.x】【x.x】
    :return:
    """
    binding_keys = ['quick.orange.rabbit', 'lazy.orange.elephant', 'quick.orange.fox',
                    'lazy.brown.fox', 'lazy.pink.rabbit', 'quick.brown.fox']
    for binding_key in binding_keys:
        with RabbitmqConnect(v) as channel:
            channel, pk = channel
            channel.exchange_declare(exchange='topic_logs', type='topic')
            channel.basic_publish(exchange='topic_logs',
                                  routing_key=binding_key,
                                  body="[%s]It is exchange topic" % binding_key)

    return "{%s}[RabbitMQ]\n[producer]\ndefine exchange name, type is topic" % v


def rabbitmq_rpc(v):
    """
    :return:
    """
    fibonacci_rpc = FibonacciRpcClient(v)
    response = fibonacci_rpc.call(20)
    return "[RabbitMQ]\n[producer]\nRpc got:[ %s ]" % response


def rabbitmq_blocking_connect(v):
    """
    :return:
    """
    queue_name = 'b_connection'
    with RabbitmqConnect(v) as channel:
        channel, pk = channel
        channel.queue_declare(queue_name)
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body='[%s]Blocking Connection channel.basic_publish()' % queue_name)

    return "{%s}[RabbitMQ]\n[producer]\nBlocking Connection channel.basic_publish()" % v


def rabbitmq_asyn_consume(v):
    """Select Connection channel.basic_publish()
    :return:
    """
    queue_name = 's_connection'

    with RabbitmqConnect(v) as channel:
        channel, pk = channel
        channel.queue_declare(queue=queue_name)
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body='[%s]It is asyn-consume')

    return "{%s}[RabbitMQ]\n[producer]\nSelect Connection" % v


def rabbitmq_select_connect(v):
    """
    :return:
    """
    with GetVersion(v) as pk:

        queue_name = 's_connection'

        def on_channel(connection):
            connection.channel(on_declare)

        def on_declare(channel):
            channel.queue_declare(publisher(channel), queue_name)

        def publisher(channel):
            channel.basic_publish(exchange='',
                                  routing_key=queue_name,
                                  body='[%s]It is asyn-publish' % queue_name)
            connection.ioloop.stop()

        # connection = pk.SelectConnection(pk.ConnectionParameters("amqp://guest:guest@%s:5672/%2F" % MQ_SERVER),
        #                                  on_channel)
        connection = pk.SelectConnection(pk.ConnectionParameters(), on_channel)
        connection.ioloop.start()
    return "{%s}[RabbitMQ]\n[produce]\nSelectConnection" % v


def rabbitmq_libev_connect(v):
    """
    :return:
    """
    with GetVersion(v) as pk:
        queue_name = "l_connection"

        def on_channel(connection):
            connection.channel(on_open_callback=on_declare)

        def on_declare(channel):
            channel.queue_declare(publisher(channel), queue_name)

        def publisher(channel):
            channel.basic_publish(exchange='',
                                  routing_key=queue_name,
                                  body='[%s]It is libev-connection publish' % queue_name)
            connection.ioloop.stop()

        connection = pk.LibevConnection(pk.ConnectionParameters(),
                                        on_open_callsback=on_channel,
                                        stop_ioloop_on_close=False)
        # connection = pk.LibevConnection(pk.ConnectionParameters("amqp://guest:guest@%s:5672/%2F" % MQ_SERVER),
        #                                 on_open_callsback=on_channel,
        #                                 stop_ioloop_on_close=False)
        connection.ioloop.start()

    return "{%s}[RabbitMQ]\n[produce]\nLibevConnection" % v


def rabbitmq_blocking_connection_publish(v):
    """Blocking Connection channel.publish()
    :return:
    """
    queue_name = 'b_connection_p'
    with RabbitmqConnect(v) as channel:
        channel, pk = channel
        channel.queue_declare(queue_name)
        channel.publish(exchange='',
                        routing_key=queue_name,
                        body='[%s]Blocking Connection channel.publish()' % queue_name)

    return "{%s}[RabbitMQ]\n[producer]\nBlocking Connection channel.publish()" % v


def rabbitmq_headers(v):
    """
    :param id:
    :return:
    """
    queue_name = 'headers'
    with RabbitmqConnect(v) as channel:
        channel, pk = channel
        channel.queue_declare(queue=queue_name)
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body='headers',
                              properties=pk.BasicProperties(
                                  headers={'a': 1,
                                           'bb': 'bbb',
                                           'sjd13': 'asijdoi245'}
                              ))

    return "{%s}[RabbitMQ]\n[producer]\nheaders" % v


def rabbitmq_error(v):
    """
    :return:
    """
    queue_name = 'errors'
    with RabbitmqConnect(v) as channel:
        channel, pk = channel
        channel.queue_declare(queue=queue_name)
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body='It is errors',
                              properties=pk.BasicProperties(
                                  headers={'a': 1,
                                           'bb': 'bbb',
                                           'sjd13': 'asijdoi245'}
                              ))

    return "{%s}[RabbitMQ]\n[producer]\nerrors" % v


def rabbitmq_sql(v):
    """
    :return:
    """
    queue_name = 'sql'
    with RabbitmqConnect(v) as channel:
        channel, pk = channel
        channel.queue_declare(queue=queue_name)
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body='It is sql')

    return "{%s}[RabbitMQ]\n[producer]\nsql" % v


def rabbitmq_nosql_redis(v):
    """
    :return:
    """
    queue_name = 'redis'
    with RabbitmqConnect(v) as channel:
        channel, pk = channel
        channel.queue_declare(queue=queue_name)
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body='It is redis')

    return "{%s}[RabbitMQ]\n[producer]\nnosql %s" % (v, queue_name)


def rabbitmq_nosql_memcache(v):
    """
    :return:
    """
    queue_name = 'memcache'
    with RabbitmqConnect(v) as channel:
        channel, pk = channel
        channel.queue_declare(queue=queue_name)
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body='It is memcache')

    return "{%s}[RabbitMQ]\n[producer]\nnosql %s" % (v, queue_name)


def rabbitmq_nosql_mongodb(v):
    """
    :return:
    """
    queue_name = 'mongodb'
    with RabbitmqConnect(v) as channel:
        channel, pk = channel
        channel.queue_declare(queue=queue_name)
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body='It is mongoDB ')

    return "{%s}[RabbitMQ]\n[producer]\nnosql %s" % (v, queue_name)


message_queue = "From Python, the queue is %s"
message_exchange = "From Python, the exchange is %s"
queue_name = "Q-%s"
exchange_name = "E-%s"


def rabbitmq_to_java():
    """
    :return:
    """
    lan = "Java"
    with RabbitmqConnect(DEFAULT_PIKA_VERSION) as channel:
        channel, pk = channel
        channel.queue_declare(queue=queue_name % lan)
        channel.basic_publish(exchange='',
                              routing_key=queue_name % lan,
                              body=message_queue % lan)

    return "[%s] OK" % (queue_name % lan)


def rabbitmq_to_dotnet():
    """
    :return:
    """
    lan = 'DotNet'
    with RabbitmqConnect(DEFAULT_PIKA_VERSION) as channel:
        channel, pk = channel
        channel.queue_declare(queue=queue_name % lan)
        channel.basic_publish(exchange='',
                              routing_key=queue_name % lan,
                              body=message_queue % lan)

    return "[%s] OK" % (queue_name % lan)


def rabbitmq_to_ruby():
    """
    :return:
    """
    lan = 'Ruby'
    with RabbitmqConnect(DEFAULT_PIKA_VERSION) as channel:
        channel, pk = channel
        channel.queue_declare(queue=queue_name % lan)
        channel.basic_publish(exchange='',
                              routing_key=queue_name % lan,
                              body=message_queue % lan)

    return "[%s] OK" % (queue_name % lan)


def rabbitmq_to_nodejs():
    """
    :return:
    """
    lan = 'Nodejs'
    with RabbitmqConnect(DEFAULT_PIKA_VERSION) as channel:
        channel, pk = channel
        channel.queue_declare(queue=queue_name % lan)
        channel.basic_publish(exchange='',
                              routing_key=queue_name % lan,
                              body=message_queue % lan)

    return "[%s] OK" % (queue_name % lan)

routing_ = 'R-%s'


def rabbitmq_exchange_to_java():
    """
    :return:
    """
    lan = 'Java'
    with RabbitmqConnect(DEFAULT_PIKA_VERSION) as channel:
        channel, pk = channel
        channel.exchange_declare(exchange=exchange_name % lan)
        channel.basic_publish(exchange=exchange_name % lan,
                              routing_key=routing_ % lan,
                              body=message_exchange % lan)

    return "[%s] OK" % (exchange_name % lan)


def rabbitmq_exchange_to_dotnet():
    """
    :return:
    """
    lan = 'DotNet'
    with RabbitmqConnect(DEFAULT_PIKA_VERSION) as channel:
        channel, pk = channel
        channel.exchange_declare(exchange=exchange_name % lan)
        channel.basic_publish(exchange=exchange_name % lan,
                              routing_key=routing_ % lan,
                              body=message_exchange % lan)

    return "[%s] OK" % (exchange_name % lan)


def rabbitmq_exchange_to_ruby():
    """
    :return:
    """
    lan = 'Ruby'
    with RabbitmqConnect(DEFAULT_PIKA_VERSION) as channel:
        channel, pk = channel
        channel.exchange_declare(exchange=exchange_name % lan)
        channel.basic_publish(exchange=exchange_name % lan,
                              routing_key=routing_ % lan,
                              body=message_exchange % lan)

    return "[%s] OK" % (exchange_name % lan)


def rabbitmq_exchange_to_nodejs():
    """
    :return:
    """
    lan = 'Nodejs'
    with RabbitmqConnect(DEFAULT_PIKA_VERSION) as channel:
        channel, pk = channel
        channel.exchange_declare(exchange=exchange_name % lan)
        channel.basic_publish(exchange=exchange_name % lan,
                              routing_key=routing_ % lan,
                              body=message_exchange % lan)

    return "[%s] OK" % (exchange_name % lan)
