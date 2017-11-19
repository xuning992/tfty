# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from piston.resource import Resource
from test_django.api.handlers import DjangoOrmTestHandler


djangoormtest_handler = Resource(DjangoOrmTestHandler)


urlpatterns = patterns(
    '',
    # url(r'^piston/(?P<school>[^/]+)/', djangoormtest_handler),
    url(r'^piston/?$', djangoormtest_handler),
)