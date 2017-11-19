# -*- coding: utf-8 -*-
# 资源 Resources
# read-GET | create-POST | update-PUT | delete-DELETE

from piston.handler import BaseHandler
from test_django.models.test_db import DjangoOrmTest
from piston.utils import rc, throttle


class DjangoOrmTestHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'DELETE')
    model = DjangoOrmTest

    def read(self, request, school=None, *args, **kwargs):
        base = DjangoOrmTest.objects.using("mysql_mysqldb")
        return "GET: %s" % base.all()

    @throttle(5, 10*60)  # allow 5 times in 10 min
    def update(self, request, *args, **kwargs):
        post = DjangoOrmTest.objects.using("mysql_mysqldb").last()
        post.name = "MZZZ"
        post.save()

        return post
        # return rc.CODES['ALL_CODE']

    def delete(self, request, *args, **kwargs):
        post = DjangoOrmTest.objects.using('mysql_mysqldb').last()
        post.delete()

        return rc.CODES['DELETED']

