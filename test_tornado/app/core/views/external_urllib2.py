# -*- coding: utf-8 -*-
from core.views.base import BaseHandler
from public.http import ex_urllib2


class Urllib2Get(BaseHandler):
    def get(self):
        self.write(ex_urllib2.test_urllib2_get_method())


class Urllib2Post(BaseHandler):
    def get(self):
        self.write(ex_urllib2.test_urllib2_post_method())


class Urllib2Cookie(BaseHandler):
    def get(self):
        self.write(ex_urllib2.test_urllib2_cookie_method())
