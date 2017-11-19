# coding: utf-8
from pika import TornadoConnection, ConnectionParameters, SelectConnection, BlockingConnection
from core.views.base import BaseHandler
# from tornado import ioloop


class RabbitmqAsynConnection(BaseHandler):
    def get(self):

        queue_name = "s_connection"

        def on_channel(connection):
            connection.channel(on_declare)

        def on_declare(channel):
            channel.queue_declare(publisher(channel), queue_name)

        def publisher(channel):
            channel.basic_publish(exchange='',
                                  routing_key=queue_name,
                                  body='[%s]It is asyn publish')

        connection = SelectConnection(ConnectionParameters('localhost'), on_channel)
        # connection = BlockingConnection(ConnectionParameters())
        # channel = connection.channel()
        # channel.queue_declare(queue=queue_name)
        # channel.basic_publish(exchange='', routing_key=queue_name, body='sss')

        self.write("[Tornado asyn produce] OK")
