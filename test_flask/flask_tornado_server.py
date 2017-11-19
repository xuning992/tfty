# -*- coding: utf-8 -*-

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from main_flask import application


http_server = HTTPServer(WSGIContainer(application))
http_server.listen(5565)
IOLoop.instance().start()
