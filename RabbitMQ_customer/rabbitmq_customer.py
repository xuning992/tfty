# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from public.packages.msg_rabbitmq.v0100.pika import BlockingConnection, ConnectionParameters, BasicProperties, \
    TornadoConnection, LibevConnection, PlainCredentials
from public.packages.msg_rabbitmq.v0100.pika.exceptions import BodyTooLongError
from public.util import do_something
from public.packages.ex_requests.v2100 import requests
# from pika import BlockingConnection, ConnectionParameters, BasicProperties, TornadoConnection,
#                  LibevConnection, SelectConnection
# from pika.exceptions import BodyTooLongError
from time import sleep
import time
from public.db_mysql import db_mysqldb
MQ_SERVER = "10.194.1.2"
n = 0


class RabbitmqStartConsuming():
    def __init__(self):
        # self.connection = BlockingConnection(ConnectionParameters("localhost"))
        self.connection = BlockingConnection(ConnectionParameters(MQ_SERVER, 5672, '/',
                                                                  PlainCredentials('guest', 'guest')))

    def __enter__(self):
        self.channel = self.connection.channel()
        return self.channel

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.channel.start_consuming()


def blocking_connection_customer():
    identify = '[blocking connection]'
    queue_name = 'b_connection'
    
    def callback(ch, method, propreties, body):
        print identify + 'get body is %s' % body

    with RabbitmqStartConsuming() as channel:
        print identify + 'start success'
        channel.queue_declare(exclusive=True)
        channel.basic_consume(callback, queue=queue_name, no_ack=True)


def tornado_connection_customer():
    identify = '[tornado connection]'
    queue_name = 's_connection'

    def on_channel(connection):
        connection.channel(on_open_callback=on_declare)

    def on_declare(new_channel):
        channel = new_channel
        channel.queue_declare(consumer(channel), queue_name)

    def consumer(channel):
        print identify + 'start success'
        channel.basic_consume(callback, queue=queue_name, no_ack=True)

    def callback(ch, method, propreties, body):
        # raise BodyTooLongError
        print identify + 'get body is %s' % body

    connection = TornadoConnection(ConnectionParameters("localhost"), on_channel)
    connection.ioloop.start()


def libev_connection_customer():
    identify = '[libev connection]'
    queue_name = 'l_connection'

    def on_channel(connection):
        connection.channel(on_open_callback=on_declare)

    def on_declare(new_channel):
        channel = new_channel
        channel.queue_declare(consumer(channel), queue_name)

    def consumer(channel):
        print identify + "start success"
        channel.basic_consume(callback, queue=queue_name, no_ack=True)

    def callback(ch, method, propreties, body):
        print identify + 'get body is %s' % body

    connection = LibevConnection(ConnectionParameters(),
                                 on_open_callback=on_channel,
                                 stop_ioloop_on_close=False)
    connection.ioloop.start()


def slow_action_queue_customer():
    identify = '[slow action queue]'
    queue_name = 'b_connection_p'

    def callback(ch, method, propreties, body):
        sleep(3)
        print identify + 'get body is %s' % body

    with RabbitmqStartConsuming() as channel:
        print identify + 'start success'

        channel.queue_declare(queue_name)
        channel.basic_consume(callback, queue=queue_name, no_ack=True)


def slow_action_exchange_customer():
    identify = '[slow action exchange]'
    exchange_name = 'fanout_logs'
    exchange_type = 'fanout'

    def callback(ch, method, propreties, body):
        sleep(2.5)
        print identify + 'get body is %s' % body
    with RabbitmqStartConsuming() as channel:
        print identify + 'start success'

        channel.exchange_declare(exchange=exchange_name, type=exchange_type)
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        channel.basic_consume(callback, queue=queue_name, no_ack=True)


def slow_action_headers_customer():
    identify = '[slow action headers]'
    queue_name = 'headers'

    def callback(ch, method, propreties, body):
        sleep(2.8)
        print identify + 'get header is %s\n' % str(propreties.headers)
    with RabbitmqStartConsuming() as channel:
        print identify + 'start success'

        channel.queue_declare(exclusive=True)

        channel.basic_consume(callback, queue=queue_name, no_ack=True)


def error_customer():
    identify = '[error headers]'
    queue_name = 'errors'

    def on_channel(connection):
        connection.channel(on_open_callback=on_declare)

    def on_declare(new_channel):
        channel = new_channel
        channel.queue_declare(consumer(channel), queue_name)

    def consumer(channel):
        print identify + 'start success'
        channel.basic_consume(callback, queue=queue_name, no_ack=True)

    def callback(ch, method, propreties, body):
        raise BodyTooLongError("body too long")
        # print llalalal

    connection = TornadoConnection(ConnectionParameters(), on_channel)
    connection.ioloop.start()


def sql_customer():
    identify = '[sql]'
    queue_name = 'sql'

    def callback(ch, method, header, body):

        rlt = db_mysqldb.mysqldb_select()
        print identify + "get body is %s\nsql result is %s" % (str(body), rlt)

    with RabbitmqStartConsuming() as channel:
        print identify + 'start success'

        channel.queue_declare(exclusive=True)
        channel.basic_consume(callback, queue=queue_name, no_ack=True)


def redis_customer():
    identify = '[nosql]'
    queue_name = 'redis'

    def callback(ch, method, header, body):
        from public.db_redis import db_redis
        rlt = db_redis.redis_get('2.10.5')
        print identify + 'get body is %s\nredis result is %s' % (str(body), rlt)

    with RabbitmqStartConsuming() as channel:
        print identify + "start success"

        channel.queue_declare(exclusive=True)
        channel.basic_consume(callback, queue=queue_name, no_ack=True)


def memcache_customer():
    identify = '[nosql]'
    queue_name = 'memcache'

    def callback(ch, method, header, body):
        from public.db_memcache import db_pymemcache
        rlt = db_pymemcache.pymemcache_get("1.4.0")
        print identify + 'get body is %s\nmemcache result is %s' % (str(body), rlt)

    with RabbitmqStartConsuming() as channel:
        print identify + "start success"

        channel.queue_declare(exclusive=True)
        channel.basic_consume(callback, queue=queue_name, no_ack=True)


def mongodb_customer():
    identify = '[nosql]'
    queue_name = 'mongodb'

    def callback(ch, method, header, body):
        from public.db_mongo import db_pymongo
        rlt = db_pymongo.mongodb_insert("3.4.0")
        print identify + 'get body is %s\nmongoDB result is %s' % (str(body), rlt)

    with RabbitmqStartConsuming() as channel:
        print identify + "start success"

        channel.queue_declare(exclusive=True)
        channel.basic_consume(callback, queue=queue_name, no_ack=True)


def define_queue_customer():
    identify = '[define queue]'
    # start = time.time()
    # global num
    # num = 0
    # print "start time is %s" % start

    def callback(ch, method, propreties, body):
        s, item = do_something()
        # print identify + "get body is %s" % body
        # rlt = db_mysqldb.mysqldb_update()
        # fp = requests.get("http://192.168.5.176:5582/normal/a")
        # print identify + 'body is : %s; headers is : %s' % (body, str(propreties.headers))
        # global num
        # num += 1
        # # print u"第 %d 次 time is %s, 数据库：%s, 外部调用：%s" % (num, time.time(), rlt, str(fp.status_code))
        # if num == 100:
        #     print u"消费 %d 次，共花费时间 %s s" % (num, time.time()-start)
        #     exit()
        print identify + "get body is %s sleep(%s) get(%s)" % (body, s, item)

    with RabbitmqStartConsuming() as channel:
        print identify + "start success"
        channel.queue_declare(exclusive=True)
        channel.basic_consume(callback, queue='hello', no_ack=True)


def define_queue_with_dot():
    identify = '[define queue with dot]'

    def callback(ch, method, propreties, body):
        print identify + "get body is %s" % body

    with RabbitmqStartConsuming() as channel:
        print identify + "start success"
        channel.queue_declare(exclusive=True)
        # channel.queue_bind(queue='key.a', exchange='', routing_key='key.*')
        channel.basic_consume(callback, queue='key.a', no_ack=True)


def round_robin_one():
    identify = '[round-robin(one)]'

    def callback(ch, method, propreties, body):
        sleep(body.count(b"."))
        print identify + "get body is %s" % body

    with RabbitmqStartConsuming() as channel:
        print identify + "start success"
        channel.queue_declare(exclusive=True)
        channel.basic_consume(callback, queue='task_queue', no_ack=True)


def round_robin_two():
    identify = '[round-robin(two)]'

    def callback(ch, method, propreties, body):
        sleep(body.count(b"."))
        print identify + "get body is %s" % body

    with RabbitmqStartConsuming() as channel:
        print identify + "start success"
        channel.queue_declare(exclusive=True)
        channel.basic_consume(callback, queue='task_queue', no_ack=True)


def define_exchange_fanout_one():
    identify = '[define exchange fanout(one)]'

    def callback(ch, method, propreties, body):
        print identify + "get body is %s" % body

    with RabbitmqStartConsuming() as channel:
        print identify + "start success"

        channel.exchange_declare(exchange='fanout_logs', type='fanout')
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange='fanout_logs', queue=queue_name)
        channel.basic_consume(callback, queue=queue_name, no_ack=True)


def define_exchange_fanout_two():
    identify = '[define exchange fanout(two)]'

    def callback(ch, method, propreties, body):
        print identify + "get body is %s" % body

    with RabbitmqStartConsuming() as channel:
        print identify + "start success"

        channel.exchange_declare(exchange='fanout_logs', type='fanout')
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange='fanout_logs', queue=queue_name)
        channel.basic_consume(callback, queue=queue_name, no_ack=True)


def define_exchange_direct_one():
    identify = '[define exchange direct(one:{red|yellow|blue})]'
    severties = ['red', 'yellow', 'blue']

    def callback(ch, method, propreties, body):
        s, item = do_something()
        print identify + "get body is %s:%s sleep(%s) get(%s)" % (method.routing_key, body, s, item)

    with RabbitmqStartConsuming() as channel:
        print identify + 'start success'

        channel.exchange_declare(exchange='direct_logs', type='direct')
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        for severty in severties:
            channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severty)

        channel.basic_consume(callback, queue=queue_name, no_ack=True)


def define_exchange_direct_two():
    identify = '[define exchange direct(two:{white|black})]'
    severties = ['white', 'black']

    def callback(ch, method, propreties, body):
        s, item = do_something()
        print identify + "get body is %s:%s sleep(%s) get(%s)" % (method.routing_key, body, s, item)

    with RabbitmqStartConsuming() as channel:
        print identify + 'start success'

        channel.exchange_declare(exchange='direct_logs', type='direct')
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        for severty in severties:
            channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severty)

        channel.basic_consume(callback, queue=queue_name, no_ack=True)


def define_exchange_topic_one():
    identify = '[define exchange topic(one:{*.orange.*})]'
    binding_keys = ['*.orange.*']

    def callback(ch, method, propreties, body):
        print identify + 'get body is %s:%s' % (method.routing_key, body)

    with RabbitmqStartConsuming() as channel:
        print identify + "start success"

        channel.exchange_declare(exchange='topic_logs', type='topic')
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        for binding_key in binding_keys:
            channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=binding_key)

        channel.basic_consume(callback, queue=queue_name, no_ack=True)


def define_exchange_topic_two():
    identify = '[define exchange topic(two:{*.*.rabbit|lazy.#})]'
    binding_keys = ['*.*.rabbit', 'lazy.#']

    def callback(ch, method, propreties, body):
        print identify + 'get body is %s:%s' % (method.routing_key, body)

    with RabbitmqStartConsuming() as channel:
        print identify + "start success"

        channel.exchange_declare(exchange='topic_logs', type='topic')
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        for binding_key in binding_keys:
            channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=binding_key)

        channel.basic_consume(callback, queue=queue_name, no_ack=True)


def rpc_customer():
    identify = '[Rpc]'

    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)

    with RabbitmqStartConsuming() as channel:
        print identify + "start success"

        def on_request(ch, method, props, body):

            n = int(body)
            print identify + "fid(%d)" % n
            response = fib(n)
            channel.basic_publish(exchange='',
                                  routing_key=props.reply_to,
                                  properties=BasicProperties(correlation_id=props.correlation_id),
                                  body=str(response))
            ch.basic_ack(delivery_tag=method.delivery_tag)

        channel.queue_declare('rpc_queue')

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(on_request, queue='rpc_queue')


def exchange_with_exchange():
    identify = '[get with exchange]'
    # exchange = "x-tingyun-appserver-metrics"
    # routing = "applicationPerfMetrics"
    exchange = 'E-Python'
    routing = "R-Python"

    def callback(ch, method, propreties, body):
        # rlt = db_mysqldb.mysqldb_select()
        # fp = requests.get("http://127.0.0.1:5582/slow/action/a?timer=2500")
        # print identify + "<h3>get body is %s<\h3>\n<h4>sql: %s<\h4>\n<h4>ex: %s<\h4>" % (body, rlt, fp.status_code)
        print "body is %s" % body

    with RabbitmqStartConsuming() as channel:
        print identify + 'start success'

        channel.exchange_declare(exchange=exchange, type='direct')
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(queue=queue_name, exchange=exchange, routing_key=routing)

        channel.basic_consume(callback, queue=queue_name, no_ack=True)


def exchange_with_queue():
    identify = '[get with queue]'
    # queue_name = "x-tingyun-appserver-metrics-persist"
    queue_name = 'Q-Python'

    def callback(ch, method, propreties, body):
        # rlt = db_mysqldb.mysqldb_select()
        # fp = requests.get("http://127.0.0.1:5582/slow/action/a?timer=2500")
        # print identify + "<h3>get body is %s<\h3>\n<h4>sql: %s<\h4>\n<h4>ex: %s<\h4>" % (body, rlt, fp.status_code)
        print "body is %s" % body

    with RabbitmqStartConsuming() as channel:
        print identify + "start success"

        channel.queue_declare(durable=True)
        channel.basic_consume(callback, queue=queue_name, no_ack=True)


if __name__ == "__main__":
    customers = {
        'queue': [define_queue_customer, define_queue_with_dot],
        'robin': [round_robin_one, round_robin_two],
        'fanout': [define_exchange_fanout_one, define_exchange_fanout_two],
        'direct': [define_exchange_direct_one, define_exchange_direct_two],
        'topic': [define_exchange_topic_one, define_exchange_topic_two],
        'rpc': [rpc_customer],
        # 'connect': [blocking_connection_customer, tornado_connection_customer, libev_connection_customer],
        'slow_action': [slow_action_queue_customer, slow_action_exchange_customer, slow_action_headers_customer],
        'other': [error_customer, sql_customer],
        'nosql': [redis_customer, memcache_customer, mongodb_customer],
        'lan': [exchange_with_exchange, exchange_with_queue]
    }


    def play_all():
        for key in ("queue", 'fanout', "direct", 'topic', 'rpc', 'connect', 'slow_action', 'other', 'nosql'):
            for i in range(len(customers[key])):
                os.system('sh startup.sh %s %s &' % (key, i))

    def player(type_, num):
        customers[type_][int(num)]()

    if len(sys.argv) == 3:
        player(sys.argv[1], sys.argv[2])
    else:
        print "[X]Usage: %s {queue|robin|fanout|direct|topic|rpc|connect|slow_action|nosql|other|lan} {0|1|2}" % sys.argv[0]
