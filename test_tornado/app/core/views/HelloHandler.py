#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.views.base import BaseHandler
from core.tools.exetime import exe_time


class HelloHandler(BaseHandler):

    @exe_time
    def get(self):
        name = self.get_argument('name', '')
        age = self.get_argument('age', '')

        if not all([name, age]):
            return self.resp_400()

        ret = {
            'say': 'hello',
            'name': name,
            'age': age
        }

        return self.resp_200(ret)



            