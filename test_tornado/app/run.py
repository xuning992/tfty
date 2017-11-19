#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import socket
import errno
import functools

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options

from core.url import urls

define("port", default=8088, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = urls

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "core/templates"),
            static_path=os.path.join(os.path.dirname(__file__), "core/static"),
            # xsrf_cookies=True,
            # cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            debug=True,
        )

        super(Application, self).__init__(handlers, **settings)


def tcp_server_listen(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(0)
    try:
        sock.bind(("", port))
        print("Bind port {p} success".format(p=port))
    except Exception as e:
        print("Bind port {p} error : {e}".format(p=port, e=e))
    sock.listen(128)

    io_loop = tornado.ioloop.IOLoop.current()
    callback = functools.partial(connection_ready, sock)
    io_loop.add_handler(sock.fileno(), callback, io_loop.READ)

def connection_ready(sock, fd, events):
    print("connec ready ==>>")
    try:
        connection, address = sock.accept()
    except socket.error as e:
       if e.args[0] not in (errno.EWOULDBLOCK, errno.EAGAIN):
            return

    try:
        connection.setblocking(0)
        connection.sendall(bytes("hello world"))
        connection.close()
    except Exception as e:
        connection.close()
        pass


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)

    tcp_server_listen(10000)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()



