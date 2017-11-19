#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options
import tornado.web
import tornado.wsgi

from core.url import urls

define("port", default=8088, help="run on the given port", type=int)


class Application(tornado.wsgi.WSGIApplication):
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

application = Application()
