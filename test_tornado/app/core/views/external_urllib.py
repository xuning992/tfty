# -*- coding: utf-8 -*-
from core.views.base import BaseHandler
from public.http import ex_urllib


class UrllibGet(BaseHandler):
    def get(self):
        self.write(ex_urllib.test_urllib_get_method())


class UrllibUrlencode(BaseHandler):
    def get(self):
        self.write(ex_urllib.test_urllib_urlencode_method())


class UrllibPost(BaseHandler):
    def get(self):
        self.write(ex_urllib.test_urllib_post_method())
